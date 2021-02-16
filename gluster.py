#!/usr/bin/python
#coding=utf-8

#######################################################################################
######				Configuración de GlusterFS			 ######
#######################################################################################
###### 		  1. Configuración de servidores de disco (nas)		         ######
######   	2. Configuración del montaje desde los servidores web (s1-s3)    ###### 
######              		 3. Comprobaciones                               ######
#######################################################################################

import time
from subprocess import call	#Si se prefiere utilizar un script en python en vez de un shellscript

# Para ejecutar comandos en las máquinas virtuales desde el host se debe utilizar el comando
# lxc-attach. Sacado del enunciado. Ejecución de comandos en las máquinas virtuales


#funcion para el nas: sacado pagina 8 enunciado
def funcion_nas(mv,comando):
	cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- "+comando;
	call(cmd_line, shell=True);

#######################################################################################################################
################################# 1. Configuración de servidores de disco (nas) #######################################
#######################################################################################################################

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Iniciando Configuración de GlusterFS...\n"+"\033[0;m");

#---------------------------------------------------------------------------------------------------------#

#Añadimos los servidores al cluster

funcion_nas("nas1","gluster peer probe 20.20.4.22");

funcion_nas("nas1","gluster peer probe 20.20.4.23");

print("\033[1;34m"+"\nServidores añadidos al cluster\n"+"\033[0;m");

#Es necesario dejar un tiempo porque sino, si es inmediato, el create da error y seria necesario ejecutar este script de nuevo

print("\033[1;34m"+"Configurando...\n"+"\033[0;m");

time.sleep(4);

	
#---------------------------------------------------------------------------------------------------------#

#Creamos un volumen con tres servidores que replican la información

funcion_nas("nas1","gluster volume create nas replica 3 20.20.4.21:/nas 20.20.4.22:/nas 20.20.4.23:/nas force");

#Arrancamos el volumen

funcion_nas("nas1","gluster volume start nas");

print("\033[1;34m"+"\nVolumen creado y arrancado\n"+"\033[0;m");


#---------------------------------------------------------------------------------------------------------#

#Para agilizar  la  recuperación  del  volumen  ante  caídas  de  uno  de  los  servers, cambiamos el valor del timeout en todos

funcion_nas("nas1","gluster volume set nas network.ping-timeout 5");

funcion_nas("nas2","gluster volume set nas network.ping-timeout 5");

funcion_nas("nas3","gluster volume set nas network.ping-timeout 5");

print("\033[1;34m"+"\nCambiado valor del timeout\n"+"\033[0;m");



#######################################################################################################################
######################### 2. Configuración del montaje desde los servidores web (s1-s3) ###############################
#######################################################################################################################

#Para acceder al sistema de ficheros exportado por los nasX desde los servidores de web

funcion_nas("s1","mkdir /mnt/nas");

funcion_nas("s2","mkdir /mnt/nas");

funcion_nas("s3","mkdir /mnt/nas");

funcion_nas("s4","mkdir /mnt/nas");

funcion_nas("s1","mount -t glusterfs 20.20.4.21:/nas /mnt/nas");

funcion_nas("s2","mount -t glusterfs 20.20.4.22:/nas /mnt/nas");

funcion_nas("s3","mount -t glusterfs 20.20.4.23:/nas /mnt/nas");

funcion_nas("s4","mount -t glusterfs 20.20.4.23:/nas /mnt/nas");

print("\033[1;34m"+"\nConfiguración del montaje realizada"+"\033[0;m");


#######################################################################################################################
########################################### 3. Comprobaciones #########################################################
#######################################################################################################################

print("\033[1;32m"+"\nLa configuración se ha realizado con exito"+"\033[0;m");

print("\033[0;34m"+"\nPuede comprobarlo desde el directorio /mnt/nas del servidor web\ndonde se verá el contenido del directorio exportado por los nas. "+"\033[0;m");

print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");

print("\033[1;30m"+"Puede ejecutar los siguientes comando para comprobarlo: "+"\033[0;m");

print("\033[0;30m"+"\nwatch tree /nas" +"\033[0;34m"+ " ---> Le permitirá ver en tiempo real el contenido del directorio compartido (/nas) de cada servidor "+"\033[0;m");

print("\033[0;30m"+"\nifconfig eth1 down" +"\033[0;34m"+ " ---> Para ver cómo se comporta el sistema en caso de fallo de un servidor, desconecte un servidor cualquiera "+"\033[0;m");

print("\033[1;30m"+"-------------------------------------------------------------------------------------------"+"\033[0;m");

print("\033[1;30m"+"********************************************************************************************************\n"+"\033[0;m");



