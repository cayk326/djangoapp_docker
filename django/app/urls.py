from django.urls import path
#from app.views import ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
'''
from app.views.searchlist_view import ItemFilterView
from app.views.detail_view import ItemDetailView
from app.views.register_view import ItemCreateView
from app.views.update_view import ItemUpdateView
from app.views.delete_view import ItemDeleteView
'''

from app.views import searchlist_view, detail_view,register_view,update_view,delete_view
searchlist_view.ItemFilterView

urlpatterns = [
    path('',  searchlist_view.ItemFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', detail_view.ItemDetailView.as_view(), name='detail'),
    path('create/', register_view.ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', update_view.ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_view.ItemDeleteView.as_view(), name='delete'),
]
