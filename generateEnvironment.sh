run(){
  COLOR='\033[1;33m'
  DEFAULT='\033[0m'
  echo -e "${COLOR}-> ${1}${DEFAULT}";
  eval ${1};
}

run 'rm -r Utilities/OutputXml/*'
run 'rm -r Utilities/OutputFcl/*'
run 'rm launchProjects.sh'
run 'python Utilities/generateProjects.py'
run 'chmod +x launchProjects.sh'
