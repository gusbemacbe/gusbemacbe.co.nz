from django.contrib import admin
from .models import BrazilBill, BrazilFood, BrazilMedicaments, BrazilShopping, BrazilSupermarket

@admin.register(BrazilBill)
class BrazilBillAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'cad_price', 'nzd_price', 'usd_price', 'uyu_price')
    
@admin.register(BrazilFood)
class BrazilFoodAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'cad_price', 'nzd_price', 'usd_price', 'uyu_price')
    
@admin.register(BrazilMedicaments)
class BrazilMedicamentsAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'cad_price', 'nzd_price', 'usd_price', 'uyu_price')

@admin.register(BrazilShopping)
class BrazilShoppingAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'cad_price', 'nzd_price', 'usd_price', 'uyu_price')

@admin.register(BrazilSupermarket)
class BrazilSupermarketAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'cad_price', 'nzd_price', 'usd_price', 'uyu_price')
