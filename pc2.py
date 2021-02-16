#!/usr/bin/python
#coding=utf-8


#######################################################################################
######				Configuración de los scripts			 ######
#######################################################################################
###### 		  		1. Configuración de los scripts	        	 ######
######   			2. Ejecución de los scripts    			 ###### 
#######################################################################################


from subprocess import call
import webbrowser #para abrir el navegador en una direccion en concreto
import os
import sys	
import zipfile

def funcion(comando):
	cmd_line = comando;
	call(cmd_line, shell=True);

print("")

#######################################################################################################################
################################# 	1. Configuración de los scripts		#######################################
#######################################################################################################################

if os.path.exists("/mnt/tmp/scripts"):
	sys.exit("\033[1;32m"+"Ya existe la carpeta, borrala antes de ejecutar todo"+"\033[0;m")
else:
	print("\033[1;32m"+"La carpeta se ha creado correctamente"+"\033[0;m")

os.chdir("/mnt/tmp")
funcion("wget -O descarga https://www.dropbox.com/sh/bb7c825aiaktym7/AADBJw00pa2HVLB_iovyuPlpa?dl=0")
funcion("mkdir scripts")
      
#descomprimimos la descarga
fantasy_zip = zipfile.ZipFile('/mnt/tmp/descarga')
fantasy_zip.extractall('/mnt/tmp/scripts')
fantasy_zip.close()


#######################################################################################################################
################################# 	2. Ejecución de los scripts		#######################################
#######################################################################################################################

os.chdir("/mnt/tmp/scripts")
funcion("python3 init.py")
funcion("python3 fw.py")
funcion("python3 bbdd.py")
funcion("python3 gluster.py")
funcion("python3 quiz.py")
funcion("python3 haproxy.py")
funcion("python3 nagios-apache.py")

# Abrir el navegador

webbrowser.open('http://20.20.2.2')
webbrowser.open('http://20.20.2.2:32700')
webbrowser.open('http://20.20.3.15/nagios')





