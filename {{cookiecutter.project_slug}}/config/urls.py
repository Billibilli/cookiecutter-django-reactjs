from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_swagger.views import get_swagger_view

# Overwrite post method for REST-AUTH VerifyEmailView
from '{{ cookiecutter.project_slug }}.users.views' import VerifyEmailView


# Swagger API docs
schema_view = get_swagger_view(title='{{ cookiecutter.project_name }} API')

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('{{ cookiecutter.project_slug }}.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # REST framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # REST-AUTH urls. See: http://django-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # This is the workaround for using API to verify email. See: https://github.com/Tivix/django-rest-auth/issues/292
    url(
        r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$',
        VerifyEmailView.as_view(),
        name='account_confirm_email'
    ),

    # REST-JWT urls. See: http://getblimp.github.io/django-rest-framework-jwt/#usage
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    # Django REST Swagger: http://marcgibbons.github.io/django-rest-swagger/
    url(r'^api-docs/', schema_view),

    # OAUTH2: https://github.com/evonove/django-oauth-toolkit
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
