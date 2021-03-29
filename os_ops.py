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
