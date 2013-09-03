# -*- coding: utf-8 -*-
import xlrd
#from decimal import Decimal
#import repr
#import sys

def cruza_campos(parametro, validado):
    return parametro[3]

def cruzados(parametro, validado, n):
    rrow_n = parametro.cell(n, 8) 
    ccolx= (rrow_n.value)
    rrowx = parametro.cell_value(rowx=n,colx =9)
    return validado.cell_value(colx=int(ccolx), rowx = int(rrowx))

# Que las estratégias de participación se definan después de la etapa de aprestamiento.
# Que los costos los asuma cada CAR
#En todo pomca debe haber consejo de cuenca
#Diagnóstico, la misma matriz permite llenar la información que se requiere, yo filtro
#variabilidad climática
matrizfile = "C:/Users/ASOCARS-FADAPT3/Documents/GitHub/POMCAS/Borradores/Matrices/matriz institucional  17 de Agosto.xls"
validafile = "C:/Users/ASOCARS-FADAPT3/Documents/GitHub/POMCAS/Borradores/Parametrizacion/Estructura de las matrices.xlsx"

book = xlrd.open_workbook(matrizfile)
pestana = book.sheet_by_index(1)

campos = xlrd.open_workbook(validafile).sheet_by_index(2)  

for fila in range(3,18):
    print  cruzados(campos, pestana, fila)


pestana = book.sheet_by_index(2)

for fila in range(26,92):
    print  cruzados(campos, pestana, fila)

#print book.sheet_names()
#print len(book.sheet_names())

#for i in range (10):
# print book.sheet_by_index(i).name
 
#for rx in range(pestana.nrows):
#    print pestana.row(rx)
#for i in range(len(campos.sheet_names())):
# print campos.sheet_by_index(i).name
 