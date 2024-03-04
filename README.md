# apptainer_demo
Demonstration for using Apptainer with HPC resources (Compute Canada, UBC Sockeye).

## Folder/File Structure
- suite2p/ 
    - suite2p_env.yml # environment setup file
    - suite2p_example.py # suite2p running file
    - suite2p.def # definition file for Apptainer
    - suite2p.sif # apptainer image with suite2p
    - example_data/
        - *.tif # data to analyze
        - suite2p/ # analysis folder created by running the .py
            - plane0/
            - op.npy
            - stat.npy
            - data.bin
            - …
## Apptainer Setup
1. On a Linux machine, prepare an Apptainer image. An Apptainer image is a “container” made up of an operating system and packages. This “container” can access files and folders on your computer, meaning you can run code using this “container” instead of your own operating system. This is necessary for running conda environments on Compute Canada.
    - Download Apptainer here (Linux only): [https://apptainer.org/docs/user/main/quick_start.html](https://github.com/apptainer/apptainer/blob/main/INSTALL.md)
2. We have provided suite2p.def and suite2p.yml for creating an Apptainer image with the suite2p conda environment.
    - Run this command to create the container: `apptainer build suite2p.sif suite2p.def`
    - This makes an Apptainer image named suite2p.sif.

## Input Setup
3. In the main directory on your computer:
    1. Create a new folder (in the same directory of your .sif) to store the microscope images that you want to process. In our example, we created “example_data” with data obtained from 
    2. Move your TIF/TIFF files into this folder.
        - The location of these files will be your data path.
        - Refer to: https://suite2p.readthedocs.io/en/latest/inputs.html for TIF image formatting.
4. Modify the suite2p_example.py file as necessary:
    1. “data_path” should be the relative path to the folder containing your TIF images (created in Step 3). Ensure your db “data_path” is accurate and has “/mnt” as a prefix (re: “Info on Paths” section of “Apptainer Notes” below).
    2. Ensure your settings are correct. https://suite2p.readthedocs.io/en/latest/settings.html 
5. Upload files to your folder (`/projects/ctb-tim/<username>`) on the Compute Canada Cedar server using secure file transfer protocol: 
   1. Open terminal and navigate to the directory that contains suite2p.sif.
   2. Run `sftp <username>@cedar.computecanada.ca` and log in.
   3. Navigate to your /projects/ctb-tim/<username> directory and `mkdir suite2p`. `cd suite2p` to go into it.
   4. Use commands `put` (for individual files) and `put -r` (for folders) to transfer the files from your computer to the remote server. You will need suite2p.sh, suite2p.sif, suite2p_example.py, and the folder with your data.
6. Log into Compute Canada with `ssh <username>@cedar.computecanada.ca`.
7. Edit the bash script with `nano suite2p.sh`. Make sure the computing distribution is correct.
8. Submit the bash script as a job with `sbatch suite2p.sh`.

## RESOLVING ERRORS:
- “DiskUsage: ...”
    - Follow the instructions here for the newly created folders to be considered within your professor’s computing group. 

# Apptainer Notes:
- Before you can use Apptainer in Compute Canada, run this command: `module load apptainer`. Otherwise, there will be a slurm output message with a module error that says “apptainer not found”.
- Here is the command we use to run our code:
    - `apptainer run -C -B .:/mnt -W ${SLURM_TMPDIR} suite2p.sif python /mnt/suite2p_exec.py`
        - `apptainer run`: calls the apptainer program and its runscript
        - `-C`: isolates the container from all of the file systems
        - `-B .:/mnt`: binds everything in the current directory to a folder called “/mnt” in the container
        - `-W ${SLURM_TMPDIR}`: sets the working directory as the SLURM temporary directory address, where there is more RAM
        - `suite2p.sif`: the Apptainer image to use
        - `python /mnt/suite2p_exec.py`: command to run the python file in the Apptainer

INFO ON PATHS: When your code runs in the container, it can only look at the files on your computer in the same directory that your .sif file is in. These files will be available in the container’s “/mnt” directory. Ensure that all the paths that you reference in your code are relative and have “/mnt” in front of them, or else you will get a “file not found” error.

# Compute Canada Notes
- You will need to sign up for an account. Ask Tim for his sponsorship information so he can add you to his group.
- Use the ctb-tim group. This allows you to use his allocated CPU processing (200? cores) and data storage (400 TB).
- Helpful keyboard shortcuts:
    - Press tab to auto-complete files/directory names
    - Alt+left/right arrow keys to move pointer to previous/next word
    - Up arrow key to cycle through previously run commands
- Helpful commands:
    - For scheduling tasks:
        - `sbatch <bash script>.sh`: submit a SLURM job
        - `sq`: check the current status of your jobs
    - For looking at files:
        - `nano <file name>`: edit the file
        - `cat <file name>`: preview the file in your command line
    - For navigation
        - `cd <directory>`: go to child directory
        - `cd ..`: go to parent directory
        - `ls`: list the current files and directories in your current directory
        - `pwd`: view your current path
    - For managing files:
        - `mkdir`: make a directory
        - `rm <file>`: delete a file
