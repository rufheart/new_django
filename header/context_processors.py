from header.models import Detail_Product

def get_detail(request):
    context = {
        'dtls': Detail_Product.objects.all()    
    }
    return context   

