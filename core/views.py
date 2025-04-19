from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Property, Member
from .forms import ContactForm, SellForm
from django.db.models import Q


# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/home.html'

class PropertyListView(ListView):
    model = Property
    template_name = 'core/property_list.html'
    context_object_name = 'properties'
    
    def get_queryset(self):
        queryset = Property.objects.filter(status='sale').order_by('-updated_at')

        #Filter by Suburb
        suburb = self.request.GET.get('suburb')
        if suburb:
            queryset = queryset.filter(suburb=suburb)

        #Filter by Bedrooms
        bedrooms = self.request.GET.get('bedrooms')
        if bedrooms:
            queryset = queryset.filter(bedrooms__gte=bedrooms)

        #Filter by Bathrooms
        bathrooms = self.request.GET.get('bathrooms')
        if bathrooms:
            queryset = queryset.filter(bathrooms__gte=bathrooms)
  

        #Search by keyword
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(address__icontains=query) |
                Q(description__icontains=query)
            )

        #Sort
        sort = self.request.GET.get('sort')
        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'date_desc':
            queryset = queryset.order_by('-created_at')
        elif sort == 'date_asc':
            queryset = queryset.order_by('created_at')
        else:
            queryset = queryset.order_by('-created_at')

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suburb_choices'] = Property._meta.get_field('suburb').choices
        context['bedroom_choices'] = [(str(i), f"{i}+") for i in range(1, 6)]
        context['bathroom_choices'] = [(str(i), f"{i}+") for i in range(1, 4)]
        return context
    
    
class PropertyDetailView(DetailView):
    model = Property
    template_name = 'core/property_detail.html'

class StoryView(TemplateView):
    template_name = 'core/story.html'

class PeopleView(ListView):
    model = Member
    context_object_name = 'members'
    template_name = 'core/people.html'

class SellView(TemplateView):
    template_name = 'core/sell.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sold_properties'] = Property.objects.filter(status='sold').order_by('-updated_at')[:3]
        return context

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