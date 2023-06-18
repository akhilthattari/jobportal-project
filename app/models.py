from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    profile_photo = models.ImageField(upload_to='profile_photo',null=True,blank=True)
    phone = models.CharField(max_length=15)
    
    
class CompanyUser(models.Model):
    REGISTRATION_STATUS_CHOICES = [
        ('Pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_address = models.TextField(null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=200,null=True)
    profile_photo = models.ImageField(upload_to='profile_photo',null=True,blank=True)
    username = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    registration_status = models.CharField(max_length=100, choices=REGISTRATION_STATUS_CHOICES, default='pending')

    
    def __str__(self):
        return self.company_name
    
   
    
class CandidateUser(models.Model):
    
    STATUS_CHOICES = (
        ('under_processing', 'Under Processing'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    )
    
    education_choices = (
        ('High School', 'High School'),
        ('Higher Secondary', 'Higher Secondary'),
        ('DIPLOMA','DIPLOMA'),
        ('Graduation', 'Graduation'),
        ('Post Graduation', 'Post Graduation'),
        ('PhD', 'PhD'),
        ('other', 'other'),
    )
    
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,null=True)
    candidate_address = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to='profile_photo',null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=100,null=True)
    qualification = models.CharField(max_length=20, choices=education_choices,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='under_processing')
    skills = models.CharField(max_length=255, blank=True, null=True)
    


    def __str__(self):
        return self.username


class JobAdd(models.Model):
    job_choices=(
        ('Full_Time', 'Full Time'),
        ('Part_Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    )
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True  )
    company_name=models.CharField(max_length=100,null=True)
    job_title = models.CharField(max_length=200,null=True)
    job_description = models.TextField(null=True)
    job_type = models.CharField(max_length=100,choices=job_choices,null=True)
    industry = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    salary = models.CharField(max_length=100,null=True)
    education_requirment = models.CharField(max_length=150,null=True)
    experience_requirement = models.CharField(max_length=150,null=True)
    skills_required = models.CharField(max_length=250,null=True)
    created_date = models.DateField(auto_now_add=True,null=True)
    updated_date = models.DateField(auto_now=True,null=True)

    
    
    def __str__(self):
        return self.job_title
    
    

class Application(models.Model):
    
    
    
    selection_choices = (
        ('Selected ', ' Selected'),
        ('Pending', 'Pending'),
        ('Not_Selected','Not_Selected'),
       
    )
    
    user = models.ForeignKey(CandidateUser,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,null=True)
    job = models.ForeignKey(JobAdd,on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume',null=True)
    job_selection = models.CharField(max_length=100,choices=selection_choices,null=True )
    status = models.CharField(max_length=255, default='Pending')
    
    def __str__(self):
        return f"{self.username} - {self.job.title}"
    
    
    

class Education(models.Model):
     user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
     college_name = models.CharField(max_length=100,null=True)
     year = models.CharField(max_length=100,null=True)
     subject = models.CharField(max_length=100,null=True)
     
     def __str__(self):
         return self.college_name
     
     
class Add_skill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.skill
    
class Add_experience(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    start_date = models.CharField(max_length=50,null=True)
    end_date = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.company_name
    
    
    

    