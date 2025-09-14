"""
Команда для автоматической миграции данных на сервер
Запускать: python manage.py migrate_data
"""

from django.core.management.base import BaseCommand
from django.core.files import File
import os
from pathlib import Path
from main.models import Service, PortfolioItem, FAQ, SocialLink, ContactInfo

class Command(BaseCommand):
    help = 'Автоматически создает все данные для сайта'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Начинаем автоматическую миграцию данных...')
        
        # Создаем услуги
        self.create_services()
        
        # Создаем портфолио
        self.create_portfolio()
        
        # Создаем FAQ
        self.create_faq()
        
        # Создаем социальные ссылки
        self.create_social_links()
        
        # Создаем контактную информацию
        self.create_contact_info()
        
        self.stdout.write(self.style.SUCCESS('✅ Все данные успешно созданы!'))

    def create_services(self):
        """Создание услуг"""
        self.stdout.write('📋 Создаем услуги...')
        
        services_data = [
            {
                'service_type': '3d_modeling',
                'title': '3D моделирование',
                'description': 'Создание 3D моделей любой сложности с использованием современных CAD-систем. От простых деталей до сложных механических узлов.',
                'image': 'services/3d_modeling.jpg',
                'order': 1
            },
            {
                'service_type': '3d_printing',
                'title': '3D печать',
                'description': 'Высокоточная 3D печать на современном оборудовании. FDM, SLA, SLM технологии. Быстрое изготовление прототипов и функциональных деталей.',
                'image': 'services/3d_printing.jpg',
                'order': 2
            },
            {
                'service_type': '3d_scanning',
                'title': '3D сканирование',
                'description': 'Точное 3D сканирование объектов любой сложности. Создание цифровых копий для дальнейшего моделирования и печати.',
                'image': 'services/3d_scanning.jpg',
                'order': 3
            },
            {
                'service_type': 'reverse_engineering',
                'title': 'Реверс-инжиниринг',
                'description': 'Высокоточное 3D сканирование объектов любой сложности. Создаем цифровые копии реальных предметов для дальнейшего моделирования и печати.',
                'image': 'services/reverse_engineering.jpg',
                'order': 4
            },
            {
                'service_type': 'engineering',
                'title': 'Инжиниринг',
                'description': 'Комплексный инжиниринг от проекта до реализации. Разрабатываем техническую документацию, создаем 3D модели и обеспечиваем полный цикл разработки.',
                'image': 'services/engineering.jpg',
                'order': 5
            },
            {
                'service_type': 'post_processing',
                'title': 'Постобработка',
                'description': 'Финишная обработка напечатанных деталей. Шлифовка, покраска, сборка, нанесение покрытий для улучшения свойств.',
                'image': 'services/post_processing.jpg',
                'order': 6
            }
        ]
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                service_type=service_data['service_type'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'  ✅ Создана услуга: {service.title}')
            else:
                self.stdout.write(f'  ⚠️ Услуга уже существует: {service.title}')

    def create_portfolio(self):
        """Создание портфолио"""
        self.stdout.write('🖼️ Создаем портфолио...')
        
        portfolio_data = [
            {
                'title': 'Механические детали',
                'image': 'portfolio/portfl1.jpg',
                'description': 'Высокоточные механические детали, напечатанные на промышленном оборудовании',
                'order': 1
            },
            {
                'title': 'Архитектурные модели',
                'image': 'portfolio/portfl2.jpg',
                'description': 'Детализированные архитектурные модели для презентаций',
                'order': 2
            },
            {
                'title': 'Прототипы изделий',
                'image': 'portfolio/portfl3.jpg',
                'description': 'Быстрые прототипы для тестирования концепций',
                'order': 3
            },
            {
                'title': 'Декоративные элементы',
                'image': 'portfolio/portfl4.jpg',
                'description': 'Уникальные декоративные элементы и сувениры',
                'order': 4
            },
            {
                'title': 'Технические узлы',
                'image': 'portfolio/portfl5.jpg',
                'description': 'Сложные технические узлы и компоненты',
                'order': 5
            },
            {
                'title': 'Медицинские модели',
                'image': 'portfolio/portfl6.jpg',
                'description': 'Специализированные модели для медицинских целей',
                'order': 6
            },
            {
                'title': 'Автомобильные детали',
                'image': 'portfolio/portfl7.jpeg',
                'description': 'Детали для автомобильной промышленности',
                'order': 7
            },
            {
                'title': 'Электронные корпуса',
                'image': 'portfolio/portfl8.jpg',
                'description': 'Корпуса и корпусные детали для электроники',
                'order': 8
            }
        ]
        
        for item_data in portfolio_data:
            item, created = PortfolioItem.objects.get_or_create(
                title=item_data['title'],
                defaults=item_data
            )
            if created:
                self.stdout.write(f'  ✅ Создана работа: {item.title}')
            else:
                self.stdout.write(f'  ⚠️ Работа уже существует: {item.title}')

    def create_faq(self):
        """Создание FAQ"""
        self.stdout.write('❓ Создаем FAQ...')
        
        faq_data = [
            {
                'question': 'Сколько времени занимает выполнение заказа?',
                'answer': 'Обычно 2–5 дней, сложные проекты до 1–2 недель, в зависимости от загруженности. При необходимости можем ускорить процесс за доплату. При согласовывание обозначаются ориентировочные сроки сразу.',
                'order': 1,
                'is_active': True
            },
            {
                'question': 'Можно ли получить индивидуальную консультацию перед заказом?',
                'answer': 'Да. После того, как вы свяжитесь с нами. Мы подскажем подходящие варианты, технологии и материалы, объясним возможные особенности и предложим лучшее решение под вашу задачу.',
                'order': 2,
                'is_active': True
            },
            {
                'question': 'Как происходит доставка готовых изделий?',
                'answer': 'Доставка курьером, почтой, транспортной компанией или самовывозом.',
                'order': 3,
                'is_active': True
            },
            {
                'question': 'Как осуществляется коммуникация с клиентом на протяжении всего процесса выполнения заказа?',
                'answer': 'Мы держим связь любым удобным способом: мессенджеры, почта, телефон. На ключевых этапах (согласование модели, печать, готовность) всегда уведомляем клиента.',
                'order': 4,
                'is_active': True
            },
            {
                'question': 'Какие цены на ваши услуги и как формируется стоимость?',
                'answer': 'Стоимость зависит от объёма, материала, сложности работы и постобработки. Для прозрачности мы всегда рассчитываем цену перед запуском заказа и согласовываем её с вами.',
                'order': 5,
                'is_active': True
            },
            {
                'question': 'Какие гарантии вы предоставляете на свои услуги и готовые изделия?',
                'answer': 'Мы гарантируем ответственное отношение к каждому заказу и делаем всё, чтобы результат соответствовал вашим ожиданиям. Каждая работа проходит проверку перед передачей клиенту. Если вдруг возникают вопросы по качеству или результату, мы всегда открыты к диалогу и предлагаем решение, которое будет комфортным для заказчика.',
                'order': 6,
                'is_active': True
            }
        ]
        
        for faq_item in faq_data:
            item, created = FAQ.objects.get_or_create(
                question=faq_item['question'],
                defaults=faq_item
            )
            if created:
                self.stdout.write(f'  ✅ Создан FAQ: {item.question[:50]}...')
            else:
                self.stdout.write(f'  ⚠️ FAQ уже существует: {item.question[:50]}...')

    def create_social_links(self):
        """Создание социальных ссылок"""
        self.stdout.write('🔗 Создаем социальные ссылки...')
        
        social_data = [
            {
                'platform': 'telegram',
                'url': 'https://t.me/modelix_spb',
                'order': 1
            },
            {
                'platform': 'whatsapp',
                'url': 'https://wa.me/79291782000',
                'order': 2
            },
            {
                'platform': 'vk',
                'url': 'https://vk.com/modelix_spb',
                'order': 3
            },
            {
                'platform': 'youtube',
                'url': 'https://youtube.com/@modelix_spb',
                'order': 4
            }
        ]
        
        for social_item in social_data:
            item, created = SocialLink.objects.get_or_create(
                platform=social_item['platform'],
                defaults=social_item
            )
            if created:
                self.stdout.write(f'  ✅ Создана ссылка: {item.get_platform_display()}')
            else:
                self.stdout.write(f'  ⚠️ Ссылка уже существует: {item.get_platform_display()}')

    def create_contact_info(self):
        """Создание контактной информации"""
        self.stdout.write('📞 Создаем контактную информацию...')
        
        contact_data = {
            'phone': '+7 (929) 178-20-00',
            'email': 'modelix.stl@gmail.com',
            'work_hours': 'ПН-ПТ 10:00-20:00',
            'owner_name': 'Худолей Илья Константинович',
            'inn': '780618190040'
        }
        
        contact, created = ContactInfo.objects.get_or_create(
            defaults=contact_data
        )
        
        if created:
            self.stdout.write('  ✅ Создана контактная информация')
        else:
            self.stdout.write('  ⚠️ Контактная информация уже существует')
