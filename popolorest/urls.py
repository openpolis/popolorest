from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from .views import PersonViewSet, OrganizationViewSet, MembershipViewSet, PostViewSet
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'popolorest.views.home', name='home'),
    # url(r'^popolorest/', include('popolorest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # django-rest-frameworks urls
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
