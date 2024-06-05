from django.contrib import admin
from .models import Products,Offer,Blog

class ProductAdmin(admin.ModelAdmin):
    list_display =('name','price','stock')


class OfferAdmin(admin.ModelAdmin):
    list_display=('code','description','discount')



class BlogAdmin(admin.ModelAdmin):
    list_display=('post','title','date','blogger')

admin.site.register(Products,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Blog,BlogAdmin)

