from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


from app.forms import ItemForm
from app.models import itemmodel





# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = itemmodel.Item
    form_class = ItemForm
    success_url = reverse_lazy('index')
