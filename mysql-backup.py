#! /usr/bin/python
# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser
import os, time, subprocess, socket

class BackupDB(object):

    str_date = time.strftime('%Y-%m-%d-%H:%M')
    exclude_database = ['information_schema','performance_schema','test','mysql']
    hostname = socket.gethostname()

    def __init__(self, path_conf, dest_backup):

        # em Debian, /etc/mysql/debian.cnf contem 'root' login and password.
        config = ConfigParser()
        config.read(path_conf)
        self.DB_username = config.get('client', 'user')
        self.DB_password = config.get('client', 'password')
        self.DB_hostname = config.get('client', 'host')

        self.dest = dest_backup


    def clear(self, directory):
        L = []
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)):
                L.append(item)

        number_of_files = len(L)

        if number_of_files > 1:
            print "% s - Foram encontrados %s arquivos de backup no diretório %s" %(self.str_date,
                                                                                    number_of_files,
                                                                                    directory)
            self.purge_dir(directory)
        else:
            print "%s - Foram encontrados %s arquivos de backup nenhum será removido %s" % (self.str_date,
                                                                                            number_of_files,
                                                                                            directory)

    def checkfile(self, filename):
        # pega informaçoes do arquivo
        filestats = os.stat(filename)
        if time.time() - filestats.st_mtime > 86400*7:
            # checa se o arquivo tem mais de 7 dias
            print "Removendo: %s" % (filename)
            os.remove(filename)

    def purge_dir(self, path):
        # Lista o diretório
        dirList = os.listdir(path)
        for filename in dirList:
            # executa funcao checkfile.
            self.checkfile(os.path.join(path, filename))


    def backup(self):
        #lista  as databases
        database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" %(self.DB_username,
                                                                                         self.DB_password,
                                                                                         self.DB_hostname)
        for database in os.popen(database_list_command).readlines():
            database = database.strip()
            if not database in self.exclude_database:
                print "%s - Criando Backup database: %s" %(self.str_date,
                                                           database)
                target_dir = "%s/%s/%s" %(self.dest,
                                          self.hostname,
                                          database)

                if not os.path.exists(target_dir):
                    print "%s - Criando novo diretório: %s" %(self.str_date,
                                                              target_dir)
                    os.makedirs(target_dir)
        
                filename = "%s/%s-%s.sql" %(target_dir,
                                             database,
                                             self.str_date)

                os.popen("mysqldump --max_allowed_packet=128M --single-transaction -u %s -p%s %s | gzip -c > %s.gz" %(self.DB_username,
                                                                                                                      self.DB_password,
                                                                                                                      database,
                                                                                                                      filename))
                self.clear(target_dir)

if __name__ == '__main__':

    '''
        configuration file with the user to access the database
        [client]
        host     = localhost
        user     = username
        password = senhha
        socket   = /var/run/mysqld/mysqld.sock
    '''
    #path padrao de maquinas Ubuntu/Debian
    path_conf = '/etc/mysql/debian.cnf'
    #dest = "/var/backups/mysql"
    dest = '/tmp'

    bkp = BackupDB(path_conf,dest)
    bkp.backup()