from django.contrib import admin
from store.models import Sale, Store, Spent

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'user', 'created_at']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Spent)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('store', 'month', 'year')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('customer_id','date', 'carrier', 'guide', 'delivery_status', 'status')
