from django.shortcuts import render
from newsapi import NewsApiClient


#get key https://newsapi.org/register
def Index(request):
    your_key = "20694cd2f7cf40b4b920dcef50c9cd2e"
    newsapi = NewsApiClient(api_key=your_key)#"YOUR API KEY")
    try:
        topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')
        #topheadlines ={'articles':{0:{'title':'title1','description':'description1','urlToImage':'urlToImage1'}}}
        
    except:
        topheadlines ={'articles':{0:{'title':'title1','description':'description1','urlToImage':'urlToImage1'}}}

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'index.html', context={"mylist":mylist})



def bbc(request):

    your_key = "20694cd2f7cf40b4b920dcef50c9cd2e"
    newsapi = NewsApiClient(api_key=your_key)
    try:
        topheadlines = newsapi.get_top_headlines(sources='bbc-english')
    except:
        topheadlines ={'articles':{0:{'title':'title1','description':'description1','urlToImage':'urlToImage1'}}}

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'bbc.html', context={"mylist":mylist})
