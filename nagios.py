#!/usr/bin/python
#coding=utf-8
import os

os.system('useradd nagios')
os.system('groupadd nagcmd')
os.system('usermod -a -G nagcmd nagios')

os.chdir('/')
os.mkdir('downloads')
os.chdir('/downloads')
os.system('wget https://ufpr.dl.sourceforge.net/project/nagios/nagios-4.x/nagios-4.4.2/nagios-4.4.2.tar.gz')
os.system('tar -zxvf nagios-4.4.2.tar.gz')

os.chdir('/downloads/nagios-4.4.2')
os.system('./configure --with-nagios-group=nagios --with-command-group=nagcmd')

os.system('make all')
os.system('make install')
os.system('make install-init')
os.system('make install-config')
os.system('make install-commandmode')
os.system('make install-webconf')

os.system('htpasswd -c -b /usr/local/nagios/etc/htpasswd.users root xxxx')
os.system('service apache2 restart')
os.system('service nagios start')

