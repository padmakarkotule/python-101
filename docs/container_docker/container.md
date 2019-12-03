# Containers
## Container primitives overview
Container primitives, Sybsystems 

#### Linux Container primitives
Containers are an abstraction over several different Linux technologies.

![alt text][container_kernel_highlevel_view]
[container_kernel_highlevel_view]:/img/container_docker/Container_kernel_highlevel_view.png
Ref. Link - https://speakerdeck.com/samuelkarp/linux-container-primitives-and-runtimes-re-invent-2018-con407?slide=3


## Control groups (cgroups)
What do control groups (cgroups) do?
    - Organize all processes in the system
    - Limit or prioritize resource utilization 
    - Account for resource usage and gather utilization data

#### Subsystems
Control groups is an abstract framework and Subsystems are concrete implementations.
Different subsystems can organize processes separately, and most subsystems are resource controllers.
Examples of subsystems:

    - Memory
    - CPU time
    - Block I/O
    - Number of discrete processes (pids)
    - CPU & memory pinning
    - Freezer (used by docker pause)
    - Devices
    - Network priority

    **Hierarchical representation**
    - Every pid is represented exactly once in each subsystem.
    - New processes inherit cgroups from their parents

#### cgroup virtual filesystem

- Typically mounted at /sys/fs/cgroup
- tasks virtual file holds all pids in the cgroup
- Other files have settings and utilization data
Example,
    
    `
     **cggroup fs (Typically mounted at /sys/fs/cgroup), E.g.**
        [root@60ff5eae5908 containerExample]# ls -al /sys/fs/cgroup/
        total 0
        dr-xr-xr-x 15 root root 300 Oct 29 08:32 .
        drwxr-xr-x  9 root root   0 Dec  2 11:28 ..
        drwxr-xr-x  2 root root   0 Dec  2 11:28 blkio
        drwxr-xr-x  2 root root   0 Dec  2 11:28 cpu
        drwxr-xr-x  2 root root   0 Dec  2 11:28 cpuacct
        drwxr-xr-x  2 root root   0 Dec  2 11:28 cpuset
        drwxr-xr-x  2 root root   0 Dec  2 11:28 devices
        drwxr-xr-x  2 root root   0 Dec  2 11:28 freezer
        drwxr-xr-x  2 root root   0 Dec  2 11:28 hugetlb
        drwxr-xr-x  2 root root   0 Dec  2 11:28 memory
        drwxr-xr-x  2 root root   0 Dec  2 11:28 net_cls
        drwxr-xr-x  2 root root   0 Dec  2 11:28 net_prio
        drwxr-xr-x  2 root root   0 Dec  2 11:28 perf_event
        drwxr-xr-x  2 root root   0 Dec  2 11:28 pids
        drwxr-xr-x  2 root root   0 Dec  2 11:28 systemd
        [root@60ff5eae5908 containerExample]#
     **task (tasks virtual file holds all pids in the cgroup), E.g.**
        [root@60ff5eae5908 cgroup]# cat cpu/tasks
        1
        7
        79848
        79850
        80109
        [root@60ff5eae5908 cgroup]#   
     **settings and utilization data (Other files have settings and utilization data), E.g.**
        [root@60ff5eae5908 cgroup]# cat cpu/cpu.stat
        nr_periods 0
        nr_throttled 0
        throttled_time 0
        root@60ff5eae5908 cgroup]#
        
        [root@60ff5eae5908 cgroup]# cat cpu/cpu.shares
        1024
        [root@60ff5eae5908 cgroup]#    
    `

#### What can you use cgroups for?

- cgroups can be used independently of containers
- cgroups control resource limits for processes
- Monitor processes and organize them
- Be careful not to break any assumptions your container runtime or orchestrator might have

#### Example - Let’s limit the cgroup to 100MB of memory and turn off swap.
      `
        root@60ff5eae5908:/# echo "100000000" > /sys/fs/cgroup/memory/demo/memory.limit_in_bytes
        root@60ff5eae5908:/# echo "0" > /sys/fs/cgroup/memory/demo/memory.swappiness
      `
      
      The tasks file is special, it contains the list of processes which are assigned to the cgroup. 
      To join the cgroup we can write our own PID.
      
      `# echo $$ > /sys/fs/cgroup/memory/demo/tasks`
      
      Finally we need a memory hungry application.
      `
        f = open("/dev/urandom", "r")
        data = ""
        i=0
            while True:
            data += f.read(10000000) # 10mb
            i += 1
            print "%dmb" % (i*10,)
      `
      
      If you’ve setup the cgroup correctly, this program won’t crash your computer.
      `
        # python hungry.py
        10mb
        20mb
        30mb
        40mb
        50mb
        60mb
        70mb
        80mb
        Killed
      `
      
      If that didn’t crash your computer, congratulations!
      
      cgroups can’t be removed until every processes in the tasks file has exited or been reassigned to another group. 
      Exit the shell and remove the directory with rmdir (don’t use rm -r).
      
      `
        # exit
        exit
        $ sudo rmdir /sys/fs/cgroup/memory/demo
      `

## Namespaces
What do namespaces do?
    - Isolation mechanism for resources
    - Changes to resources within namespace are invisible outside the namespace.

#### What namespaces are available?
- Network
- Filesystem (mounts)
- Processes (pid)
- Inter-process communication (ipc)
- Hostname and domain name (uts)
- User and group IDs
- cgroup

#### Namespace sharing

![alt text][Namespace_sharing]
[Namespace_sharing]:/img/container_docker/Namespace_sharing.png
Ref. Link - https://speakerdeck.com/samuelkarp/linux-container-primitives-and-runtimes-re-invent-2018-con407?slide=3

- **Network namespace**
        - Frequently used in containers
        - **docker run uses a separate network namespace per container**
        
        - Multiple containers can share a network namespace
            - Kubernetes pods
            - Amazon Elastic Container Service (Amazon ECS) tasks with the awsvpc networking mode
    
- **Mount namespace**
        - Used for giving containers their own filesystem
        - Container image is mounted as the root filesystem
        - More about filesystems to come!

       E.g.
       `
            [root@60ff5eae5908 cgroup]# mount
            
            **overlay** on / type overlay** (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/KOO4ONN252GY6**
            
            overlay2/l/OAY5QSO77VZFYVSGNFQG7VGVNQ:/var/lib/docker/overlay2/l/CY2JLIP2WUNJBWSLVNCLAWB
            /BDWFUJSQSR7K5ACM3J367OPETG:/var/lib/docker/overlay2/l/U274LT3PHOPI3O774WGDJP4B2K:/var/l
            5HUXQPJBQAPVPNKP4:/var/lib/docker/overlay2/l/NH5GL4RK4VX23ZXW6RTGEDTRDE,upperdir=/var/li
            iff,workdir=/var/lib/docker/overlay2/4cd4a2f471248b240defee90cdc1b76c23b8c0a63217371e3af
            proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
            tmpfs on /dev type tmpfs (rw,nosuid,size=65536k,mode=755)
            devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=666)
            sysfs on /sys type sysfs (ro,nosuid,nodev,noexec,relatime)
            tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,relatime,mode=755)
            cpuset on /sys/fs/cgroup/cpuset type cgroup (ro,nosuid,nodev,noexec,relatime,cpuset)
            cpu on /sys/fs/cgroup/cpu type cgroup (ro,nosuid,nodev,noexec,relatime,cpu)
            cpuacct on /sys/fs/cgroup/cpuacct type cgroup (ro,nosuid,nodev,noexec,relatime,cpuacct)
       `

- **procfs virtual filesystem**
- Namespaces are visible in /proc
- Files are symbolic links to the namespace
- The link contains the namespace type and inode number to identify the namespace

Example,
    `
        [root@60ff5eae5908 cgroup]# readlink /proc/$$/ns/*
        cgroup:[4026531835]
        ipc:[4026532298]
        mnt:[4026532296]
        net:[4026532301]
        pid:[4026532299]
        user:[4026531837]
        uts:[4026532297]
        [root@60ff5eae5908 cgroup]#
    `

#### Creating namespaces
- clone(2) and 
- unshare(2) 
- CLONE_NEW* flags to specify which namespaces

**clone(2)**
    clone(2)is for new processes to create new namespaces

**unshare(2)** 
    **unshare is for existing processes** to create new namespaces
    **unshare** (Creating namespaces with unshare)
   Namespaces allow us to create restricted views of systems like the process tree, network interfaces, and mounts.
   **Example without namespace**  
   **How isolated is this chrooted process? 
   Let’s run a command on the host in another terminal.**
   
   `$ # outside of the chroot
    $ top`
    
    **we can see the top invocation from inside the chroot.**
    E.g. Run following commands to see outside top command in inside chroot env.
     
    `$ sudo chroot rootfs /bin/bash`  
    `$ mount -t proc proc /proc`
    `$ ps aux | grep top`
    ` pkill top`
    
    **In above example, user is able to kill top command**.<br>
    This is where we get to talk about namespaces. Namespaces allow us to create restricted views 
    of systems like the process tree, network interfaces, and mounts.
    
   **Creating namespace is super easy, just a single syscall with one argument, unshare.**
   The unshare command line tool gives us a nice wrapper around this syscall and lets us setup namespaces manually.
   E.g. In this case, we’ll create a PID namespace for the shell, then execute the chroot like the last example.
   
   `$ sudo unshare -p -f --mount-proc=$PWD/rootfs/proc chroot rootfs /bin/bash`
   `$ ps aux`

**nsenter** Entering namespaces with nsenter
   The kernel exposes namespaces under /proc/(PID)/ns as files.
   E.g.
    `[root@60ff5eae5908 containerExample]# ps
    PID TTY          TIME CMD
    7 pts/0    00:00:00 bash
    80033 pts/0    00:00:00 ps
    [root@60ff5eae5908 containerExample]# chroot rootfs /bin/bash
    root@60ff5eae5908:/#`
    
    `$ ls -l /proc/29840/ns`
    and it's output is,
    `
     [root@60ff5eae5908 containerExample]# ls -l /proc/7/ns
        total 0
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 cgroup -> cgroup:[4026531835]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 ipc -> ipc:[4026532298]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 mnt -> mnt:[4026532296]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 net -> net:[4026532301]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 pid -> pid:[4026532299]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 user -> user:[4026531837]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 uts -> uts:[4026532297]
        [root@60ff5eae5908 containerExample]#
    `  
    **The nsenter command provides a wrapper around setns to enter a namespace.**
    `root@localhost:/# ps aux
        USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
        root         1  0.0  0.0  20272  3064 ?        S+   00:25   0:00 /bin/bash
        root         5  0.0  0.0  20276  3248 ?        S    00:29   0:00 /bin/bash
        root         6  0.0  0.0  17504  1984 ?        R+   00:30   0:00 ps aux
    `
    Having entered the namespace successfully, when we run ps in the second shell (PID 5) 
    we see the first shell (PID 1).
  
#### Persisting namespaces
- The kernel automatically garbage-collects namespaces by reference-counting
- New namespace remains open as long as
    - a process runs or
    - a mount is open  
- Bind-mount a file in /proc/$$/ns to another place on the filesystem
    E.g. 
    `# mount --bind /proc/$$/ns/net /var/run/netns/con407`
**Note** - $$ means PID of the current shell. <br> 
the $ character represents the process ID number, or PID, of the current shell

#### Entering namespaces
- Open a file from /proc/$$/ns (or a bindmount) 
- Pass to setns(2) to enter the existing namespace
- Namespace remains open as long as the process is running, even if the original file goes away.
 
**nsenter** Entering namespaces with nsenter (The kernel exposes namespaces under /proc/(PID)/ns as files).
- nsenter(1) is a command for doing this interactively
- ip-netns(8) works specifically for network namespaces
   E.g.
    `[root@60ff5eae5908 containerExample]# ps
    PID TTY          TIME CMD
    7 pts/0    00:00:00 bash
    80033 pts/0    00:00:00 ps
    [root@60ff5eae5908 containerExample]# chroot rootfs /bin/bash
    root@60ff5eae5908:/#` 
    
    Just enter nsenter command, 
    `[root@60ff5eae5908 containerExample]# nsenter`
    Or,
    `$ sudo nsenter --pid=/proc/7/ns/pid`
    
    `$ ls -l /proc/29840/ns`
    and it's output is,
    `
     [root@60ff5eae5908 containerExample]# ls -l /proc/7/ns
        total 0
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 cgroup -> cgroup:[4026531835]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 ipc -> ipc:[4026532298]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 mnt -> mnt:[4026532296]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 net -> net:[4026532301]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 pid -> pid:[4026532299]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 user -> user:[4026531837]
        lrwxrwxrwx 1 root root 0 Oct 29 09:39 uts -> uts:[4026532297]
        [root@60ff5eae5908 containerExample]#
    `  
    **The nsenter command provides a wrapper around setns to enter a namespace.**
    `root@localhost:/# ps aux
        USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
        root         1  0.0  0.0  20272  3064 ?        S+   00:25   0:00 /bin/bash
        root         5  0.0  0.0  20276  3248 ?        S    00:29   0:00 /bin/bash
        root         6  0.0  0.0  17504  1984 ?        R+   00:30   0:00 ps aux
    `
    Having entered the namespace successfully, when we run ps in the second shell (PID 5) 
    we see the first shell (PID 1).
    


#### Troublshooting container
- **Use nsenter** or **ip netns** **to troubleshoot container networking**
- Monitor containers by entering the pid namespace
- Access binaries in your containers with the mount namespace


## Images, layers and Union filesystems/Overlay File system

**General terminology of union**
The action of joining together or the fact of being joined together,

**Union in data type**
A union is a special data type available in C that allows to store different data types in the same memory location. 
You can define a union with many members, but only one member can contain a value at any given time. 
Unions provide an efficient way of using the same memory location for multiple-purpose.

**Python examples of union**
Python Set union() The union() method returns a new set with distinct elements from all the sets. 
The union of two or more sets is the set of all distinct elements present in all the sets. 
For example: The syntax of union() is: union() Parameters. In Python, union() allows arbitrary number of arguments.
    `
    Example1,
        A = {'a', 'c', 'd'}
        B = {'c', 'd', 2 }
        C= {1, 2, 3}
        
        print('A U B =', A.union(B))
        print('B U C =', B.union(C))        
        print('A U B U C =', A.union(B, C))      
        print('A.union() = ', A.union())
    
    When you run the program, the output will be:,
        A U B = {2, 'a', 'd', 'c'}
        B U C = {1, 2, 3, 'd', 'c'}
        A U B U C = {1, 2, 3, 'a', 'd', 'c'}
        A.union() =  {'a', 'd', 'c'}
        
    Example2, (Using Operator)
        A = {'a', 'c', 'd'}
        B = {'c', 'd', 2 }
        C= {1, 2, 3}
        
        print('A U B =', A| B)
        print('B U C =', B | C)        
        print('A U B U C =', A | B | C)
        
     When you run the program, the output will be:
        A U B = {2, 'a', 'c', 'd'}
        B U C = {1, 2, 3, 'c', 'd'}
        A U B U C = {1, 2, 3, 'a', 'c', 'd'}    
    `

**Union filesystems**
- Popular in **container runtimes (like Docker)** to implement layers
- **Efficient use of storage when starting multiple containers with identical images**
- Efficient use of storage when making minor modifications to images

**Overlay filesystem**
OverlayFS is a modern union filesystem that is similar to AUFS, but faster and with a simpler implementation. 
Example, implementation in Docker provides two storage drivers for OverlayFS: 
the original overlay, and the newer and more stable overlay2.

- Joins two directories (upper and lower) to form a union
- Uses file name to describe the files
- When writing to the overlay 
    - **lowerdir is not modified, all changes go to upperdir**
    - **Existing files are copied-up to the upperdir for modificiation**
    - Whole file is copied, not just blocks.
- “Deleting” a file in the upperdir creates a **whiteout**
    - Files: character devices with 0/0 device number 
    - Directories: xattr “trusted.overlay.opaque” set to “y”
- An upperdir can have multiple lowerdirs
- Overlay filesystems can be created with mount(2)
- You can examine the mounts with 
    - mount(8) 
    - /proc/mounts 
    - /proc/$$/mountinfo   
    E.g.
    `
        [root@60ff5eae5908 ~]# cat /proc/$$/mountinfo
        509 355 0:114 / / rw,relatime master:141 - overlay overlay rw,lowerdir=/var/lib/docker/overlay2/l/KOO4ONN25
        RHSDGO:/var/lib/docker/overlay2/l/OAY5QSO77VZFYVSGNFQG7VGVNQ:/var/lib/docker/overlay2/l/CY2JLIP2WUNJBWSLVNC
        r/lib/docker/overlay2/l/BDWFUJSQSR7K5ACM3J367OPETG:/var/lib/docker/overlay2/l/U274LT3PHOPI3O774WGDJP4B2K:/v
        er/overlay2/l/GUYU3DY3B5HUXQPJBQAPVPNKP4:/var/lib/docker/overlay2/l/NH5GL4RK4VX23ZXW6RTGEDTRDE,upperdir=/va
        7371e3afd472005d2e6e4/diff,workdir=/var/lib/docker/overlay2/4cd4a2f471248b240defee90cdc1b76c23b8c0a63217371
        510 509 0:116 / /proc rw,nosuid,nodev,noexec,relatime - proc proc rw
        511 509 0:117 / /dev rw,nosuid - tmpfs tmpfs rw,size=65536k,mode=755
        512 511 0:118 / /dev/pts rw,nosuid,noexec,relatime - devpts devpts rw,gid=5,mode=620,ptmxmode=666
        513 509 0:119 / /sys ro,nosuid,nodev,noexec,relatime - sysfs sysfs ro
        514 513 0:120 / /sys/fs/cgroup ro,nosuid,nodev,noexec,relatime - tmpfs tmpfs rw,mode=755
        515 514 0:28 /docker/60ff5eae590889a646d9b50c4352857268e6301d5bc320caca66547979d4d76c /sys/fs/cgroup/cpuset
        set
    `

Note: In docker, If you use OverlayFS, use the overlay2 driver rather than the overlay driver, 
because it is more efficient in terms of inode utilization. To use the new driver, 
you need version 4.0 or higher of the Linux kernel, or RHEL or CentOS using version 3.10.0-514 and above.

**How the overlay2 driver works?**
    **OverlayFS layers two directories on a single Linux host** and **presents them as a single directory.** 
    **These directories are called layers** and the unification process is referred to as a union mount. 
    OverlayFS refers to the lower directory as lowerdir and the upper directory a upperdir. 
    The unified view is exposed through its own directory called merged.
    
    The **overlay2 driver natively supports up to 128 *lower* OverlayFS layers.** 
    This capability provides better performance for layer-related Docker commands such as,
    **docker build** and **docker commit**, and consumes fewer inodes on the backing filesystem.

**How Docker layers work**
    Docker’s default layer storage uses the overlay filesystem 
    - upperdir, lowerdir, and diff directories are in /var/lib/docker/overlay2
    
    After downloading a five-layer image using docker pull ubuntu, you can see six directories 
    under /var/lib/docker/overlay2.
    E.g.
    $ ls -l /var/lib/docker/overlay2

    The lowest layer contains a file called link, which contains the name of the shortened identifier, 
    and a directory called diff which contains the layer’s contents.

![alt text][OverlayFS]
[OverlayFS]:/img/container_docker/Overlay_fs_union_fs_in_docker.png

![alt text][Dockerlayer]
[Dockerlayer]:/img/container_docker/Overlay_fs_docker_layer_example.png

![alt text][OverlayExampleImage]
[OverlayExampleImage]:/img/container_docker/Overlay_fs_example.png

![alt text][VM_vs_containerization]
[VM_vs_containerization]:/img/container_docker/VM_vs_containerization.png    

- **Images are representations of a filesystem**
      E.g. 
    - Images are popular for virtualization and container systems
    - Docker helped popularize the concept of layers
    - **A union filesystem/Overlay filesystem is one where two or more filesystems are joined together in a unified view.**
    Example,
    1. Download rootfs (tar file) and untar it.
        E.g.
        `mkdir /containerExample/`
        `cd /containerExample/`  
        `$ wget https://github.com/ericchiang/containers-from-scratch/releases/download/v0.1.0/rootfs.tar.gz`
        `$ ls -al`
        `$ -rw-r--r--  1 root root 265734209 May 24  2017 rootfs.tar.gz`    
        `$ tar zxvf rootfs.tar.gz`
        `$ cd rootfs`
    2. After untar the resulting directory looks like a Linux system.
       There’s a bin directory with executables, an etc with system configuration, a lib with shared libraries, and so on.
    
       Note - Excellent talk on container (sysdiag & CoreOS) **https://www.youtube.com/watch?v=gMpldbcMHuI**

#### How to check/use overlay2, How can you leverage this? 
- Locate files in your layers 
- Examine which files and layers contribute to your disk usage
- Understand the impact of writable files in your containers and how to reduce
- Use "docker diff" command to check difference and use docker build/commit commands to merge new data.
Ref. Link for OverlayFS
https://docs.docker.com/storage/storagedriver/overlayfs-driver/#how-the-overlay2-driver-works

**Image and container layers on-disk**
E.g. 
    `
     Docke pull command ( Docker image comprising five layers.)**
        $ docker pull ubuntu
        Using default tag: latest
        latest: Pulling from library/ubuntu
        
        5ba4f30e5bea: Pull complete
        9d7d19c9dc56: Pull complete
        ac6ad7efd0f9: Pull complete
        e7491a747824: Pull complete
        a3ed95caeb02: Pull complete
        Digest: sha256:46fb5d001b88ad904c5c732b086b596b92cfb4a4840a3abd0e35dbb6870585e4
        Status: Downloaded newer image for ubuntu:latest
    
    **The image layers**
    $ ls -l /var/lib/docker/overlay/
        total 20
        drwx------ 3 root root 4096 Jun 20 16:11 38f3ed2eac129654acef11c32670b534670c3a06e483fce313d72e3e0a15baa8
        drwx------ 3 root root 4096 Jun 20 16:11 55f1e14c361b90570df46371b20ce6d480c434981cbda5fd68c6ff61aa0a5358
        drwx------ 3 root root 4096 Jun 20 16:11 824c8a961a4f5e8fe4f4243dab57c5be798e7fd195f6d88ab06aea92ba931654
        drwx------ 3 root root 4096 Jun 20 16:11 ad0fe55125ebf599da124da175174a4b8c1878afe6907bf7c78570341f308461
        drwx------ 3 root root 4096 Jun 20 16:11 edab9b5e5bf73f2997524eebeac1de4cf9c8b904fa8ad3ec43b3504196aa3
    
    **The container layer**
    $ ls -l /var/lib/docker/overlay/<directory-of-running-container>
        total 16
        -rw-r--r-- 1 root root   64 Jun 20 16:39 lower-id
        drwxr-xr-x 1 root root 4096 Jun 20 16:39 merged
        drwxr-xr-x 4 root root 4096 Jun 20 16:39 upper
        drwx------ 3 root root 4096 Jun 20 16:39 work    
        
    **container reads and writes work with overlay or overlay2**
        Ref. Link - https://docs.docker.com/storage/storagedriver/overlayfs-driver/#how-the-overlay2-driver-works
        Reading files
            - The file does not exist in the container layer
            - The file only exists in the container layer
            - The file exists in both the container layer and the image layer
        Modifying files or directories
            - Writing to a file for the first time
            - The first time a container writes to an existing file, that file does not exist 
            in the container (upperdir). The overlay/overlay2 driver performs a copy_up operation 
            to copy the file from the image (lowerdir) to the container (upperdir). 
            The container then writes the changes to the new copy of the file in the container layer.
        Deleting files and directories
            - When a file is deleted within a container, a whiteout file is created in the 
              container (upperdir). The version of the file in the image layer (lowerdir) 
              is not deleted (because the lowerdir is read-only).   
        Renaming directories
            - Calling rename(2) for a directory is allowed only when both the source and 
              the destination path are on the top layer.             
    `
    
    **docker Volumes**
        Use volumes for write-heavy workloads: Volumes provide the best and most predictable performance 
        for write-heavy workloads. This is because they bypass the storage driver and do not incur 
        any of the potential overheads introduced by thin provisioning and copy-on-write. Volumes have 
        other benefits, such as allowing you to share data among containers and persisting your data even 
        if no running container is using them.

## Runtimes
- **A software tool that configures Linux primitives to create and run containers on a host**
Examples include:
    - Docker 
    - containerd 
    - CRI-O (Container Runtime Interface (CRI) and -O ability to use different OCI-compliant container runtimes)
    - rkt ( Simply put, rkt is a more secure container technology, designed to alleviate many of 
            the flaws inherent in Docker's container model, by CoreOS).
            Another CoreOS strength is open operability: rkt uses an open source container format called appc, 
            while Docker uses its own proprietary image format.
    - systemd-nspawn  
        systemd-nspawn may be used to run a command or OS in a light-weight namespace container. 
        It is more powerful than chroot since it fully virtualizes the file system hierarchy, 
        as well as the process tree, the various IPC subsystems and the host and domain name.
- **Open Containers Initiative (OCI)** aims to standardize container runtimes, image format, and distribution 
    Established in June 2015 by Docker and other leaders in the container industry, 
    the OCI currently contains two specifications: the Runtime Specification (runtime-spec) 
    and the Image Specification (image-spec). 
- The OCI reference implementation (runc) powers Docker, containerd, and CRI-O

**OCI runtime spec**
- Containers are “bundles”
    - Filesystem
    - JSON document
- Filesystem can be a union
- JSON document describes
    - cgroups
    - Namespaces
    - Additional mounts
    - Linux capabilities
    - Linux security modules
    - And more
- Hooks can modify the bundle

**OCI runtime hooks**
Ref. Link - https://speakerdeck.com/samuelkarp/linux-container-primitives-and-runtimes-re-invent-2018-con407?slide=3
- Hooks run
    - Before a container starts
    - After a container starts
    - After a container stop
- Hooks can modify the filesystem, modify the JSON file, or take other actions 
- Hooks run sequentially, in an order defined in the JSON file

- Docker generates a bundle without hooks 
- Docker does let you specify your own runtime 
- Your runtime could inject hooks, then execute the real runtime 
- This is how Nvidia’s container runtime works

## Appendix
- Container from scratch (Without docker) <br>
    https://ericchiang.github.io/post/containers-from-scratch/ <br>
- Excellent talk on container (sysdiag & CoreOS) **https://www.youtube.com/watch?v=gMpldbcMHuI**
- AWS re-invent -<br>
  https://speakerdeck.com/samuelkarp/linux-container-primitives-and-runtimes-re-invent-2018-con407?slide=3 <br>
- Union FS/Overlay FS <br>
    https://www.datalight.com/blog/2016/01/27/explaining-overlayfs-%E2%80%93-what-it-does-and-how-it-works/ <br>
- OverlayFS docker Ref. link
    https://docs.docker.com/storage/storagedriver/overlayfs-driver/#how-the-overlay2-driver-works
