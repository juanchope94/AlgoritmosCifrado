#!/usr/bin/python3

import sys
import argparse
import os
import os.path as path
from time import time
import base64


def cifrarTexto(alfabeto,archivo,a,c,n):
	start_time = time()
	salida=""
	claro=""
	textoEnClaro = open(archivo, mode='r',encoding='ISO8859-15').read()
	#Primero se codifica en bytes con utf-8
	b=textoEnClaro.encode("UTF-8")
	#segundo se codifica a base 64
	codificacion= base64.b64encode(b)
	#tercero se decodifica de utf-8 
	s=codificacion.decode("UTF-8")
	particion=archivo.split(".")
	salida=particion[0]+".cif"
	cadena=""

	for i in  range(len(s)):
		x=s[i]
		mi=int(alfabeto.index(x))			
		ci=((a*mi)+c)%n
		cadena+=alfabeto[ci]
			

	textoCifrado = open(salida, mode='w',encoding='ISO8859-15')
	textoCifrado.write(cadena)
	textoCifrado.close()
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)


def cifrarTextoNormal(alfabeto,archivo,a,b,n):
	start_time = time()
	salida=""
	particion=archivo.split(".")
	salida=particion[0]+".cif"
	textoEnClaro = open(archivo, mode='r',encoding='ISO8859-15')
	cadena=""
	while True:
		x=textoEnClaro.read(1)
		if not x:
			break	

		if x in alfabeto:
			mi=alfabeto.index(x)
			ci=(a*mi+b)%n
			cadena+=alfabeto[ci]
			bandera=True
		
		if bandera==False:
			cadena+=x			
		bandera=False
	textoEnClaro.close()

	textoCifrado = open(salida, mode='w',encoding='ISO8859-15')
	textoCifrado.write(cadena)
	textoCifrado.close()


	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)


def descifrarTextoNormal(alfabeto,archivo,a,b,n):
	
	start_time = time()
	salida=""
	particion=archivo.split(".")
	salida=particion[0]+".Dec"
	textoCifrado = open(archivo, mode='r',encoding='ISO8859-15')
	cadena=""
	bandera=False
	
	while True:
		x=textoCifrado.read(1)
		if not x:
			break
	
		if x in alfabeto:
			ci=alfabeto.index(x)
			m=(4*(ci-b))%n
			cadena+=alfabeto[m]
			bandera=True
		
		if bandera==False:
			cadena+=x
		bandera=False
	textoCifrado.close()

	textoDescifrado = open(salida,  mode='w',encoding='ISO8859-15')
	textoDescifrado.write(cadena)
	textoDescifrado.close()
	

	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)

def descifrarTexto(alfabeto,archivo,a,c,n):
	
	start_time = time()
	salida=""
	particion=archivo.split(".")
	salida=particion[0]+".Dec"
	textoCifrado = open(archivo, mode='r',encoding='ISO8859-15')	
	cadena=""
	while True:
		x=textoCifrado.read(1)
		if not x:
			break	

		ci=alfabeto.index(x)
		m=(28*(ci-c))%n
		cadena+=alfabeto[m]
	
	textoCifrado.close()

	
	#Primero se codifica en bytes con utf-8
	e=cadena.encode("UTF-8")
	#segundo se decodifica a base 64
	f=base64.b64decode(cadena)
	#tercero se decodifica de utf-8 
	h=f.decode("utf-8")
	textoDescifrado = open(salida,  mode='w',encoding='ISO8859-15')
	textoDescifrado.write(h)
	textoDescifrado.close()

	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)
	

class MyParser(argparse.ArgumentParser): 
    def error(self, message): 
     sys.stderr.write('-h Ayuda.. Sintaxis: python Afin.py -h ') 
     sys.exit(2) 


def main():

	alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/','=']

	a=7
	b=3
	n=65

	alfabeto2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	c=7
	d=3
	e=27

	criptograma=""
	mensaje=""

	if len(sys.argv)==1 or sys.argv[1]=="-h": 
		print("---------------------------------------------------------------------------------------------------------------------------")
		print("|     Algoritmo Afin Desarrollado por:                                                                                    |")
		print("|     Astrid Carolina Ordoñez Guerrero             astridordonez@unicauca.edu.co                                          |")
		print("|     Juan David Muñoz Garzon                      mjuan@unicauca.edu.co                                                  |")
		print("|                                                                                                                         |")
		print("|     Electiva: Criptografia                                                                                              |")
		print("|     Profesor: Siler Amador Donado                                                                                       |")
		print("|                                                                                                                         |")
		print("|     Comandos de uso:                                                                                                    |")
		print("|     -h Ayuda.. Sintaxis: python Afin.py -h                                                                              |")
		print("|     -cA Afin.Ingrese un archivo para codificar base64 y cifrar.. Sintaxis: python Afin.py <archivoEnClaro> -cT          |")
		print("|     -dA Afin.Ingrese un archivo para decodificar base64 y descifrar.. Sintaxis: python Afin.py <archivoCriptograma> -dT |")
		print("|     -cN Afin.Ingrese un archivo para cifrado normal.. Sintaxis: python Afin.py <archivoCriptograma> -cN                 |")
		print("|     -dN Afin.Ingrese un archivo para descifrado normal.. Sintaxis: python Afin.py <archivoCriptograma> -dN              |")
		print("---------------------------------------------------------------------------------------------------------------------------")
		
		sys.exit(1) 

	parser = MyParser() 
	
    	 
	parser = argparse.ArgumentParser()
	parser.add_argument("string", type=str)
	parser.add_argument("-cA", "--cAfile",   action="store_true")
	parser.add_argument("-dA", "--dAfile",   action="store_true")
	parser.add_argument("-cN", "--cNfile",   action="store_true")
	parser.add_argument("-dN", "--dNfile",   action="store_true")
	

	args = parser.parse_args()
	archivo = args.string


	if args.cAfile:	
		cifrarTexto(alfabeto,archivo,a,b,n)
	
	if args.dAfile:
		descifrarTexto(alfabeto,archivo,a,b,n)
	
	if args.cNfile:
		cifrarTextoNormal(alfabeto2,archivo,c,d,e)
	
	if args.dNfile:
		descifrarTextoNormal(alfabeto2,archivo,c,d,e)


if __name__ == '__main__':
    main()