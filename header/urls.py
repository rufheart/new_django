
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index',IndexView.as_view(), name='index' ),
    path('product/', Product_View.as_view(), name='product'),
    path('product-detail/<slug:slug>/', ProductDetail_View.as_view(), name='productdetail'),
    path('review/<int:pk>/<slug:slug>/', ReviewCreate_View.as_view(), name='review'),
    path('blog/', BlogView.as_view(), name='blog'),
    # path('prduct-create/', product_create, name='product_create'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('product/', Product_List.as_view(), name = 'product'),
    # path('about/<slug:slug>', Product_Detail.as_view(), name='about'),
    path('cont_info/', ContInfo_View.as_view(), name = 'cont_info'),
    path('product-create/', ProductCreate_View.as_view(), name='productcreate'),
    path('add_to_card/<int:pk>/<slug:slug>/', Add_To_Card_View.as_view(), name='add_to_card'),
    path('export/', export, name='export'),
    path('subscribe/', SubscriberViews.as_view(),name='subscribe')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)