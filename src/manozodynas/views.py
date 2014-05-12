from django.shortcuts import render
from manozodynas.models import Word
from django.views.generic import CreateView

class NaujasZodis(CreateView):
	model = Word
	success_url = '/zodziai'
	template_name = 'manozodynas/zodis.html'

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def zodziai_view(request):
    zodziai = Word.objects.all()
    return render(request, 'manozodynas/zodziai.html', {'zodziai': zodziai})

#def zodis_view(request):
#	 zodis = ""
#    return render(request, 'manozodynas/zodis.html', {'zodis': zodis})