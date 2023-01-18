from django.db import models

class register(models.Model):

    objects = None
    DOMAIN_CHOICHES = (
        ('LESSOR','lessor'),
        ('LESSEE','lessee')
    )
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Emailid = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    ConfirmPassword = models.CharField(max_length=20)
    Phoneno = models.CharField(max_length=10)
    Companyname = models.CharField(max_length=40)
    County = models.CharField(max_length=40)
    pincode = models.CharField(max_length=20)
    Domain = models.CharField(max_length=20,choices=DOMAIN_CHOICHES)

class containerupload(models.Model):
    Objects = None
    Containertype = models.CharField(max_length=30)
    Containerprice = models.CharField(max_length=30)
    Containercount = models.CharField(max_length=30)
    Lessorname = models.CharField(max_length=30)
    picture = models.FileField(default=0)
    status = models.BooleanField(default=False)

class leasingcontainer(models.Model):
    Objects = None
    Type = models.CharField(max_length=30)
    Count = models.IntegerField(default=0)
    Price = models.CharField(max_length=20)
    Leaseddate = models.CharField(max_length=20)
    Returndate = models.CharField(max_length=20)
    Lessename = models.CharField(max_length=20)
    Status = models.BooleanField(default=False)















