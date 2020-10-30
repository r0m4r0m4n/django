from django.db import models
from django.shortcuts import reverse
from datetime import datetime
from django.utils.text import slugify
from phone_field import PhoneField


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-created_at-' + slugify(datetime.now().strftime("%m-%d-%Y, %H-%M"))


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Название товара:")
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True, )
    photo = models.ImageField(upload_to='photo/', blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='Product', verbose_name="Тэги товара:")
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('product_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
        return

    def photo_of_title(self):
        return self.photo.__format__('photo/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    name = models.CharField(max_length=150)
    product = models.ManyToManyField('Product',  related_name='order')
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    delivery_address = models.CharField(max_length=50)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def get_update_url(self):
        return reverse('order_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('order_delete_url', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('order_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)
        return

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_of_creation']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


