#!/usr/bin/python3

import sys
import argparse
import os
import os.path as path
from time import time


def cifrarMensaje(alfabeto,nuevaletra,mensaje):
	criptograma=""
	for x in mensaje:
		cont=0
		for y in alfabeto:
			cont +=1
			if(x==y):
				criptograma+=nuevaletra[cont-1]
	print(criptograma)


def descifrarMensaje(alfabeto,nuevaletra,mensaje):
	textoClaro=""
	for x in mensaje:
		cont=0
		for y in nuevaletra:
			cont +=1
			if(x==y):
				textoClaro+=alfabeto[cont-1]
	print(textoClaro)
	

def cifrarTexto(alfabeto,nuevaletra,archivo):

	start_time = time()
	salida=""
	textoEnClaro = open(archivo, "r",encoding='ISO8859-15')
	particion=archivo.split(".")
	salida=particion[0]+".cif"	
	bandera=False
	concat=""
	for y in textoEnClaro.readlines():
		for x in y:
			if x in alfabeto:
				cont=alfabeto.index(x)+1
				concat=concat+nuevaletra[cont-1]
				bandera=True
			if bandera==False:
				concat=concat+x                
			bandera=False
		
	textoCifrado = open(salida, "w",encoding='ISO8859-15')	
	textoCifrado.write(concat)
	textoCifrado.close()
	textoEnClaro.close()

	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)



					


def descifrarTexto(alfabeto,nuevaletra,archivo):
	
	start_time = time()
	salida=""
	textoCifradoo = open(archivo, mode='r',encoding='ISO8859-15')
	particion=archivo.split(".")
	salida=particion[0]+"Descifrado.dec"
	concat=""
	bandera=False

	for y in textoCifradoo.readlines():
		for x in y:	
			if x in nuevaletra:
				cont=nuevaletra.index(x)+1
				concat=concat+alfabeto[cont-1]			
				bandera=True
				
			if bandera==False:
				concat=concat+x
			bandera=False
	
	textoDescifrado = open(salida, mode='w',encoding='ISO8859-15')
	textoDescifrado.write(concat)
	textoDescifrado.close()
	textoCifradoo.close()

	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)
	
def cifrarSerie(bloque1,bloque2,bloque3,archivo):
	start_time = time()
	salida=""
	claro=""
	cont=0
	textoEnClaro = open(archivo, mode='r',encoding='ISO8859-15')
	concat=""
	while True:
		letra = textoEnClaro.read(1)
		concat=concat+letra
		if not letra:
			break
		cont=cont+1
	textoEnClaro.close()
	particion=archivo.split(".")
	salida=particion[0]+".cif"
	
		
	for x in range(1,cont+1):
		

		if x%5==0:
				letra = concat[x-1]
				bloque1+=letra

		elif x%2==0:
				
				letra1 = concat[x-1]
				bloque2+=letra1	
	
		else:

				letra2 = concat[x-1]
				bloque3+=letra2
	textoCifrado = open(salida,mode='w',encoding='ISO8859-15')
	textoCifrado.write(bloque1+bloque2+bloque3)
	textoCifrado.close()

	
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)

def descifrarSerie(archivo):
	start_time = time()
	salida=""
	claro=""
	mensaje=""
	cont=0
	listaFinal=[]
	dic={}
	textoEnClaro = open(archivo, mode='r',encoding='ISO8859-15')
	while True:
		letra = textoEnClaro.read(1)
		if not letra:
			break
		cont=cont+1
	textoEnClaro.close()
	print(cont)
	particion=archivo.split(".")
	salida=particion[0]+"Descifrado.dec"
	textoCifrado = open(salida,mode='w',encoding='ISO8859-15')
	textoEnClaro = open(archivo, mode='r',encoding='ISO8859-15')

	cont1=0
	cont2=0
	cont3=0
	lista1=[]
	lista2=[]
	lista3=[]
	for x in range(1,cont+1):

		if x%5==0:
				lista1.append(x)
				cont1+=1
				listaFinal.append(textoEnClaro.read(1))

		elif x%2==0:
				lista2.append(x)
				cont2+=1
				listaFinal.append(textoEnClaro.read(1))
	
		else:
				lista3.append(x)
				cont3+=1
				listaFinal.append(textoEnClaro.read(1))
				

	lista1+=lista2+lista3

	textoEnClaro.close()	


	for i in range(0, cont):
		dic[lista1[i]]=listaFinal[i]



	for i in dict(sorted(dic.items())):
		mensaje+=dic[i]

	
	textoCifrado.write(mensaje)
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)

class MyParser(argparse.ArgumentParser): 
    def error(self, message): 
     sys.stderr.write('-h Ayuda.. Sintaxis: python Cesar.py -h ') 
     sys.exit(2) 


def main():

	alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	nuevaletra=['D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']

	bloque1=""
	bloque2=""
	bloque3=""

	criptograma=""
	mensaje=""

	if len(sys.argv)==1 or sys.argv[1]=="-h": 
		print("-----------------------------------------------------------------------------------------------------")
		print("|     Algoritmo De Cesar y Series Desarrollado por:                                                 |")
		print("|     Astrid Carolina Ordoñez Guerrero             astridordonez@unicauca.edu.co                    |")
		print("|     Juan David Muñoz Garzon                      mjuan@unicauca.edu.co                            |")
		print("|                                                                                                   |")
		print("|     Electiva: Criptografia                                                                        |")
		print("|     Profesor: Siler Amador Donado                                                                 |")
		print("|                                                                                                   |")
		print("|     Comandos de uso:                                                                              |")
		print("|     -h Ayuda.. Sintaxis: python Cesar.py -h                                                       |")
		print("|     Cesar:                                                                                        |")
		print("|     -cM Ingrese un texto en claro para cifrar.. Sintaxis: python Cesar.py <textoEnClaro> -cM      |")
		print("|     -dM Ingrese un criptograma para descifrar.. Sintaxis: python Cesar.py <criptograma> -dM       |")
		print("|     -cT Ingrese un archivo para cifrar.. Sintaxis: python Cesar.py <archivoEnClaro>.txt -cT       |")
		print("|     -dT Ingrese un archivo para descifrar.. Sintaxis: python Cesar.py <archivoCriptograma>.cif -dT|")
		print("|     Transposicion por Series:                                                                     |")
		print("|     -cS Ingrese un archivo para cifrar.. Sintaxis: python Cesar.py <archivoCriptograma>.txt -cS   |")
		print("|     -dS Ingrese un archivo para descifrar.. Sintaxis: python Cesar.py <archivoCriptograma>.cif -dS|")
		print("-----------------------------------------------------------------------------------------------------")
		
		sys.exit(1) 

	parser = MyParser() 
	'''try:
		args=parser.parse_args()
		
	except:
		
		print("Error: Syntaxis no reconocida")		
		sys.exit(0) '''
    	 
	parser = argparse.ArgumentParser()
	parser.add_argument("string", type=str)
	parser.add_argument("-cM", "--cMprint",  action="store_true")
	parser.add_argument("-dM", "--dMprint",   action="store_true")
	parser.add_argument("-cT", "--cTfile",   action="store_true")
	parser.add_argument("-dT", "--dTfile",   action="store_true")
	parser.add_argument("-cS", "--serieC",  action="store_true")
	parser.add_argument("-dS", "--serieD",  action="store_true")
	
	
    	   


	args = parser.parse_args()
	archivo = args.string

	if args.cMprint:
		cifrarMensaje(alfabeto,nuevaletra,archivo)

	if args.dMprint:
		descifrarMensaje(alfabeto,nuevaletra,archivo)


	if args.cTfile:	
		cifrarTexto(alfabeto,nuevaletra,archivo)
	
	if args.dTfile:
		descifrarTexto(alfabeto,nuevaletra,archivo)

	if args.serieC:
		cifrarSerie(bloque1,bloque2,bloque3,archivo)

	if args.serieD:
		descifrarSerie(archivo)


if __name__ == '__main__':
    main()

	
	
