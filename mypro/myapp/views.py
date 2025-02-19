from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import State, District,Reg,Login

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def first_pgm(request):
    template=loader.get_template("1stpro.html")
    context={}
    return HttpResponse(template.render(context,request))
def state(request):
    if request.method=="POST":
        s=State()
        s.sname=request.POST.get("sname")
        s.save()
        return HttpResponse("<script>alert('inserted');window.location='/state';</script>")
    else:
        s=State.objects.all()
        # s=State.objects.get(id=2)
        template=loader.get_template("state.html")
        context={'s':s}
        return HttpResponse(template.render(context,request))
    
def district(request):
    if request.method=="POST":
        d=District()
        d.sid_id=request.POST.get("sid")
        d.dname=request.POST.get("dname")
        d.save()
        return HttpResponse("<script>alert('inserted');window.location='/district';</script>")
    else:
        s=State.objects.all()
        template=loader.get_template("district.html")
        context={'s':s}
        return HttpResponse(template.render(context,request))

def reg(request):
    if request.method=="POST":
        r=Reg()
        r.name=request.POST.get("name")
        r.age=request.POST.get("age")
        r.gender=request.POST.get("gender")
        r.email=request.POST.get("email")
        r.dob=request.POST.get("date")
        r.addr=request.POST.get("address")
        r.phno=request.POST.get("phno")
        r.loc=request.POST.get("loc")
        r.qual=",".join(request.POST.getlist("qual"))
        r.image=request.FILES["file"]
        r.save()
        id=Reg.objects.latest("id").id
        l=Login()
        l.uname=request.POST.get("uname")
        l.pswd=request.POST.get("pwd")
        l.utype='user'
        l.uid_id=id
        l.save()
        subject = 'Welcome'
        message = 'Thank you for registering to our site'
        email_from = settings.EMAIL_HOST_USER
        mailid = request.POST.get("email")
        recipient_list = [mailid, ]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse("<script>alert('inserted');window.location='/reg';</script>")
    else:
        
        template=loader.get_template("Form.html")
        context={}
        return HttpResponse(template.render(context,request))
    
def login(request):
    if request.method=='POST':
        uname=request.POST.get("uname")
        pwd=request.POST.get("pwd") 
        if Login.objects.filter(uname=uname,pswd=pwd):
            l=Login.objects.get(uname=uname,pswd=pwd)  
            if l.utype=="user":
                request.session["uid"]=l.uid_id
                return HttpResponse("<script>alert('welcome user');window.location='/userhome';</script>")
            elif l.utype=="admin":
                return HttpResponse("<script>alert('welcome admin');window.location='/adminhome';</script>")
            else:
                return HttpResponse("<script>alert('invalid user');window.location='/login';</script>")


        else:
            return HttpResponse("<script>alert('invalid user');window.location='/login';</script>")

    else:

        template=loader.get_template("login.html")
        context={}
        return HttpResponse(template.render(context,request))
    
    
def userhome(request):
    template=loader.get_template("userhome.html")
    context={}
    return HttpResponse(template.render(context,request))

def adminhome(request):
    template=loader.get_template("adminhome.html")
    context={}
    return HttpResponse(template.render(context,request))

def viewuser(request):
    
    u=Reg.objects.all()
    template=loader.get_template("viewuser.html")
    context={'u':u}
    return HttpResponse(template.render(context,request))
def edituser(request):
    if request.method=="POST":
        r=Reg.objects.get(id=request.session["uid"])
        r.name=request.POST.get("name")
        r.save()
        return HttpResponse("<script>alert('updated');window.location='/edituser';</script>")
    else:
        u=Reg.objects.get(id=request.session["uid"])
        template=loader.get_template("edituser.html")
        context={'u':u}
        return HttpResponse(template.render(context,request))
    


def deleteuser(request,id):
    
    u=Reg.objects.get(id=id)
    l=Login.objects.get(uid_id=id)
    u.delete()

    return HttpResponse("<script>alert('deleted');window.location='/viewuser';</script>")
def viewuser_qry(request):
    
    u=Reg.objects.raw("select * from myapp_reg where id=%s",[request.session["uid"]])
    template=loader.get_template("viewuser_qry.html")
    context={'u':u}
    return HttpResponse(template.render(context,request))
def search(request):
    if request.method=="POST":
        id=request.POST.get("id")
        i=Reg.objects.get(id=id)
        template=loader.get_template("search.html")
        context={'i':i}
        return HttpResponse(template.render(context,request))

    else:
        u=Reg.objects.raw("select id,name from myapp_reg")
        template=loader.get_template("search.html")
        context={'u':u}
        return HttpResponse(template.render(context,request))

def index(request):
    template=loader.get_template("index.html")
    context={}
    return HttpResponse(template.render(context,request))