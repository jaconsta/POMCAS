from django.http import HttpResponse

def GetForm(request):
    if request.method == 'POST':
        return HttpResponse(u'Hello World')
    return HttpResponse(u'Nothing recieved')
