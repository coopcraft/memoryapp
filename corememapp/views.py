from django.shortcuts import render, get_object_or_404
from corememapp.models import Memory, Author

def memory_list(request):
    num_memories = Memory.objects.all().count()
    num_authors = Author.objects.all().count()
    memories = Memory.objects.all()

    context = {
        'num_memories': num_memories,
        'num_authors': num_authors,
        'memories': memories,
    }

    return render(request, 'index.html', context=context)

def memory_detail(request, pk):
    memory = get_object_or_404(Memory, pk=pk)
    return render(request, 'memory_detail.html', {'memory': memory})

def rjc(request):
    return render(request, 'rjc.html')

def klc(request):
    return render(request, 'klc.html')

def lac(request):
    memories = Memory.objects.all()
    return render(request, 'lac.html', {'memories': memories})