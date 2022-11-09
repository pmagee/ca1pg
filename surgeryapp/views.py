from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Doctor, Surgery

# Create your views here.
class DoctorListView(ListView):
    model = Doctor
    template_name = 'dlist.html'
    context_object_name = 'all_ds_list'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'd_detail.html'

class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'd_create.html'
    fields = ['name', 'surgery', 'num_patients']

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'd_edit.html'
    fields = ['num_patients']

class DPListView(ListView):
    model = Surgery
    template_name = 'sd_list.html'
    context_object_name = 'all_s_list'