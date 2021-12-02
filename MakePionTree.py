#! /usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
import sys
from DataFormats.FWLite import Events, Handle
import progressbar
#import pickle
from array import array
import math
import argparse
from os import path
#import numpy as np

#events = Events('/eos/cms/store/mc/RunIIAutumn18DRPremix/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/GEN-SIM-RECO/102X_upgrade2018_realistic_v15_ext1-v2/110000/029D064E-9209-C549-95E4-6437E54BE1DD.root')

#event_files = [
#    '/eos/user/m/mseidel/SamplePUvsNoPU/Znunu-RunIIAutumn18DR_RECOSIM.root', # pure W
#    #'/eos/user/m/mseidel/SamplePUvsNoPU/Nu-RunIIAutumn18DRPremix_RECOSIM.root' # pure PU
#]

#event_files = glob.glob('/eos/user/m/mseidel/SamplePUvsNoPU/*_RECOSIM/*[!calotowers].root')

parser = argparse.ArgumentParser(description='Convert RECOSIM to Pion tree.')
parser.add_argument('input', metavar='input', help='Input file name')
parser.add_argument('--local', action='store_true')
parser.add_argument('--overwrite', action='store_true')
args = parser.parse_args()

event_file = args.input

deltaR = 0.15
offPhis = [-0.75*math.pi, -0.5*math.pi, -0.25*math.pi, 0.25*math.pi, 0.5*math.pi, 0.75*math.pi, math.pi]

# l1t::CaloTools
towerEtas = [0.,0.087,0.174,0.261,0.348,0.435,0.522,0.609,0.696,0.783,0.870,0.957,1.044,1.131,1.218,1.305,1.392,1.479,1.566,1.653,1.740,1.830,1.930,2.043,2.172,2.322,2.5,2.650,2.853,3.139,3.314,3.489,3.664,3.839,4.013,4.191,4.363,4.538,4.716,4.889,5.191,5.191]

def detIdToEtaPhi(ieta_iphi):
    ieta, iphi = ieta_iphi
    sign = math.copysign(1, ieta)
    aieta = min(abs(ieta), len(towerEtas)-1)
    eta = sign * (towerEtas[aieta] + towerEtas[aieta-1]) / 2
    phi = ROOT.TVector2.Phi_mpi_pi(iphi / 72. * 2. * math.pi)
    return eta, phi

def ptFromEtaE(eta, e):
    return e * math.sin(2*math.atan(math.e**(-eta)))

outfilename = event_file.replace('.root', '_PionTree_dR%s.root' % str(deltaR))
if args.local:
    outfilename = outfilename.split('/')[-1]
if not args.overwrite and path.isfile(outfilename):
    print('File exists, use --overwrite to recreate.')
    sys.exit()
f = ROOT.TFile( outfilename, 'recreate' )
t = ROOT.TTree( 'Pions', 'Pions' )

# GEN branches
gen_pt  = array('f', [0.])
gen_eta = array('f', [0.])
gen_phi = array('f', [0.])
gen_e   = array('f', [0.])

t.Branch('gen_e',   gen_e,   'gen_e/F')
t.Branch('gen_pt',  gen_pt,  'gen_pt/F')
t.Branch('gen_eta', gen_eta, 'gen_eta/F')
t.Branch('gen_phi', gen_phi, 'gen_phi/F')

pu_n  = array('f', [0.])
t.Branch('pu_n',   pu_n,   'pu_n/F')

# RECO branches
max_ntower = 50
max_ndepth = 10

reco_n     = array('i', [0])
reco_e     = array('f', max_ntower*max_ndepth*[0.])
reco_eta   = array('f', max_ntower*[0.])
reco_phi   = array('f', max_ntower*[0.])
reco_ieta  = array('i', max_ntower*[0])
reco_iphi  = array('i', max_ntower*[0])

reco_sume  = array('f', [0.]) # MAHI energy sum
reco_offe  = array('f', [0.]) # average off-angle energy sum
raw_sume   = array('f', [0.]) # M0
raw_offe   = array('f', [0.])
pf_sume    = array('f', [0.]) # PF
pf_offe    = array('f', [0.])
pfcalo_sume= array('f', [0.]) # PF ECAL+HCAL
pfcalo_offe= array('f', [0.])
pfch_sume= array('f', [0.]) # PF ECAL+HCAL
pfch_offe= array('f', [0.])

t.Branch('reco_n', reco_n, 'reco_n/I')
t.Branch('reco_e',   reco_e,   'reco_e[reco_n][%i]/F'  % max_ndepth)
t.Branch('reco_eta', reco_eta, 'reco_eta[reco_n]/F')
t.Branch('reco_phi', reco_phi, 'reco_phi[reco_n]/F')
t.Branch('reco_ieta', reco_ieta, 'reco_ieta[reco_n]/I')
t.Branch('reco_iphi', reco_iphi, 'reco_iphi[reco_n]/I')
t.Branch('reco_sume', reco_sume, 'reco_sume/F')
t.Branch('reco_offe', reco_offe, 'reco_offe/F')
t.Branch('raw_sume', raw_sume, 'raw_sume/F')
t.Branch('raw_offe', raw_offe, 'raw_offe/F')
t.Branch('pf_sume', pf_sume, 'pf_sume/F')
t.Branch('pf_offe', pf_offe, 'pf_offe/F')
t.Branch('pfcalo_sume', pfcalo_sume, 'pfcalo_sume/F')
t.Branch('pfcalo_offe', pfcalo_offe, 'pfcalo_offe/F')
t.Branch('pfch_sume', pfch_sume, 'pfch_sume/F')
t.Branch('pfch_offe', pfch_offe, 'pfch_offe/F')

events = Events(event_file)
hbhehandle  = Handle("edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >")
# hfhandle    = Handle("edm::SortedCollection<HFRecHit,edm::StrictWeakOrdering<HFRecHit> >")
towerhandle = Handle("edm::SortedCollection<CaloTower,edm::StrictWeakOrdering<CaloTower> > ")
genhandle   = Handle("vector<reco::GenParticle>")
puhandle   = Handle("vector<PileupSummaryInfo>")
pfhandle    = Handle("vector<reco::PFCandidate>")

# set up track propagator to correct for magnetic field :o)
pdg = ROOT.TDatabasePDG()
prop = ROOT.TEveTrackPropagator('prop', '', ROOT.TEveMagFieldConst(0., 0., -3.8))
# prop.SetStepper(ROOT.TEveTrackPropagator.kRungeKutta) # no difference for this case?
prop.SetMaxR(185.) # HCAL radius
prop.SetMaxZ(400.)
prop.SetMaxStep(2.)

for e,event in progressbar.progressbar(enumerate(events)):
        
    # if e > 100: break
    eid = event.eventAuxiliary().id()
    
    event.getByLabel("hbhereco", hbhehandle)
    hbherechits = hbhehandle.product()
    
    # event.getByLabel("hfreco", hfhandle)
    # hfrechits = hfhandle.product()
    
    event.getByLabel("towerMaker", towerhandle)
    calotowers = towerhandle.product()
    
    event.getByLabel("genParticles", genhandle)
    genparticles = genhandle.product()
    
    event.getByLabel("addPileupInfo", puhandle)
    puinfo = puhandle.product()
    pu_n[0] = puinfo.begin().getTrueNumInteractions()
    # for pu in puinfo:
    #     print(pu.getPU_NumInteractions(), pu.getTrueNumInteractions())
    
    event.getByLabel("particleFlow", pfhandle)
    pfcandidates = pfhandle.product()

    reco = {}
    raw = {}
    calotower = {}
    towerEtaPhi = {}
    
    # CaloTowers for ECAL -> depth 0
    for ct in calotowers:
        p4 = ct.p4(0)
        if math.isnan(p4.Eta()) or math.isnan(p4.Phi()):
            continue
        id = ct.id()
        key = (id.ieta(), id.iphi())
        if not key in reco:
            reco[key] = {}
            raw[key] = {}
            calotower[key] = {}
        reco[key][0] = ct.emEnergy()
        raw[key][0] = ct.emEnergy()
        calotower[key]['em'] = ct.emEnergy()
        calotower[key]['had'] = ct.hadEnergy()
        towerEtaPhi[key] = (p4.Eta(), p4.Phi())
        # HF
        if abs(id.ieta()) > 29:
            reco[key][1] = ct.hadEnergy()
            raw[key][1] = ct.hadEnergy()
        
        # TODO: merge 28+29
        # TODO: add HO?
    
    # HBHERecHits for HCAL
    for hit in hbherechits:
        id = hit.id()
        key = (id.ieta(), id.iphi())
        if not key in reco: # skip RecHits that are not in CaloTowers
            reco[key] = {0: 0.}
            raw[key] = {0: 0.}
            towerEtaPhi[key] = detIdToEtaPhi(key)
        reco[key][id.depth()] = hit.energy()
        raw[key][id.depth()] = hit.eraw()
        
        #print('%i: iEta = %i, iPhi = %i, depth = %i; energy = %.2f' % (h, id.ieta(), id.iphi(), id.depth(), hit.energy()), id.subdet())
        #break
    
    ## HFRecHits
    #for hit in hfrechits:
    #    id = hit.id()
    #    if id.depth() == 1: continue # long fibers -> EM
    #    #if not id.subdet() == 2: # HE
    #    #    continue
    #    key = (id.ieta(), id.iphi())
    #    if not key in towers: # skip RecHits that are not in CaloTowers
    #        continue
    #    towers[key][1] = 2*hit.energy()
        
        #print('[HF] iEta = %i, iPhi = %i, depth = %i; energy = %.2f' % (id.ieta(), id.iphi(), id.depth(), hit.energy()), id.subdet())

    for i,gp in enumerate(genparticles):
        gen_e[0]   = gp.energy()
        gen_pt[0]  = gp.pt()
        gen_eta[0] = gp.eta()
        gen_phi[0] = gp.phi()
        #print('gen pt,eta,phi = ', gp.pt(), gp.eta(), gp.phi())
        
        # Calculate track deflection in magnetic field
        mcparticle = ROOT.TParticle(gp.pdgId(), 1, 0, 0, 0, 0, gp.px(), gp.py(), gp.pz(), gp.energy(), gp.vx(), gp.vy(), gp.vz(), 0.)
        track = ROOT.TEveTrack(mcparticle, i, prop)
        track.MakeTrack()
        x = []
        y = []
        points = prop.GetLastPoints()
        for point in points:
            x.append(point[0])
            y.append(point[1])
        v1 = ROOT.TVector2(gp.px(), gp.py())
        v2 = ROOT.TVector2(x[-1], y[-1])
        deflection = v1.DeltaPhi(v2)
        # print('pt = %.2f' % gp.pt())
        # print('deflection = %.4f (%.2f deg)' % (deflection, deflection/2/math.pi*360.))
        # gen_phi[0] = gp.phi() + deflection

        # reset
        reco_n[0] = 0
        reco_sume[0] = 0.
        reco_offe[0] = 0.
        raw_sume[0] = 0.
        raw_offe[0] = 0.
        pf_sume[0] = 0.
        pf_offe[0] = 0.
        pfcalo_sume[0] = 0.
        pfcalo_offe[0] = 0.
        pfch_sume[0] = 0.
        pfch_offe[0] = 0.
        for i in range(max_ntower*max_ndepth):
            reco_e[i]  = 0.
        for i in range(max_ntower):
            reco_eta[i] = 0.
            reco_phi[i] = 0.
            reco_ieta[i] = 0
            reco_iphi[i] = 0
        
        for key,depths in reco.items():
            if reco_n[0] == max_ntower:
                break
            
            eta, phi = towerEtaPhi[key]
            phi += deflection
            
            dEta = eta - gen_eta[0]
            dPhi = ROOT.TVector2.Phi_mpi_pi(phi - gen_phi[0])
            #print(dEta, dPhi)
            if math.sqrt(dEta**2 + dPhi**2) < deltaR:
                #accept
                reco_n[0] += 1
                reco_eta[reco_n[0]] = eta
                reco_phi[reco_n[0]] = phi
                reco_ieta[reco_n[0]] = key[0]
                reco_iphi[reco_n[0]] = key[1]
                # if key in calotower:
                    # print(key)
                    # print(calotower[key])
                    # print(depths)
                # MAHI
                for d,de in depths.items():
                    idx = reco_n[0]*max_ndepth + d
                    reco_e[idx] = de
                    reco_sume[0] += de
                # M0
                for d,de in raw[key].items():
                    raw_sume[0] += de
            # off-angle energies
            for op in offPhis:
                dEta = eta - gen_eta[0]
                dPhi = ROOT.TVector2.Phi_mpi_pi(phi + op - gen_phi[0])
                if math.sqrt(dEta**2 + dPhi**2) < deltaR:
                    # MAHI
                    for d,de in depths.items():
                        reco_offe[0] += de / len(offPhis)
                    # M0
                    for d,de in raw[key].items():
                        raw_offe[0] += de / len(offPhis)
        
        for pf in pfcandidates:
            eta = pf.eta()
            phi = pf.phi()
            if pf.charge() == 0:
                phi += deflection
            dEta = eta - gen_eta[0]
            dPhi = ROOT.TVector2.Phi_mpi_pi(phi - gen_phi[0])
            if math.sqrt(dEta**2 + dPhi**2) < deltaR:
                de = pf.ecalEnergy() + pf.hcalEnergy()
                pfcalo_sume[0] += de
                pf_sume[0] += pf.energy()
                if pf.charge() != 0:
                    pfch_sume[0] += pf.energy()
            for op in offPhis:
                dEta = eta - gen_eta[0]
                dPhi = ROOT.TVector2.Phi_mpi_pi(phi + op - gen_phi[0])
                if math.sqrt(dEta**2 + dPhi**2) < deltaR:
                    de = pf.ecalEnergy() + pf.hcalEnergy()
                    pfcalo_offe[0] += de / len(offPhis)
                    pf_offe[0] += pf.energy()
                    if pf.charge() != 0:
                        pfch_offe[0] += pf.energy()

        t.Fill()

f.Write()
f.Close()

exit(0)