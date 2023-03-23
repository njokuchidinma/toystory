"""toyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from toystory.views import Index, About, Blog, Cart, Checkout, Compare, Contact, Login, Myaccount, UserFormView, Shop, Singleproduct, Wishlist, Faq, BlogDS, BlogD, BlogLS, BlogRS, Error, ShopLS, ShopRS, ShopLLS, ShopLRS, ShopLF, SP, SPA, SPGL, SPGR, SPG, SPN, SPSale, SPS, SPSL, SPSR, SPTSL, SPTSR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('blog/', Blog.as_view(), name='blog'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('compare/', Compare.as_view(), name='compare'),
    path('contact/', Contact.as_view(), name='contact'),
    path('login/', Login.as_view(), name='login'),
    path('my-account/', Myaccount.as_view(), name='my-account'),
    path('register/', UserFormView.as_view(), name='register'),
    path('shop/', Shop.as_view(), name='shop'),
    path('single-product/', Singleproduct.as_view(), name='single-product'),
    path('wishlist/', Wishlist.as_view(), name='wishlist'),
    path('faq/', Faq.as_view(), name='faq'),
    path('blog-details-sidebar/', BlogDS.as_view(), name='blog-details-sidebar'),
    path('blog-details/', BlogD.as_view(), name='blog-details'),
    path('blog-left-sidebar/', BlogLS.as_view(), name='blog-left-sidebar'),
    path('blog-right-sidebar/', BlogRS.as_view(), name='blog-right-sidebar'),
    path('error-404/', Error.as_view(), name='error-404'),
    path('shop-left-sidebar/', ShopLS.as_view(), name='shop-left-sidebar'),
    path('shop-list-fullwidth/', ShopLF.as_view(), name='shop-list-fullwidth'),
    path('shop-list-left-sidebar/', ShopLLS.as_view(), name='shop-list-left-sidebar'),
    path('shop-list-right-sidebar/', ShopLRS.as_view(), name='shop-list-right-sidebar'),
    path('shop-right-sidebar/', ShopRS.as_view(), name='shop-right-sidebar'),
    path('single-product-2/', SP.as_view(), name='single-product-2'),
    path('single-product-affiliate/', SPA.as_view(), name='single-product-affiliate'),
    path('single-product-gallery-left/', SPGL.as_view(), name='single-product-gallery-left'),
    path('single-product-gallery-right/', SPGR.as_view(), name='single-product-gallery-right'),
    path('single-product-group/', SPG.as_view(), name='single-product-group'),
    path('single-product-normal/', SPN.as_view(), name='single-product-normal'),
    path('single-product-sale/', SPSale.as_view(), name='single-product-sale'),
    path('single-product-slider/', SPS.as_view(), name='single-product-slider'),
    path('single-product-sticky-left/', SPSL.as_view(), name='single-product-sticky-left'),
    path('single-product-sticky-right/', SPSR.as_view(), name='single-product-sticky-right'),
    path('single-product-tab-style-left/', SPTSL.as_view(), name='single-product-tab-style-left'),
    path('single-product-tab-style-right/', SPTSR.as_view(), name='single-product-tab-style-right'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
