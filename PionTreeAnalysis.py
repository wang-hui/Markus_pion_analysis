#! /usr/bin/env python

import ROOT
ROOT.EnableImplicitMT()
ROOT.TH1.SetDefaultSumw2()
from array import array
import math
import argparse
import numpy as np
bins = array('d', np.logspace(0.7, 3, 20))

# base = '/afs/cern.ch/work/m/mseidel/HCALDPG/RecoPaper/CMSSW_10_6_29/src/'
base = ''
deltaR = 0.
subdet = {
    'HB': (0.000, 1.305-deltaR),
    # 'TR': (1.305, 1.392),
    'HElo': (1.392+deltaR, 2.500-deltaR),
    'HEhi': (2.500+deltaR, 3.000-deltaR),
    # 'HF': (3.000, 5.191),
}
EtaRange = {
    'HB': "0 < |#eta| < 1.3",
    'HElo': "1.4 < |#eta| < 2.5",
    'HEhi': "2.5 < |#eta| < 3.0",
}
recos = {
    'M0': 'raw',
    'MAHI': 'reco',
#    'PFCalo': 'pfcalo',
#    'PF': 'pf',
#    'PFCharged': 'pfch',
}
colors = {
    'MAHI': ROOT.kRed,
    'M0': ROOT.kBlue,
#    'PFCalo': ROOT.kGreen+1,
#    'PF': ROOT.kCyan+1,
#    'PFCharged': ROOT.kAzure+1,
}
files = {
    'PU': 'merged_PionTree_PU_dR0.15_corr.root',
    'OOTPU': 'merged_PionTree_OOTPU_dR0.15_corr.root',
    'NoPU': 'merged_PionTree_NoPU_dR0.15_corr.root',
}
hists = {}
profiles = {}
rms = {}

parser = argparse.ArgumentParser(description='Analyze Pion tree.')
parser.add_argument('--loadhist', action='store_true')
args = parser.parse_args()

ROOT.gStyle.SetPalette(ROOT.kViridis)
ROOT.TColor.InvertPalette()
ROOT.gStyle.SetOptStat(0)
c = ROOT.TCanvas('c','c',600,600)
c.cd()
c.SetRightMargin(0.1)
c.SetLeftMargin(0.15)
#c.SetBottomMargin(0.15)
#c.SetTopMargin(0.05)
c.SetLogx()
c.SetLogz()

for region,etas in subdet.items():
    #c.SetRightMargin(0.12)
    for pu,file in files.items():
        hists[pu] = {}
        profiles[pu] = {}
        rms[pu] = {}
        rdf = ROOT.RDataFrame('Pions', base+file)
        for name,reco in recos.items():
            histmodel = ROOT.RDF.TH2DModel('%s_%s' % (name, pu), ';Generated pion energy [GeV];%s / generated response (%s, %s)' % (name, pu, region), len(bins)-1, bins, 50, 0, 5)
            # rdf = rdf.Define('%s_ratio' % reco, '(%s_sume-%s_offe)/gen_e' % (reco, reco))
            rdf = rdf.Filter('abs(gen_eta) > %.3f && abs(gen_eta) < %.3f' % (etas[0], etas[1]))
            rdf = rdf.Define('%s_ratio' % reco, '(%s_sume)/gen_e' % (reco))
            rdf = rdf.Filter('%s_ratio > 0.' % reco)
            hists[pu][name] = rdf.Histo2D(histmodel, 'gen_e', '%s_ratio' % reco)
        for name,reco in recos.items():
            hists[pu][name].Draw('colz')
            profiles[pu][name] = hists[pu][name].ProfileX('%s_%s_px' % (name, pu), 1, -1)
            rms[pu][name] = hists[pu][name].ProfileX('%s_%s_rms' % (name, pu), 1, -1, 's')
            rms[pu][name].SetLineColor(ROOT.kRed+1)
            rms[pu][name].Draw('same,e')
            #c.Print('PionTreeAnalysisPlots/%s_%s_%s.pdf'  % (region, name, pu))
            #c.Print('PionTreeAnalysisPlots/%s_%s_%s.png'  % (region, name, pu))

    #c.SetRightMargin(0.05)
    legend = ROOT.TLegend(0.6,0.7,0.9,0.9)
    legend.SetLineWidth(0)
    legend.SetFillStyle(0)

    firstPU = True
    for pu,_ in files.items():
        if pu == 'NoPU':
            continue
        first = True
        for name,_ in recos.items():
            p1 = profiles[pu][name]
            p2 = profiles['NoPU'][name]
            h = p1.ProjectionX('%s_%s_ratio' % (pu, name))
            for i in range(1, p1.GetNbinsX()+1):
                err1 = p1.GetBinError(i)/p1.GetBinContent(i)
                err2 = p2.GetBinError(i)/p2.GetBinContent(i)
                err = math.sqrt(err1**2 + err2**2)
                val = p1.GetBinContent(i)/p2.GetBinContent(i)
                h.SetBinContent(i, val)
                h.SetBinError(i, err*val)
            h.SetLineColor(colors[name])
            h.SetLineWidth(2)
            #h.GetYaxis().SetTitle('%s / NoPU   response (%s)' % (pu, region))
            h.GetYaxis().SetTitle('%s / NoPU   response' % (pu))
            h.GetXaxis().SetTitleOffset(1.1)
            drawoption = ''
            if not first: drawoption += ',same'
            h.Draw(drawoption)
            if firstPU:
                legend.AddEntry(h, name, 'l')
            first = False
        firstPU = False
        legend.Draw()
        latex = ROOT.TLatex()
        latex.SetTextSize(0.04)
        latex.SetNDC()
        latex.DrawLatex(0.15,0.91,"CMS #bf{Simulation 2018}")
        latex.SetTextAlign(31)
        latex.DrawLatex(0.9,0.91,"#bf{13TeV}")
        latex.SetTextSize(0.06)
        latex.DrawLatex(0.89,0.6,EtaRange[region])
        c.Print('PionTreeAnalysisPlots/%s_response_%s_NoPU_ratio.pdf' % (region, pu))
        c.Print('PionTreeAnalysisPlots/%s_response_%s_NoPU_ratio.png' % (region, pu))

        first = True
        for name,_ in recos.items():
            p1 = rms[pu][name]
            p2 = rms['NoPU'][name]
            h = p1.ProjectionX('%s_%s_rms_ratio' % (pu, name))
            for i in range(1, p1.GetNbinsX()+1):
                err1 = p1.GetBinError(i)/p1.GetBinContent(i)
                err2 = p2.GetBinError(i)/p2.GetBinContent(i)
                val = err1/err2
                h.SetBinContent(i, val)
                h.SetBinError(i, 0.)
            h.SetLineColor(colors[name])
            h.SetLineWidth(2)
            h.GetYaxis().SetRangeUser(0.5, 2.)
            h.GetYaxis().SetTitle('%s / NoPU   resolution / response (%s)' % (pu, region))
            drawoption = ''
            if not first: drawoption += ',same'
            h.Draw(drawoption)
            first = False
        legend.Draw()
        #c.Print('PionTreeAnalysisPlots/%s_rms_%s_NoPU_ratio.pdf' % (region, pu))
        #c.Print('PionTreeAnalysisPlots/%s_rms_%s_NoPU_ratio.png' % (region, pu))

    for pu,_ in files.items():
        first = True
        for name,_ in recos.items():
            p1 = rms[pu][name]
            h1 = p1.ProjectionX('%s_%s_rms' % (pu, name))
            for i in range(1, p1.GetNbinsX()+1):
                err1 = p1.GetBinError(i)/p1.GetBinContent(i)
                h1.SetBinContent(i, err1)
                h1.SetBinError(i, 0.)
            h1.SetLineColor(colors[name])
            h1.SetLineWidth(2)
            h1.GetYaxis().SetRangeUser(0., 1.5)
            h1.GetYaxis().SetTitle('%s   resolution / response (%s)' % (pu, region))
            drawoption = ''
            if not first: drawoption += ',same'
            h1.Draw(drawoption)
            first = False
        legend.Draw()
        #c.Print('PionTreeAnalysisPlots/%s_rms_%s.pdf' % (region, pu))
        #c.Print('PionTreeAnalysisPlots/%s_rms_%s.png' % (region, pu))
