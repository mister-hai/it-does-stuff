"""
This is a test of the command framework
This performs the steps necessary to debootstrap a new
Debian/Ubuntu/Mint/PopOS installation for use as a sandbox
or new OS install.
TODO:
    Download:
        -PopOS Hybrid ISO
    Unpack:
        - PopOS filesystem.squashfs
    Overlay:
        - PopOS filesystem over Ubuntu of same release version
    Mount:
        - /boot/efi 
            add UUID to fstab, mount before chroot
            
    Create:
        - /etc/fstab
        - /etc/resolvconf entries
        - butt-stuff
"""
#class Debootstrap:
#    '''
#    Does disk stuff
#    pass True to "active" to set it to perform the task on init
#    '''
#    def __init__(self, components,arch,sandy_path,repository, user,password,extras, active = False):
#        self.active = active
#        self.components = components
#        self.arch = arch
#        self.sandy_path = sandy_path
#        self.repository = repository
#        self.user = user
#        self.password = password
#        self.extras = extras
        #running on init
#        if getattr(self, 'active') == True:
#            self.do_it_all()


    #def do_it_all(self):
    #    self.debootstrap_action(self.components,self.arch,self.sandy_path,self.repository)
    #    self.stage1(self.components,self.arch,self.sandy_path,self.repository,self.user,self.password,self.extras)
    #    self.chroot_staging(self.sandy_path)
    #    self.stage2(self.sandy_path, self.user, self.password, self.extras)

def debootstrap_action(self, components,arch,sandy_path,repository):
        steps = {
                 'debootstrap' : ["sudo debootstrap --components {} --arch {} , bionic {} {}".format(components,arch,sandy_path,repository),
                 "[+] Beginning Debootstrap",
                 "[+] Debootstrap Finished Successfully!",
                 "[-]Debootstrap Failed! Check the logfile!"]
                }
        
def stage1(self, components,arch,sandy_path,repository, user, password, extras):
        '''
    Stage 1 :
        - sets up base files/directory's
            * debootstrap
            * copy resolv.conf
        - mounts for chroot
            * /dev, /proc, /sys
            '''
        # Sequential commands
        steps = {
            'copy_resolvconf':["sudo cp /etc/resolv.conf {}/etc/resolv.conf".format(sandy_path),
            "[+] Copying Resolv.conf",
            "[+] Resolv.conf copied!",
            "[-]Copying Resolv.conf Failed! Check the logfile!"],
            'copy_sourceslist':["sudo cp /etc/apt/sources.list {}/etc/apt/".format(sandy_path)],
            "[+] Copying Sources.list",
            "[+] Sources.list copied!",
            "[-]Copying Sources.list Failed! Check the logfile!"]
            }
        

def chroot_staging(sandy_path):
        '''
    used in stage2()
        '''
        #mount and bind the proper volumes
        steps = {
                ['mount_dev' : "sudo mount -o bind /dev {}/dev".format(sandy_path),"[+] Mounting /dev" "[+] Mounted!", "[-]Mounting /dev Failed! Check the logfile!"],
                ['mount_proc' : "sudo mount -o bind -t proc /proc {}/proc".format(sandy_path),"[+] Mounting /proc", "",""],
                ['mount_sys' : "sudo mount -o bind -t sys /sys {}/sys".format(sandy_path),"[+] Mounting /sys", "",""]
                }

def stage2(self, sandy_path, user, password, extras):
        '''
    Establishes Chroot
        - sets username / password
        - LOG'S IN, DONT LEAVE THE COMPUTER
            -for security/data entry purposes
        - updates packages
        - installs debconf, nano, curl
        - installs extras
        '''
        steps = {'chroot':
                    ["sudo chroot {} ".format(sandy_path),
                      "[+] Chrooted!".format(),
                      "[-] Chroot Failed! Check the logfile!".format()     ],
                 'adduser':
                     ["useradd {}".format(user),
                      "[+] User Added!",
                      "[-] Failed! Check the logfile!"     ],
                 'change_password':
                     ["passwd  {}".format(password),
                      "[+] Password Changed!",
                      "[-] Failed! Check the logfile!"     ],
                 'login':
                     ["login {}".format(user),
                      "[+] Logged In!",
                      "[-] Failed! Check the logfile!"     ],
                 'apt_update':
                     ["sudo -S apt-get update",
                      "[+] Packages Updated!",
                      "[-] Failed! Check the logfile!"     ],
                 'apt_install_extras':
                     ["sudo -S apt-get --no-install-recommends install {}".format(extras),
                      "[+] Extras Installed!",
                      "[-] Failed! Check the logfile!"     ]
                }
                # TODO: clean the gpg error message
                # sudo -S apt-get install locales dialog
                # sudo -S locale-gen en_US.UTF-8  # or your preferred locale
                # tzselect; TZ='Continent/Country'; export TZ  #Congure and use our local time instead of UTC; save in .prole
 ...
#update-initramfs: Generating /boot/initrd.img-5.4.0-7634-generic
#kernelstub.Config    : INFO     Looking for configuration...
#kernelstub           : WARNING  Live mode is enabled!
#Kernelstub is running in live environment mode. This usually means that you are running a live disk, and kernelstub should not run. We are thus exiting with 0.
#If you are not running a live disk, please run `sudo kernelstub` to disable live mode.

#class Chroot:
#    '''
#    Does what it says on the label
#    '''
#    def __init__(self, kwargs):
#        for (k, v) in kwargs.items():
#            setattr(self, k, v)
#    
#    def step_on_through(self):
def step_on_through(self):
        steps = { 'mount_dev': 
                    ["sudo mount -o bind /dev {}/dev".format(self.chroot_base),
                     "[+] Mounted /dev on {}!".format(self.chroot_base),
                     "[-] Mounting /dev on {} Failed! Check the logfile!".format(self.chroot_base) ],
                 'mount_proc': 
                     ["sudo mount -o bind /proc {}/proc".format(self.chroot_base),
                     "[+] Mounted /proc on {}!".format(self.chroot_base),
                     "[-] Mounting /proc on {} Failed! Check the logfile!".format(self.chroot_base)],
                 'mount_sys': 
                     ["sudo mount -o bind /sys {}/sys".format(self.chroot_base),
                     "[+] Mounted /sys on {}!".format(self.chroot_base),
                     "[-] Mounting /sys on {} Failed! Check the logfile!".format(self.chroot_base)],
                    'move_resolvconf':
                         ["sudo cp /etc/resolv.conf {}/etc/resolv.conf".format(self.chroot_base),
                         "[+] Resolv.conf Copied!",
                         "[-] Failure To Copy Resolv.conf! Check the logfile!"],
                'chroot':    
                    ["sudo chroot {} ".format(chroot_base),
                    "[+] Success!",
                    "[-] Failed! Check the logfile!"]
                }

def swap_resume_location():
                # add a grep from SPACE UUID= to the end of uuid
                '':["blkid | awk -F\" '/swap/ {print $2}'

                 # add swap UUID to /etc/initramfs-tools/conf.d/resume
                 #printf "RESUME=UUID=$(blkid | awk -F\" '/swap/ {print $2}')\n" | sudo tee /etc/initramfs-tools/conf.d/resume
                 '':["printf 'RESUME=UUID=$(blkid | awk -F\\" '/swap/ {print $2}\')\n" | sudo tee /etc/initramfs-tools/conf.d/resume',
                 
                #  update the kernels on the system:
                '':["sudo update-iniramfs -u -k all
                    
 
# After change to a text console (pressing Ctrl+Alt+F2) and logging in as root, 
# use the following command to disable the graphical target, which is what keeps 
# the display manager running:
#stop x
stop_graphical1 = { 'stop_graphical1' : ['systemctl isolate multi-user.target',"",""]}
# start x
start_x_session = { 'start_x_session' : ['systemctl start graphical.target',"",""]}
# set default to text
set_default_multiuser1 = { 'set_default_multiuser1' : ['sudo systemctl set-default multi-user.target',"",""]}
set_default_multiuser2 = { 'set_default_multiuser2' : ['sudo systemctl set-default runlevel3.target',"",""]}
#set default to x
set_default_graphical1  = { 'set_default_graphical1' : ['sudo systemctl set-default graphical.target',"",""]}
set_default_graphical2  = { 'set_default_graphical2' : ['sudo systemctl set-default runlevel5.target',"",""]}
# unload the Nvidia drivers using modprobe -r (or rmmod directly):
remove_nvidia_drm = { 'remove_nvidia_drm' : ['modprobe -r nvidia-drm',"",""]}
# remove the proprietary Nvidia driver:
remove_nvidia_drivers   = { 'remove_nvidia_drivers' : ["sudo dpkg -P $(dpkg -l | grep nvidia-driver | awk '{print $2}')","",""]}
apt_autoremove          = { 'apt_autoremove' : ["sudo apt autoremove","",""]}                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
