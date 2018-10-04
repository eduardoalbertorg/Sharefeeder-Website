"""
ome Web frameworks such as Rails provide functionality for automatically determining
how the URLs for an application should be mapped to the logic that deals with
handling incoming requests. Router automatically create such request on it’s own.
Moreover create a common file for all the routers for various apps to handle api’s easily.
"""

from rest_framework import routers
from feeder.viewsets import UserViewSet, CredentialViewSet, FeederViewSet, GalileoViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'credential', CredentialViewSet)
router.register(r'feeder', FeederViewSet)
router.register(r'galileo', GalileoViewSet)

