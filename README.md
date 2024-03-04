# apptainer_demo
Demonstration for using Apptainer with HPC resources (Compute Canada, UBC Sockeye).

# Apptainer Notes:
- Before you can use Apptainer in Compute Canada, run this command: `module load apptainer`. Otherwise, there will be a slurm output message with a module error that says “apptainer not found”.
- Here is the command we use to run our code:
    - `apptainer run -C -B .:/mnt -W ${SLURM_TMPDIR} <sif_file>.sif python /mnt/<code_file>.py`
        - `apptainer run`: calls the apptainer program and its runscript
        - `-C`: isolates the container from all of the file systems
        - `-B .:/mnt`: binds everything in the current directory to a folder called “/mnt” in the container
        - `-W ${SLURM_TMPDIR}`: sets the working directory as the SLURM temporary directory address, where there is more RAM
        - `<sif_file>.sif`: the Apptainer image to use
        - `python /mnt/<code_file>.py`: command to run the python file in the Apptainer

INFO ON PATHS: When your code runs in the container, it can only look at the files on your computer in the same directory that your .sif file is in. These files will be available in the container’s “/mnt” directory. Ensure that all the paths that you reference in your code are relative and have “/mnt” in front of them, or else you will get a “file not found” error.