from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('beats/', views.get_beats, name='beats'),
    path('soundkits/', views.get_soundkits, name='soundkits'),

    path('create/', views.create_product, name="product-create"),
    path('upload/image/', views.upload_image, name="image-upload"),
    path('upload/file/', views.upload_file, name="file-upload"),
    path('<str:pk>/', views.get_product, name="product"),
    path('delete/<str:pk>/', views.delete_product, name="product-delete"),
    path('update/<str:pk>/', views.update_product, name="product-update"),
]
