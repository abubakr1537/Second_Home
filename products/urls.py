from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.create, name='create'),
	path('<int:product_id>', views.detail, name='detail'),
	path('user_room', views.user_room, name='userroom'),
	path('<int:product_id>/delete', views.delete, name='delete'),
	path('<int:product_id>/modify', views.modify, name='modify'),
]