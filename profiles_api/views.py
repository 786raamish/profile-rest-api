from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ TEST API VIEW """

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'Is similar to the tradional Django View',
            'Gives the most control over your appliction logic',
            'Is mapped manually to the URL\'s'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
