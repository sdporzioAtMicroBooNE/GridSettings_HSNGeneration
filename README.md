Generation of HSN events on the Grid@Fermilab

* Modify settings in `Utilities/generateProjects.py`
* Then run `./generateEnvironment.sh`, which will creates the XML and FHICL files from the samples and copy them to `/pnfs`
* Run `./launchProjects.sh` to run the first _project.py_ job, then modify the arguments to run the followings.

