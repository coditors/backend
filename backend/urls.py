
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("api/", include('accounts.urls')),
    path('newjob/',include('newjob.urls'))
]
