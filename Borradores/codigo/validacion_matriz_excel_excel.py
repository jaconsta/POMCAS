import xlrd

def cruza_campos(parametro, validado):
    return parametro[3]

def cruzados(parametro, validado, n):
    ccol_n = parametro.cell(n, 8)
    rrowx= round(ccol_n.value)
    #rrowx = parametro.cell_value(rowx=n,colx =8)
    #rrowx = parametro.cell_type(rowx=n,colx =8) 
    ccolx = parametro.cell_value(rowx=n,colx =9)
    print ('%s, %s')%((rrowx),type(ccolx))
    return "" #parametro.cell_value(rowx=rrowx, colx = ccolx)

matrizfile = "C:/Users/ASOCARS-FADAPT3/Documents/GitHub/POMCAS/Borradores/Matrices/matriz institucional  17 de Agosto.xls"
validafile = "C:/Users/ASOCARS-FADAPT3/Documents/GitHub/POMCAS/Borradores/Parametrizacion/Estructura de las matrices.xlsx"

book = xlrd.open_workbook(matrizfile)
pestana = book.sheet_by_index(1)

campos = xlrd.open_workbook(validafile).sheet_by_index(2)


for fila in range(1,18):
    print cruzados(campos, pestana, fila)
#    print cruza_campos(campos.row(fila), pestana)

#print book.sheet_names()
#print len(book.sheet_names())

#for i in range (10):
# print book.sheet_by_index(i).name
 
#for rx in range(campos.nrows):
#    print campos.row(rx)
#for i in range(len(campos.sheet_names())):
# print campos.sheet_by_index(i).name
 