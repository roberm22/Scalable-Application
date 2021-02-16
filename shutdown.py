#!/usr/bin/python
#coding=utf-8


#######################################################################################
######		   	Instalación y arranque del entorno			 ######
#######################################################################################
###### 			      Eliminamos todos los archivos 		         ######
######   		 de configuración y destruimos el escenario		 ###### 
#######################################################################################


from subprocess import call


def funcion_shutdown(comando):
	cmd_line = comando;
	call(cmd_line, shell=True);

#---------------------------------------------------------------------------------------------------------#

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Destruyendo el escenario...\n"+"\033[0;m");

funcion_shutdown("sudo vnx -f /mnt/tmp/pc2/pc2.xml --destroy");

print("\033[1;34m"+"\nEl escenario se ha destruido\n"+"\033[0;m");

#---------------------------------------------------------------------------------------------------------#

print("\033[1;30m"+"Borrando los archivos...\n"+"\033[0;m");

funcion_shutdown("rm /mnt/tmp/pc2.tgz -f");

funcion_shutdown("rm /mnt/tmp/descarga -f");

funcion_shutdown("rm -rf /mnt/tmp/scripts");

print("\033[1;34m"+"\nLos archivos de configuración se han borrado\n"+"\033[0;m");


print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");

print("\033[1;30m"+"Si quiere volver a arrancar el escenario, ejecute de nuevo el script:"+"\033[0;m");

print("\033[0;30m"+"\npython pc2.py" +"\033[0;34m"+ " ---> Script que inicializa el entorno y lo configura "+"\033[0;m");


print("\033[1;30m"+"-------------------------------------------------------------------------------------------\n"+"\033[0;m");


print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");




