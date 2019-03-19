#!/usr/bin/python3

import sys
import argparse
import os
import os.path as path
from time import time

import sys


def cifrarDoble(archivo):
	start_time = time()
	bloque1=""
	bloque2=""
	bloque3=""
	bloque4=""
	concat=""
	lis=[]
	cont=0
	textoEnClaro = open(archivo, "r",encoding='ISO8859-15')
	while True:
		letra = textoEnClaro.read(1)
		lis.append(letra)
		if not letra:
			break
		cont=cont+1
	textoEnClaro.close()
	particion=archivo.split(".")
	salida=particion[0]+".cif"	
	for x in range(0,cont):
		if x%2==0:
				letra = lis[x]
				bloque1+=letra	
	
		else:
				letra = lis[x]
				bloque2+=letra
	
	concat=bloque1+bloque2	

	for y in range(0,cont):
		if y%2==0:
				letra = concat[y]
				bloque3+=letra	
	
		else:
				letra = concat[y]
				bloque4+=letra

	textoCifrado = open(salida, "w",encoding='ISO8859-15')
	textoCifrado.write(bloque3+bloque4)
	textoCifrado.close()
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)
	
	

def descifrarDoble(archivo):
	start_time = time()
	bloque1=""
	bloque2=""
	bloque3=""
	bloque4=""
	lis=[]

	mensaje=""
	cont=0
	textoCifrado = open(archivo, "r",encoding='ISO8859-15')
	while True:
		letra = textoCifrado.read(1)
		lis.append(letra)
		if not letra:
			break
		cont=cont+1
	textoCifrado.close()
	formula=int(cont/2)+1	
	bloque1=lis[:formula+1]
	
	rango=len(lis[formula:len(lis)])
	bloque2=lis[formula:len(lis)-1]
	
	for x in range(0,rango-1):
		mensaje+=(bloque1[x]+bloque2[x])

	mensaje+=bloque1[len(bloque1)-2]
	mensaje1=""
	
	bloque3=mensaje[:formula+1]
	bloque4=mensaje[formula:len(mensaje)]	
	rango=len(mensaje[formula:len(mensaje)])
	
	for x in range(0,rango):
		mensaje1+=(bloque3[x]+bloque4[x])

	particion=archivo.split(".")
	salida=particion[0]+".dec"
	mensaje1+=bloque3[len(bloque3)-2]
	textoDescifrado = open(salida, "w",encoding='ISO8859-15')
	textoDescifrado.write(mensaje1)
	textoDescifrado.close()
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)	
	
	




def cifrarMensajeSimple(bloque1,bloque2,archivo):
	start_time = time()
	salida=""
	claro=""
	cont=0
	lis=[]
	textoEnClaro = open(archivo, "r",encoding='ISO8859-15')
	while True:
		letra = textoEnClaro.read(1)
		lis.append(letra)
		if not letra:
			break
		cont=cont+1
	textoEnClaro.close()
	particion=archivo.split(".")
	salida=particion[0]+".cif"
	cont2=0
	cont3=0
	for x in range(0,cont):
		if x%2==0:
				letra = lis[x]
				bloque1+=letra	
	
		else:
				letra = lis[x]
				bloque2+=letra
				
	textoCifrado = open(salida, "w",encoding='ISO8859-15')
	textoCifrado.write(bloque1+bloque2)
	textoCifrado.close()
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)
	


def descifrarMensajeSimple(bloque1,bloque2,archivo):
	start_time = time()
	mensaje=""
	lis=[]
	cont=0
	textoCifrado = open(archivo, "r",encoding='ISO8859-15')
	while True:
		letra = textoCifrado.read(1)
		lis.append(letra)
		if not letra:
			break
		cont=cont+1
	textoCifrado.close()
	formula=int(cont/2)+1
	
	bloque1=lis[:formula+1]
	bloque2=lis[formula:len(lis)-1]
	rango=len(lis[formula:len(lis)])
	for x in range(0,rango-1):
		mensaje+=(bloque1[x]+bloque2[x])

	mensaje+=bloque1[len(bloque1)-2]
	particion=archivo.split(".")
	salida=particion[0]+"DesSimple.dec"
	textoDescifrado = open(salida, "w",encoding='ISO8859-15')
	textoDescifrado.write(mensaje)
	textoDescifrado.close()
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)	
		
def cifrarInversa(archivo):
	start_time = time()
	cont=0
	bloque=""
	salida=""
	textoEnClaro= open(archivo, "r",encoding='ISO8859-15')
	while True:
		letra=textoEnClaro.read(1)
		if not letra:
			break
		cont=cont+1;
	textoEnClaro.close()
	particion=archivo.split(".")
	salida=particion[0]+".cif"
	textoCifrado=open(salida,"w",encoding='ISO8859-15')
	textoEnClaro=open(archivo,"r",encoding='ISO8859-15')

	for x in range(0,cont):
		letra=textoEnClaro.read(1)
		bloque+=letra

	textoCifrado.write(bloque[::-1])
	textoCifrado.close()
	textoEnClaro.close()
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)


def DescifrarInversa(archivo):
	start_time = time()
	cont=0
	bloque=""
	salida=""
	textoEnClaro= open(archivo, "r",encoding='ISO8859-15')
	while True:
		letra=textoEnClaro.read(1)
		if not letra:
			break
		cont=cont+1;
	textoEnClaro.close()
	particion=archivo.split(".")
	salida=particion[0]+".dec"
	textoCifrado=open(salida,"w",encoding='ISO8859-15')
	textoEnClaro=open(archivo,"r",encoding='ISO8859-15')

	for x in range(0,cont):
		letra=textoEnClaro.read(1)
		bloque+=letra

	textoCifrado.write(bloque[::-1])
	textoCifrado.close()
	textoEnClaro.close()
	tiempo_transcurrido = time() - start_time
	print("Tiempo de ejecucion: %0.10f segundos." % tiempo_transcurrido)
	

class MyParser(argparse.ArgumentParser): 
    def error(self, message): 
     sys.stderr.write('error: %s\n' % message) 
     self.print_help() 
     sys.exit(2) 

def main():


	bloque1=""
	bloque2=""
	criptograma=""
	mensaje=""

	if len(sys.argv)==1 or sys.argv[1]=="-h": 
		print("-------------------------------------------------------------------------------------------------------------------")
		print("|     Algoritmos De Transpocision Desarrollados por:                                                              |")
		print("|     Astrid Carolina Ordoñez Guerrero                  astridordonez@unicauca.edu.co                             |")
		print("|     Juan David Muñoz Garzon                           mjuan@unicauca.edu.co                                     |")
		print("|                                                                                                                 |")
		print("|     Electiva: Criptografia                                                                                      |")
		print("|     Profesor: Siler Amador Donado                                                                               |")
		print("|                                                                                                                 |")
		print("|     Comandos de uso:                                                                                            |")
		print("|     -h Ayuda.. Sintaxis: python Transpocision.py -h                                                             |")
		print("|     -cS Transposicion simple cifrar archivo.. Sintaxis: python Transposicion.py <archivoEnClaro> -cS            |")
		print("|     -dS Transposicion simple descifrar archivo... Sintaxis: python Transposicion.py <archivoCriptograma> -dS    |")
		print("|     -cD Transposicion doble cifrar archivo ... Sintaxis: python Transposicion.py <archivoEnClaro> -cD           |")
		print("|     -dD Transposicion doble descifrar archivo Sintaxis: python Transposicion.py <archivoCriptograma> -dD        |")
		print("|     -cI Transposicion inversa cifrar archivo ... Sintaxis: python Transposicion.py <archivoEnClaro> -cI         |")
		print("|     -dI Transposicion inversa descifrar archivo... Sintaxis: python Transposicion.py <archivoCriptograma> -dI   |")
		print("-------------------------------------------------------------------------------------------------------------------")
		
		sys.exit(1) 

	parser = MyParser()
	parser = argparse.ArgumentParser()
	parser.add_argument("string", type=str)
	parser.add_argument("-cS", "--simC",  action="store_true")
	parser.add_argument("-dS", "--simD",   action="store_true")
	parser.add_argument("-cD", "--doC",   action="store_true")
	parser.add_argument("-dD", "--doD",   action="store_true")
	parser.add_argument("-cI", "--invC",  action="store_true")
	parser.add_argument("-dI", "--invD",   action="store_true")
	args = parser.parse_args()
	archivo = args.string

	if args.simC:
		cifrarMensajeSimple(bloque1,bloque2,archivo)

	if args.simD:
		descifrarMensajeSimple(bloque1,bloque2,archivo)

	if args.doC:
		cifrarDoble(archivo)	

	if args.doD:
		descifrarDoble(archivo)

	if args.invC:
		cifrarInversa(archivo)

	if args.invD:
		DescifrarInversa(archivo)




if __name__ == '__main__':
    main()

	
