from django.contrib import admin
from .models import User, Vacancies


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    pass

