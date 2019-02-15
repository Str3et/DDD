from django.urls import path
from adminapp.views import users, categories, products
from adminapp.controllers import user, category

app_name = 'adminapp'

urlpatterns = [
    # пользователи
    # path('users/index', users.index, name='users'),
    # path('users/create/', users.create, name='users_create'),
    # path('users/update/<int:id>', users.update, name='users_update'),
    # path('users/delete/<int:id>', users.delete, name='users_delete'),
    # path('users/read/<int:id>', users.read, name='users_read'),
    path('users/index', user.UserListView.as_view(), name='users'),
    path('users/create/', user.UserCreateView.as_view(), name='users_create'),
    path('users/read/<int:pk>', user.UserReadView.as_view(), name='users_read'),
    path('users/update/<int:pk>', user.UserUpdateView.as_view(), name='users_update'),
    path('users/delete/<int:pk>', user.UserDeleteView.as_view(), name='users_delete'),
    # категории
    path('categories/index/', category.UserCategoryListView.as_view(), name='categories'),
    path('categories/create/', categories.create, name='category_create'),
    path('categories/read/<int:id>', categories.read, name='category_read'),
    path('categories/update/<int:id>', categories.update, name='category_update'),
    path('categories/delete/<int:id>', categories.delete, name='category_delete'),

    # продукты
    path('products/create/', products.create, name='product_create'),
    path('products/read/<int:id>', products.read, name='product_read'),
    path('products/list/<int:category>', products.list_by_category, name='product_category'),
    path('products/update/<int:id>', products.update, name='product_update'),
    path('products/delete/<int:id>', products.delete, name='product_delete'),
]
