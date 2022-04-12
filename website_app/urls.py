from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('error/<str:err>/', views.error, name="error_page"),
    path('delete-<str:model_name>/<int:model_pk>/', views.delete_record, name="delete_record"),
    path('categories/', views.categories, name="categories"),
    path('categories/new', views.category_new, name="category_new"),
    path('categories/<int:category_pk>/', views.category, name="category"),
    path('categories/<int:category_pk>/edit/', views.category_edit, name="category_edit"),
    path('categories/<int:category_pk>/subcategory/<int:subcategory_pk>/', views.subcategory, name="subcategory"),
    path('categories/<int:category_pk>/subcategory/<int:subcategory_pk>/posts/new', views.post_new, name="post_new"),
    path('categories/<int:category_pk>/subcategory/<int:subcategory_pk>/posts/<int:post_pk>/', views.post, name="post"),
    path('categories/<int:category_pk>/subcategory/<int:subcategory_pk>/posts/<int:post_pk>/edit', views.post_edit, name="post_edit"),
    

]