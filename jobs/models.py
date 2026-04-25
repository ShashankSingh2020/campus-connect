from django.db import models
from django.contrib.auth.models import User


class JobListing(models.Model):
    # This choice list makes your project look more professional
    CATEGORY_CHOICES = [
        ('SDE', 'Software Development'),
        ('DA', 'Data Analyst'),
        ('QA', 'Quality Assurance'),
        ('UX', 'UI/UX Designer'),
    ]

    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='SDE')
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary_package = models.CharField(max_length=50, help_text="e.g. 12 LPA")
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This is what shows up in the Admin Panel
        return f"{self.title} - {self.company_name}"


class Application(models.Model):
    # ForeignKey creates the link: 1 Job can have many Applications
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='apps')
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} for {self.job.title}"