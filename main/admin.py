from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import PrintOrder, CallRequest, PortfolioItem, Service, SocialLink, ContactInfo, FAQ, TechnologyPrice, Material

@admin.register(TechnologyPrice)
class TechnologyPriceAdmin(admin.ModelAdmin):
    list_display = ['technology', 'price_per_gram', 'materials_count', 'production_time']
    list_editable = ['price_per_gram', 'materials_count', 'production_time']
    fields = ['technology', 'price_per_gram', 'materials_count', 'production_time']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'technology', 'description']
    list_filter = ['technology']
    search_fields = ['name', 'description']
    fields = ['technology', 'name', 'description']

@admin.register(PrintOrder)
class PrintOrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at', 'is_processed']
    list_filter = ['created_at', 'is_processed']
    search_fields = ['name', 'phone', 'email']
    readonly_fields = ['created_at']
    list_editable = ['is_processed']

@admin.register(CallRequest)
class CallRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created_at', 'is_processed']
    list_filter = ['created_at', 'is_processed']
    search_fields = ['name', 'phone']
    readonly_fields = ['created_at']
    list_editable = ['is_processed']

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'get_image_preview']
    list_editable = ['order']
    search_fields = ['title', 'description']
    fields = ['title', 'image', 'description', 'order']
    
    def get_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;">', obj.image.url)
        return 'Нет изображения'
    get_image_preview.short_description = 'Превью'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_type', 'title', 'is_active', 'order', 'get_image_preview']
    list_editable = ['title', 'order', 'is_active']
    list_filter = ['service_type', 'is_active']
    search_fields = ['title', 'description']
    fields = ['service_type', 'title', 'description', 'image', 'is_active', 'order']
    ordering = ['order']
    
    def save_model(self, request, obj, form, change):
        """Принудительно сохраняем изменения"""
        from django.core.cache import cache
        # Очищаем кэш при сохранении
        cache.clear()
        super().save_model(request, obj, form, change)
        print(f"🔄 Услуга обновлена: {obj.get_service_type_display()} - {obj.title}")
    
    def get_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;">', obj.image.url)
        return 'Нет изображения'
    get_image_preview.short_description = 'Превью'

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['platform', 'is_active']
    search_fields = ['url']
    fields = ['platform', 'url', 'is_active', 'order']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['question', 'answer']
    fields = ['question', 'answer', 'order', 'is_active']
    ordering = ['order']
    
    def save_model(self, request, obj, form, change):
        """Принудительно сохраняем изменения"""
        from django.core.cache import cache
        # Очищаем кэш при сохранении
        cache.clear()
        super().save_model(request, obj, form, change)
        print(f"🔄 FAQ обновлен: {obj.question[:50]}...")
    
    def response_change(self, request, obj):
        """Обработка после изменения"""
        from django.contrib import messages
        messages.success(request, 'FAQ успешно обновлен!')
        return super().response_change(request, obj)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'work_hours', 'owner_name', 'inn']
    fields = ['phone', 'email', 'work_hours', 'owner_name', 'inn']
    
    def has_add_permission(self, request):
        # Разрешаем добавление только если записей нет
        return not ContactInfo.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление
        return False
    
    def changelist_view(self, request, extra_context=None):
        # Если нет записей, создаем дефолтную
        if not ContactInfo.objects.exists():
            ContactInfo.objects.create()
        return super().changelist_view(request, extra_context)
    
    def save_model(self, request, obj, form, change):
        """Принудительно сохраняем изменения"""
        from django.core.cache import cache
        # Очищаем кэш при сохранении
        cache.clear()
        super().save_model(request, obj, form, change)
        print(f"🔄 Контактная информация обновлена: {obj.phone}, {obj.email}")
    
    def response_change(self, request, obj):
        """Обработка после изменения"""
        from django.contrib import messages
        messages.success(request, 'Контактная информация успешно обновлена!')
        return super().response_change(request, obj)