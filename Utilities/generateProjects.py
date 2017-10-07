import os, sys, argparse, shutil

# Settings
nEvents = "50000"
nJobs = str((int(nEvents)/int(20)))
dataSets = []
dataSets.append(["1","0.250",nEvents,nJobs])
dataSets.append(["1","0.350",nEvents,nJobs])
dataSets.append(["1","0.450",nEvents,nJobs])
dataSets.append(["2","0.150",nEvents,nJobs])
dataSets.append(["2","0.300",nEvents,nJobs])
dataSets.append(["2","0.450",nEvents,nJobs])

def Warning(string):
    START_W = '\033[1;32m'
    END_W = '\033[0m'
    print START_W + string + END_W

def GenerateFCL(dataSets):
    Warning('Generating fcl files...')
    path = os.path.dirname(os.path.realpath(__file__)) # Get path to current directory
    textIn = open(path+'/sampleProdFcl.fcl').read() # Get sample text of the Xml file
    outDir = path+'/OutputFcl' # Prepare output directory
    for i,dataSet in enumerate(dataSets):
        # Get metadata
        channel = dataSet[0]
        mass = dataSet[1]
        n = dataSet[2]
        nj = dataSet[3]
        # Replace text in sample
        textOut = textIn.replace('${MASS}',mass)
        textOut = textOut.replace('${CHANNEL}',channel)
        textOut = textOut.replace('${N}',n)
        textOut = textOut.replace('${NJ}',nj)
        # Open outfile and save
        outName = 'prodHsn_channel%s_mass%s_n%s.fcl' %(channel,mass,n)
        fOut = open(outDir+'/'+outName,'w')
        fOut.write(textOut)
        fOut.close()
        print "Copying file %i of %i." %(i+1,len(dataSets))
        shutil.copy2(outDir+'/'+outName,'/pnfs/uboone/scratch/users/sporzio/GridFiles/HeavySterileNeutrinos/'+outName)

def GenerateXML(dataSets):
    Warning('Generating xml files...')
    path = os.path.dirname(os.path.realpath(__file__)) # Get path to current directory
    textIn = open(path+'/sampleXml.xml').read() # Get sample text of the Xml file
    outDir = path+'/OutputXml' # Prepare output directory
    for dataSet in dataSets:
        # Get metadata
        channel = dataSet[0]
        mass = dataSet[1]
        n = dataSet[2]
        nj = dataSet[3]
        # Replace text in sample
        textOut = textIn.replace('${MASS}',mass)
        textOut = textOut.replace('${CHANNEL}',channel)
        textOut = textOut.replace('${N}',n)
        textOut = textOut.replace('${NJ}',nj)
        # Open outfile and save
        outName = 'gridSettings_channel%s_mass%s_n%s.xml' %(channel,mass,n)
        fOut = open(outDir+'/'+outName,'w')
        fOut.write(textOut)
        fOut.close()

def GenerateShellScript(dataSets):
    Warning('Generating shell script...')
    currDir = os.path.dirname(os.path.realpath(__file__)) # Get path to current directory
    launcher = open(currDir+'/../launchProjects.sh','w')
    for dataSet in dataSets:
        # Get metadata
        channel = dataSet[0]
        mass = dataSet[1]
        n = dataSet[2]
        nj = dataSet[3]
        launcher.write('project.py --xml Utilities/OutputXml/gridSettings_channel%s_mass%s_n%s.xml --stage sim --submit\n' %(channel,mass,n))
    launcher.close()


GenerateFCL(dataSets)
GenerateXML(dataSets)
GenerateShellScript(dataSets)
