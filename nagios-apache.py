#!/usr/bin/python
#coding=utf-8

#######################################################################################
######		   			Instalación y arranque de Nagios			 			 ######
#######################################################################################
###### 				   1. Instalar Apache 		          	 					 ######
######   		   	   2. Instalar Nagios 		     			 				 ###### 
#######################################################################################

from subprocess import call	
import os

def funcion_nagios(comando):
	cmd_line = "sudo lxc-attach --clear-env -n nagios -- "+comando;
	call(cmd_line, shell=True);

def funcion_mv(mv, comando, bash = False):
	if (bash == False) :
		cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- "+comando;
		call(cmd_line, shell=True);
	else:
		cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- bash -c \" " +comando+"\""
		call(cmd_line, shell=True);


#######################################################################################################################
#######################################     		1. Instalacion de Apache 			#######################################
#######################################################################################################################

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Instalando Apache...\n"+"\033[0;m");

funcion_nagios("apt-get -y update")

funcion_nagios("apt-get -y install libgd-dev unzip wget build-essential")
funcion_nagios("apt-get -y install apache2 php libapache2-mod-php php-gd")

funcion_nagios("service apache2 stop")
funcion_nagios("a2enmod rewrite")
funcion_nagios("a2enmod cgi")
funcion_nagios("service apache2 start")


print("\033[1;32m"+"\nApache instalado\n"+"\033[0;m");

print("\033[1;30m"+"\n---------------------------------------------------------------------------------------------------------\n"+"\033[0;m");


#######################################################################################################################
#######################################     		2. Instalación de Nagios		###################################
#######################################################################################################################

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Instalando Nagios...\n"+"\033[0;m");


os.chdir("/mnt/tmp/scripts")
os.system("sudo /lab/cdps/bin/cp2lxc nagios.py /var/lib/lxc/nagios/rootfs/home")

funcion_nagios("python /home/nagios.py")


print("\033[1;32m"+"\nNagios instalado\n"+"\033[0;m");

print("\033[1;30m"+"\n---------------------------------------------------------------------------------------------------------\n"+"\033[0;m");


