from django.shortcuts import render

def index(request):
    num_memories = Memory.objects.all().count()
    num_authors = Memory.objects.all().count()

    context = {
        'num_memories': num_memories,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)
