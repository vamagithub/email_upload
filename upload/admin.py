from django.contrib import admin
from .models import Email
from .forms import EmailForm

class EmailAdmin(admin.ModelAdmin):
    list_display = ["__str__", "attach", "subject", "message"]
    form = EmailForm
    # class Meta:
    #     model = Email


admin.site.register(Email, EmailAdmin)
