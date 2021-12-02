# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --mc --eventcontent RAWSIM --runUnscheduled --pileup 2018_25ns_UltraLegacy_PoissonOOTPU --datatier GEN-SIM-DIGI --conditions 106X_upgrade2018_realistic_v11_L1v1 --step DIGI,L1,DIGI2RAW --nThreads 4 --geometry DB:Extended --era Run2_2018 --filein file:GEN-SIM.root --fileout file:DIGI.root --pileup_input dbs:/MinBias_TuneCP5_13TeV-pythia8/RunIISummer20UL18SIM-106X_upgrade2018_realistic_v11_L1v1-v2/GEN-SIM
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('DIGI2RAW',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:GEN-SIM.root'),
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:DIGI.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.Special_Pileup_Studies = cms.untracked.string("Fixed_ITPU_Vary_OOTPU")
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/00412F76-3FA8-1B4F-8EA3-671953558471.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/007253BB-FBB3-0641-8E38-2F6F9DA1E03C.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/007D004A-FD76-7E4D-9886-694E908179AE.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/007DE848-C52C-1F46-8991-7B811097AA85.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/008FB9E9-0DCB-8943-8E94-A60152C440AA.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/00912350-E69F-034B-B572-003E9F2A322A.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/00AF7D54-DAE0-1440-8A2B-614A4A326FDE.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/00C6BCEA-3FD2-8F40-A875-E7248569195A.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/00CA4785-5056-774E-B5A1-F6F25229054F.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0103D625-F483-4647-89F2-1239C4D0473F.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/01457076-33BD-BE41-81CE-46AF1F86FBFF.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/01636FE9-8830-D143-A1A4-3EF5891050F9.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/01737916-9726-F24D-910D-E025B49E799A.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/01905344-F241-3B41-A422-1D3F76335798.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/01D12F00-CF18-B04D-829A-DBC5753126F1.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/01E7BE7A-CFF7-9A48-ADCF-1F9225C4C49B.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/02154D4F-9646-3649-AEBF-40F788187BCC.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/021A7971-3926-6143-B786-1BF3F761356C.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/02318D18-D338-0A4F-93DB-FD5379F3AD92.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/02670844-0058-7944-9A55-3E69457AEA75.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/02CA3465-6924-1D41-BDF5-D7A5930676D8.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0340DC50-42DD-3D4D-BEED-FE6ED7068F94.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/03775862-7FD3-D84F-AF26-58ABC2CFCEC1.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/03884A52-39CE-6B4C-AB94-90BDC9A072BF.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/03B573C8-52BD-594C-8A1C-38EF9FDEA79F.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/03BA78E8-DB50-A442-98B8-7A5382CD2420.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/03E64D3D-A78B-2B40-BB0D-0408C9966F9A.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/041E0287-437E-FC49-BF14-AC2CF2F98ED5.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/04218B43-F263-994F-BE24-2FA39A66D890.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0423F636-CBDE-3846-B0D0-FAB475E21B7D.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/044D1671-CB65-2A4A-A6E5-E4DD1CFF5C1B.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0463979D-9F39-D340-8E9B-006CF3F1D559.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0469248F-D7E4-D74B-B43B-2F9D5A4B0317.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/04C0C19B-0461-5D48-A2E1-7C2FB2CAC20C.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/04E33728-36F8-BE44-BF74-AEF87F38CEFF.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/04E5C6DF-4418-AF48-8A67-5D5736E8304A.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/04FCC4FF-260E-F744-A793-E7AF371979ED.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0511B12E-3406-D447-A2DB-3834271298C6.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/051BE759-3A25-4646-9BD8-F90A48EE2169.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/052FA0C5-50E6-A640-A516-0D6A934B120F.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0532F1EA-7308-5E42-B675-41B3F677FCB7.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0542854A-0D9C-ED43-B275-88E48E1BAE7E.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/056B0E58-BE79-D14B-B782-3AF5D1219CA6.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/056DCB28-B069-CF4F-879A-085A6FE61181.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/05705CF5-CB65-994E-831A-022C9C95F236.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/057F5743-7172-9244-81DA-7E7A40BDDB67.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0599E7FA-7702-D14D-BA15-8772FE2EA31E.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/05B46181-70A7-AD4B-87A8-D30AFB58D2E5.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/05C95350-6A58-3947-BBA3-6F8B72EA6309.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/05E2352D-CE7B-234C-B6B7-8371A020E7B4.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/05F0390B-EE18-0240-AA41-C8B22B214446.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/06134101-C61A-214E-BA03-604381371FF4.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/063A4CE3-5B2F-564D-9E2C-8A68CB619A18.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0642CBBC-8FC8-2042-9CFD-0374BB15A08E.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/066288AE-1213-E14E-84CC-79FD74592202.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/067169B4-137C-3F41-B958-826F4332329B.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/067EA987-7CDA-0743-99D6-1CB36BB5AA51.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/06A0436F-B098-334E-8EC3-204608BFDF7D.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/06C21C43-018F-9648-BBF5-F73516F46A48.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/0726059D-EF6B-A041-94E7-EA8CA169E28F.root', '/store/mc/RunIISummer20UL18SIM/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/106X_upgrade2018_realistic_v11_L1v1-v2/120000/07350C95-BEFE-BE4C-BFD3-70B976A77535.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v11_L1v1', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
