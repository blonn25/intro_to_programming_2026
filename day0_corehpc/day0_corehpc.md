# Day 0: Introduction to CoreHPC

This tutorial is designed to familiarize UCSF 1st year Biophysics students with CoreHPC and FAC - UCSF's primary High Performance Computing (HPC) resources. It covers everything from accessing your account to running your first job, providing the backbone knowledge required to efficiently use CoreHPC’s resources. By the end, you'll be comfortable navigating CoreHPC and setting up + submitting jobs.

Credit: Most of the information from this page was cobbled together using content from [CoreHPC's wiki](https://wiki.library.ucsf.edu/spaces/CHPC/overview) + some writing and rewriting by Beau Lonnquist.

### Outline
- [Day 0: Introduction to CoreHPC](#day-0-introduction-to-corehpc)
  - [What is CoreHPC?](#what-is-corehpc)
  - [What is FAC?](#what-is-fac)
  - [What is the difference between CoreHPC and FAC?](#what-is-the-difference-between-corehpc-and-fac)
  - [Accessing CoreHPC](#accessing-corehpc)
  - [Signing into CoreHPC](#signing-into-corehpc)
- [Running Your First Job: 'Hello World' on the CoreHPC Cluster](#running-your-first-job-hello-world-on-the-corehpc-cluster)
  - [Basics of Terminal Use](#basics-of-terminal-use)
  - [Running a 'Hello World' Job](#running-a-hello-world-job)
  - [CoreHPC ↔ Your Computer File Transfer](#files-transfer-between-your-computer-and-corehpc-with-scp)
- [Final Notes](#final-notes)
- [Need Help?](#Need-Help?)
---

### What is CoreHPC?

CoreHPC is UCSF’s next-generation high-performance computing (HPC) environment, designed to support large-scale data processing, AI-driven research, and compute-intensive scientific workloads. Featuring a mix of GPU and CPU resources, CoreHPC enables researchers to tackle massive, multidimensional datasets with remarkable speed and efficiency. 

Built on clustered, parallelized servers connected via a high-speed [InfiniBand interconnect](https://it.ucsf.edu/how-to/hpc-glossary/#infiniband), CoreHPC provides low-latency, high-bandwidth communication across nodes—ideal for tightly coupled scientific applications. 

All services are fully compliant with UC security policies and support [P1 through P4 data classifications](https://it.ucsf.edu/node/48310), ensuring confidentiality, integrity, and data protection. 

The CoreHPC environment is fully managed by UCSF’s HPC team—so you can focus on your data, code, and results without the burden of system administration. Usage reporting, consulting, and training options are available to help you run code at scale and make the most of the platform. 

Seamless integration with [FAC Capacity Storage](https://it.ucsf.edu/how-to/fac-capacity-storage) ensures streamlined workflows and persistent storage for long-term research projects. Learn more about [how CoreHPC and FAC work together](https://it.ucsf.edu/how-to/HPCfrequently-asked-questions/#worktogether).

### What is FAC?

The [Facility for Advanced Computing (FAC)](https://it.ucsf.edu/service/facility-advanced-computing-fac) at UCSF, managed by UCSF [Academic Research Services](https://ars.ucsf.edu/), provides secure, affordable, and scalable data storage and computing. The FAC supports a range of needs to enable researchers to meet their objectives: diverse storage offerings, server hosting, network isolation and computing services. FAC Capacity Storage, Virtual Machines and BaS physical servers are available now.

### What is the difference between CoreHPC and FAC?

CoreHPC is UCSF’s high-performance computing (HPC) environment designed for large-scale data processing, parallel workflows, and compute-intensive research. It offers access to powerful compute nodes, GPU acceleration, high-speed scratch storage, and Slurm-based job scheduling.

The [Facility for Advanced Compute (FAC)](https://it.ucsf.edu/service/facility-advanced-computing-fac), by contrast, is a broader research infrastructure platform focused on secure, compliant data services. FAC supports storage, virtual machine hosting, and server co-location, with a strong emphasis on IS-3 compliance and support for P1 through P4 data. Additionally, FAC provides foundational storage infrastructure that is directly accessible from within the CoreHPC environment, enabling seamless integration between compute and data services. 

### Accessing CoreHPC

Fortunately for you, you should already have access to CoreHPC compute and FAC storage resources and should not need to request an account. However, if you ever need to request an account in the future, you can do so by [submitting a ticket](https://redcap.ucsf.edu/surveys/?s=JAYNXF7FJ4AA94KX) to the UCSF [ARS](https://ars.ucsf.edu/) team.

To connect to CoreHPC, you will need to use the ***terminal***.

<details>
<summary>What is the terminal?</summary>
The **terminal** is a text-based interface that allows you to interact directly with your computer by typing commands, rather than using a graphical interface like clicking on icons. It might seem intimidating at first, but it's a powerful tool that gives you a lot of control over your computational environment.
</details>

Perform the following steps ():
1. Connect to the UCSF VPN (this is still required, even when connected to the UCSFwpa network).

2. Open the terminal:
  - On Mac: Use `command ⌘ + space ␣` to open Spotlight, then type "terminal" to open it.
  - (This tutorial assumes you're using Mac or Linux. See [WSL](http://google.com/search?q=Windows+Subsystem+for+Linux) for Windows users)

3. In the terminal, type:
  ```sh
  ssh <user>@chpc-ucsf-bastion-vm1.corehpc.ucsf.edu
  ```
  where <user> is your CoreHPC username. This is most likely your first initial followed by your last name. For example, if your name is Jane Doe, your username is likely `jdoe`, and you would type:
  ```sh
  ssh jdoe@chpc-ucsf-bastion-vm1.corehpc.ucsf.edu
  ```
  If you are unsure of your username, please contact the CoreHPC support team at [COREHPC-Support@ucsf.edu](mailto:COREHPC-Support@ucsf.edu).

4. Approve the MFA/DUO request sent to your mobile device.

<details>
<summary>If successful, you'll see the following message indicating you are now connected to the bastion host:</summary>

```console
jdoe@MacOS ~ % ssh jdoe@chpc-ucsf-bastion-vm1.corehpc.ucsf.edu
Autopushing login request to phone...
Success. Logging you in...
###############################################################################
#                       AUTHORIZED CoreHPC ACCESS ONLY                        #
#                                                                             #
#         This is a BASTION HOST. Do not perform work on this system.         #
#                   All sessions are logged and monitored.                    #
###############################################################################
[jdoe@chpc-ucsf-bastion-vm1 ~]$

```
</details>

Nice! You're now connected to the ***bastion host***. This is not the final destination, but a secure gateway that allows you to access the CoreHPC cluster. From here, you can connect to the login nodes of CoreHPC.

5. To connect to the login node, simply type:
  ```console
  ssh chpc-ucsf-login-vm1
  ```

6. Enter your password when prompted. This is the same password you use to log into your UCSF account.
  
<details>
<summary>If successful, you'll see the following message indicating you are now connected to the login node:</summary>

```console
[jdoe@chpc-ucsf-bastion-vm1 ~]$ ssh chpc-ucsf-login-vm1
(jdoe@chpc-ucsf-login-vm1) Password: 

                888     888   .d8888b.    .d8888b.   8888888888
                888     888  d88P  Y88b  d88P  Y88b  888
                888     888  888    888  Y88b.       888
                888     888  888          "Y888b.    8888888
                888     888  888             "Y88b.  888
                888     888  888    888        "888  888
                Y88b. .d88P  Y88b  d88P  Y88b  d88P  888
                 "Y88888P"    "Y8888P"    "Y8888P"   888

 Authorized for use by UCSF CoreHPC and Academic Research Services users only.
                 All activity may be monitored and reported.

          By using CoreHPC, users agree to abide by the CoreHPC User
       Agreement and Acceptable Use Policy: https://tiny.ucsf.edu/HPCUA

Last login: Fri Aug 28 10:39:40 2026 from <IP_ADDRESS>
[jdoe@chpc-ucsf-login-vm1 ~]$
```
</details>

CONGRATULATIONS! You are now connected to the CoreHPC cluster. You can now run jobs, transfer files, and perform other tasks on the cluster.

**IMPORTANT**: When you are finished using CoreHPC, make sure to log out of the cluster by typing `logout` in the terminal. You will need to do this twice: once to log out of the login node, and once to log out of the bastion host.

### Accessing CoreHPC via Open OnDemand (beta):

Instead of logging into CoreHPC via the terminal, you can also access CoreHPC via Open OnDemand (OOD). OOD is a web-based interface that allows you to access CoreHPC resources without using the terminal. It provides access to software such as MatLab, VSCode, R Studio and JupyterLab. You can access OOD by visiting [https://ood.corehpc.ucsf.edu](https://ood.corehpc.ucsf.edu) and logging in with your UCSF credentials.

Please note that OOD is currently in a beta development phase and changes may occur without warning. That said, please feel free to test OOD and send any comments, questions, feedback to [corehpc@ucsf.edu](mailto:corehpc@ucsf.edu).

---

## Running Your First Job: 'Hello World' on the CoreHPC Cluster

The CoreHPC cluster consists of a large number of compute nodes ready to execute users' tasks (jobs). Since all compute nodes are configured similarly, it doesn’t matter which node your analysis runs on. To manage resources and ensure fair use, CoreHPC uses a job scheduler, which places your jobs in a queue and allocates resources as they become available. CoreHPC's scheduler is called SLURM, which stands for Simple Linux Utility for Resource Management.

### Basics of Terminal Use

Before running jobs on CoreHPC, familiarize yourself with some basic terminal commands:

#### 1. `pwd`: Print Working Directory
- **Displays the current directory** you are in.
  ```sh
  [jdoe@chpc-ucsf-login-vm1 ~]$ pwd
  /home/remote/jdoe
  ```

#### 2. `ls`: List Directory Contents
- **Lists files and directories** in the current directory.
  ```sh
  [jdoe@chpc-ucsf-login-vm1 ~]$ ls
  Documents  Downloads
  ```
- (Note: `Documents  Downloads` is an example output. On CoreHPC, `~/` will most likely be empty.)

#### 3. `mkdir`: Make Directory
- **Creates a new directory**.
  ```sh
  [jdoe@chpc-ucsf-login-vm1 ~]$ mkdir tests

  [jdoe@chpc-ucsf-login-vm1 ~]$ ls
  Documents  Downloads  tests
  ```

#### 4. `cd`: Change Directory
- **Moves between directories**.
  ```sh
  [jdoe@chpc-ucsf-login-vm1 ~]$ cd tests
  [jdoe@chpc-ucsf-login-vm1 tests]$

  [jdoe@chpc-ucsf-login-vm1 tests]$ pwd
  /home/remote/jdoe/tests

  [jdoe@chpc-ucsf-login-vm1 ~]$ cd ..
  [jdoe@chpc-ucsf-login-vm1 ~]$ pwd
  /home/remote/jdoe
  
  [jdoe@chpc-ucsf-login-vm1 ~]$ ls
  Documents  Downloads  tests
  ```

### Running a 'Hello World' Job

Now that you're familiar with basic commands, let us set up and run a simple job!

#### Step 1: Create a Script

1. **Navigate to your home directory** (if not already there):
   ```sh
   [jdoe@chpc-ucsf-login-vm1 ~]$ cd ~
   ```

2. **Create a directory** to store your script (if not already created):
   ```sh
   [jdoe@chpc-ucsf-login-vm1 ~]$ mkdir tests
   ```

3. **Navigate to the `tests` directory**:
   ```sh
   [jdoe@chpc-ucsf-login-vm1 ~]$ cd tests
   ```

4. **Create a script** called `hello_world.sh`:
   ```sh
   [jdoe@chpc-ucsf-login-vm1 ~/tests]$ nano hello_world.sh
   ```
   - Use `nano` (a terminal-based text editor) to enter the following script:
     ```sh
     #!/bin/bash                      # Run job as a Bash shell [IMPORTANT]
     #SBATCH --job-name=hello_world   # Name of the job
     #SBATCH --output=hello.out       # Name of the output file
     
     srun echo "Hello world, I am running on node $HOSTNAME"
     sleep 10
     date
     ```
   - Save and exit the editor (`Ctrl+X`, then `Y`, then `Enter` if using `nano`).
   - Side-note: Of course, there are a plethora of terminal text editor other than `nano`. Notable ones are emacs, vi, vim, neovim, etc. Choose wisely! Obligatory xkcd:


<div align="center">
  <img src="https://imgs.xkcd.com/comics/real_programmers.png" alt="Real Programmers"/>
</div>


For future reference, here's a more detailed sample submission script provided by CoreHPC (more examples can be found on the [CoreHPC Submission Examples](https://wiki.library.ucsf.edu/spaces/CHPC/pages/736476672/CoreHPC+Submission+Examples) page):

```sh
#!/bin/bash
#SBATCH --mem=4g                # Job memory request.
#SBATCH --ntasks=1              # How many instances of the script will run, if using --nodes, set --ntasks to the same value.
#SBATCH --cpus-per-task=64      # How many CPUs per instance of the script will be needed.
#SBATCH --partition=gpu         # Run on partition "dgx" (e.g. not the default partition called "long").
#SBATCH --gres=gpu:1            # Allocate 1 GPU resource for this job.
### OPTIONAL
#SBATCH --nodes=13              # Run on 13 nodes (if resources available).  
                                #The number of ntasks should be set to the same number, e.g. --ntasks=13.

#Load all of your necessary modules.
module load nvidia/nvhpc/nvhpc-hpcx/25.5
module load openmpi5/5.0.7

#Uncomment to run a script on a single node, or resources in a single node.
#/path/to/gpu_script.py

#Uncomment when using --ntasks=n and/or --nodes=n [n>1], this is basically plug-n-play parallelism.  
#srun /path/to/gpu_script.py
```

#### Step 2: Make the Script Executable

5. **Change the file permissions** to make it executable:
   ```sh
   [jdoe@chpc-ucsf-login-vm1 tests]$ chmod ugo+x hello_world.sh
   ```

#### Step 3: Run the Script Directly

6. **Test the script** by running it directly (optional but recommended):
   ```sh
   [jdoe@chpc-ucsf-login-vm1 tests]$ ./hello_world.sh
   Hello world, I am running on node chpc-ucsf-login-vm1.corehpc.ucsf.edu
   Fri Aug 28 11:01:06 AM PDT 2026
   ```

#### Step 4: Submit the Script as a Job

7. **Submit the script** to the job queue using `sbatch`:
   ```sh
   [jdoe@chpc-ucsf-login-vm1 tests]$ sbatch hello_world.sh
   Submitted batch job 1504151
   ```

8. **Check the job status** using `squeue -u <user>`:
   ```sh
   [jdoe@chpc-ucsf-login-vm1 tests]$ squeue -u jdoe
                JOBID PARTITION                 NAME         USER    STATE         TIME   TIME_LIMIT  NODES NODELIST(REASON)         DEPENDENCY
           1504151       cpu          hello_world   jdoe  RUNNING         0:03      1:00:00      1         gcpu2-55             (null)
   ```
   Initially, the job may be in a queued state (`PD` or `PENDING`). Once it starts running, it will be in the running state (`R` or `RUNNING`).

#### Step 5: Review the Job Output

9. **Locate the output** in the current directory:
   ```sh
   [jdoe@chpc-ucsf-login-vm1 tests]$ ls
   hello_world.sh  hello.out
   ```

10. **Print the job output** to your terminal:
    ```sh
    [jdoe@chpc-ucsf-login-vm1 tests]$ cat hello.out
    Hello world, I am running on node gcpu2-55
    Fri Aug 28 11:08:51 PDT 2026
    ```

    Alternatively, you can use `less` to view the output file without printing it all at once:
    ```sh
    [jdoe@chpc-ucsf-login-vm1 tests]$ less hello.out
    ```

    Press `q` to quit the `less` viewer.

Congratulations! You've successfully submitted and run a simple 'Hello World' job on the CoreHPC cluster.

This is only a simple script, but there are a number of great examples of more complex scripts on the CoreHPC wiki' [CoreHPC Submission Examples](https://wiki.library.ucsf.edu/spaces/CHPC/pages/736476672/CoreHPC+Submission+Examples) page. Here you can learn more about how to request different resources, such as GPUs, and how to run jobs in parallel across multiple nodes.

## File Transfer Between Your Computer and CoreHPC

### Using SCP for File Transfer

I am not familiar with using `scp` for file transfer on CoreHPC, but it is a common method for transferring files between your local machine and a remote server. You may explore this option on your own, but we recommend using Globus or drive mapping to access CoreHPC files from your local machine.

### Using Globus for Data Transfer

[Globus](https://www.globus.org/) is a non-profit service for moving, syncing, and sharing large amounts of data asynchronously in the background. Transfers are done from and to, so called, Collections. In order to perform a file transfer from one location to another using the Globus service, both ends must have a Collection. UCSF has a site license for Globus, and several UCSF departments and services, including the Wynton HPC environment, provide Globus Collection. This will allow you to transfer and share data efficiently with any other Globus user in the world.

***Set up Globus on your local machine:***
If you want to transfer files from or to your local machine, you need to set up a personal Collection on that machine. Below is an outline on how to do this. For full details, see the [Globus Docs How To](https://docs.globus.org/how-to/).

1. [local] Make sure [Globus Connect Personal](https://www.globus.org/globus-connect-personal) is installed on your local machine (available for macOS, Linux, and MS Windows)

2. [local] (optional) The default is that Globus will have access to all of the content under your home directory, e.g. when connected to Globus you will be able to browse it from the Global website online. To limit this, create a folder to be used solely for Globus transfers, e.g. `~/globus/`. Launch the ‘Globus Connect Personal’ software, go to ‘Preferences’ and change the ‘Access Path Configuration’ to `~/globus`. Then, click ‘Save’.

3. [online] Setup a [Globus Connect Personal (GCP) Collection](https://app.globus.org/file-manager/gcp) for your local machine. Use one GCP collection per machine. This step will produce a ***GCP Security Key*** for your local machine. Make sure to write it down in a safe place. If you lose it, you will have to create a new GCP collection.

4. [local] Launch the ‘Globus Connect Personal’ software, and enter your ***GCP Security Key*** code to connect.

5. [online] Go to [Collection -> ‘Administered by You’](https://app.globus.org/collections?scope=administered-by-me), go to on your GCP Collection, and click on ‘Open in File Manager’. This will display the files and folders on your local computer. If you restricted access to ~/globus (Step 2), then it is only that folder that is accessible via Globus.

6. [local] In the Globus Connect Personal software, make sure to disconnect when no longer needed.

7. [online] (Optional) If you require to transfer data to or from Globus High Assurance Collections, your account must be associated with the “University of California San Francisco High Assurance Globus Plus” Group. To join the group, login to [globus.org](https://www.globus.org/) with your UCSF MyAccess credentials, select the groups side tab, deselect “My Groups”, and search for “University of California San Francisco” - locate the “University of California San Francisco High Assurance Globus Plus” group and hit the join. The person who manages the UCSF Globus subscription will approve any account associated with a UCSF Email Address.

***Set up a Globus Collection for your Wynton account:***
If you want to transfer files from or to CoreHPC, you need to set up the ‘UCSF CoreHPC - User Home’ and ‘UCSF CoreHPC - User Scratch’ Collections. Below is an outline on how to do this.

1. [online] Go to [Globus.org](https://www.globus.org/) and log in with your UCSF MyAccess credentials.
2. Then find the Collections menu on the left and click it.
3. Then locate the [‘UCSF CoreHPC - User Home' collection](https://app.globus.org/file-manager/collections/e6390f3c-59bb-4c9e-b908-938375d88b37/overview).
4. This will bring up the “Overview” of the [‘UCSF CoreHPC - User Home' collection](https://app.globus.org/file-manager/collections/e6390f3c-59bb-4c9e-b908-938375d88b37/overview).
5. Click “Open in File Manager”.
6. If you are prompted to login/authenticate, do so.
7. You should now see your CoreHPC home directory in the Globus File Manager. You can now transfer files to and from your CoreHPC home directory using Globus.
8. Repeat the above steps for the [‘UCSF CoreHPC - User Scratch' collection](https://app.globus.org/file-manager/collections/dd241e70-0935-4f48-b8c0-1351bc1e2c43/overview).

***For future reference***: Globus can also be used to transfer directly from CoreHPC to UCSF Box - convenient for larger data transfers which you may not want to store on your personal machine.

*Note:* these instructions were adapted from the [setup guide for Globus with Wynton](https://wynton.ucsf.edu/hpc/transfers/globus.html) (the cluster before CoreHPC). It may be useful to refer back to this page if you run into issues.

### Using Drive Mapping for File Transfer

Last but not least, you can also map FAC storage to your local machine. This allows you to access CoreHPC files as if they were on your local machine, making it easy to transfer files back and forth. To set up drive mapping, follow the instructions on this page:
[https://it.ucsf.edu/how-to/fac-drive-mapping-instructions](https://it.ucsf.edu/how-to/fac-drive-mapping-instructions)

## Where to Store Your Files

### Storage Options

Perhaps the most important - and also most confusing - aspect of CoreHPC is where to store your files. You have four primary options:

1. **User Home Storage**

  This is your personal space on the CoreHPC cluster. You have 20GB of storage here and it will not be cleared during maintenance. Use this sparingly for small files and configuration files. This directory is not for heavy computational lifting.

  Access your home directory by typing `cd` in the terminal, or explicitly specifying the path: `cd /home/<user>`.

2. **User Scratch Storage**

  This is your personal high-performance storage area for temporary files. It is not backed up and will be purged during quarterly CoreHPC/FAC maintanence. Use this for large datasets, intermediate files, and temporary outputs.

  Access your scratch directory by typing `cd /scratch/user/<user>` in the terminal.

3. **Group Scratch Storage (FOR HEAVY COMPUTING)**

  This is a shared storage area, and likely where you will perform most of your computational work. It is not backed up and may be purged during quarterly CoreHPC/FAC maintanence. This is an excellent choice for collaborative projects in your research group.

  Access your group's scratch directory by typing `cd /mnt/scratch/group/CX500147_DS2` in the terminal. Do not store your filed directly in this directory. Instead, create a subdirectory with your username such as `/mnt/scratch/group/CX500147_DS2/<user>`.

4. **Group FAC Storage (FOR YOUR MOST IMPORTANT DATA)**

  This is a shared storage area for collaborative projects. It is backed up and persistent, but has limited storage capacity. Use this for files that need to be accessed by multiple users, important data outputs from experiments, and any other data you may want access to long-term. You share this storage with the other students in your cohort, so please be mindful of your storage usage.

  Access your group's FAC directory by typing `cd /mnt/fac/CX500147_DS2` in the terminal. Do not store your filed directly in this directory. Instead, create a subdirectory with your username such as `/mnt/fac/CX500147_DS2/<user>`.

My suggestion is to default to performing computation in your group scratch storage and saving any important outputs to your group FAC storage.

### Moving Files Between Storage Options

Now, if you perform computation in one location, you may later want to copy some of the outputs to your group FAC storage for long-term preservation. You can do this using the `cp` command in the terminal. For example, to copy the hello world output file from your home directory to your group FAC storage, you would type:

```sh
[jdoe@chpc-ucsf-login-vm1 ~]$ cp /home/remote/<user>/tests/hello.out /mnt/fac/CX500147_DS2/<user>/
```

This is particularly useful for copying interesting scientific outputs to your group FAC storage, which you can then access from your local machine via drive mapping.

---

## Final Notes

### Good File System Practices (don't be *the* person who breaks CoreHPC)
- **Distribute Files:** Spread out files across multiple directories, including SGE output and error files.
- **Prefer Larger Files:** Use fewer, larger files rather than many small ones.
- **Limit Directory I/O:** Keep the number of reads and writes to a single directory reasonable.

### Need Help?
- [CoreHPC Overview Website](https://it.ucsf.edu/service/corehpc)
- [CoreHPC Overview](https://wiki.library.ucsf.edu/spaces/CHPC/overview)
- [CoreHPC Access Primer](https://wiki.library.ucsf.edu/spaces/CHPC/pages/720396955/CoreHPC+Access+Primer)
- [FAC Overview Website](https://it.ucsf.edu/service/facility-advanced-computing-fac)
- **CoreHPC Staff Support**:
  - Email: [COREHPC-Support@ucsf.edu](mailto:COREHPC-Support@ucsf.edu), [FACTeam@ucsf.edu](mailto:FACTeam@ucsf.edu)
  - Request help (also for account requests) by [submitting a ticket](https://redcap.ucsf.edu/surveys/?s=JAYNXF7FJ4AA94KX)
  - Join the [CoreHPC Slack](https://join.slack.com/t/ars-clients/shared_invite/zt-3o791f2r5-DVXKBNbJAqltOxTtxAeEZQ)
