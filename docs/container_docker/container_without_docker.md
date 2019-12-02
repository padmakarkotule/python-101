# Container without docker 
Introduction to containers without Docker.
Ref. Link - https://ericchiang.github.io/post/containers-from-scratch/
Often thought of as cheap VMs, 
**Containers are just isolated groups of processes running on a single host.** 
That isolation leverages several underlying technologies built into the Linux kernel: 
    - namespaces, 
    - cgroups, 
    - chroots and lots of terms you’ve probably heard before.

Using underlying technologies to build our own containers.

    - Setting up a file system
    - chroot (restrict process to the “rootfs” directory and then exec a shell)
    - unshare (isolate chrooted process)
    - nsenter 
    - bind mounts
    - cgroups
    - capabilities

## Container file systems
Container images, the thing you download from the internet, are 
literally just tarballs (or tarballs in tarballs).

###### Example,
build a simple tarball by stripping down a Docker image. The tarball holds something that 
looks like a Debian file system and will be our playground for isolating processes.

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
   Excellent talk on container (sysdiag & CoreOS) **https://www.youtube.com/watch?v=gMpldbcMHuI**
3. **chroot**
    The first tool we’ll be working is chroot.
   **chroot. A thin wrapper around the similarly named syscall, it allows us to restrict a process view of 
      the file system. E.g.  restrict process to the “rootfs” directory and then exec a shell.**<br>
   
   **A process/command that is run in such a modified environment cannot access files outside the root directory. 
   This **modified environment is commonly known as “jailed directory” or “chroot jail”.** 
   Only a privileged process and root user can use chroot command.
   
   Once we’re in there we can play around, run commands, and do typical shell things.
   Try to execute the Python interpreter, from *rootfs/usr/bin/python* and not the host’s Python.
   E.g.
    `[root@60ff5eae5908 containerExample]# ls -al
    total 259520
    drwxr-xr-x  3 root root      4096 Dec  2 09:12 .
    drwxr-xr-x  1 root root      4096 Dec  2 08:21 ..
    drwxr-xr-x 21 root root      4096 Jan  1  1970 rootfs
    -rw-r--r--  1 root root 265734209 May 24  2017 rootfs.tar.gz
    [root@60ff5eae5908 containerExample]# sudo chroot rootfs /bin/bash
    root@60ff5eae5908:/#`
   `$ sudo chroot rootfs /bin/bash <br>`
   e.g. Output <br> 
   `[root@60ff5eae5908 containerExample]# sudo chroot rootfs /bin/bash`
   `root@60ff5eae5908:/#`

   `root@60ff5eae5908:/# ls /
    bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    root@60ff5eae5908:/# ls -al /`
    
    **Note** Note the output, there is no "containerExample" directory under /. which we have created initially 
    in host system. The above output showing rootfs directories under rootfs.
    
    Try with other example, running an application.
   `$ /usr/bin/python -c 'print "Hello, container world!"'<br>`
   E.g. output,
   `root@60ff5eae5908:/# /usr/bin/python -c 'print "Hello, container world!"'
    Hello, container world!
    root@60ff5eae5908:/#`  
      
   Instead of shell we can run applications in chroot environment. E.g. <br>
   `$ sudo chroot rootfs python -m SimpleHTTPServer`

# Namespace   
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
5. **nsenter** Entering namespaces with nsenter
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
    
# cgroups
  cgroups, short for control groups, allow kernel imposed isolation on resources like memory and CPU. 
  **After all, what’s the point of isolating processes if they can still kill neighbors by hogging RAM?** 
  
  The kernel exposes cgroups through the /sys/fs/cgroup directory. 
  
  **If your machine doesn’t have one you may have to mount the memory cgroup to follow along.**
  E.g. (On host system)
  `
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
  `
  
  On (chroot system)
  `
  [root@60ff5eae5908 containerExample]# chroot rootfs /bin/bash
  root@60ff5eae5908:/# ls -al /sys/fs/cgroup/
  ls: cannot access /sys/fs/cgroup/: No such file or directory
  root@60ff5eae5908:/#
  `
  
  For this example we’ll create a cgroup to restrict the memory of a process. 
  Creating a cgroup is easy, just create a directory.    
  In this case we’ll create a memory group called “demo”. Once created, the kernel fills 
  the directory with files that can be used to configure the cgroup. 
  
  `
  [root@60ff5eae5908 containerExample]# chroot rootfs /bin/bash
    root@60ff5eae5908:/# mkdir /sys/fs/cgroup/memory/demo
    mkdir: cannot create directory '/sys/fs/cgroup/memory/demo': No such file or directory
    root@60ff5eae5908:/# mkdir /sys/fs
    root@60ff5eae5908:/# mkdir /sys/fs/cgroup/
    root@60ff5eae5908:/# mkdir /sys/fs/cgroup/memory/
    root@60ff5eae5908:/# mkdir /sys/fs/cgroup/memory/demo
    root@60ff5eae5908:/#
  `
  
  To adjust a value we just have to write to the corresponding file. 
  Let’s limit the cgroup to 100MB of memory and turn off swap.
  
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
  
# Container security and capabilities
Containers are extremely effective ways of running arbitrary code from the internet as root, and this 
is where the low overhead of containers hurts us. Containers are significantly easier to break out 
of than a VM. As a result many technologies used to improve the security of containers, 
such as SELinux, seccomp, and capabilities involve limiting the power of processes already running as root.

In this section we’ll be exploring Linux capabilities.
Consider the following Go program which attempts to listen on port 80.

    `
    package main
    
    import (
        "fmt"
        "net"
        "os"
    )
    
    func main() {
        if _, err := net.Listen("tcp", ":80"); err != nil {
            fmt.Fprintln(os.Stdout, err)
            os.Exit(2)
        }
        fmt.Println("success")
    }
    `
    
   What happens when we compile and run this?
   `
    $ go build -o listen listen.go
    $ ./listen
    listen tcp :80: bind: permission denied
   ` 
   
   Predictably this program fails; listing on port 80 requires permissions we don’t have. 
   Of course we can just use sudo, but we’d like to give the binary just the one permission 
   to listen on lower ports.
   
   Capabilities are a set of discrete powers that together make up everything root can do. 
   This ranges from things like setting the system clock, to kill arbitrary processes. 
   In this case, CAP_NET_BIND_SERVICE allows executables to listen on lower ports.
   We can grant the executable CAP_NET_BIND_SERVICE using the setcap command.
   
   `
    $ sudo setcap cap_net_bind_service=+ep listen
    $ getcap listen
    listen = cap_net_bind_service+ep
    $ ./listen
    success
   `
   
   For things already running as root, like most containerized apps, we’re more interested in taking capabilities away than granting them. 
   First let’s see all powers our root shell has:
   
   `
    $ sudo su
    # capsh --print
    [root@60ff5eae5908 containerExample]# capsh --print
    Current: = cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_w
    rite,cap_setfcap+eip
    Bounding set =cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audi
    t_write,cap_setfcap
    Securebits: 00/0x0/1'b0
     secure-noroot: no (unlocked)
     secure-no-suid-fixup: no (unlocked)
     secure-keep-caps: no (unlocked)
    uid=0(root)
    gid=0(root)
    groups=
    [root@60ff5eae5908 containerExample]#
    `
    As an example, we’ll use capsh to drop a few capabilities including CAP_CHOWN. 
    If things work as expected, our shell shouldn’t be able to modify file ownership despite being root.
    `
    $ sudo capsh --drop=cap_chown,cap_setpcap,cap_setfcap,cap_sys_admin --chroot=$PWD/rootfs --
    root@localhost:/# whoami
    root
    root@localhost:/# chown nobody /bin/ls
    chown: changing ownership of '/bin/ls': Operation not permitte 
    `
    E.g.
    `
    root@60ff5eae5908:/# touch testfile
    root@60ff5eae5908:/# chown 777 testfile
    root@60ff5eae5908:/# ls -al
    total 88
    drwxr-xr-x 21 root root 4096 Dec  2 12:07 .
    drwxr-xr-x 21 root root 4096 Dec  2 12:07 ..
    drwxr-xr-x  2 root root 4096 Oct 15  2016 bin
    drwxr-xr-x  2 root root 4096 Sep 12  2016 boot
    drwxr-xr-x  2 root root 4096 Oct 15  2016 dev
    drwxr-xr-x 56 root root 4096 Dec  2 10:03 etc
    drwxr-xr-x  2 root root 4096 Sep 12  2016 home
    drwxr-xr-x  9 root root 4096 Sep 24  2016 lib
    drwxr-xr-x  2 root root 4096 Sep 23  2016 lib64
    drwxr-xr-x  2 root root 4096 Sep 23  2016 media
    drwxr-xr-x  2 root root 4096 Dec  2 10:39 mnt
    drwxr-xr-x  2 root root 4096 Sep 23  2016 opt
    drwxr-xr-x  2 root root 4096 Sep 23  2016 proc
    drwx------  2 root root 4096 Dec  2 10:04 root
    drwxr-xr-x  3 root root 4096 Sep 23  2016 run
    drwxr-xr-x  2 root root 4096 Sep 23  2016 sbin
    drwxr-xr-x  2 root root 4096 Sep 23  2016 srv
    drwxr-xr-x  3 root root 4096 Dec  2 11:35 sys
    -rw-r--r--  1 root root  131 Dec  2 11:40 t.py
    -rw-r--r--  1  777 root    0 Dec  2 12:07 testfile
    drwxrwxrwt  2 root root 4096 Sep 24  2016 tmp
    drwxr-xr-x 10 root root 4096 Oct 15  2016 usr
    drwxr-xr-x 12 root root 4096 Dec  2 11:24 var
    root@60ff5eae5908:/# exit
    exit
    [root@60ff5eae5908 containerExample]# capsh --drop=cap_chown,cap_setpcap,cap_setfcap,cap_sys_admin --chroot=$PWD/rootfs --
    root@60ff5eae5908:/#
    $ sudo capsh --drop=cap_chown,cap_setpcap,cap_setfcap,cap_sys_admin --chroot=$PWD/rootfs --
    root@localhost:/# whoami
    root
    root@localhost:/# chown nobody /bin/ls
    chown: changing ownership of '/bin/ls': Operation not permitted
    `

Conventional wisdom still states that VMs isolation is mandatory when running untrusted code. 
But security features like capabilities are important to protect against hacked applications running in containers.
Beyond more elaborate tools like seccomp, SELinux, and capabilities, applications running in 
containers generally benefit from the same kind of best practices as applications running 
outside of one. Know what your linking against, don’t run as root in your container, update 
for known security issues in a timely fashion.  

# Union File System (Overlay FS)
Ref. Link - https://www.datalight.com/blog/2016/01/27/explaining-overlayfs-%E2%80%93-what-it-does-and-how-it-works/
Union file systems are a creative solution to allow a virtual merge of multiple folders, 
while keeping their actual contents separate. The Overlay file system (OverlayFS) is one example of these,
though it is more of a mounting mechanism than a file system.

# Conclusion
Containers aren’t magic. Anyone with a Linux machine can play around with them and 
**tools like Docker and rkt are just wrappers around things built into every modern kernel.** 
No, you probably shouldn’t go and implement your own container runtime. 
But having a better understanding of these lower level technologies will help you work 
with these higher level tools (especially when debugging).
Ref. Link - https://ericchiang.github.io/post/containers-from-scratch/
Some other Ref.. Link
https://itnext.io/chroot-cgroups-and-namespaces-an-overview-37124d995e3d
Fog Cggroup (from Redhat)
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/ch-using_control_groups#The_cgconfig.conf_File



