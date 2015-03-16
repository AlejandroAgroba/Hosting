# * coding: utf8 *

import sys
import os
import MySQLdb
import string
from random import choice


#Preguntamos por el nombre de ususario y dominio

usuario=sys.argv[1]
dominio=sys.argv[1]

#Primero comprobamos si el usuario y el dominio existen.
#En caso de que no creamos la carpeta
#Si existen lanzamos el error

if os.path.isdir("/var/www/%s" % (usuario)) == False and os.path.isfile("/etc/apache2/sites-available/%s" % (dominio)) == False:
os.system("mkdir /var/www/%s" % (usuario))
