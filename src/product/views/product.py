from django.core.paginator import Paginator
from django.db.models import Q
from django.views import generic

from product.forms import ProductForm
from product.models import (Product, ProductVariant, ProductVariantPrice,
                            Variant)

# class BaseProductView(generic.View):
#     form_class = ProductForm
#     model = ProductVariantPrice
#     template_name = 'products/list.html'
#     success_url = 'products/list/'


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(generic.ListView):

    paginate_by = 2
    model = Product

    def get_queryset(self):
        #context_object_name = "data"
        #template_name = "products/list.html"
        filter_string = {}
        self.request.GET = self.request.GET.copy()
        for key in self.request.GET:
            if self.request.GET.get(key) not in ['','--Select A Variant--']:
                filter_string[key] = self.request.GET.get(key)
        print(filter_string)

        products = Product.objects.all()
        if "title" in filter_string:
            products = products.filter(title__contains = filter_string['title'])

        variants_prices_stocks = {}
        if "variant" not in filter_string:
            for i in products:
                variants_prices_stocks[i.id] = ProductVariantPrice.objects.filter(product_id = i.id)
        else:
            for i in products:
                variants_prices_stocks[i.id] = ProductVariantPrice.objects.filter(Q(product_id = i.id),Q(ProductVariant__variant_title = filter_string["variant"]))
        print(variants_prices_stocks)

        data = {"products": products, "variants_prices_stocks": variants_prices_stocks}

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['request'] = ''
        if self.request.GET:
            context['request'] = self.request.GET['title']
        return context
