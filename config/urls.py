from django.contrib import admin
from django.urls import include, path
from rest_framework.response import Response
from rest_framework.views import APIView


class EndpointsView(APIView):
    """API Endpoints view on root """

    def get(self, request, *args, **kwargs):
        apidocs = {
            "Login": request.build_absolute_uri('api-auth/login/'),
            "Admin": request.build_absolute_uri('admin/'),
        }
        return Response(apidocs)


urlpatterns = [
    path('', EndpointsView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
