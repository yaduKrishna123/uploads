from django.urls import path

from starapp import views

urlpatterns = [
    # path('',views.demo,name="demo"),
    path('',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('new_uploads',views.new_uploads,name='new_uploads'),
    path('uploads',views.uploads,name='uploads'),

]