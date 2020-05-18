from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.models import itemmodel




class ItemDetailView(LoginRequiredMixin, DetailView):
    model = itemmodel.Item