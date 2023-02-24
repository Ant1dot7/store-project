from .models import Basket


# чтобы работало нужно подключить это в settings - templates
def baskets(request):
    user = request.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else []}
