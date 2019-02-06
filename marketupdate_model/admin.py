from django.contrib import admin

from marketupdate_model.models import Update, Category, Symbol, Value


# Register your models here.
admin.site.register(Update)
admin.site.register(Category)
admin.site.register(Symbol)
admin.site.register(Value)