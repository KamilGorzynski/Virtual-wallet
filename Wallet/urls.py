from django.contrib import admin
from django.urls import path


from django.conf.urls import url, include
from rest_framework import routers
from wallets.views import UserViewSet, GroupViewSet, WalletViewSet
# from credits.views import CreditViewSet, OfferAvgRateViewSet
from transfers.views import TransferViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'wallets', WalletViewSet, basename='wallets')
# router.register(r'credits', CreditViewSet, basename='credits')
# router.register(r'offer_rate', OfferAvgRateViewSet, basename='avg_rate')
router.register(r'transfers', TransferViewSet, basename='transfers')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
