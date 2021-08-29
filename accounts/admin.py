from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUserForm, StaffEditUserForm

from .models import User

class Admin(UserAdmin):
    add_form = CreateUserForm
    form = StaffEditUserForm
    model = User
    list_display = ['email','username','is_staff','balance','banned','phone',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('balance','banned','phone',) } ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('balance','banned','phone',) } ),
    )
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }


admin.site.register(User, Admin)



class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

## 'is_staff','email','address_home','address_work','phone','occupation','referral_source','balance','banned','regular_customer',