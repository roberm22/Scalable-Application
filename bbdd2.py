#!/usr/bin/python
#coding=utf-8

#######################################################################################
######		   		 Configuracion de bbdd Slave			 ######
#######################################################################################
###### 				  1. Modificacion de pc2		         ######
######   		   	   2. Configuración		     		 ###### 
#######################################################################################

from subprocess import call	
import os

def funcion_bbdd2(comando):
	cmd_line = comando;
	call(cmd_line, shell=True);

flag = False;

#######################################################################################################################
#######################################     	1. Modificacion de pc2 		#######################################
#######################################################################################################################

#https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
#Duplicamos pc2.xml 

funcion_bbdd2("cp ../pc2/pc2.xml prueba.xml")

#Copiamos s4.xml a pc2.xml

with open("prueba.xml","r") as prueba:

	with open("../pc2/pc2.xml","w") as pc2:

		for line in prueba:

			if 'name="bbdd"' in line:

				pc2.write(line);

				flag = True;

			elif "</vm>" in line and flag:

				pc2.write(line+"\n  <vm name=\"bbdd2\" type=\"lxc\" arch=\"x86_64\">\n    <filesystem type=\"cow\">filesystems/rootfs_lxc64-cdps</filesystem>\n    <if id=\"1\" net=\"LAN4\"><ipv4>20.20.4.32/24</ipv4></if>\n    <if id=\"9\" net=\"virbr0\"><ipv4>dhcp</ipv4></if>\n    <route type=\"ipv4\" gw=\"20.20.3.1\">20.20.0.0/16</route> \n    <filetree seq=\"on_boot\" root=\"/root/\">conf/hosts</filetree>\n    <exec seq=\"on_boot\" type=\"verbatim\">\n        cat /root/hosts >> /etc/hosts\n        rm /root/hosts\n        dhclient eth9\n    </exec>\n  </vm>"+"\n ");
				
				flag = False;

			else:

				pc2.write(line);

funcion_bbdd2("rm -f prueba.xml");


print("\033[1;30m"+"\n---------------------------------------------------------------------------------------------------------\n"+"\033[0;m");

#######################################################################################################################
#######################################     	2. Configuracion 		#######################################
#######################################################################################################################


hosts=open("../pc2/conf/hosts","a");

hosts.write("20.20.4.32   bbdd2"+"\n");

hosts.close();

print("\033[1;32m"+"BBDD Slave añadida al escenario"+"\033[m");



