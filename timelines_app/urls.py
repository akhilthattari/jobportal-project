from django.urls import path
from .views import * 


urlpatterns = [
      #HOME PAGE
      
      path('',home,name='home'),
      
      #CANDIDATE
      path('candidate_home/',candidate_home,name='candidate_home'),
      path('candidate_updation/<int:id>/',candidate_updation,name='candidate_updation'),
      path('job_list/',job_list,name='job_list'),
      path('job_apply/<int:id>/',job_apply,name='job_apply'),
      path('applied_list/list_view/',applied_list,name="list_applied"),
      path('add_skill/',add_skill,name="add_skill"),
      path('education/',education,name='education'),
      path('work_experience/',work_experience,name='work_experience'),
      
      #COMPANY
      path('company_updation/<int:id>/',company_updation,name='company_updation'),
      path('company_home/',company_home,name='company_home'),
      path('job_post/',job_post,name='job_post'),
      path('job_details/', job_details, name='job_details'),
      path('job_delete/<int:id>/',job_delete,name='job_delete'),
      path('all_candidate/',all_candidate,name='all_candidate'),
      path('candidate_list/<int:id>/',candidate_list,name='candidate_list'),
      # path('applications/<int:id>/',applications,name='applications'),
      # path('application_lists/',application_lists,name='application_lists'),
      path('applicants_list/<int:id>/', applicants_list, name='applicants_list'),
      path("comapany/select/<int:id>/<int:id_2>/",select_application,name="select"),
      path("comapany/reject/<int:id>/<int:id_2>/",reject_application,name="reject"),
      
  
      
      #ADMIN
      
      path('admin_home',admin_home,name='admin_home'),
      path('company_list',company_list,name='company_list'),
      path('candidates_list',candidates_list,name='candidates_list'),
      path('company_activate/<int:id>/',company_activate,name='company_activate'),
      path('comcompany_list_activated/',company_list_activated,name='company_list_activated'),
      path('company_reject/<int:id>',company_reject,name="company_reject"),
      path('select_applicant/<int:application_id>/', select_applicant, name='select_applicant'),
      path('about_us',about_us,name='about_us'),
      
 
]
