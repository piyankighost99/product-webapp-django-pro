from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product


class ProductDetailsView(TemplateView):
    template_name = "shop/details.html"

    def get(self, request):
        context = {}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))