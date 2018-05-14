from django.contrib import admin

from .models import Cell, Doctor, Clinic


class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('clinic', 'efio', 'espec',)
    raw_id_fields = ('clinic',)
    search_fields = ('clinic',)


class CellAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'time_start', 'time_end', 'free',)
    raw_id_fields = ('doctor',)
    search_fields = ('doctor',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Cell, CellAdmin)
