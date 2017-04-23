import os, sys, argparse

def Warning(string):
    START_W = '\033[1;32m'
    END_W = '\033[0m'
    print START_W + string + END_W

Warning('Generating xml files...')
path = os.path.dirname(os.path.realpath(__file__))
inDir = path+'/../TextFiles/Output'
outDir = path+'/Output'

fileNames = os.listdir(inDir)
fileNames.remove('Lists')
filePaths = [inDir+fileName for fileName in fileNames]
textIn = open(path+'/sample.xml').read()

launcher = open(outDir+'/../../launchProjects.sh','w')
for inFileName,inFilePath in zip(fileNames,filePaths):
    # Get metadata
    title = inFileName
    meta = title.split('_')
    channel = int(meta[1].replace('channel',''))
    mass = float(meta[2].replace('mass',''))
    n = int(meta[3].replace('n',''))
    nf = int(meta[4].replace('nf',''))
    ef = int(meta[5].replace('ef',''))
    # Replace text in sample
    textOut = textIn.replace('${MASS}',str(mass))
    textOut = textOut.replace('${CHANNEL}',str(channel))
    textOut = textOut.replace('${N}',str(n))
    textOut = textOut.replace('${EF}',str(ef))
    textOut = textOut.replace('${NF}',str(nf))
    # Open outfile and save
    outName = 'gridSettings_channel%i_mass%g_n%i_nf%i_ef%i.xml' %(channel,mass,n,nf,ef)
    fOut = open(outDir+'/'+outName,'w')
    fOut.write(textOut)
    launcher.write('project.py --xml Xml/Output/gridSettings_channel%i_mass%g_n%i_nf%i_ef%i.xml --stage gen --submit\n' %(channel,mass,n,nf,ef))
