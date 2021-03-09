from django.contrib import admin
from .models import Maghale,Student,Professor,University,AddressUny,AboutUs

class BlogMaghale(admin.ModelAdmin):
    fieldsets = [
        ('title',                {'fields' : ['title']}),
        ('file',                {'fields' : ['file']}),
        
    ]

    list_display = ['title' , 'date']
    search_fields = ['title' , 'content']



admin.site.register(Maghale)
admin.site.register(Student)

admin.site.register(Professor)

admin.site.register(University)
admin.site.register(AddressUny)
admin.site.register(AboutUs)