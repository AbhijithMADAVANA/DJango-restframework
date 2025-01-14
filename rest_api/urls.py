from django.urls import path,include
from .views import PostsView,posts_detail,PostAPIView,postdetailAPIView,genericApiView,PostViewSet

from rest_framework import routers

router=routers.SimpleRouter()
router.register('posts',PostViewSet,basename='posts')

urlpatterns = [
   # path('posts/',PostsView),
   # path('details/<int:pk>',posts_detail)
   
   # path('postsApiView/', PostAPIView.as_view()),
   # path('detailsApiView/<int:pk>',postdetailAPIView.as_view())

     path('genericApiView/<int:id>/',genericApiView.as_view()),
     
     path('',include(router.urls)),
]