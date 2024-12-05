from django.urls import path, include
from rest_framework import permissions
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Gestão de Cursos API",
        default_version='v1',
        description="API para gestão de cursos, incluindo operações de atualização de quórum.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@exemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('login/', include('sgset.urls.AuthUrls')),
    path('goal/', include('sgset.urls.GoalUrls'))
=======
    path('login/', include('sgset.urls.auth_urls')),
    path('course-class/', include('sgset.urls.course_class_urls')),
    path('course/', include('sgset.urls.course_urls')),
    path('quorum/', include('sgset.urls.update_quorum_urls')),
    path('goals/', include('sgset.urls.goals_urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
>>>>>>> 69b6d6df39826ff1932b63d645179bc2d66bf142
]
