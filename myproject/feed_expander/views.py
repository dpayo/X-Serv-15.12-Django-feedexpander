from django.shortcuts import render
import feedparser
from django.http import HttpResponse
# Create your views here.

def show_tweets(request,user):
    url="https://twitrss.me/twitter_user_to_rss/?user="+user
    salida="<html><body>"  
    dic = feedparser.parse(url)
    fila = 0
    for fila in [0,1,2,3,4]:
        salida += "<h1>"+dic.entries[fila].title+"\n\n"
    return HttpResponse(salida+"</body></html>")
