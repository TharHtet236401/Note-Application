from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Note
from .forms import NoteForm
from django.shortcuts import redirect
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
# Create your views here.
def home(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'base/home.html', context)


def edit_note(request, pk):
    note = Note.objects.get(id=pk)
    print(note)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/edit-form.html', context)

def get_note_detail(request, pk):
    try:
        note = Note.objects.get(id=pk)
        data = {
            'title': note.title,
            'content': note.content,
            'author': note.author.username,
            'created_at': note.created_at.strftime("%b %d, %Y"),
            'updated_at': note.updated_at.strftime("%b %d, %Y")
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

