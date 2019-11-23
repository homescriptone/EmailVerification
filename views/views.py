from django.shortcuts import render
from views.functions import HomeScriptEmail
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    if ("POST" == request.method):
        email = request.POST.get('email')
        email_obj = HomeScriptEmail()
        is_valid = email_obj.email_is_valid(email)
        if (is_valid):
            print('Congratitulations')
        else:
            print('Sorry another time')
        return HttpResponseRedirect('https://homescriptone.com')
    else:
        print("life is hustle")
    return render(request,'index.html')