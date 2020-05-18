from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from app.models import itemmodel




# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = itemmodel.Item
    success_url = reverse_lazy('index')
