from django.contrib.auth.models import User
from matriz_cartografica.models import matrcartogb
import xlrd

def gogo():
	theexcel = '/home/pomcas/001INFORMACION_CARTOGRAFICA.xlsx'
	book = xlrd.open_workbook(theexcel).sheet_by_index(0)
	book_size = book.nrows
	
	formato = ['SCH', 'e00', 'ArcInfo', 'GDB']
	licenciatiene = {'SI': True, 'NO': False, '': False}
	licenciatipo = {'Multiusuario':'MUL' , 'Usuario':'USR', '':'NONE'}
	
	
	for i in range(12, book_size-1):
	    sigla = book.cell_value(colx = 1, rowx = i)
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
	    #u = User.objects.get(username = sigla)
	      
	    #Valid licence, place, watersheed
	    
	    cartog = matrcartogb(cartcorp = sigla, 
                cartnupl = plancha, 
                cartform = formato, 
                cartfeel = fecha, 
                cartliex = licenciatiene[tienelic], 
                cartliti = licenciatipo[tipolic], 
                cartlinu = numelic, 
                cartubde = descubic, 
                cartubre = respubic, 
                cartcuco = codcuenc, 
                cartcuno = nomcuenc,
	        )
            print cartog.cartcorp
            cartog.save()
