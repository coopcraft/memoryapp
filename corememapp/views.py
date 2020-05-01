from django.shortcuts import render
from corememapp.models import Memory, Author
# from audios.models import Audio, Author

def index(request):
    num_memories = Memory.objects.all().count()
    num_authors = Author.objects.all().count()

    context = {
        'num_memories': num_memories,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

def rjc(request):
    return render(request, 'rjc.html')

def klc(request):
    return render(request, 'klc.html')