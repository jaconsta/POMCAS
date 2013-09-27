from django.contrib.auth.models import User
from matriz_cartografica.models import matrcartogb
import xlrd

theexcel = '/home/pomcas/cars.xlsx'
book = xlrd.open_workbook(theexcel).sheet_by_index(0)
book_size = book.nrows

formato = ['SCH', 'e00', 'ArcInfo', 'GDB']
licenciatiene = ['SI': True, 'NO': False]
licenciatipo = ['MUL': 'Multiusuario', 'USR':'Usuario']


for i in range(12, book_size-1):
    nit = book.cell_value(colx = 2, rowx = i)
    plancha = book. cell_value(colx = 3, rowx = i)
    formato = book. cell_value(colx = 4, rowx = i)
    fecha = book. cell_value(colx = 5, rowx = i)
    tienelic = book. cell_value(colx = 6, rowx = i)
    tipolic = book. cell_value(colx = 7, rowx = i)
    numelic = book. cell_value(colx = 8, rowx = i)
    descubic = book. cell_value(colx = 9, rowx = i)
    respubic = book. cell_value(colx = 10, rowx = i)
    codcuenc = book. cell_value(colx = 11, rowx = i)
    nomcuenc = book. cell_value(colx = 12, rowx = i)
    
    #get user
    u = User.objects.get(nit = nit)
      
    #Valid licence, place, watersheed
    
    cartog = matrix_cartografica(

