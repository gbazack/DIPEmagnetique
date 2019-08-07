import numpy as np
import sys
import os
import datetime as dt
import xlrd as excel
from os.path import dirname, exists, expanduser, isdir, join, splitext


_path=("/home/gbazack/Documents/GROUPONE/DIPEMagnetique")

t=dt.datetime.now()
m=t.month
y=t.year

def fill_space(element, size):
	length = len(element)
	temp_str='0'
	
	if element!='':
		if length == size:
			f.write(str(element))
		elif length < size:
			i=1
			while i < size - length:
				temp_str +='0'; i+=1
			f.write(str(temp_str)+str(element))
		else:
			i=0
			while i < size - length:
				temp_str +='0'; i+=1
			f.write(str(temp_str)+str(element))
			
	else:
		for i in range(size-1):
			temp_str +='0'
		f.write(str(temp_str))
	temp_str='0'

def fill_space_int(element, size):
	temp_str='0'
	
	if element!='':
		length=len(str(int(element)))
		if length == size:
			f.write(str(int(element)))
		elif length < size:
			i=1
			while i < size - length:
				temp_str +='0'; i+=1
			f.write(str(temp_str)+str(int(element)))
		else:
			i=0
			while i < size - length:
				temp_str +='0'; i+=1
			f.write(str(temp_str)+str(int(element)))
			
	else:
		for i in range(size-1):
			temp_str +='0'
		f.write(str(temp_str))
	temp_str='0'

def fill_space_name(element, size):
	while element[-1] == ' ':
		element = element[:len(element)-1]

	length = len(element)
	temp_str = " "

	if element!='':
		if length == size:
			f.write(str(element))
		elif length < size:
			i=1
			while i < size - length:
				temp_str += " "; i+=1
			f.write(str(temp_str)+str(element))
		else:
			i=1
			while i < size - length:
				temp_str +=" "; i+=1
			f.write(str(temp_str)+str(element))
			
	else:
		for i in range(size-1):
			temp_str +=" "
		f.write(str(temp_str))
	temp_str=" "


def convertdipe(excelfile):
	#-------Variables declaration
	#temp_str='0'
	
	#------Create the text file for the DIPE	
	f=open("DIPE"+str(m)+str(y)+".txt","w")
	#------Open the excel file
	wb=excel.open_workbook(_path+excelfile)
	sheet=wb.sheet_by_index(0)
	
	for i in range(1,sheet.nrows):
		it=1
		if it < 17:
			#--------Code d'enregistrement, numero DIPE et cle numero DIPE
			f.write('C0400000 ')
			#-------Numero contribuable
			fill_space(sheet.cell_value(i,0), 14)
			
			#----------Mois
			if len(str(m))<2:
				f.write("0"+str(m))
			else:
				f.write(str(m))
			
			#----------Numero employeur
			fill_space_int(sheet.cell_value(i,1), 10)
			#----------Cle numero employeur
			f.write(sheet.cell_value(i,2))
			#----------Regime employeur
			f.write(str(int(sheet.cell_value(i,3))))
			#----------Annee du DIPE
			f.write(str(y))
			#----------Matricule assure + cle
			fill_space_int(sheet.cell_value(i,4), 11)
			#----------Nombre de jours
			fill_space_int(sheet.cell_value(i,5), 2)
			#----------salaire brut
			fill_space_int(sheet.cell_value(i,6), 10)
			#----------salaire exceptionnel
			fill_space_int(sheet.cell_value(i,7), 10)
			#----------salaire taxable
			fill_space_int(sheet.cell_value(i,8), 10)
			#----------salaire cotisable cnps
			fill_space_int(sheet.cell_value(i,9), 10)
			#----------salaire cotisable plafonne
			fill_space_int(sheet.cell_value(i,10), 10)
			#----------retenue IRPP
			f.write("00000000")
			#----------retenue taxable communale
			f.write("000000")
			#----------numero de ligne
			if len(str(it))<2:
				f.write("0"+str(it))
			else:
				f.write(str(it))
			it +=1
			#----------matricule interne
			fill_space(sheet.cell_value(i,11), 14)
			#---------filer
			f.write(' ')
			#--------noms employe
			fill_space(sheet.cell_value(i,12), 60)
			f.write("\n")
	f.close()
            	
