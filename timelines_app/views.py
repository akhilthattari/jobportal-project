from django.shortcuts import render,redirect
from app .models import *
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage





#HOME PAGE

def home(request):
    return render(request,'home.html')


#CANDIDATE HOME_VIEW
def candidate_home(request):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    data = CandidateUser.objects.get(user=request.user)
    skill = Add_skill.objects.filter(user=request.user)
    education = Education.objects.filter(user=request.user)
    experience = Add_experience.objects.filter(user=request.user)
    context = {
        'data': data,
        'skills':skill,
        'education':education,
        'experience':experience,
    }
    return render(request,'candidate/candidate_home.html',context)




#CANDIDATE_PROFILE_EDIT

def candidate_updation(request, id):
    if not request.user.is_authenticated:
        return redirect('candidate_login')

    data = CandidateUser.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        profile_photo = request.FILES.get('profile_photo')
        email = request.POST.get('email')
        candidate_address = request.POST.get('candidate_address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        qualification = request.POST.get('qualification')
        
        if profile_photo:
            data.profile_photo = profile_photo
            # profile_photo.profile_photo=profile_photo
        
        data.username = username
        data.phone = phone
        data.email = email
        data.candidate_address = candidate_address
        data.first_name = first_name
        data.last_name = last_name
        data.qualification = qualification
        data.save() 
        return redirect('candidate_home')
    
    education_choices = [
        ('High School', 'High School'),
        ('Higher Secondary', 'Higher Secondary'),
        ('DIPLOMA','DIPLOMA'),
        ('Graduation', 'Graduation'),
        ('Post Graduation', 'Post Graduation'),
        ('PhD', 'PhD'),
        ('other', 'other'),
        
    ]
    
    context = {
        'data': data,
        'education_choices': education_choices,
    }
    
    return render(request, 'candidate/profile_edit.html', context)




#Add Skill(Candidate)

def add_skill(request):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    if request.method == 'POST':
        skill_name = request.POST.get("skill")
        description = request.POST.get("description")
        
        Add_skill.objects.create(
            user = request.user,
            skill=skill_name,
            description=description,
        )
        return redirect('candidate_home')
    return render(request,'candidate/skill.html')


#Add Education (Candidate)

def education(request):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    if request.method == 'POST':
        college_name = request.POST.get("college_name")
        year = request.POST.get('year')
        subject = request.POST.get('subject')
        
        Education.objects.create(
            user = request.user,
            college_name = college_name,
            year = year,
            subject = subject,
        )
        return redirect('candidate_home')
    return render(request,'candidate/education.html')

#Add Work Experience(Candidate)

def work_experience(request):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        position = request.POST.get('position')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        Add_experience.objects.create(
            user = request.user,
            company_name = company_name,
            position = position,
            start_date = start_date,
            end_date = end_date,
        )
        return redirect('candidate_home')
    return render(request,'candidate/experience.html')



#Candidate application status
def applied_list(request):
    
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    user=CandidateUser.objects.filter(user=request.user).first()
    print(user)
    list = Application.objects.filter(user=user)
    context = {
        'lists':list
    }
    return render(request,'candidate/applied_list.html',context)    



#Job details Candidate
def job_list(request):
    
    
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    vacancies = JobAdd.objects.all()
    context = {
        'vacancies':vacancies
    }
    return render(request,'candidate/job_list.html',context)



#CANDIDATE JOB APPLY
def job_apply(request,id):
    
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    user = CandidateUser.objects.get(user=request.user)
    job = JobAdd.objects.get(id=id)
    if request.method == 'POST':
        resume = request.FILES.get('resume')
        username = request.POST.get('username')
        Application.objects.create(
            user=user,
            username = username,
            job = job,
            resume = resume,
            status='Pending',
        )
        return redirect('job_list')
    return render(request,'candidate/job_apply.html')



#COMPANY HOME_VIEW
def company_home(request):
    
    if not request.user.is_authenticated:
        return redirect('compnay_login')
    
    data = CompanyUser.objects.get(user=request.user)
    context = {
        'data': data
    }
    return render(request,'company/company_home.html',context)




    
    
     
#COMPANY EDIT
def company_updation(request,id):
    
    if not request.user.is_authenticated:
        return redirect('company_login')
    
    data = CompanyUser.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        company_name = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        profile_photo = request.FILES.get('profile_photo')
        location = request.POST.get('location')
        description = request.POST.get('description')
        
        if profile_photo:
            data.profile_photo=profile_photo
        data.username = username
        data.company_name = company_name
        data.company_address = company_address
        data.phone = phone
        data.email = email
        data.location = location
        data.description = description
        data.save()
        return redirect('company_home')
    context = {
        'data': data
    }
    return render(request,'company/profile_edit.html',context)
    
    
    
    

#Job Post(Company)
def job_post(request):
    
    if not request.user.is_authenticated:
        return redirect('company_login')
    
    company = CompanyUser.objects.get(user=request.user)
    if company.user.is_active == False:
        return redirect("company/error.html")
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        industry = request.POST.get('industry')
        location = request.POST.get('location')
        position = request.POST.get('position')
        salary = request.POST.get('salary')
        education_requirment = request.POST.get('education_requirment')
        experience_requirement = request.POST.get('experience_requirement')
        skills_required = request.POST.get('skills_required')
        JobAdd.objects.create(
            user = request.user,
            job_title = job_title,
            company_name=company_name,
            job_description = job_description,
            industry = industry,
            location = location,
            position = position,
            salary = salary,
            education_requirment = education_requirment,
            experience_requirement = experience_requirement,
            skills_required = skills_required,
          
        )
        
        return redirect('job_details')
    return render(request,'company/job_add.html')
        
        
        
# Job Details Company

def job_details(request):
    
    if not request.user.is_authenticated:
        return redirect('company_login')
    
    job = JobAdd.objects.filter(user=request.user)
    context = {
        'job': job
    }
    return render(request,'company/job_details.html',context)



#JOB DELETE COMPANY

def  job_delete(request,id):
    
    if not request.user.is_authenticated:
        return redirect('company_login')
    
    delete_job = JobAdd.objects.get(id=id)
    if request.method =='POST':
        delete_job.delete()
        return redirect('job_details')
    context={
        'delete_job':delete_job
    }
    return render(request,'company/job_delete.html',context)




# ALL CANDIDATE PROFILE VIEW(COMPANY)

def all_candidate(request):
    
    if not request.user.is_authenticated:
        return redirect('company_login')
    
    candidate_datas = CandidateUser.objects.all()
    context = {
        'candidate_datas':candidate_datas
    }
    return render(request,'company/all_candidate.html',context)
    


# CANDIDATE PROFILE VIEW BY COMPANY(BY ID)

def candidate_list(request,id):
    
    if not request.user.is_authenticated:
        return redirect('company_login')
    
    candidate_data = CandidateUser.objects.get(id=id)
    context = {
        'candidate_data':candidate_data
    }
    return render(request,'company/candidate_list.html',context)



#REJECTING COMPANY BY ADMIN
def company_reject(request, id):
     
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    company = CompanyUser.objects.get(id=id)
    user = company.user
    user.is_active = False  
    user.save()
    return redirect('company_list_activated')




#PENDING APPLICATION BY COMPNAY
def select_applicant(request, application_id):
     
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    try:
        application = Application.objects.get(id=application_id)
    except Application.DoesNotExist:
       
        application = None

    if application:
      
        application.job_selection = 'Selected'
        application.save()
    return redirect('applicant_list') 


#SELECTED APPLICATION BY COMPNAY
def select_application(request,id,id_2):
     
    if not request.user.is_authenticated:
        return redirect('company_login')
    
    application =  Application.objects.get(id=id)
    
    application.status = "Selected"
    application.save()
    return redirect('applicants_list',id_2) 

#REJECTED APPLICATION BY COMPNAY
def reject_application(request,id,id_2):
    
    if not request.user.is_authenticated:
        return redirect('company_login')
    
    application =  Application.objects.get(id=id)
    
    application.status = "Not_Selected"
    application.save()
    return redirect('applicants_list',id_2) 



# #APPLICATION LISTS

# def application_lists(request):
#     applications = Application.objects.all()
#     context = {
#         'applications':applications
#     }
#     return render(request,'company/application_list.html',context)


#APPLICATIONS FOR COMPNAY
def applicants_list(request, id):
    
    if not request.user.is_authenticated:
        return redirect('compnay_login')
    
    try:
        job = JobAdd.objects.get(id=id) 
    except JobAdd.DoesNotExist:
        job = None
    applications = Application.objects.filter(job=job)
    context = {
        'job': job,
        'applications': applications,
        "id":id
    }
    return render(request, 'company/applicants_list.html', context)






      
    

# #CANDIDATE APPLICATIONS(COMPANY)

# def applications(request,id):
#     job = JobAdd.objects.get(id=id)
#     application = Application.objects.filter(job=job)
#     print(application)
#     context = {
#         'application':application
#     }
#     return render(request,'company/applications.html',context)



#ADMIN HOME PAGE
def admin_home(request):
    
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin/admin_home.html')



#COMPNAY LISTS FOR ADMIN
def company_list(request):
    
     
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    companies = CompanyUser.objects.all()
    context = {
        'companies':companies,
        
    }
    return render(request,'admin/company_list.html',context)

#CANDIDATE LISTS FOR ADMIN

 
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
def candidates_list(request):
      candidates = CandidateUser.objects.all()
      context = {
          'candidates':candidates
      }
      return render(request,'admin/candidates_list.html',context)
  
  
#ACTIVATE COMPANIES BY ADMIN
def company_activate(request,id):
    
     
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    company = CompanyUser.objects.get(id=id)
    user = company.user
    user.is_active = True
    user.save()
    return redirect('company_list')


#ACTIVATED COMPANIES BY ADMIN
def company_list_activated(request):
     
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    companies = CompanyUser.objects.all()
    context = {
        'companies':companies,
        
    }
    return render(request,'admin/company_list_activated.html',context)



#ABOUT US

def about_us(request):
    return render(request,'admin/about.html')


