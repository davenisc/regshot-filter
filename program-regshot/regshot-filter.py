#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
import os.path
import csv
import time
from functools import reduce
import re
import json
from os import path
from colorama import Back, Fore, init, Style
from time import sleep
from tqdm import tqdm


def almacenardatos():
    """a='cualquier cosa'
    print('si funciona esta chimbada')
    return a"""
    init()
    print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
    init()
    print(Fore.RED + "Coincidencias de (port) o puertos encontrados "+Fore.GREEN+" **************************************")
    print ("")
    RED = '\033[1;31m'
    NOCOLOR = '\033[0;0m'

    palabras4 = ['tcp', '.com', 'n/a']

    palabra4 = 'tcp'
    ocurrencias4 = []
    with open('doc.txt') as lineas:
        for linea in lineas:
            if palabra4 in linea:
                ocurrencias4.append(linea)

    
        #print(aImprimir4)
    return ocurrencias4

def crear_archivo():
    if path.exists('prueba1.txt'):
        print('El archivo ya existe')
        file=open("prueba1.txt", "a")
    else:
        file=open("prueba1.txt", "a")
        print('El archivo fue creado')

        pass    

def menu():

    """
Inicio logo         ###################################################################
    """
#Color de texto inicio  ################################################################
#Color de texto fin  ###################################################################
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
init()
print(Fore.RED + "Software link "+Fore.GREEN+" : https://github.com/davenisc")
init()
print(Fore.RED + "Description "+Fore.GREEN+"   : BASIC SCRIPT TO MAKE FILTERS TO REGSHOT LOGS")
init()
print(Fore.RED + "Contact Mail "+Fore.GREEN+"  : sysvd@protonmail.com")
print ("")
#Color de texto inicio ###################################################################
init()
print(Fore.WHITE + "")
#Color de texto fin    ###################################################################
print ("____________________________________________________________________________")
print ("                                                                                      ")
print ("                                                                                     ")
print ("----------------------------------- By DvSyS -------------------------------                   ")
init()
print(Fore.RED + "     ___           ______        __    ____ ____            "+Fore.GREEN+"     . ---- .")
init()   
print(Fore.RED + "    / _ \___ ___ _/ __/ /  ___  / /_  / _(_) / /____ ____   "+Fore.GREEN+"    /        \ ")
init()
print(Fore.RED + "   / , _/ -_) _ `/\ \/ _ \/ _ \/ __/ / _/ / / __/ -_) __/   "+Fore.GREEN+"   |  O  _  O | ")
init()
print(Fore.RED + "  /_/|_|\__/\_, /___/_//_/\___/\__/ /_//_/_/\__/\__/_/      "+Fore.GREEN+"   |  ./   \. |")
init()
print(Fore.RED + "          /___/                                             "+Fore.GREEN+"   /  `-._.-'  \  ")
init()    
print(Fore.RED + "                                                            "+Fore.GREEN+" .' /         \ `.   ")
init()
print(Fore.RED + "    ---------------------------------------------        "+Fore.GREEN+".-~.-~/           \~-.~-.")
init()
print(Fore.RED + "    |   @DaveNISC   |     2018      |   v 1.0   |   "+Fore.GREEN+" .-~ ~    |             |    ~ ~-.")
init()
print(Fore.RED + "    ---------------------------------------------"+Fore.GREEN+"    `- .     |             |     . -'")
init()                  
print(Fore.RED + "    | @Sebastianf94 | @whitepadawan |           |   "+Fore.GREEN+"      ~ - |             | - ~     ")
init() 
print(Fore.RED + "                                                    "+Fore.GREEN+"          \             /         ")
init()
print(Fore.RED + "                                                    "+Fore.GREEN+"        ___\           /___       ")
init()
print(Fore.RED + "                                                    "+Fore.GREEN+"        ~;_  >- . . -<  _i~       ")
init()
print(Fore.RED + "                                                       "+Fore.GREEN+"        `'         `'          ") 
print (Fore.WHITE +"____________________________________________________________________________\n")
#print ("")  

#Color de texto inicio 


#Color de texto fin
"""
fin logo
"""
"""
Funci�n que limpia la pantalla y muestra nuevamente el menu
"""
#os.system('clear') # NOTA para windows tienes que cambiar clear por cls

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce una opcion')
            print ("")
     
    return num
 
salir = False
opcion = 0

while not salir:

    init()
    print(Fore.RED + "Requerimientos del sistema "+Fore.GREEN+" : \n")
    init()
    print(Fore.RED + "Sistemas Operativos "+Fore.GREEN+"   Windows 10 , Kali linux")
    init()
    print(Fore.RED + "Instalar Python "+Fore.GREEN+"       https://www.python.org/downloads/")
    init()
    print(Fore.RED + "Instalar Pip "+Fore.GREEN+"          https://pip.pypa.io/en/stable/installing/")
    init()
    print(Fore.RED + "Ejucutar Terminal"+Fore.GREEN+"      Root")
    init()
    print(Fore.RED + "Ejucutar CMD"+Fore.GREEN+"           Administrador \n\n")
 
    init()
    print(Fore.RED + "1. "+Fore.CYAN+" Actualizar complementos")
    init()
    print(Fore.RED + "2. "+Fore.CYAN+" Filtrar y crear logs con TCP, WWW, HTTP, EXE, PORT")
    init()
    print(Fore.RED + "3. "+Fore.CYAN+" Mostrar URLs encontradas")
    init()
    print(Fore.RED + "4. "+Fore.CYAN+" Analizar URLs")
    init()
    print(Fore.RED + "5. "+Fore.CYAN+" Salir")
    print ("") 
    print ("Elige una opcion")
    print ("") 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opcion 1\n")
        print ("Este proceso puede tardar varios minutos")
        print ("")
        print(Fore.RED + "Iniciando instalación ")
        print ("")
        time.sleep(5)
        init()
        print(Fore.RED + "Instalando pip")
        os.system('python get-pip.py')
        time.sleep(5)
        init()
        print(Fore.GREEN + ".....................")
        #scan = raw_input("Ingresa URL a analisar\n")
        init()
        print(Fore.RED + "Instalando Nmap")
        os.system('pip install nmap')
        time.sleep(5)
        init()
        print(Fore.GREEN + ".....................")
        init()
        print(Fore.RED + "Instalando colorama")
        os.system('pip install colorama')
        time.sleep(5)
        init()
        print(Fore.GREEN + ".....................")
        init()
        print(Fore.RED + "Instalando tqdm")
        os.system('pip install tqdm')
        time.sleep(5)
        init()
        print(Fore.GREEN + ".....................")
       
        print ("")
    elif opcion == 2:
        print ("Opcion 2")
        #data = os.system('netstat -ano')
        #os.system('netstat -ano > c:\escaneo1.txt')
        print ("")
        """
        time.sleep(5)"""
        ############################################################################################################################################ inicio
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "Coincidencias de (port) o puertos encontrados "+Fore.GREEN+" **************************************")
        print ("")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'

        palabras1 = ['port', 'n/a', 'n/a']
        palabra1 = 'port'
        ocurrencias = []
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra1 in linea:
                    ocurrencias.append(linea)

        for frase in ocurrencias:
            aImprimir1 = frase
            for palabra1 in palabras1:
                if palabra1 in frase:
                    aImprimir1 = re.sub(r'(%s)' % palabra1, r'%s\1%s' % (RED, NOCOLOR), frase)

                    url06 = frase
                    f1 = open ('port.txt','a')
                    f1.write(url06)
                    f1.flush()
                    break
                    
            print(aImprimir1) 
            
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")    
        #print (ocurrencias)
        ############################################################################################################################################## fin
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "Coincidencias de (.exe) o ejecutables encontrados "+Fore.GREEN+" **********************************")
        print ("")
        print ("")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'
        palabras = ['.exe', 'n/a', 'n/a']
        palabra = '.exe'
        ocurrencias1 = []
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra in linea:
                    ocurrencias1.append(linea)            
        #print (ocurrencias1)
        for frase in ocurrencias1:
            aImprimir = frase
            for palabra in palabras:
                if palabra in frase:
                    aImprimir = re.sub(r'(%s)' % palabra, r'%s\1%s' % (RED, NOCOLOR), frase)
                    

                    url02 = frase
                    f1 = open ('exe.txt','a')
                    f1.write(url02)
                    f1.flush()
                    break
            print(aImprimir)

            
        
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        #print (len(ocurrencias1))
        ############################################################################################################################################ inicio
        #os.system("gnome-terminal -e 'sudo apt-get update'")

        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "Coincidencias de (www) o URL encontrados "+Fore.GREEN+" **************************************")
        print ("")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'

        palabras2 = ['www', 'n/a']
        palabra2 = 'www'
        ocurrencias2 = []
        lista02 = []
        comillas = '""'
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra2 in linea:
                    ocurrencias2.append(linea)

                           
        for frase in ocurrencias2:
            aImprimir2 = frase
            for palabra2 in palabras2:
                if palabra2 in frase:
                    aImprimir2 = re.sub(r'(%s)' % palabra2, r'%s\1%s' % (RED, NOCOLOR), frase)

                    url01 = frase
                    f1 = open ('www.txt','a')
                    f1.write(url01)
                    f1.flush()
                    break

            print(aImprimir2)            
        
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("") 
        ############################################################################################################################################ fin

        ############################################################################################################################################ inicio
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "Coincidencias de (http) o URL encontrados "+Fore.GREEN+" **************************************")
        print ("")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'

        palabras3 = ['http', '.com', 'n/a']

        palabra3 = 'http'
        ocurrencias3 = []
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra3 in linea:
                    ocurrencias3.append(linea)

        for frase in ocurrencias3:
            aImprimir3 = frase
            for palabra3 in palabras3:
                if palabra3 in frase:
                    aImprimir3 = re.sub(r'(%s)' % palabra3, r'%s\1%s' % (RED, NOCOLOR), frase)
                    
                    url03 = frase
                    f1 = open ('http.txt','a')
                    f1.write(url03)
                    f1.flush()
                    break
            print(aImprimir3)
        
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("") 
        ############################################################################################################################################ fin


        ############################################################################################################################################ inicio
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "Coincidencias de (TCP) o protocolo encontrados "+Fore.GREEN+" **************************************")
        print ("")
        RED = '\033[1;31m'
        NOCOLOR = '\033[0;0m'

        palabras4 = ['tcp', '.com', 'n/a']

        palabra4 = 'tcp'
        ocurrencias4 = []
        with open('doc.txt') as lineas:
            for linea in lineas:
                if palabra4 in linea:
                    ocurrencias4.append(linea)

        for frase in ocurrencias4:
            aImprimir4 = frase
            for palabra4 in palabras4:
                if palabra4 in frase:
                    aImprimir4 = re.sub(r'(%s)' % palabra4, r'%s\1%s' % (RED, NOCOLOR), frase)
                    
                    url04 = frase
                    f1 = open ('tcp.txt','a')
                    f1.write(url04)
                    f1.flush()
                    break
            print(aImprimir4)

        
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(7)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("") 
        ############################################################################################################################################ fin



    elif opcion == 3:
        
        print("Opcion 3")
        print ("")
       
        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "URLs econtradas "+Fore.GREEN+" **************************************")
        print ("")

        #########################################################################################
        
        """input = ('ingrese su nombre')
        text = 'URLs son www.prueba.com'
        match_pattern = re.search(r'www.prueba.com', text)
        print (match_pattern.group(0))"""

        #########################################################################################

        analizar_url = open('url.txt','w')

        regex = '[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]'


        datos2 = open('www.txt')
        for line2 in datos2:
            line2 = line2.rstrip()
            y = re.findall('[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]', line2)
            if len(y) > 0 :
                analizar_url.write(str(y[0]+ "\n"))
                print (y[0])

        analizar_url = open('url.txt','w')


        lines = [line.strip() for line in open('www.txt', 'r')]
        for x in lines:
            found_h = re.search('[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]+', x)
            if found_h:
                analizar_url.write(x + "\n")
                
        """datos2 = open('usuario.txt')
        for line2 in datos2:
            line2 = line2.rstrip()
            y = re.findall('.*?Validation,(\w+).*', line2)
            if len(y) > 0 :
                print (y[0])"""

        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        ########################################################################################

        """init()
        print(Fore.RED + "Ejecutables encontrados "+Fore.GREEN+" **************************************")
        print ("")

        datos3 = open('exe.txt')
        for line3 in datos3:
            line3 = line3.rstrip()
            z = re.findall('[A-Za-z]+.[exe]+', line3)
            if len(z) > 0 :
                print (z)


        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(3)
        print ("")"""
        #########################################################################################
    elif opcion == 4:
        
        print("Opcion 4")
        print ("")    

        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        init()
        print(Fore.RED + "Analisis de URLs encontradas "+Fore.GREEN+" **************************************")
        print ("")
        init()
        print(Fore.RED + "Iniciando Analisis, esto puede tardar varios minutos, por favor espere "+Fore.GREEN+" **************************************")
        print ("")

        for i in tqdm(range(10000)):
            sleep(0.02)

        
        ruta_carpeta = os.path.dirname(os.path.realpath(__file__))
        ruta_log = ruta_carpeta+'/url.txt'
        os.system("automater"+" " +ruta_log)

        #ruta_log = os.path.dirname(os.path.realpath(__file__))

        init()
        print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
        time.sleep(3)
        print ("")



    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
print ("") 
print ("********Script finalizado***********")
print ("")

#comandos error

"""ping 
 apt-cache show nmap
 apt-cache search nmap
 sudo apt-get install python-nmap
 sudo apt-get install python3-nmap

"""

#paginas de consulta
#https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/
#http://www.poketcode.com/es/python/archivos_csv/index.html
#http://python-para-impacientes.blogspot.com/2014/02/ejecutar-un-comando-externo.html