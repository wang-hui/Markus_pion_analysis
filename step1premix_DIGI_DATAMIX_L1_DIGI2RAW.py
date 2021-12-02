# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --mc --eventcontent PREMIXRAW --runUnscheduled --datatier GEN-SIM-DIGI --conditions 106X_upgrade2018_realistic_v11_L1v1 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run2_2018 --filein file:GEN-SIM.root --fileout file:DIGI.root --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL18_106X_upgrade2018_realistic_v11_L1v1-v2/PREMIX
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.ProcessModifiers.premix_stage2_cff import premix_stage2

process = cms.Process('DIGI2RAW',Run2_2018,premix_stage2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDM_cff')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
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

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:DIGI.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/001C891A-19C5-C54C-A5A0-7EFA425D0693.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/001F4A9F-FE7E-1040-AA4B-B02AC0C95C8A.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/004199A2-21D8-294C-A748-B178E761871D.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/00586595-F81F-1747-9685-C5452078524B.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/00592F3D-22A8-5A43-A4E4-4B785EA13FFD.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/005BCE5C-27F9-1640-9905-8E5B0FE01FF7.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/00F3B621-CAF8-974D-8C91-346D7581BE22.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/01174EB8-55DF-A249-A1A5-27CE948F49C0.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0174B84E-E07F-634F-B5B9-A26371C8C91B.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/01894993-1D4E-714F-8A98-A3DE88289039.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/01A5E4BD-B6C2-5A42-B97E-8E02986F5BA5.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/01AF0715-3F0F-7341-A109-77786ED8CA27.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/01EF27FD-B6B0-B046-BC2A-FC19EDB0AF6B.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/01F9EF3C-6F85-7948-82B5-A9A84CE9D863.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/02315C75-6C62-0841-B8DC-89C982A4FBE2.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0263DA56-9666-E74F-AD05-A93FC37BEAF3.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0269B5AB-7567-3140-A654-053534720C2D.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/029DBF25-6E9E-7F44-B92E-429478C4BF86.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/02D99E30-9AAD-AC4D-BCEC-AA33B987EFEA.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/03501462-16D2-1B45-8A96-5EE8F5D410B1.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/03512D55-E760-7D40-91AD-70F96C91D615.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0353A60D-2F35-FE49-85EF-24E402BFA7EE.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/03C47C02-BD33-8F49-BE60-72759C0094D3.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/03F15756-5DC5-874C-9FE7-A0BE75A69393.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/041AF311-A4F9-B744-B79B-DDF54F0D38FE.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/04285775-E145-1C44-A76C-41E904F15445.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/044974AA-41A1-354E-9136-95940C76B0E4.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/04620A94-8F67-AD45-ACCB-2A333DDF77E0.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/04706CE3-4097-264C-AC6E-C00D013B94B6.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/05586370-9F20-FE4C-908E-EFF41F48D761.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/056A7A24-2361-214E-A382-5ACC7428EC53.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/05A59642-A6F2-504F-9FD9-C4A4548A5510.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/05DA709E-FF84-6343-8C58-15E7290BBD23.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/06BB8EDE-2413-FA4E-8447-3EADA7FD5D56.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/06C718BB-842A-1642-8AF2-9F163D9A1E5C.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/06D19AFD-5157-9E41-A3A8-E1B12AA28880.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/06D9E87D-E79D-FB40-BFFD-0845C1B4519C.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/07554937-7D86-5745-AD1C-E5F6E422923E.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/07878BDA-8793-5343-A3A3-D1BE8B9F1A73.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/078C759B-8997-DD43-B778-C555A0F94F95.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/07A19D1E-10DE-DA45-9904-867F391A6128.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/07AB526C-52BB-D547-9A3F-6EFE30BC2292.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/07B6F8C6-68AE-5C41-9599-8E4D59837AFF.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0834AD7F-1AAD-364A-857E-5B4FEB2D05B0.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/088102EF-8F90-CF4B-BEC5-B096E7246540.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/097EAACF-1982-D64E-8207-D7D261949B62.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/09AC921A-9C28-7C42-A80F-798AD63154AE.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/09F1348E-B104-6748-87A6-D83A3BEDA09D.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/09F4EFAA-946B-BC44-A42C-FC07866EC667.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0A1A8E96-F55B-C742-BB67-49045E2A7BA1.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0A36EDF4-0EDF-854F-9188-E6B0796FF13B.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0AA61BF8-AA7D-B043-BE75-813ABFF571DE.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0AD72669-4056-E442-8E1E-FD26ABB4762C.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0AEBD58A-2870-254E-8977-9B6A62DBBC64.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0B528749-060C-3746-8D28-3C4676526D01.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0B6D60A3-95C7-E446-A2EA-8DD262CD2544.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0B72B789-A66F-2243-8288-E1A111B3E28A.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0B8D1800-2BCB-9B4D-9623-866C6A4813DF.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0B9C8936-80BC-9641-818F-947ACBA8C079.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0BA4D6B2-0973-0D44-9584-CEE33F7E06FA.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0BEF3F50-CE68-3C47-ACF0-E5153E916EA3.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0C25B436-7514-C54A-96B3-DC5BF6805014.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0C312BD7-34D3-2E40-B3E2-DB158D9320B0.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0C66E16D-C0EF-DD4E-BC72-528E56341F02.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0C9138E9-39AE-2541-839C-93EE3BBCB0F4.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0D0371F7-CEE0-B44C-A159-FFA22872CF65.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0D2DC56E-A15A-1549-A0D6-9CDAC3F5F03C.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0D2E2C47-BAE4-B241-8330-C58E136F67FE.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0D893A99-B041-A94F-9316-C0F4BB0852FC.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0DE64BE7-258E-3741-8AC4-B8150F52AE0C.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0DEC762C-5566-7D4E-8E4E-AD83CFD4FEC4.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0E0491BC-AB44-8141-A675-169A2551AF60.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0E582F7A-0D47-4949-9ECC-58482291EF2C.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0E6B764F-BBB7-E346-B9ED-FBA60D303F53.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0E7DB64A-634C-3045-ABE3-72F094AA283B.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0EF4D46B-DE4D-9A42-8C6B-08341DD59EC7.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0EFA4CD8-3495-D64E-8324-90406494B0C4.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0F01C0B6-0BD2-994E-99A3-7A983392D6E5.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0F46BE0B-367A-2746-8EE6-AAAF733D46C8.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0F5CA101-5167-8841-8A12-87E7CABE480E.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/0F64F6A4-B6F4-704B-B55A-72B7C7027A9A.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/10648740-D34F-734A-B086-74E5F40EE5CB.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/10A1259A-041A-1349-A0A3-428A00066DEB.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/10C6B445-E4A5-A34B-B4C8-A9D1B09DA89D.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/1134B4CD-324B-2B44-AEE0-814EFE2E3944.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/118DBAAC-905D-BB48-9999-87E4F80FE61F.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/1201EFAC-671F-A54B-B2F1-667A58FE54B7.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/12023378-ABC0-3B4C-A343-FD9D88434EBF.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/120487D1-A629-C84A-BD7B-3F4E16866102.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/12052FAE-75CE-6343-8A14-D24374156483.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/1277B4DB-2995-3D4C-8D17-BDCBCA7088A0.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/129E2C50-CAB0-A34F-B85C-84DF0EA220AC.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/12AF8C1A-44F0-2448-B2BB-797E0EC67BA5.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/136C9706-005E-FE4D-BC4A-E64322FDEA57.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/13A54D70-76F2-C541-AF22-FFD0309328C0.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/142F3921-BFBD-504E-A8A1-91029D2FDE94.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/144D0E80-1EE4-9049-B694-7195B4A05B8E.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/14941287-F82D-B744-8C13-DCBBEDE6085E.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/14F753FE-4B3C-6D4B-9943-CB1D91BF2795.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/154EF244-7459-7948-ADE0-FF3664AD0C4B.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/15BC3377-E9ED-D045-9391-EC78C4E0AFFE.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/15D507F5-5A48-5946-96D8-180D837F5210.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/15E551C7-5CFC-EF4E-9381-B97C93BC3DE5.root', '/store/mc/RunIISummer20ULPrePremix/Neutrino_E-10_gun/PREMIX/UL18_106X_upgrade2018_realistic_v11_L1v1-v2/00000/16612B37-E600-924A-B0A7-88808D105A94.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v11_L1v1', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.PREMIXRAWoutput_step)
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
