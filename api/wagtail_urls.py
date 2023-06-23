from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet

from api.views import WagtailPagesAPIView


router = WagtailAPIRouter('wagtail_api')
router.register_endpoint('pages', WagtailPagesAPIView)
router.register_endpoint('images', ImagesAPIViewSet)
router.register_endpoint('documents', DocumentsAPIViewSet)
