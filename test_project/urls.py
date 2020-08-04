# Django
from django.conf import settings
from django.conf.urls import include, url

include_kwargs = dict(namespace='test_app')

urlpatterns = [
    url(r'^test_app/', include('test_project.test_app.urls', **include_kwargs)),
]

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += [
        url(r'', admin.site.urls),
    ]

if 'django.contrib.staticfiles' in settings.INSTALLED_APPS and settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
