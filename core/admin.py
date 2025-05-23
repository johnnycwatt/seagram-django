from django.contrib import admin
from .models import Property, Member, ContactInquiry, SellRequest

# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'status', 'suburb', 'created_at')
    list_filter = ('status', 'suburb')
    search_fields = ('address', 'description')
    ordering = ('-created_at',)
    list_per_page = 10

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('position',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name',)
    list_per_page = 10

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
    list_per_page = 10

@admin.register(SellRequest)
class SellRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'property_address', 'created_at')
    search_fields = ('name', 'email', 'property_address')
    ordering = ('-created_at',)
    list_per_page = 10