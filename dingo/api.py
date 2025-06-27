from rest_framework import routers
from posts import api_views as posts_views

router = routers.DefaultRouter()
router.register('posts', posts_views.PostViewset)