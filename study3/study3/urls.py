
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app3.urls')),
    path('products/', include('product.urls'))
]
