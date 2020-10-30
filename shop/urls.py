from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_list, ProductCreate, ProductDelete, ProductDetail, ProductUpdate
from .views import TagCreate, TagDelete, TagDetail, TagUpdate, tags_list
from .views import OrderCreate, OrderDetail, OrderUpdate, OrderDelete,  order_list
urlpatterns = [
    path('product/', product_list,  name="product_list_url"),
    path('product/create/', ProductCreate.as_view(), name='product_create_url'),
    path('product/<str:slug>/', ProductDetail.as_view(), name='product_detail_url'),
    path('product/<str:slug>/update/', ProductUpdate.as_view(), name='product_update_url'),
    path('product/<str:slug>/delete/', ProductDelete.as_view(), name='product_delete_url'),
    path('tags/',  tags_list, name='tags_list_url'),
    path('tag/create/',  TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('orders/', order_list,  name="orders_list_url"),
    path('order/create/',  OrderCreate.as_view(), name='order_create_url'),
    path('order/<str:slug>/', OrderDetail.as_view(), name='order_detail_url'),
    path('order/<str:slug>/update/', OrderUpdate.as_view(), name='order_update_url'),
    path('order/<str:slug>/delete/', OrderDelete.as_view(), name='order_delete_url'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)