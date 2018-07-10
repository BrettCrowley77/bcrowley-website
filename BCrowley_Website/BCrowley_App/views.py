from django.shortcuts import render
from BCrowley_App.models import Media, Inspiration

# Create your views here.
def index(request):
    return render(request, 'BCrowley_App/index.html')

def ideas(request):
    return render(request, 'BCrowley_App/ideas.html')

def inspiration(request):
    inspiration_records = Inspiration.objects.order_by('description')

    inspiration_dict = {'inspiration_list':inspiration_records,}
    return render(request, 'BCrowley_App/inspiration.html', context=inspiration_dict)

def lists(request):
    book_records = Media.objects.filter(med_type="BK").order_by('title')
    movie_records = Media.objects.filter(med_type="MV").order_by('title')
    music_records = Media.objects.filter(med_type="MS").order_by('title')
    article_records = Media.objects.filter(med_type="AT").order_by('title')

    media_dict = {'book_list':book_records, 'movie_list':movie_records, 'music_list':music_records, 'article_list':article_records}
    return render(request, 'BCrowley_App/lists.html', context=media_dict)

def projects(request):
    return render(request, 'BCrowley_App/projects.html')
