from django.contrib import admin
from django.urls import path, include  # Importa a função include para incluir as rotas da aplicação

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/services/', include('apps.service.urls')),
    path('api/categories/', include('apps.category.urls')),
    path('api/subcategories/', include('apps.subcategory.urls')),
    path('api/products/', include('apps.product.urls')),
    path('api/professionals/', include('apps.professional.urls')),
    path('api/sales/', include('apps.sale.urls')),
    path('api/images/', include('apps.image.urls')),
    path('api/customers/', include('apps.customer.urls'))
]
