import os, sys, argparse

def Warning(string):
    START_W = '\033[1;32m'
    END_W = '\033[0m'
    print START_W + string + END_W

def GenerateFiles(inDir,outDir,ef):
    Warning('Generating .hepevt text files...')
    fileNames = os.listdir(inDir)
    filePaths = [inDir+fileName for fileName in fileNames]

    for inFileName,inFilePath in zip(fileNames,filePaths):
        print 'Splitting file %s...' %inFileName
        # Get metadata
        title = '.'.join(inFileName.split('.')[:-1])
        meta = title.split('_')
        channel = int(meta[1].replace('channel',''))
        mass = float(meta[2].replace('mass',''))
        n = int(meta[3].replace('n',''))
        nf = n/int(ef)
        # Make sure events are evenly distributed among all files
        if n%int(ef)!=0:
            raise Exception('Number of events in each file must be a divisor of total number of events!')
        zNum = len(str(nf)) # Number of digits in number of files (to keep same-length filenames)
        # Create output directories
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        dirName = outDir+'SterileEvents_channel%i_mass%g_n%i_nf%i_ef%i' %(channel,mass,n,nf,ef)
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        else:
            raise Exception('Directory %s already exists!' %dirName)

        # Open file containing list of files
        if not os.path.exists(outDir+'Lists'):
            os.makedirs(outDir+'Lists')
        listName = 'sterileEvents_channel%i_mass%g_n%i_nf%i_ef%i.list' %(channel,mass,n,nf,ef)
        fList = open(outDir+'Lists/'+listName,'w')
        # Open original file and list file
        fIn = open(inFilePath)
        # Initialize loop variables
        nOutFile = 0 # Number of current output file
        nStrOutFile = str(nOutFile).zfill(zNum) # Number of current output file as zfill string
        nEvent = 0 # Number of current event (in current file)
        nEventTot = 0 # Number of current event (in total)

        outFileName = title+'_%s.hepevt' %nStrOutFile
        outFilePath = dirName+'/'+outFileName
        fOut = open(outFilePath,'w')
        fList.write(outFilePath+'\n')
        for line in fIn:
            x = line.split() # Split line
            # if line is event line, increase event counter
            if len(x)==2:
                nEvent += 1
                nEventTot += 1
            # if file still needs events, write down events, otherwise move to new file
            if nEvent <= ef:
                fOut.write(line)
            else:
                nOutFile = nOutFile + 1
                nStrOutFile = str(nOutFile).zfill(zNum)
                outFileName = title+'_%s.hepevt' %nStrOutFile
                sys.stdout.write('\rWriting file %i of %i.' %(nOutFile,nf))
                sys.stdout.flush()
                outFilePath = dirName+'/'+outFileName
                fOut = open(outFilePath,'w')
                fList.write(outFilePath+'\n')
                fOut.write(line)
                nEvent = 1
        sys.stdout.write('\r\033[K'+'File splitted.'+'\n')


def main():
    # Parser snippet
    path = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', required=False, default=path+'/Originals', help='Directory containing input files', type=str)
    parser.add_argument('-o','--output', required=False, default='/pnfs/uboone/scratch/users/sporzio/GridFiles/HeavySterileNeutrinos/TextFiles/', help='Output directory', type=str)
    parser.add_argument('-ef','--eventsPerFile', required=False, default=20, help='Number of events in each file (must be a divisor of total number of events)', type=int)

    args = parser.parse_args()
    # Make sure input and output paths end in '/', for consistency
    if args.input[-1]!='/':
        args.input += '/'
    if args.output[-1]!='/':
        args.output += '/'

    GenerateFiles(args.input,args.output,args.eventsPerFile)

if __name__ == '__main__':
    main()
