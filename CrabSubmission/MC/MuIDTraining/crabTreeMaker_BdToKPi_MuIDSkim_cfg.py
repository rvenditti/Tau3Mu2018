from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SkimMuID_BdToKPi_SoftQCDnonD_2018_CMSSW_10_2_1_v3'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/lustrehome/venditti/Tau3Mu2018_final/CMSSW_10_2_1/src/SkimTools/SkimTau3Mu/test/run_MC_2018_PatAndTree_MuonID_cfg.py'
config.Data.inputDataset = '/BdToKPi_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v2/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 7
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'SkimMuID_BdToKPi_SoftQCDnonD_2018_CMSSW_10_2_1_v3'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
#config.Site.ignoreGlobalBlacklist  = True
