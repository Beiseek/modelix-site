from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import PrintOrder, PortfolioItem, CallRequest, Service, SocialLink, ContactInfo, FAQ
import json

def index(request):
    """Главная страница"""
    # Получаем данные для отображения
    portfolio_items = PortfolioItem.objects.all()  # Все работы
    services = Service.objects.filter(is_active=True).order_by('order')  # Активные услуги
    social_links = SocialLink.objects.filter(is_active=True).order_by('order')  # Активные социальные ссылки
    faq_items = FAQ.objects.filter(is_active=True).order_by('order')  # Активные FAQ
    
    # Получаем контактную информацию (создаем если не существует)
    contact_info, created = ContactInfo.objects.get_or_create(
        defaults={
            'phone': '+7 (929) 178-20-00',
            'email': 'modelix.stl@gmail.com',
            'work_hours': 'ПН-ПТ 10:00-20:00',
            'owner_name': 'Худолей Илья Константинович',
            'inn': '780618190040'
        }
    )
    
    context = {
        'portfolio_items': portfolio_items,
        'services': services,
        'social_links': social_links,
        'contact_info': contact_info,
        'faq_items': faq_items,
    }
    
    return render(request, 'main/index.html', context)

def submit_order(request):
    """Обработка заявки на печать"""
    print(f"Получен запрос: {request.method}")
    print(f"POST данные: {request.POST}")
    print(f"FILES данные: {request.FILES}")
    
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            phone = request.POST.get('phone', '').strip()
            email = request.POST.get('email', '').strip()
            message = request.POST.get('message', '').strip()
            file = request.FILES.get('file')
            
            print(f"Данные: name={name}, phone={phone}, email={email}, message={message}")
            
            if not all([name, phone, email]):
                print("Ошибка: не все обязательные поля заполнены")
                return JsonResponse({'success': False, 'error': 'Заполните все обязательные поля'})
            
            order = PrintOrder.objects.create(
                name=name,
                phone=phone,
                email=email,
                message=message,
                file=file
            )
            
            print(f"Заявка создана: {order}")
            return JsonResponse({'success': True, 'message': 'Заявка успешно отправлена!'})
            
        except Exception as e:
            print(f"Ошибка при создании заявки: {e}")
            return JsonResponse({'success': False, 'error': f'Произошла ошибка: {str(e)}'})
    
    print("Неподдерживаемый метод")
    return JsonResponse({'success': False, 'error': 'Метод не поддерживается'})



def submit_call_request(request):
    """Обработка заявки на звонок"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            phone = request.POST.get('phone', '').strip()
            
            if not all([name, phone]):
                return JsonResponse({'success': False, 'error': 'Заполните все поля'})
            
            call_request = CallRequest.objects.create(
                name=name,
                phone=phone
            )
            
            return JsonResponse({'success': True, 'message': 'Заявка на звонок принята!'})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Произошла ошибка при отправке заявки'})
    
    return JsonResponse({'success': False, 'error': 'Метод не поддерживается'})