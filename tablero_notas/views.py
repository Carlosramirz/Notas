from django.http import HttpResponse

def check_auth(request):
    if request.user.is_authenticated:
        return HttpResponse("Estás autenticado.")
    else:
        return HttpResponse("No estás autenticado.")