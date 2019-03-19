#!/usr/bin/python3

import sys
import argparse
import os
import os.path as path
from time import time
import base64


def cifrarTexto(alfabeto,archivo,k,n):
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
	cont=0
	for i in  range(len(s)):
		x=s[i]		
		if(cont==3):
			cont=0
		if k[cont] in alfabeto:
				mi=alfabeto.index(x)
				k1=alfabeto.index(k[cont])
				ci=(k1-mi)%n
				cadena+=alfabeto[ci]
				cont +=1
	
	textoCifrado = open(salida, mode='w',encoding='ISO8859-15')
	textoCifrado.write(cadena)
	textoCifrado.close()


	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)



def cifrarTextoNormal(alfabeto,archivo,k,n):
	start_time = time()
	salida=""
	claro=""
	particion=archivo.split(".")
	salida=particion[0]+".cif"	
	textoEnClaro = open(archivo,  mode='r',encoding='ISO8859-15')

	cont=0
	cadena=""

	while True:
		x=textoEnClaro.read(1)
		if not x:
			break

		if(cont==6):
			cont=0

		if x in alfabeto:
			if k[cont] in alfabeto:
				mi=alfabeto.index(x)
				k1=alfabeto.index(k[cont])
				ci=(k1-mi)%n
				cadena+=alfabeto[ci]
				cont +=1
			bandera=True
		
		if bandera==False:
			cadena+=x
		bandera=False

	textoEnClaro.close()
	
	textoCifrado = open(salida,  mode='w',encoding='ISO8859-15')
	textoCifrado.write(cadena)
	textoCifrado.close()


	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)


def descifrarTextoNormal(alfabeto,archivo,k,n):
	
	start_time = time()
	salida=""
	particion=archivo.split(".")
	salida=particion[0]+".Dec"
	textoCifrado = open(archivo,  mode='r',encoding='ISO8859-15')
	
	

	bandera=False
	cont=0
	cadena=""
	while True:
		x=textoCifrado.read(1)
		if not x:
			break
	
		if(cont==6):
			cont=0		
				
		if x in alfabeto:
			if k[cont] in alfabeto:
				ci=alfabeto.index(x)
				k1=alfabeto.index(k[cont])
				m=(k1-ci)%n
				cadena+=alfabeto[m]		
				cont+=1
			bandera=True
		
		if bandera==False:
			cadena+=x
		bandera=False
	textoCifrado.close()

	textoDescifrado = open(salida, mode='w',encoding='ISO8859-15')
	textoDescifrado.write(cadena)
	textoDescifrado.close()
	

	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)
	

def descifrarTexto(alfabeto,archivo,k,n):
	
	start_time = time()
	salida=""
	cont=0
	particion=archivo.split(".")
	salida=particion[0]+".Dec"
	cadena=""
	bandera=False
	cont=0
	textoCifrado = open(archivo, mode='r',encoding='ISO8859-15')
	while True:
		x=textoCifrado.read(1)
		if not x:
			break
	
		if(cont==3):
			cont=0		
		if k[cont] in alfabeto:
				ci=alfabeto.index(x)
				k1=alfabeto.index(k[cont])
				m=(k1-ci)%n
				cadena+=alfabeto[m]			
				cont+=1
	
	
	textoCifrado.close()

	#Primero se codifica en bytes con utf-8
	e=cadena.encode("UTF-8")
	#segundo se decodifica a base 64
	f=base64.b64decode(cadena)
	#tercero se decodifica de utf-8 
	h=f.decode("UTF-8")
	textoDescifrado = open(salida,  mode='w',encoding='ISO8859-15')
	textoDescifrado.write(h)
	textoDescifrado.close()


	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)
	

class MyParser(argparse.ArgumentParser): 
    def error(self, message): 
     sys.stderr.write('-h Ayuda.. Sintaxis: python Vigenere.py -h ') 
     sys.exit(2) 


def main():

	alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/','=']


	k="KEY"
	n=65
	
	
	alfabeto2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	ke="NORMAL"
	nu=27
	

	if len(sys.argv)==1 or sys.argv[1]=="-h": 
		print("-----------------------------------------------------------------------------------------------------------------------------------")
		print("|     Algoritmo De Vigenere Desarrollado por:                                                                                     |")
		print("|     Astrid Carolina Ordoñez Guerrero             astridordonez@unicauca.edu.co                                                  |")
		print("|     Juan David Muñoz Garzon                      mjuan@unicauca.edu.co                                                          |")
		print("|                                                                                                                                 |")
		print("|     Electiva: Criptografia                                                                                                      |")
		print("|     Profesor: Siler Amador Donado                                                                                               |")
		print("|                                                                                                                                 |")
		print("|     Comandos de uso:                                                                                                            |")
		print("|     -h Ayuda.. Sintaxis: python Vigenere.py -h                                                                                  |")
		print("|     -cV Vigenere.Ingrese un archivo para codificar base64 y cifrar.. Sintaxis: python Vigenere.py <archivoEnClaro> -cV          |")
		print("|     -dV Vigenere.Ingrese un archivo para descifrar y decodificar base64.. Sintaxis: python Vigenere.py <archivoCriptograma> -dV |")
		print("|     -cN Vigenere.Ingrese un archivo para cifrar.. Sintaxis: python Vigenere.py <archivoCriptograma> -cN                         |")
		print("|     -dN Vigenere.Ingrese un archivo para descifrar.. Sintaxis: python Vigenere.py <archivoCriptograma> -dN                      |")
		print("-----------------------------------------------------------------------------------------------------------------------------------")
		
		sys.exit(1) 

	parser = MyParser() 
	
    	 
	parser = argparse.ArgumentParser()
	parser.add_argument("string", type=str)
	parser.add_argument("-cV", "--cVfile",   action="store_true")
	parser.add_argument("-dV", "--dVfile",   action="store_true")
	parser.add_argument("-cN", "--cNfile",   action="store_true")
	parser.add_argument("-dN", "--dNfile",   action="store_true")
	

	args = parser.parse_args()
	archivo = args.string


	if args.cVfile:	
		cifrarTexto(alfabeto,archivo,k,n)
	if args.dVfile:
		descifrarTexto(alfabeto,archivo,k,n)
	if args.cNfile:
		cifrarTextoNormal(alfabeto2,archivo,ke,nu)
	if args.dNfile:
		descifrarTextoNormal(alfabeto2,archivo,ke,nu)


if __name__ == '__main__':
    main()