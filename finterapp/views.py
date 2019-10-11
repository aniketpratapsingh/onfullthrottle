# Create your views here.
#from rest_framework.response import JsonResponse
from rest_framework.views import APIView
from django.http import JsonResponse
import pandas as pd
from django.template import loader
from django.http import HttpResponse
from .models import WordsModel
from .serializers import WordsSerializer
import requests

class SearchView(APIView):
    def get(self, request):
        word = request.GET.get('word',None)
        #import pdb;pdb.set_trace()
        dataframe = pd.read_csv('./word_search.tsv', sep='\t', header=None)
        dataframe['index'] = dataframe[0].str.find(word)
        dataframe['len'] = dataframe[0].str.len()
        result_words = list(dataframe.loc[dataframe['index'] != -1].sort_values(by=["index", "len", 1],
                                                                 ascending=[True, True, False]).head(25)[0].dropna())
        #serializer = WordsSerializer(words, many=True)
        return JsonResponse({"words": result_words,'search': word})

def index(request):
    template = loader.get_template('index.html')
    context = {}
    #import pdb;pdb.set_trace()
    if request.GET.get('word'):
        res = requests.get(url='http://onfullthrottle.herokuapp.com/search', params={'word': request.GET.get('word')})
        context = { 'result_words' : res.json()["words"]}
        #return JsonResponse(res.json())

    return HttpResponse(template.render(context, request))