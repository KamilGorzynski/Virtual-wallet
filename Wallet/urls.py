from django.contrib import admin
from django.urls import path


from django.conf.urls import url, include
from rest_framework import routers
from quickstart.views import UserViewSet, GroupViewSet, WalletViewSet
from credits.views import CreditViewSet, OfferAvgRateViewSet
from transfers.views import TransferViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'wallets', WalletViewSet, base_name='wallets')
router.register(r'credits', CreditViewSet, base_name='credits')
router.register(r'offer_rate', OfferAvgRateViewSet, base_name='avg_rate')
router.register(r'transfers', TransferViewSet, base_name='transfers')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
