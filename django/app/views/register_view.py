from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django_filters.views import FilterView

from app.forms import ItemForm
from app.models import itemmodel





# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = itemmodel.Item
    form_class = ItemForm
    success_url = reverse_lazy('index')
