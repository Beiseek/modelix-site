from django.db import models

class TechnologyPrice(models.Model):
    """Модель для управления ценами технологий печати"""
    TECHNOLOGY_CHOICES = [
        ('FDM', 'FDM'),
        ('SLA', 'SLA'),
        ('SLM', 'SLM'),
    ]
    
    technology = models.CharField('Технология', max_length=10, choices=TECHNOLOGY_CHOICES, unique=True)
    price_per_gram = models.DecimalField('Цена за грамм (руб)', max_digits=10, decimal_places=2, default=1.00)
    materials_count = models.IntegerField('Количество материалов', default=7)
    production_time = models.IntegerField('Срок изготовления (дни)', default=2)
    
    class Meta:
        verbose_name = 'Цена технологии'
        verbose_name_plural = 'Цены технологий'
    
    def __str__(self):
        return f'{self.technology} - {self.price_per_gram} руб/г'

class Material(models.Model):
    """Модель для материалов"""
    technology = models.ForeignKey(TechnologyPrice, on_delete=models.CASCADE, verbose_name='Технология')
    name = models.CharField('Название материала', max_length=100)
    description = models.TextField('Описание', blank=True)
    
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
    
    def __str__(self):
        return f'{self.technology.technology} - {self.name}'

class PrintOrder(models.Model):
    """Модель для заявок на печать"""
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    message = models.TextField('Сообщение')
    file = models.FileField('Файл модели', upload_to='orders/', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)
    
    class Meta:
        verbose_name = 'Заявка на печать'
        verbose_name_plural = 'Заявки на печать'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Заявка от {self.name} - {self.created_at.strftime("%d.%m.%Y %H:%M")}'

class PortfolioItem(models.Model):
    """Модель для портфолио"""
    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', upload_to='portfolio/')
    description = models.TextField('Описание', blank=True)
    order = models.IntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Работа в портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['order']
    
    def __str__(self):
        return self.title

class FAQ(models.Model):
    """Модель для часто задаваемых вопросов"""
    question = models.CharField('Вопрос', max_length=200)
    answer = models.TextField('Ответ')
    order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)
    
    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Часто задаваемые вопросы'
        ordering = ['order']
    
    def __str__(self):
        return self.question

class CallRequest(models.Model):
    """Модель для заявок на звонок"""
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)
    
    class Meta:
        verbose_name = 'Заявка на звонок'
        verbose_name_plural = 'Заявки на звонок'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Звонок {self.name} - {self.created_at.strftime("%d.%m.%Y %H:%M")}'

class Service(models.Model):
    """Модель для управления услугами (Наши 3D-возможности)"""
    SERVICE_CHOICES = [
        ('3d_modeling', '3D моделирование'),
        ('3d_printing', '3D печать'),
        ('3d_scanning', '3D сканирование'),
        ('reverse_engineering', 'Реверс-инжиниринг'),
        ('engineering', 'Инжиниринг'),
        ('post_processing', 'Постобработка'),
    ]
    
    service_type = models.CharField('Тип услуги', max_length=20, choices=SERVICE_CHOICES, unique=True)
    title = models.CharField('Название услуги', max_length=100)
    description = models.TextField('Описание услуги')
    image = models.ImageField('Изображение', upload_to='services/')
    is_active = models.BooleanField('Активна', default=True)
    order = models.IntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги (Наши 3D-возможности)'
        ordering = ['order']
    
    def __str__(self):
        return f'{self.get_service_type_display()} - {self.title}'

class SocialLink(models.Model):
    """Модель для управления социальными ссылками"""
    SOCIAL_CHOICES = [
        ('telegram', 'Telegram'),
        ('whatsapp', 'WhatsApp'),
        ('vk', 'VKontakte'),
        ('youtube', 'YouTube'),
    ]
    
    platform = models.CharField('Социальная сеть', max_length=20, choices=SOCIAL_CHOICES, unique=True)
    url = models.URLField('Ссылка', max_length=200)
    is_active = models.BooleanField('Активна', default=True)
    order = models.IntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Социальная ссылка'
        verbose_name_plural = 'Социальные ссылки'
        ordering = ['order']
    
    def __str__(self):
        return f'{self.get_platform_display()} - {self.url}'
    
    def get_icon_class(self):
        """Возвращает CSS класс для иконки"""
        icon_map = {
            'telegram': 'fab fa-telegram-plane',
            'whatsapp': 'fab fa-whatsapp',
            'vk': 'fab fa-vk',
            'youtube': 'fab fa-youtube',
        }
        return icon_map.get(self.platform, 'fas fa-link')

class ContactInfo(models.Model):
    """Модель для управления контактной информацией"""
    phone = models.CharField('Телефон', max_length=20, default='+7 (929) 178-20-00')
    email = models.EmailField('Email', default='modelix.stl@gmail.com')
    work_hours = models.CharField('Часы работы', max_length=50, default='ПН-ПТ 10:00-20:00')
    owner_name = models.CharField('ФИО владельца', max_length=100, default='Худолей Илья Константинович')
    inn = models.CharField('ИНН', max_length=20, default='780618190040')
    
    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
    
    def __str__(self):
        return 'Контактная информация'
    
    def save(self, *args, **kwargs):
        # Простое сохранение без сложной логики
        return super().save(*args, **kwargs)