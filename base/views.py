from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Note
from .forms import NoteForm
from django.shortcuts import redirect
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from utils.statusCodes import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

# Home View
def home(request):
    try:
        notes = Note.objects.all()
        context = {'notes': notes}
        return render(request, 'base/home.html', context)
    except Exception as e:
        return JsonResponse(
            {'error': str(e)}, 
            status=HTTP_500_INTERNAL_SERVER_ERROR
        )

# Edit Note View
def edit_note(request, pk):
    try:    
        note = Note.objects.get(id=pk)
        form = NoteForm(instance=note)
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'base/edit-form.html', context)
    except Note.DoesNotExist:
        return JsonResponse(
            {'error': 'Note not found'}, 
            status=HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return JsonResponse(
            {'error': str(e)}, 
            status=HTTP_500_INTERNAL_SERVER_ERROR
        )

# Get Note Detail View
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
        return JsonResponse(data, status=HTTP_200_OK)
    except Note.DoesNotExist:
        return JsonResponse(
            {'error': 'Note not found'}, 
            status=HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return JsonResponse(
            {'error': str(e)}, 
            status=HTTP_500_INTERNAL_SERVER_ERROR
        )

# Create Note View
def create_note(request):
    try:
        if request.method == 'POST':
            form = NoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.author = request.user
                note.save()
                return redirect('home')
        else:
            form = NoteForm()
        
        context = {'form': form}
        return render(request, 'base/create-form.html', context)
    except Exception as e:
        return JsonResponse(
            {'error': str(e)}, 
            status=HTTP_500_INTERNAL_SERVER_ERROR
        )

# Delete Note View
def delete_note(request, pk):
    try:
        note = Note.objects.get(id=pk)
        note.delete()
        return redirect('home')
    except Note.DoesNotExist:
        return JsonResponse(
            {'error': 'Note not found'}, 
            status=HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return JsonResponse(
            {'error': str(e)}, 
            status=HTTP_500_INTERNAL_SERVER_ERROR
        )
