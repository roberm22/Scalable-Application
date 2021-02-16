#!/usr/bin/python
#coding=utf-8

#######################################################################################
######				Configuración de la base de datos		 ######
#######################################################################################
###### 				  1. Creación de la bbdd		         ######
######   			  2. Comprobaciones    			         ###### 
######   			  3. Master - Slave    			         ###### 
#######################################################################################


from subprocess import call	#Si se prefiere utilizar un script en python en vez de un shellscript

# Para ejecutar comandos en las máquinas virtuales desde el host se debe utilizar el comando
# lxc-attach. Sacado del enunciado. Ejecución de comandos en las máquinas virtuales


#funcion para la bbdd:

def funcion_bbdd(comando, mv = None, bash = False):
	if (mv == None) :
		cmd_line = "sudo lxc-attach --clear-env -n bbdd -- "+comando;
		call(cmd_line, shell=True);

	elif (bash == True):
		cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- bash -c \" " +comando+"\""
		call(cmd_line, shell=True);

	else:
		cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- "+comando;
		call(cmd_line, shell=True);

def funcion_bbdd2(comando, mv = None):
	if (mv == None) :
		cmd_line = "sudo lxc-attach --clear-env -n bbdd2 -- "+comando;
		call(cmd_line, shell=True);
	else:
		cmd_line = "sudo lxc-attach --clear-env -n "+mv+" -- bash -c \" " +comando+"\""
		call(cmd_line, shell=True);


# La base de datos a utilizar será MariaDB que correrá en el servidor BBDD  
# y  que  será  accedida  en  remoto  desde  los  servidores  s1-3  para  almacenar  
# la información de la aplicación QUIZ. Para instalarla en el servidor BBDDse deben ejecutar 



#######################################################################################################################
#######################################     1. Creación de la bbdd    #################################################
#######################################################################################################################

print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Creando la BBDD...\n"+"\033[0;m");

#---------------------------------------------------------------------------------------------------------#
# actualizamos la lista de paquetes disponibles y sus versiones
funcion_bbdd("apt update");

# Instalamos MariaDB
funcion_bbdd("apt -y install mariadb-server");

print("\033[1;34m"+"\nMariaDB está instalada\n"+"\033[0;m");

#---------------------------------------------------------------------------------------------------------#

# Creación database Quiz

funcion_bbdd("sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf");

funcion_bbdd("systemctl restart mysql");

funcion_bbdd("mysqladmin -u root password xxxx");

funcion_bbdd("mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\"");

funcion_bbdd("mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\"");

funcion_bbdd("mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to'quiz'@'localhost' IDENTIFIED by 'xxxx';\"");

funcion_bbdd("mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\"");

funcion_bbdd("mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\"");

funcion_bbdd("systemctl restart mysql");

#---------------------------------------------------------------------------------------------------------#


#######################################################################################################################
########################################### 2. Comprobaciones #########################################################
#######################################################################################################################

print("\033[1;32m"+"\nLa configuración se ha realizado con exito"+"\033[0;m");

funcion_bbdd("apt -y install mariadb-client","s1");

funcion_bbdd("apt -y install mariadb-client","s2");

funcion_bbdd("apt -y install mariadb-client","s3");

funcion_bbdd("apt -y install mariadb-client","s4");

print("\033[1;32m"+"\nSe ha instalado MariaDB en los servers"+"\033[0;m");

print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");

print("\033[1;30m"+"Una  forma  de  comprobar  que  la  base  de  datos  esta  funcionando consiste  en\ntratar  de acceder a ella en remoto desde los servidores s1-s3. \nPara ello, desde alguno de los servidores ejecute: "+"\033[0;m");

print("\033[0;30m"+"\napt -y install mariadb-client" +"\033[0;34m"+ " ---> Para instalar MariaDB en el servidor "+"\033[0;m");

print("\033[0;30m"+"\nmysql -h 20.20.4.31 -u quiz --password='xxxx' quiz" +"\033[0;34m"+ " ---> Si funciona, debería aparecer el prompt deMariaDB "+"\033[0;m");

print("\033[0;30m"+"\nshow databases;" +"\033[0;34m"+ " ---> Dentro de MariaDB para ver las bases de datos "+"\033[0;m");

print("\033[1;30m"+"-------------------------------------------------------------------------------------------\n"+"\033[0;m");

print("\033[1;30m"+"********************************************************************************************************\n"+"\033[0;m");


#######################################################################################################################
########################################### 3. Master - Slave #########################################################
#######################################################################################################################


print("\033[1;30m"+"\n********************************************************************************************************"+"\033[0;m");

print("\033[1;30m"+"Creando la BBDD Master-Slave...\n"+"\033[0;m");


funcion_bbdd("cd /etc/mysql/mariadb.conf.d; echo 'server-id=150' >> 50-server.cnf", "bbdd", True);

funcion_bbdd("mysqladmin -u root password xxxx");

funcion_bbdd("mysql -u root --password=xxxx -e \"GRANT REPLICATION SLAVE ON *.* to 'root'@'%' IDENTIFIED BY 'xxxx';\"");

funcion_bbdd("mysql -u root --password=xxxx -e \"FLUSH PRIVILEGES;\"");

funcion_bbdd("cd /etc/mysql/mariadb.conf.d; echo 'log_bin=/var/log/mysql/mariadb-bin' >> 50-server.cnf", "bbdd", True);

funcion_bbdd("systemctl restart mysql");


print("\033[1;30m"+"\n-----------"+"\033[0;m");

funcion_bbdd2("apt update");

funcion_bbdd2("apt -y install mariadb-server");

print("\033[1;30m"+"-----------"+"\033[0;m");


funcion_bbdd2("cd /etc/mysql/mariadb.conf.d; echo '[mysqld]' >> 50-server.cnf", "bbdd2");

funcion_bbdd2("sed -i -e 's/bind-address.*/bind-address=20.20.4.31/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf");

funcion_bbdd2("cd /etc/mysql/mariadb.conf.d; echo 'server-id=151' >> 50-server.cnf", "bbdd2");

funcion_bbdd2("cd /etc/mysql/mariadb.conf.d; echo 'log_bin=/var/log/mysql/mariadb-bin' >> 50-server.cnf", "bbdd2");

funcion_bbdd2("cd /etc/mysql/mariadb.conf.d; echo 'report-host=mariadb-slave1' >> 50-server.cnf", "bbdd2");

funcion_bbdd2("systemctl restart mysql");


funcion_bbdd2("mysql -u root --password=xxxx -e \"CHANGE MASTER TO MASTER_HOST='20.20.4.31', MASTER_USER='root', MASTER_PASSWORD='xxxx', MASTER_LOG_FILE='mariadb-bin.000001', MASTER_LOG_POS=315;\"");

funcion_bbdd2("mysql -u root --password=xxxx -e \"start slave;\"");


print("\033[1;32m"+"\nLa configuración se ha realizado con exito"+"\033[0;m");

print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------"+"\033[0;m");

print("\033[1;30m"+"Una  forma  de  comprobar  que  las  bases  de  datos Master-Slave  estan  funcionando.\nEjecutar dentro de MariaDB los siguientes comandos: "+"\033[0;m");

print("\033[0;30m"+"\nshow slave status\G" +"\033[0;34m"+ " ---> To check slave status. Slave IO and SQL should indicate running state "+"\033[0;m");

print("\033[0;30m"+"\nshow master status\G" +"\033[0;34m"+ " ---> To check master status."+"\033[0;m");

print("\033[0;30m"+"\nselect ID,user,host,db,command,time,state from information_schema.processlist order by time desc limit 5;\n" +"\033[0;34m"+ "---> Check of process list on the master should also display connections from slave servers "+"\033[0;m");

print("\033[1;30m"+"\n-------------------------------------------------------------------------------------------\n"+"\033[0;m");


print("\033[1;30m"+"********************************************************************************************************\n"+"\033[0;m");



