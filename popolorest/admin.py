from django.contrib import admin
from popolo.models import Person, Organization


class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person)
admin.site.register(Organization)
