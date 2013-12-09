def CartoUpdtOne(request):
    '''
    Sets some updates on the mapping grids.
    Comments where recieved from partners
    '''
    log = ''
    ## CORANTIOQUIA: 
    # 'Año de Fuente' year must be from 1986.
    log += 'CORANTIOQUIA \r\n' 
    log += u'\'Año de Fuente\' year must be from 1986.\r\n'
    grids = cartoginven.objects.filter(cartuser = 20, cartfano = None)
    log += u'%s' % grids 
    grids.update(cartfano = 1986)
    log += u'\r\n\r\n'

    ## CARDER
    # 'Año de elaboración' year must be from 1997.
    log += u'CARDER\r\n'
    log += u'\'Año de elaboración\' year must be from 1997.\r\n'
    grids = cartoginven.objects.filter(cartuser = 13, cartfano = None)
    log += u'%s' % grids
    grids.update(cartfano = 1997)
    # Delete all grids starting with 'P' or 'p'.
    log += u'Delete all grids starting with \'P\' or \'p\'.'
    grids = cartoginven.objects.filter(cartplan__istartswith = 'p')
    log += u'%s' % grids
    grids.delete()
    log += u'\r\n\r\n'

    ## CORPOGUAVIO
    # 'Año de Fuente' is 2007.
    log += u'CORPOGUAVIO\r\n'
    log += u'\'Año de Fuente\' is 2007.\r\n'
    grids = cartoginven.objects.filter(cartuser = 22, cartfano = None)
    log += u'%s' % grids
    grids.update(cartfano = 2007)
    log += u'\r\n\r\n'
    # 'Año de Elaboración' is 2010.
    log += u'\'Año de Elaboración\' is 2010.'
    grids = cartoginven.objects.filter(cartuser = 22, carteano = None)
    log += u'%s' % grids
    grids.update(carteano = 2010)
    log += u'\r\n\r\n'

    ## CORPOAMAZONIA
    # Empty 'Año de Elaboración' Is assumed to be as equal from the others 1987
    log += u'CORPOAMAZONIA\r\n'
    log += u'Empty \'Año de Elaboración\' Is assumed to be as equal from the others 1987'
    grids = cartoginven.objects.filter(cartuser = 30, cartfano = None)
    log += u'%s' % grids
    grids.update(cartfano = None)
    log += u'\r\n\r\n'

    ## CORPONOR

    #Store log file
    print log
