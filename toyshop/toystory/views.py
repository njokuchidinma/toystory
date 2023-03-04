from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = 'toystory/index.html'

class About(TemplateView):
    template_name = 'toystory/about.html'

class Cart(TemplateView):
    template_name = 'toystory/cart.html'

class Checkout(TemplateView):
    template_name = 'toystory/checkout.html'

class Contact(TemplateView):
    template_name = 'toystory/contact.html'

class Blog(TemplateView):
    template_name = 'toystory/blog.html'

class Compare(TemplateView):
    template_name = 'toystory/compare.html'

class Register(TemplateView):
    template_name = 'toystory/register.html'

class Myaccount(TemplateView):
    template_name = 'toystory/my-account.html'

class Shop(TemplateView):
    template_name = 'toystory/shop.html'

class Singleproduct(TemplateView):
    template_name = 'toystory/single-product.html'

class Wishlist(TemplateView):
    template_name = 'toystory/wishlist.html'

class Login(TemplateView):
    template_name = 'toystory/login.html'

class Faq(TemplateView):
    template_name = 'toystory/faq.html'

class BlogDS(TemplateView): 
    template_name = 'toystory/blog-details-sidebar.html'

class BlogD(TemplateView):
    template_name = 'toystory/blog-details.html'

class BlogLS(TemplateView):
    template_name = 'toystory/blog-left-sidebar.html'

class BlogRS(TemplateView):
    template_name = 'toystory/blog-right-sidebar.html'

class Error(TemplateView):
    template_name = 'toystory/error-404.html'

class ShopLS(TemplateView):
    template_name = 'toystory/shop-left-sidebar.html'

class ShopRS(TemplateView): 
    template_name = 'toystory/shop-right-sidebar.html'

class ShopLLS(TemplateView):
    template_name = 'toystory/shop-list-left-sidebar.html'

class ShopLRS(TemplateView):
    template_name = 'toystory/shop-list-right-sidebar.html'

class ShopLF(TemplateView):
    template_name = 'toystory/shop-list-fullwidth.html'

class SP(TemplateView):
    template_name = 'toystory/single-product-2.html'

class SPA(TemplateView):
    template_name = 'toystory/single-product-affiliate.html'

class SPGL(TemplateView):
    template_name = 'toystory/single-product-gallery-left.html'

class SPGR(TemplateView):
    template_name = 'toystory/single-product-gallery-right.html'

class SPG(TemplateView):
    template_name = 'toystory/single-product-group.html'

class SPN(TemplateView):
    template_name = 'toystory/single-product-normal.html' 

class SPSale(TemplateView): 
    template_name = 'toystory/single-product-sale.html'

class SPS(TemplateView):
    template_name = 'toystory/single-product-slider.html'

class SPSL(TemplateView):
    template_name = 'toystory/single-product-sticky-left.html'

class SPSR(TemplateView):
    template_name = 'toystory/single-product-sticky-right.html'

class SPTSL(TemplateView):
    template_name = 'toystory/single-product-tab-style-left.html'

class SPTSR(TemplateView):
    template_name = 'toystory/single-product-tab-style-right.html'