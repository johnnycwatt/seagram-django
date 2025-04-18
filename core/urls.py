from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HomeView,
    PropertyListView,
    PropertyDetailView,
    SellView,
    StoryView,
    PeopleView,
    ContactFormView,
    SellFormView,
    ContactSuccessView,
    SellSuccessView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('buy/', PropertyListView.as_view(), name='property_list'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('sell/', SellView.as_view(), name='sell'),
    path('sell/form', SellFormView.as_view(), name='sell_form'),
    path('about/story', StoryView.as_view(), name='story'),
    path('about/people', PeopleView.as_view(), name='people'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('contact/success/', ContactSuccessView.as_view(), name='contact_success'),
    path('sell/success/', SellSuccessView.as_view(), name='sell_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)