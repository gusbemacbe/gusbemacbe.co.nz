from django.contrib import admin
from .models import BrazilBill, BrazilFood, BrazilMedicaments, BrazilShopping, BrazilSupermarket, NZBill, NZFood, NZOffice, NZPreTravel, NZShopping, NZSupermarket

# region [ rgba(0, 39, 118, 0.1) ]
## Brazil
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
# endregion

# region [ rgba() ]
## New Zealand
@admin.register(NZPreTravel)
class NZPreTravelAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'cad_price', 'nzd_price', 'usd_price', 'uyu_price')
    
@admin.register(NZBill)
class NZBillAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'brl_price', 'cad_price', 'usd_price', 'uyu_price')
    
@admin.register(NZFood)
class NZFoodAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'brl_price', 'cad_price', 'usd_price', 'uyu_price')
    
@admin.register(NZOffice)
class NZOfficeAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'brl_price', 'cad_price', 'usd_price', 'uyu_price')
    
@admin.register(NZShopping)
class NZShoppingAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'brl_price', 'cad_price', 'usd_price', 'uyu_price')
    
@admin.register(NZSupermarket)
class NZSupermarketAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'brl_price', 'cad_price', 'usd_price', 'uyu_price')
