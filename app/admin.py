from django.contrib import admin
from app.models import Mail

# Register your models here.
@admin.register(Mail)
class CategoryAdmin(admin.ModelAdmin):
    pass