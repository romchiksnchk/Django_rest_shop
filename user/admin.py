from django.contrib import admin
from .models import Profile, Vacancies


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    pass

