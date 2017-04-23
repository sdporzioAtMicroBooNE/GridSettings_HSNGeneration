Generation of HSN events on the Grid@Fermilab

* Place .hepevt files in `TextFiles/Originals/`.
* They must be in the format `sterileEvents_channel1_mass0.16_n20000.hepevt`.
* Then run `source generateEnvironment.sh`, which will split the .hepevt files into smaller files and generate xml files to send those files to the grid.
* Run `source launchProjects.sh` to run the first _project.py_ job, then modify the arguments to run the followings.