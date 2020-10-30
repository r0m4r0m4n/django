from django.views.generic import View
from .utils import ObjectCreateMixin, ObjectDetailMixin, ObjectDeleteMixin, ObjectUpdateMixin, render
from .forms import TagForm, ProductForm, OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Product, Tag, Order
from django.shortcuts import render


def product_list(request):
    posts = Product.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'shop/index.html', context=context)


def order_list(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'shop/order/orders_list.html', context=context)


class ProductDetail(ObjectDetailMixin, View):
    model = Product
    template = 'shop/product/product_detail.html'


class ProductCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = ProductForm
    template = 'shop/product/product_create_form.html'
    raise_exception = True


class ProductUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Product
    model_form = ProductForm
    template = 'shop/product/product_update_form.html'
    raise_exception = True


class ProductDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Product
    template = 'shop/product/product_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'shop/tag/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'shop/tag/tag_create_form.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'shop/tag/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'shop/tag/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'shop/tag/tags_list.html', context={'tags': tags})


class OrderCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = OrderForm
    template = 'shop/order/order_create_form.html'
    raise_exception = True


class OrderDetail(ObjectDetailMixin, View):
    model = Order
    template = 'shop/order/order_detail.html'


class OrderUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Order
    model_form = OrderForm
    template = 'shop/order/order_update_form.html'
    raise_exception = True


class OrderDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Order
    template = 'shop/order/order_delete_form.html'
    redirect_url = 'order_list_url'
    raise_exception = True
