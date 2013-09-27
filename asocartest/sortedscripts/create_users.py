from django.contrib.auth.models import User
import xlrd

cars = 30
theexcel = '/home/pomcas/cars.xlsx'
book = xlrd.open_workbook(theexcel).sheet_by_index(1)

for i in range(1, cars+1):
    nombre = book.cell_value(colx = 1, rowx = i)
    sigla = book.cell_value(colx = 2, rowx = i)
    nit = book. cell_value(colx = 3, rowx = i)
    user = User.objects.create_user(username = sigla, password = nit)
