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
- [Beyond the Basics](#beyond-the-basics)
  - [Overview of CoreHPC Nodes](#overview-of-corehpc-nodes)
  - [CoreHPC Job Queues](#corehpc-job-queues)
  - [Using Scratch Storage](#using-scratch-storage)
  - [Additional Info / Tips](#additional-info--tips)
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

### Files Transfer Between Your Computer and CoreHPC with **`scp`**

The `scp` (secure copy) command allows you to securely transfer files between your machine and CoreHPC via SSH.

#### CoreHPC → Local Machine

To copy a file from CoreHPC to your local machine, on your local machine, type:

```sh
scp zack@dt1.corehpc.ucsf.edu:/corehpc/home/rotation/zack/tests/hello_world.o201 /path/to/local/destination/
```

Replace `zack` with your CoreHPC username, `/corehpc/home/rotation/zack/hello_world.o201` of the path of the file on CoreHPC, and `/path/to/local/destination/` with the path where you want the file to be saved on your local machine. (Note: we are using the data transfer node, `dt1`, rather than `log1` for moving the file. This isn't necessary but is recommended. More on this below.)


#### Local Machine → CoreHPC

On your local machine:

```sh
scp /path/to/local/file zack@dt1.corehpc.ucsf.edu:/corehpc/home/rotation/zack/
```

Replace `/path/to/local/file` with the path to the file on your local machine, and `zack` with your CoreHPC username. `/corehpc/home/rotation/zack/` is where the file will land.


#### Copying Entire Directories

To copy entire directories, use the recursive `-r` option with `scp`:

```sh
# CoreHPC to your local machine:
scp -r zack@dt1.corehpc.ucsf.edu:/corehpc/home/rotation/zack/tests /path/to/local/destination/

# Your machine to CoreHPC
scp -r /path/to/local/directory zack@log1.corehpc.ucsf.edu:/corehpc/home/rotation/zack/
```


#### Using Globus for Data Transfer

Alternatively, you may find it more convenient to transfer files to/from CoreHPC using Globus. You can find more information on how to set up Globus with CoreHPC on this website:

[https://corehpc.ucsf.edu/hpc/transfers/globus.html](https://corehpc.ucsf.edu/hpc/transfers/globus.html)

Globus can also be used to transfer directly from CoreHPC to UCSF Box - convenient for larger data transfers which you may not want to store on your personal machine.

Wohoo! You're are now proficient enough to start using CoreHPC 😎. We can't wait to see all the cool science you'll do!

## Beyond the basics

### Overview of CoreHPC Nodes
Sign into login, data transfer, and development nodes for logging in, transferring data, or prototyping / testing code. Simply `ssh log1@corehpc.ucsf.edu` or `ssh dt1@corehpc.ucsf.edu`. For development, you can`ssh dev1@corehpc.ucsf.edu` but you have to be logged into CoreHPC first. Here's a quick overview of all of CoreHPC's nodes:

| Feature                                        | Login Nodes                                                         | Transfer Nodes                                         | Development Nodes                                                                                                                            | Compute Nodes                                 |
| ---------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Hostname**                                   | `log[1-2].corehpc.ucsf.edu`                                          | `dt[1-2].corehpc.ucsf.edu`                              | `dev[1-3]`, `gpudev1`                                                                                                                        | …                                             |
| **Purpose**                                    | *Submit and query jobs. SSH to development nodes. File management.* | *Fast in- & outbound file transfers. File management.* | *Compile and install software. Prototype and test job scripts. Submit and query jobs. Version control (clone, pull, push). File management.* | *Running short and long-running job scripts.* |
| **Accessible via SSH from outside of cluster** | ✓ (2FA if outside of UCSF)                                          | ✓ (2FA if outside of UCSF)                             | no                                                                                                                                           | no                                            |
| **Network speed**                              | 1 Gbps                                                              | 10 Gbps                                                | 1 Gbps                                                                                                                                       | 1,10,40 Gbps                                  |
| **Core software**                              | Minimal                                                             | Minimal                                                | Same as compute nodes + compilers and source-code packages                                                                                   | Rocky 8 packages                              |
| **Job submission**                             | ✓                                                                   | no                                                     | ✓                                                                                                                                            | ✓                                             |

### CoreHPC Job Queues
The cluster provides different queues that each is optimized for a different purpose. Some queues are faster because they are limited to 30min run times (`short.q`). Others are slower, but ensure that your job is allocated a GPU (`gpu.q`). 

To specify a queue, use the flag `-q {queue_name_here}` when submitting a job, e.g., `qsub -q long.q my_submission_script.sh`.

Here's a quick summary:

| Queue Name | Maximum Runtime                                                        | Process Priority | Availability                                                       | Quota                                                                                    | Purpose                                                                      |
| ---------- | ---------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **short.q**    | 30 minutes                                                             | 10 (medium)      | All compute nodes                                                  | 100 jobs per user                                                                        | Low-latency needs, e.g., pipeline prototyping and quick turn-around analysis |
| **long.q**     | 2 weeks (336 hours)                                                    | 19 (lowest)      | All compute nodes                                                  | Unlimited                                                                                | General needs                                                                |
| **member.q**   | 2 weeks (336 hours)                                                    | 0 (highest)      | All compute nodes (except GPU and institutionally purchased nodes) | Proportional to lab's [contributed share](https://corehpc.ucsf.edu/hpc/about/shares.html) | Research groups needing more resources than communal queues                  |
| **gpu.q**      | 2 weeks (336 hours) (communal GPU nodes) or 2 hours (non-contributors) | 0 (highest)      | Specific GPU nodes                                                 | Unlimited                                                                                | Software utilizing GPUs                                                      |
| **4gpu.q**     | 2 weeks (336 hours) (contributors) or 2 hours (non-contributors)       | 0 (highest)      | Specific "All-4-GPU" nodes                                         | Unlimited                                                                                | Software needing to utilize all four GPUs on the node                        |
| **ondemand.q** | 2 weeks (336 hours)                                                    | 0 (highest)      | Institutionally purchased nodes                                    | Available upon application and approval                                                  | Scheduled high-priority computing needs or temporary paid priority access    |

### Using Scratch Storage

- All nodes (compute and development) have local storage mounted as `/scratch`. The `/scratch` storage is faster than system-wide storage such as home folders and `/corehpc/scratch`, making it ideal for holding intermediate data files. Using local `/scratch` reduces the load on system-wide storage and the local network, benefiting everyone.
- As the name implies, `/scratch` is susceptible to deletion without warning by CoreHPC admin. Do not hold precious data on it.

### Additional Info / Tips

- **Email Notifications**: Get email notifications for job status by adding the flag `-m bea` to your `qsub` command, e.g., `qsub -m bea`.
- **Disk Quota**: Check your disk quota with:
  ```sh
  beegfs-ctl --getquota --storagepoolid=11 --uid "$USER"
  ```
  - Note: The displayed quota is double the actual size. For example, if it shows 1 TB, you have 500 GB available. [See more](https://corehpc.ucsf.edu/hpc/howto/storage-size.html#user-disk-quota-on-corehpchome-or-corehpcprotectedhome).
- There are some ways to automatically sign into nodes without typing in your password every time. You can also log directly into `dev` nodes without first going to a login node. [This tutorial](https://corehpc.ucsf.edu/hpc/howto/log-in-without-pwd.html) on the CoreHPC website will help.

### Good File System Practices (don't be *the* person who breaks CoreHPC)
- **Distribute Files:** Spread out files across multiple directories, including SGE output and error files.
- **Prefer Larger Files:** Use fewer, larger files rather than many small ones.
- **Limit Directory I/O:** Keep the number of reads and writes to a single directory reasonable.

---

## Need Help?
- [CoreHPC Overview Website](https://it.ucsf.edu/service/corehpc)
- [CoreHPC Overview](https://wiki.library.ucsf.edu/spaces/CHPC/overview)
- [CoreHPC Access Primer](https://wiki.library.ucsf.edu/spaces/CHPC/pages/720396955/CoreHPC+Access+Primer)
- [FAC Overview Website](https://it.ucsf.edu/service/facility-advanced-computing-fac)
- **CoreHPC Staff Support**:
  - Email: [COREHPC-Support@ucsf.edu](mailto:COREHPC-Support@ucsf.edu), [FACTeam@ucsf.edu](mailto:FACTeam@ucsf.edu)
  - Request help (also for account requests) by [submitting a ticket](https://redcap.ucsf.edu/surveys/?s=JAYNXF7FJ4AA94KX)
  - Join the [CoreHPC Slack](https://join.slack.com/t/ars-clients/shared_invite/zt-3o791f2r5-DVXKBNbJAqltOxTtxAeEZQ)
