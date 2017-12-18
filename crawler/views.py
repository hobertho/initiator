from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import traceback
import cfscrape
import json
from bs4 import BeautifulSoup
from django.core.cache import cache
import datetime

HEAD_KEY = 'head_key'
BODY_KEY = 'body_key'


def index(request):
    link = request.GET.get('link', None)
    if link == None:
        response_code = 422
        response_message = "Link parameter not provided"
        return JsonResponse({'code': response_code, 'message': response_message}, status= response_code)
    else:
        response_code = 200
        scraper = cfscrape.create_scraper()

        if (cache.get(HEAD_KEY + "_" + link, None) == None) or (cache.get(BODY_KEY + "_" + link, None) == None):
            print('step 1')
            soup = BeautifulSoup(scraper.get(link).content, "lxml")
            head_message = str(soup.find('head'))
            body_message = str(soup.find('body'))
            cache.set(HEAD_KEY + "_" + link, head_message, datetime.timedelta(hours= 12).total_seconds())
            cache.set(BODY_KEY + "_" + link, body_message, datetime.timedelta(hours= 12).total_seconds())
        else:
            print('step 2')
            head_message = cache.get(HEAD_KEY + "_" + link)
            body_message = cache.get(BODY_KEY + "_" + link)


        return JsonResponse({'code': response_code, 'head_message': head_message, 'body_message': body_message}, status= response_code)
