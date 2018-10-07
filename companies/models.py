from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    def __str__(self):
        return self.company_name

class Job(models.Model):
    job = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100)
    job_url = models.URLField()
    applied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.job_name

    def have_applied(self):
        return self.applied 
    