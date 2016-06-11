# Django
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    url(r'^test_app/', include('test_project.test_app.urls', namespace='test_app',
                               app_name='test_app')),
]

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += [
        url(r'', include(admin.site.urls)),
    ]

if 'django.contrib.staticfiles' in settings.INSTALLED_APPS and settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
