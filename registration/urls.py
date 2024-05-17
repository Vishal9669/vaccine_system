from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('welcome',views.welcome,name='welcome'),
    path('addnewchild',views.addnewchild,name='addnewchild'),
    path('viewchild',views.viewchild,name='viewchild'),
    path('addchild',views.addchild,name='addchild'),
    path('showdetails',views.showdetails,name='showdetails'),
    path('logout',views.logout,name='logout'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('vaccine/<int:id>',views.vaccine,name='vaccine'),
    path('passwordchange/<int:id>',views.passwordchange,name='passwordchange'),
    path('passwordform',views.passwordform,name='passwordform'),
  
]
