#! /usr/bin/env python

import ROOT
import math
import numpy as np

ROOT.gSystem.IgnoreSignal(ROOT.kSigSegmentationViolation, False)

r_hcal = 185.

pdg = ROOT.TDatabasePDG()
prop = ROOT.TEveTrackPropagator('prop', '', ROOT.TEveMagFieldConst(0., 0., -3.8))
prop.SetStepper(ROOT.TEveTrackPropagator.kRungeKutta)
prop.SetMaxR(r_hcal)
prop.SetMaxStep(2.)

pts = np.logspace(0, 3) #[1, 2, 4, 10, 20, 50]
deflections = []

for i,pt in enumerate(pts):
# pt = 1.2
    pid = 211

    p = ROOT.TLorentzVector()
    p.SetPtEtaPhiM(pt, 0, 0, pdg.GetParticle(pid).Mass())
    v = ROOT.TLorentzVector()

    mcparticle = ROOT.TParticle(211, 1, 0, 0, 0, 0, p, v)

    track = ROOT.TEveTrack(mcparticle, i, prop)
    track.MakeTrack()

    x = []
    y = []
    points = prop.GetLastPoints()
    for point in points:
        # print(point[0], point[1], point[2], point[3], math.sqrt(point[0]**2 + point[1]**2))
        x.append(point[0])
        y.append(point[1])

    v1 = ROOT.TVector2(p.Px(), p.Py())
    v2 = ROOT.TVector2(x[-1], y[-1])
    deflection = v1.DeltaPhi(v2)
    deflections.append(deflection)
    print('pt = %.2f' % pt)
    print('deflection = %.4f (%.2f deg)' % (deflection, deflection/2/math.pi*360.))
    
    prop.ResetTrack()

# del(prop)

# getTrackDeflection(1.)
# getTrackDeflection(5.)
# getTrackDeflection(10.)
# getTrackDeflection(20.)
# getTrackDeflection(50.)

import matplotlib.pyplot as plt
plt.plot(pts,deflections)
plt.xscale('log')
plt.show()