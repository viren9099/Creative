from django.shortcuts import render
from django.conf import settings
from . models import Contact,Login
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def Services(request):
    return render(request,'services.html')

def product(request):
    return render(request,'product.html')

def Contacts(request):
    if request.method=='POST':
        n = request.POST['name']
        e = request.POST['email']
        p = request.POST['phone']
        s = request.POST['subject']
        m = request.POST['msg']
        print(n,e,p,s,m)
        try:
            Contact.objects.create(name=n,email=e,phone=p,subject=s,msg=m)
            msg="Message has been Send  Successefully"
            return render(request,'contact.html',{'msg':msg})
        except:
            msg="Message not Submited"
            return render(request,'contact.html',{'msg':msg})
    else:
            return render(request,'contact.html')
  
def login(request):
    if request.method=="POST":
        admin_user=request.POST['user']
        admin_password=request.POST['password']
        print(admin_user,admin_password)
        try:
            admin_user=Login.objects.get(user=admin_user,password=admin_password)
            request.session['admin_user']=admin_user.user
            all_user = Contact.objects.all()
            return render(request,'ViewResponce.html',{'all_user':all_user})
        except:
            msg="Incorrect Username or Password"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['admin_user']
        return render(request,'index.html')
    except:
        msg="Login Again"
        return render(request,'login.html',{'msg':msg})
        