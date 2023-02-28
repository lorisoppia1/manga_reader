from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bs4 import BeautifulSoup
import requests
from .models import Manga
class MangaAPI(APIView):

    def get(self, request):
        manga = Manga.objects.get(id=1)
        return render(request, 'manga/image_get.html',{'last':manga.last})
    
    def post(delf, request):
        images = []
        if 'chapter' in request.POST:
            capitolo = request.POST['chapter']
        else:
            if request.POST['which'] == 'prev':
                capitolo = str(int(request.POST['capitolo']) - 1)
            else:
                capitolo = str(int(request.POST['capitolo']) + 1)
        response = requests.get('https://www.mangaworld.so/manga/2744/the-breaker-new-waves/')
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.findAll('a', attrs={'class':'chap'})
        for el in elements:
            if capitolo in el['title']:
                url = el['href']
        url = url + '/1?style=list'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.findAll('img', attrs={'class':'page-image img-fluid'})
        for el in elements:
            images.append(el['src'])
        context = {'images':images,'capitolo':capitolo}
        manga = Manga.objects.get(id=1)
        manga.last = capitolo
        manga.save()
        return render(request,'manga/image_post.html',context)
    
class TestAPI(APIView):
    
    def get(self, request):
        return Response(status=status.HTTP_200_OK)