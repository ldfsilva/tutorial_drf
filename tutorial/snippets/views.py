from tutorial.snippets.models import Snippet
from tutorial.snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
