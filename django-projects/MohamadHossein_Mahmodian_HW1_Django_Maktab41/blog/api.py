from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import PostSerializer
from .models import Post


@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'Post':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_detail(request, pk):
    pass
    """
    Retrieve, update or delete a code snippet.
    """
    # try:
    #     snippet = Snippet.objects.get(pk=pk)
    # except Snippet.DoesNotExist:
    #     return HttpResponse(status=404)
    #
    # if request.method == 'GET':
    #     serializer = SnippetSerializer(snippet)
    #     return JsonResponse(serializer.data)
    #
    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(snippet, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)
    #
    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return HttpResponse(status=204)