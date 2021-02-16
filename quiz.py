#!/usr/bin/python
#coding=utf-8


#######################################################################################
######		   Instalación y configuración de la aplicación QUIZ		 ######
#######################################################################################
###### 				  1. Creación del quiz		          	 ######
######   		   	2. Configuración del quiz     			 ###### 
######   		   	  3. Enlaces simbolicos     			 ###### 
#######################################################################################


from subprocess import call	#Si se prefiere utilizar un script en python en vez de un shellscript
import webbrowser #para abrir el navegador en una direccion en concreto

# Para ejecutar comandos en las máquinas virtuales desde el host se debe utilizar el comando
# lxc-attach. Sacado del enunciado. Ejecución de comandos en las máquinas virtuales


#funcion para el quiz: sacado pagina 8 enunciado + doc funciones python

def funcion_quiz(mv, comando, bash = False):
	if (bash == False) :
		cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- "+comando;
		call(cmd_line, shell=True);
	else:
		cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- bash -c \" " +comando+"\""
		call(cmd_line, shell=True);


#######################################################################################################################
#######################################     1. Creación de la app del QUIZ    #########################################
#######################################################################################################################

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Creando QUIZ-2021...\n"+"\033[0;m");


#Instalacion de la app QUIZ2021

funcion_quiz("s1","git clone https://github.com/CORE-UPM/quiz_2021.git");

funcion_quiz("s2","git clone https://github.com/CORE-UPM/quiz_2021.git");

funcion_quiz("s3","git clone https://github.com/CORE-UPM/quiz_2021.git");

funcion_quiz("s4","git clone https://github.com/CORE-UPM/quiz_2021.git");


print("\033[1;34m"+"\nEl repositorio se ha clonado en todos los servers\n"+"\033[0;m");


#Edición del fichero app.js

funcion_quiz("s1","sed '29d' quiz_2021/app.js > quiz_2021/app2.js; rm quiz_2021/app.js; mv quiz_2021/app2.js quiz_2021/app.js ", True);

funcion_quiz("s2","sed '29d' quiz_2021/app.js > quiz_2021/app2.js; rm quiz_2021/app.js; mv quiz_2021/app2.js quiz_2021/app.js ", True);

funcion_quiz("s3","sed '29d' quiz_2021/app.js > quiz_2021/app2.js; rm quiz_2021/app.js; mv quiz_2021/app2.js quiz_2021/app.js ", True);

funcion_quiz("s4","sed '29d' quiz_2021/app.js > quiz_2021/app2.js; rm quiz_2021/app.js; mv quiz_2021/app2.js quiz_2021/app.js ", True);

print("\033[1;34m"+"\nSe ha editado app.js correctamente\n"+"\033[0;m");


#Edición del puerto -> 80

funcion_quiz("s1","sed -i 's/3000/80/g' quiz_2021/bin/www");

funcion_quiz("s2","sed -i 's/3000/80/g' quiz_2021/bin/www");

funcion_quiz("s3","sed -i 's/3000/80/g' quiz_2021/bin/www");

funcion_quiz("s4","sed -i 's/3000/80/g' quiz_2021/bin/www");

print("\033[1;34m"+"\nSe ha editado www correctamente\n"+"\033[0;m");


#######################################################################################################################
###########################################  2. Configuración  ########################################################
#######################################################################################################################

# Esta  forma  es  muy  útil  cuando  se  requiere  ejecutar comandos  desde  un  determinado directorio
# (ej: “cd directorio; comando1; comando2”), ya que cada llamada a lxc-attaches independiente  y  si  se  cambia  de  
# directorio  en  una  llamada,  ese  cambio  no  aplica  a  la siguiente.

print("\033[1;34m"+"\nInstalando QUIZ2021...\n"+"\033[0;m");

#--------------------------------------------------------s1--------------------------------------------------------------#

print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");

funcion_quiz("s1","cd /quiz_2021; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; npm run-script migrate_env; npm run-script seed_env; ./node_modules/forever/bin/forever start ./bin/www", True);

print("\033[1;34m"+"\nQUIZ2021 instalado en S1\n"+"\033[0;m");

#--------------------------------------------------------s2--------------------------------------------------------------#

# Recuerde que los comandos para aplicar las migraciones y ejecutar el seeder, solo deben ejecutarse desde uno de los servidores.

print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");

funcion_quiz("s2","cd /quiz_2021; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www", True);

print("\033[1;34m"+"\nQUIZ2021 instalado en S2\n"+"\033[0;m");

#--------------------------------------------------------s3--------------------------------------------------------------#

print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");

funcion_quiz("s3","cd /quiz_2021; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www", True);

print("\033[1;34m"+"\nQUIZ2021 instalado en S3\n"+"\033[0;m");


#--------------------------------------------------------s4--------------------------------------------------------------#

print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");

funcion_quiz("s4","cd /quiz_2021; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www", True);

print("\033[1;34m"+"\nQUIZ2021 instalado en S4\n"+"\033[0;m");


print("\033[1;30m"+"-------------------------------------------------------------------------------------------\n"+"\033[0;m");

#######################################################################################################################
###########################################  3. Enlaces simbolicos  ###################################################
#######################################################################################################################


funcion_quiz("s1","ln -s /mnt/nas /quiz_2021/public/uploads");

funcion_quiz("s2","ln -s /mnt/nas /quiz_2021/public/uploads");

funcion_quiz("s3","ln -s /mnt/nas /quiz_2021/public/uploads");

funcion_quiz("s4","ln -s /mnt/nas /quiz_2021/public/uploads");


print("\033[1;34m"+"\nEnlaces simbolicos configurados\n"+"\033[0;m");


print("\033[1;32m"+"\nQUIZ2021 instalado y configurado\n"+"\033[0;m");
print("\033[1;30m"+"********************************************************************************************************\n"+"\033[0;m");










