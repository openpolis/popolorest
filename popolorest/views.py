__author__ = 'guglielmo'
from popolo.models import Person, Organization
from rest_framework import viewsets

# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    model = Person

class OrganizationViewSet(viewsets.ModelViewSet):
    model = Organization

