# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
import pandas as pd
from django.template import loader
from django.http import HttpResponse
import requests

class SearchView(APIView):
    def get(self, request):
        word = request.GET.get('word',None)
        dataframe = pd.read_csv('./word_search.tsv', sep='\t', header=None)
        dataframe['index'] = dataframe[0].str.find(word)
        dataframe['len'] = dataframe[0].str.len()
        result_words = list(dataframe.loc[dataframe['index'] != -1].sort_values(by=["index", "len", 1],
                                                                 ascending=[True, True, False]).head(25)[0].dropna())
        return JsonResponse({"words": result_words})

def index(request):
    template = loader.get_template('index.html')
    context = {}
    if request.GET.get('word'):
        res = requests.get(url='http://onfullthrottle.herokuapp.com/search', params={'word': request.GET.get('word')})
        count = 0
        while res.status_code != 200:
            res = requests.get(url='http://onfullthrottle.herokuapp.com/search', params={'word': request.GET.get('word')})
            print("Retrying : " + str(count))
            if count > 30:
                return JsonResponse({"Error": "Could not connect to the API. :("})
            count += 1

        context = { 'result_words' : res.json()["words"]}
    return HttpResponse(template.render(context, request))