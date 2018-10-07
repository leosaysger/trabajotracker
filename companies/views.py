from .models import Company, Job
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'companies/index.html'
    context_object_name = 'companies_list'
    
    def get_queryset(self):
        return Company.objects.all()

class DetailsView(generic.DetailView):
    model = Company
    template_name = 'companies/detail.html'

def apply(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    print(request.POST)
    try:
        selected_job = company.job_set.get(pk=request.POST['apply'])
    except (KeyError, Company.DoesNotExist):
        return render(request, 'companies/detail.html', {'company': company, 'error_message': "you didn't select a job",})
    else:
        selected_job.applied = True
        selected_job.save()
        return HttpResponseRedirect(reverse('companies:detail', args=(company.id,)))