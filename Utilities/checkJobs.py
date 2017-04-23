import sys, os, subprocess

def Run(cmd):
    START_W = '\n\033[1;33m-> '
    END_W = '\033[0m'
    print START_W + cmd + END_W
    subprocess.Popen(cmd,shell=True).wait()

currDir = os.getcwd()
xmlFiles = [fileName for fileName in os.listdir(currDir) if 'xml' in fileName[-3:]]
for xmlFile in xmlFiles:
    cmd = 'project.py --xml %s --status' %xmlFile
    Run(cmd)
