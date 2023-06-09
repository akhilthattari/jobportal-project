from django.shortcuts import render,redirect
from django.contrib import messages
from .models import CompanyUser,CandidateUser,CustomUser
from django.contrib.auth import login,authenticate,logout
from django.core.mail import send_mail



#COMPANY REGISTER

def Company_register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        company_name = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        profile_photo = request.FILES.get('profile_photo')
        location = request.POST.get('location')
        description = request.POST.get('description')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        
        
        if not CustomUser.objects.filter(username=username).exists():
            if password1 == password2:
                CustomUser.objects.create_user(
                    username = username,
                    email = email,
                    password = password1,
                    phone = phone,
                    profile_photo = profile_photo,
                    is_active = False
                    )
                company_user = CustomUser.objects.get(username=username)
                CompanyUser.objects.create(
                    user = company_user,
                    username = username,
                    company_name = company_name,
                    company_address = company_address,
                    phone = phone,
                    email = email,
                    profile_photo = profile_photo,
                    location = location,
                    description = description,
                    
                        
                    )
                
                messages.success(request,'Account created')
                return redirect('company_login')
            else:
                messages.error(request,'Password doesn\'t match')
        else:
            messages.error(request,'Username already exist')
    return render(request,'company/company_register.html')
                

#COMPNAY LOGIN
def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = CompanyUser.objects.get(username=username)
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                if authenticated_user.is_active:
                    return redirect('company_home')
                else:
                    return render(request, 'company/error.html')
            else:
                messages.error(request, 'Invalid username or password')
        except CompanyUser.DoesNotExist:
            messages.error(request, 'User does not exist')
    
    return render(request, 'company/company_login.html')


#COMPANY SELECTION OF CANDIDATE


# def selection(request,id):

def logout_view(request):
    logout(request)
    return redirect('home')
             
                
                
                

#APPLICANT REGISTER

def Candidate_register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        profile_photo = request.FILES.get('profile_photo')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        candidate_address = request.POST.get('candidate_address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        qualification = request.POST.get('qualification')
        
        
        if not CustomUser.objects.filter(username=username).exists():
            if password1 == password2:
                
                CustomUser.objects.create_user(
                    username = username,
                    email = email,
                    password = password1,
                    phone = phone,
                    profile_photo = profile_photo,
                    
                    )
                candidate_user = CustomUser.objects.get(username=username)
                CandidateUser.objects.create(
                    user = candidate_user,
                    candidate_address = candidate_address,
                    username = username,
                    profile_photo = profile_photo,
                    phone = phone,
                    first_name = first_name,
                    last_name=last_name,
                    email = email,
                    qualification = qualification
                )
                
            messages.success(request,'Account created')
            return redirect('candidate_home')
        else:
            messages.error(request,'Password doesn\'t match')
    else:
            messages.error(request,'Username already exist')
    return render(request,'candidate/candidate_register.html',{'choices':CandidateUser.education_choices})        
    



#CANDIDATE LOGIN

def candidate_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user=authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('candidate_home')
        messages.error(request,'Invalid username or password')
    return render(request,'candidate/candidate_login.html')


#CANDIDATE PROFILE DELETE

def candidate_delete(request,id):
    candidate = CandidateUser.objects.get(id=id)
    if request.method == 'POST':
        candidate.delete()
        return redirect('candidate_login')
    context={
        'candidate':candidate
    }
    return render(request,'candidate/candidate_delete.html',context)

#CANDIDATE SETTINGS

def candidate_settings(request):
    return render(request,'candidate/candidate_settings.html')



#ADMIN LOGIN    


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None and (user.is_staff or user.is_superuser):
            login(request, user)
            return redirect('admin_home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'admin/admin_login.html')