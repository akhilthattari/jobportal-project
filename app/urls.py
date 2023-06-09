from django.urls import path
from .views import *



urlpatterns = [
    #COMPANY
    
    path('company_register/',Company_register,name='company_register'),
    path('company_login',company_login,name='company_login'),
    
    #CANDIDATE
    path('candidate_register/',Candidate_register,name='candidate_register'),
     path('candidate_login',candidate_login,name='candidate_login'),
    path('logout_view',logout_view,name='logout_view'),
    path('candidate_delete/<int:id>/',candidate_delete,name='candidate_delete'),
    path('candidate_settings',candidate_settings,name='candidate_settings'),
    
    
    #ADMIN
    path('admin_login',admin_login,name='admin_login'),
    
    
    
   
    
]
