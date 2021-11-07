import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django_rest_demo.settings import DEBUG
from drf_spectacular.views import SpectacularAPIView, \
    SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView
from .auth import CustomTokenObtainPairView

'''
Keeping API and static paths different from each other.
'''
apiurlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', 
        SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), 
        name='redoc'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('clients/', include('clients.urls')),
    path('projects/', include('projects.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apiurlpatterns))
]

if DEBUG:
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
