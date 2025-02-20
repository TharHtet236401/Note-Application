from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.shortcuts import redirect
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

