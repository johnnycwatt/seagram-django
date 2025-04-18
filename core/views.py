from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Property
from .forms import ContactForm, SellForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/home.html'

class PropertyListView(ListView):
    model = Property
    template_name = 'core/property_list.html'
    context_object_name = 'properties'
    queryset = Property.objects.filter(status='sale')

    
    
class PropertyDetailView(DetailView):
    model = Property
    template_name = 'core/property_detail.html'

class StoryView(TemplateView):
    template_name = 'core/story.html'

class PeopleView(TemplateView):
    template_name = 'core/people.html'

class SellView(TemplateView):
    template_name = 'core/sell.html'

#Forms
class ContactFormView(CreateView):
    model = ContactForm
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = '/contact/success/'

class SellFormView(CreateView):
    model = SellForm
    form_class = SellForm
    template_name = 'core/sell_form.html'
    success_url = '/sell/success/'
    
#Success Views
class ContactSuccessView(TemplateView):
    template_name = 'core/contact_success.html'

class SellSuccessView(TemplateView):
    template_name = 'core/sell_success.html'