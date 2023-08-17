from django.contrib import admin
from app1.modals.customer  import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display=('user_name','first_name','last_name','email_field','password')
admin.site.register(Customer,CustomerAdmin)
#admin.site.register(Customer)

# Register your models here.
