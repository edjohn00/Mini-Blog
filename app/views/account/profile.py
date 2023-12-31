from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from app.views.mixin import TemplateLocationMixin


class IndexView(LoginRequiredMixin, TemplateLocationMixin, generic.TemplateView):
    template_name = "index.html"
