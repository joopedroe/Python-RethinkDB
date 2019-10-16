# https://docs.djangoproject.com/en/2.1/topics/http/urls/

from django.conf import settings
from django.urls import path, include
from django.urls.base import reverse_lazy
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        RedirectView.as_view(
            url=reverse_lazy(
                'clientes:cadastroCliente'
            ),
            permanent=False
        ),
        name="home"
    ),
    path(
        'cliente/',
        include(
            'Gerencia_ClienteApp.urls',
            namespace='clientes'
        ),
        name='clientes'
    ),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
