from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1><a href = "https://fast.com/">fast</a></h1><br>'
                        '<h1><a href = "https://www.facebook.com/">facebook</a></h1><br>'
                        '<h1><a href = "https://www.youtube.com/">youtube</a></h1><br>'
                        '<h1><a href = "http://google.com/">google</a></h1><br>'
                        '<h1><a href = "https://open.spotify.com/collection/tracks">spotify</a></h1><br>')