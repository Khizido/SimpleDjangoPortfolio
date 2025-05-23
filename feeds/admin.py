from django.contrib import admin
from .models import *
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('name_complete', 'address')
    search_fields = ["name_complete"]

class ProjectsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'skill')  # skill de ekledim
    list_editable = ('order',)  # Order'ı doğrudan düzenlenebilir yap
    ordering = ['order']  # Sıralama

class AboutAdmin(admin.ModelAdmin):
    list_display = ['__str__']

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['__str__']

# Model kayıtları
admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Skills, SkillsAdmin)