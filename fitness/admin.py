from django.contrib import admin
from .models import (
    YogaClass, YogaBooking,
    ZumbaClass, ZumbaBooking,
    HIITClass, HIITBooking
)

# ======================================
# Yoga Admin
# ======================================

@admin.register(YogaClass)
class YogaClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'start_time', 'total_vacancy', 'available_slots_display')
    list_filter = ('start_time', 'instructor')
    search_fields = ('title', 'instructor')

    def available_slots_display(self, obj):
        return obj.available_slots()
    available_slots_display.short_description = 'Available Slots'


@admin.register(YogaBooking)
class YogaBookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'yoga_class', 'booked_at')
    list_filter = ('yoga_class', 'booked_at')
    search_fields = ('client_name', 'client_email')


# ======================================
#  Zumba Admin
# ======================================

@admin.register(ZumbaClass)
class ZumbaClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'start_time', 'total_vacancy', 'available_slots_display')
    list_filter = ('start_time', 'instructor')
    search_fields = ('title', 'instructor')

    def available_slots_display(self, obj):
        return obj.available_slots()
    available_slots_display.short_description = 'Available Slots'


@admin.register(ZumbaBooking)
class ZumbaBookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'zumba_class', 'booked_at')
    list_filter = ('zumba_class', 'booked_at')
    search_fields = ('client_name', 'client_email')


# ======================================
#  HIIT Admin
# ======================================

@admin.register(HIITClass)
class HIITClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'start_time', 'total_vacancy', 'available_slots_display')
    list_filter = ('start_time', 'instructor')
    search_fields = ('title', 'instructor')

    def available_slots_display(self, obj):
        return obj.available_slots()
    available_slots_display.short_description = 'Available Slots'


@admin.register(HIITBooking)
class HIITBookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'hiit_class', 'booked_at')
    list_filter = ('hiit_class', 'booked_at')
    search_fields = ('client_name', 'client_email')
