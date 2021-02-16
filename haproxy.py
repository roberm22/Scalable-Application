#!/usr/bin/python
#coding=utf-8


#######################################################################################
######				Configuración de HAPROXY			 ######
#######################################################################################
###### 		 	 1. Configuración del balanceador de trafico 	         ######
######   		 2. Edición de las paginas web de los servers	    	 ###### 
#######################################################################################

from subprocess import call


#funcion para el haproxy:

def funcion_haproxy(comando, copy = False, mv = None):

	if (copy == True) :
		print("\033[0;34m"+"\n"+comando+"\033[0;m");
		cmd_line = "sudo /lab/cdps/bin/cp2lxc haproxy.cfg /var/lib/lxc/lb/rootfs/etc/haproxy";
		call(cmd_line, shell=True);

	elif (mv == None) :
		cmd_line = "sudo lxc-attach --clear-env -n lb -- "+comando;
		call(cmd_line, shell=True);

	else:
		cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- bash -c \" " +comando+"\"";
		call(cmd_line, shell=True);


#######################################################################################################################
################################# 1. Configuración del balanceador de trafico   #######################################
#######################################################################################################################

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Iniciando Configuración de HAproxy...\n"+"\033[0;m");


funcion_haproxy("apt-get update -y");

funcion_haproxy("apt-get install haproxy -y");


print("\033[1;34m"+"\nHAproxy está instalado\n"+"\033[0;m");

print("\033[1;30m"+"-------------------------------------------------------------------------------------------"+"\033[0;m");


funcion_haproxy("service apache2 stop");

funcion_haproxy("Copiando haproxy.cfg al balanceador\n", True);


print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");


#######################################################################################################################
################################# 2. Edición de las paginas web de los servers  #######################################
#######################################################################################################################


funcion_haproxy("echo '<h3>Servidor 1<h3>' >> /quiz_2021/views/index.ejs", False, "s1");

funcion_haproxy("echo '<h3>Servidor 2<h3>' >> /quiz_2021/views/index.ejs", False, "s2");

funcion_haproxy("echo '<h3>Servidor 3<h3>' >> /quiz_2021/views/index.ejs", False, "s3");

funcion_haproxy("echo '<h3>Servidor 4<h3>' >> /quiz_2021/views/index.ejs", False, "s4");

print("\033[1;34m"+"\nSe han modificado las páginas web de los servers\n"+"\033[0;m");


funcion_haproxy("sudo service haproxy restart");



print("\033[1;32m"+"\nLa configuración se ha realizado con exito"+"\033[0;m");

print("\033[1;30m"+"********************************************************************************************************\n"+"\033[0;m");


