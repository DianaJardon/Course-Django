from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from django.utils.datastructures import MultiValueDictKeyError


class PostApiWiew(APIView):
    def get(self, request):
       # posts = Post.objects.all()
        posts = [post.title for post in Post.objects.all()]
        return Response(status=status.HTTP_200_OK, data=posts)

    def post(self, request):
        Post.objects.create(title=request.POST.get('title', 'Sin titulo'), description=request.POST.get('description', 'sin description'),
                            order=request.POST.get('order'))

        return self.get(request)