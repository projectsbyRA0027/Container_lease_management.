from django.shortcuts import render,HttpResponse,redirect
from .models import register,containerupload,leasingcontainer

# Create your views here.
# creating views for registration and login
def indexpage(request):
    return render(request,'index.html')

def registerpage(request):
    if request.method == 'POST':
        FirstName = request.POST.get('fname')
        LastName = request.POST.get('lname')
        Emailid = request.POST.get('email')
        Password = request.POST.get('psw')
        ConfirmPassword = request.POST.get('cpsw')
        Phoneno = request.POST.get('phone')
        Companyname = request.POST.get('companyname')
        Country = request.POST.get('country')
        Pincode = request.POST.get('code')
        Domain = request.POST.get('domain')
        user = register()
        user.Firstname = FirstName
        user.Lastname = LastName
        user.Emailid = Emailid
        user.Password = Password
        user.ConfirmPassword = ConfirmPassword
        user.Phoneno = Phoneno
        user.Companyname = Companyname
        user.County = Country
        user.Pincode = Pincode
        user.Domain = Domain
        user.save()


    return render(request,'register.html')



def loginpage(request):
    if request.method == 'POST':
        Emailid = request.POST.get('mailid')
        Password = request.POST.get('psw')

    try:
        register.Objects.get(Emailid=Emailid,Password=Password)
        return HttpResponse('welcome user')
    except:
        return render(request,'login.html')


# views for admin page
def adminlogin(request):
    if request.method == 'POST':
        Emailid = request.POST.get('mailid')
        Password = request.POST.get('psw')
        if Emailid == 'admin' and Password == 'admin':
            return HttpResponse('welcome Admin')
        else:
            return HttpResponse('invalid')
    return render(request,'login.html')

# this views writen for Lessor side uploading details
def addcontainer(request):
   if request.method == 'POST':
       Containertype = request.POST.get('type')
       Containerprice = request.POST.get('price')
       Containercount = request.POST.get('count')
       Lessorname = request.POST.get('name')
       picture = request.FILES.get('picture')
       lessor = containerupload()
       lessor.Containertype = Containertype
       lessor.Containerprice = Containerprice
       lessor.Containercount = Containercount
       lessor.Lessorname = Lessorname
       lessor.picture = picture
       lessor.save()

   return render(request,'add_container.html')


def pendinglist(request):
    details = containerupload.Objects.filter(status=False).value()
    return render(request, 'pendingcont.html', {'value': details})

def approvedlist(request):
    details = containerupload.Objects.Filter(status=True).value()
    return render(request,'containe-upload-approved.html',{'value':details})
def approve(request,id):
    dta = containerupload.Objects.get(id=id)
    dta.status = True
    dta.save()
    return redirect('\pendinglist')

def container_view(request):
    details = containerupload.Objects.all()
    return render(request,'viewcontainer.html',{'value':details})

def editcontainer(request,id):
    details = containerupload.Objects.filter(status=True)
    user = containerupload.Objects.get(id=id)
    if request.method =='post':
        Containercount = request.post.get('Containercount')
        user.Containercount = Containercount
        user.save()
        return redirect('/approved')
    return render(request,'containe-upload-approved',{'value':details,'a':user})

def delete(request,id):
    data = containerupload.Objects.filter(id=id).delete()
    return render('/container_view')



#this view is writen for Container Booking process.
def Bookingpage(request):
    if request.method == 'POST':
        Type = request.POST.get('type')
        Count = request.POST.get('count')
        Price = request.POST.get('price')
        LeasedDate = request.POST.get('ldate')
        ReturnDate = request.POST.get('rdate')
        LesseName = request.POST.get('lname')
        lessee = leasingcontainer()
        lessee.Type = Type
        lessee.Count = Count
        lessee.Price = Price
        lessee.Leaseddate = LeasedDate
        lessee.Returndate = ReturnDate
        lessee.Lesseename = LesseName
        lessee.save()
    return render(request,'leasing_container.html')

def Pendingbooking(request):
    details = leasingcontainer.Objects.filter(Status=False)
    return render(request,'bookcontainer.html',{'value':details})

def Approvedbooking(request):
    details = leasingcontainer.Objects.filter(Status=True)
    return render(request,'booking_approve.html',{'value':details})

def Book(request,id):
    data = leasingcontainer.Objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('\Pendingbooking')

def approvebook(request,id):
    data = leasingcontainer.Objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('\Pendingbooking')





