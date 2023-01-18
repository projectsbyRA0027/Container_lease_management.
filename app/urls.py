from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage),
    path('register/',views.registerpage),
    path('loginpage/',views.loginpage),
    path('adminlogin/',views.adminlogin),
    path('addcontainer/',views.addcontainer),
    path('pendinglist/',views.pendinglist),
    path('approvedlist/',views.approvedlist),
    path('approve/<int:id>/',views.approve),
    path('container_view/',views.container_view),
    path('editcontainer/<int:id>/',views.editcontainer),
    path('delete/<int:id>/',views.delete),
    path('Bookingpage/',views.Bookingpage),
    path('Pendingbooking/',views.Pendingbooking),
    path('Approvedbooking/',views.Approvedbooking),
    path('Book/<int:id>/',views.Book)

]