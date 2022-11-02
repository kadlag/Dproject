from django.views.generic import ListView
from .models import Product


class HomePageView(ListView):
    model = Product
    template_name = "home.html"
