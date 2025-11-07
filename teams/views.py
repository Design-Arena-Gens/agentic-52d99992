from django.http import HttpResponse

def index(request):
    return HttpResponse("Teams are managed via Django Admin.")
