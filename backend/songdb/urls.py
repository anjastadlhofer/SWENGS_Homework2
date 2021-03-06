from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1'
    ),
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('country/options', views.country_option_list),
    path('person/list', views.person_list),
    path('person/create', views.person_form_create),
    path('person/<int:pk>/get', views.person_form_get),
    path('person/<int:pk>/update', views.person_form_update),
    path('person/<int:pk>/delete', views.person_delete),
    path('song/list', views.songs_list),
    path('song/create', views.song_form_create),
    path('song/<int:pk>/get', views.song_form_get),
    path('song/<int:pk>/update', views.song_form_update),
    path('song/<int:pk>/delete', views.song_delete),
    url(r'^api-token-auth/', obtain_jwt_token),
    #url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #url(r'^api-token-auth/', obtain_jwt_token),
]
