from django.shortcuts import render
from .models import Chemical

# Create your views here.
def get_all_chemicals(request):
    chemical_list = Chemical.objects.all()

    return render(request, 'chemicalsearch/chemical_list.html', {'chemicals': chemical_list})