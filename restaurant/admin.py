from django.contrib import admin

from restaurant.models import Category, Ingredient, Table, Dish

class TableAdmin(admin.ModelAdmin):
	list_display = ('name', 'take_away', 'status')
	list_filter = ('take_away', 'status')
	ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'status')
	list_filter = ('status', )

class IngredientAdmin(admin.ModelAdmin):
    pass

class DishAdmin(admin.ModelAdmin):
    pass

admin.site.register(Table, TableAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Dish, DishAdmin)
