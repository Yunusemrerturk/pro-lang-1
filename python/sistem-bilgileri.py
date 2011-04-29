#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################
# sistem bilgilerinizin tümünü öğrenin
# internet bağlantınız olduğu sürece
#
# emineker                     group19
######################################


import time, os, sys, commands, socket, fcntl, struct, urllib2

print '\tTarih\t\t» ', time.strftime("%d.%m.%Y")
print '\tSaat\t\t» ' , time.strftime("%X") 


def ip_adres(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa( fcntl.ioctl( s.fileno(), 0x8915, struct.pack('256s', ifname[:15] ) ) [20:24] )

def mac_adres(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

net_ip = urllib2.urlopen('http://www.whatismyip.com/automation/n09230945.asp').read().decode("utf8")

dosya  = open('/etc/resolv.conf' , 'r')
okunan =dosya.read()
dns    = okunan[ okunan.find('nameserver') + len('nameserver') + 1 :-2 ]
dosya.close()

print '\nAğ Bilgileri:'
print '\tlocalhost       »' , socket.gethostbyname(socket.gethostname())
print '\tip adres        »' , ip_adres('eth0')
print '\tinternet ip     »' , net_ip
print '\tdns adres       »' , dns
print '\tmac adres       »' , mac_adres('eth0')



disk = os.statvfs('/')
cap = disk.f_bsize*disk.f_blocks
ava = disk.f_bsize*disk.f_bavail
hop = float(1024*1024*1024)

print '\nDisk Kullanımı:'
print '\ttoplam alan     »' , "%.2f" %(cap/hop)      , 'GB' 
print '\tkullanılan      »' , "%.2f" %(ava/hop)      , 'GB'
print '\tboş alan        »' , "%.2f" %((cap-ava)/hop), 'GB'



henvir = {'GDM_KEYBOARD_LAYOUT':'klavye dili','LOGNAME':'login name' , 'USER':'kullanıcı',  'LANG':'sistem dili' , 'GDM_LANG':'gnome dili' , 'DESKTOP_SESSION':'masaüstü oturum' , 'HOME':'ev dizini' , 'PWD':'çalışma dizini' , 'PATH':'yol dizinleri'}

print '\nSistem Bilgileri' 
for i in henvir:
    print '\t' + henvir[i] + '\t» ' + os.environ[i]


print '\nSistem Bilgileri'
print '\tçekirdek adı        »' , commands.getoutput('uname -s')
print '\tbilgisayarının adı  »' , commands.getoutput('uname -n')
print '\tçekirdek sürümü     »' , commands.getoutput('uname -r')
print '\tkernel sürümü       »' , commands.getoutput('uname -v')
print '\tdonanım ismi        »' , commands.getoutput('uname -m')
print '\tişlemci tipi        »' , commands.getoutput('uname -p')
print '\tdonanım platformu   »' , commands.getoutput('uname -i')
print '\tişletim sistemi     »' , commands.getoutput('uname -o')




