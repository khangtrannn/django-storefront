from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)

products_routers = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_routers.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_routers = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_routers.register('items', views.CartItemViewSet, basename='cart-items')

# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:id>/', views.ProductDetail.as_view()),
#     path('collections/', views.CollectionList.as_view(), name='collection-detail'),
#     path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
# ]

urlpatterns = router.urls + products_routers.urls + carts_routers.urls

