from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import *

# Create your views here.

def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()  # Bu zaten order'a göre sıralı gelecek
    skills = Skills.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills
    }
    return render(request, 'home_page.html', context)

@require_POST
@csrf_exempt  # CSRF token kullanıyorsanız bunu kaldırın
def update_project_order(request):
    try:
        # POST verilerinden project order bilgilerini al
        projects_data = json.loads(request.POST.get('projects', '[]'))
        
        # Her project için order değerini güncelle
        for project_data in projects_data:
            try:
                project = Projects.objects.get(id=project_data['id'])
                project.order = project_data['order']
                project.save()
            except Projects.DoesNotExist:
                continue
                
        return JsonResponse({
            'status': 'success',
            'message': 'Proje sıralaması başarıyla güncellendi'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Geçersiz JSON verisi'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Hata oluştu: {str(e)}'
        })

# Admin paneli için toplu order güncelleme (opsiyonel)
def reset_project_orders(request):
    """Tüm projelerin order değerlerini sıfırlar"""
    if request.method == 'POST':
        projects = Projects.objects.all().order_by('id')
        for index, project in enumerate(projects, 1):
            project.order = index
            project.save()
        return JsonResponse({'status': 'success', 'message': 'Order değerleri sıfırlandı'})
    
    return JsonResponse({'status': 'error', 'message': 'Sadece POST isteği kabul edilir'})