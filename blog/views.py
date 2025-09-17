from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from . forms import Post_Form
from . models import post

# Create your views here.
def home(request):
    if request.method=='POST':
        forms=Post_Form(request.POST)
        if forms.is_valid():
            forms.save()
            
            return redirect('home')
    else:
        forms=Post_Form()
    posts=post.objects.last()
    return render(request,"home.html",{'forms':forms,'post':posts})



