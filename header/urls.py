
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    # path('blog/', BlogView.as_view(), name='blog'),
    # path('contact/', ContactView.as_view(), name='contact'),
    # path('product/', Product_List.as_view(), name = 'product'),
    # path('about/<slug:slug>', Product_Detail.as_view(), name='about'),
    # path('cont_info/', cont_info, name = 'cont_info'),
    # path('review/<int:pk>/<slug:slug>/', Review_Create.as_view(), name='review'),
    # path('product_det/', product_det, name='product_det'),
    # path('add_to_card/<int:pk>/<slug:slug>/', add_to_card, name='add_to_card'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)