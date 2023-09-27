from django.urls import path
from main.views import show_main, create_product, show_xml, show_json
from main.views import register
from main.views import logout_user
from main.views import login_user
from main.views import edit_product
from main.views import delete_product
app_name = 'main'

urlpatterns = [
    path('delete/<int:id>', delete_product, name='delete_product'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml'), 
    path('create-product', create_product, name='create_product'),
    path('', show_main, name='show_main'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
]