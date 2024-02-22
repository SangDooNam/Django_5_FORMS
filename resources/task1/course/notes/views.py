"""Views for the notes app."""
from django.template.loader import get_template
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View
from .forms import SearchForm, AddForm, EditForm
from django.shortcuts import render

from notes.models import NoteStore

store = NoteStore()
notes = store.get()


def redirect_to_note_detail(request, note_id):
    """Redirect to the note details view."""
    return redirect(reverse("notes:details", args=[note_id]))


def home(request):
    """Home for my notes app."""
    template = get_template("notes/home.html")
    context = {
        "title": "Welcome to my course notes!",
        "links": [
            {
                "url": reverse("notes:sections"),
                "label": "Check the list of sections"
            },
            {
                "url": reverse("notes:details", args=[1]),
                "label": "Read my first notes"
            },
            {
                "url": reverse("notes:search"),
                'label': "Search a note"
            },
            {
                "url": reverse('notes:add'),
                "label" : "Add a new note"
            }
            
        ]
    }
    return HttpResponse(template.render(context))


class SectionList(TemplateView):
    """List of sections."""

    template_name = "notes/sections.html"

    def get_context_data(self):
        """Return the list of sections."""
        return {
            "sections": ["Web Frameworks",
                         "Setting up Django",
                         "URL Mapping"]
            }


class NotesBySection(TemplateView):
    """Show the notes of a section."""

    template_name = "notes/by_section.html"

    def get_context_data(self, section_name):
        """Return the section name and the note list."""
        return {
            "section": section_name,
            "notes": _get_notes_by_section(section_name)
        }


def _get_notes_by_section(section_name):
    """Return the notes of a section."""
    notes = store.get()
    return [note for note in notes
            if note["section"] == section_name]


class SearchResultsView(TemplateView):
    """Execute the search and show results."""

    template_name = "notes/search.html"

    def get_context_data(self, search_term, select):
        """Return the term and list of notes."""
        notes = store.get()
        n = []
        for note in notes:
            if select == 'Any':
                n = notes
            elif select == note['section']:
                n.append(note)
                
        return {
            "notes": n,
            "term": search_term
        }


def search(request, search_term):
    """Show a list of all notes matching the search."""
    response = [
        f"<h1>Notes matching {search_term}</h1>",
        "<ol>"]
    response = response + _get_note_items_matching_search(search_term)
    response = response + [
        "</ol>",
        "<a href=\"", reverse("notes:home"), "\">Back to home</a>"
    ]
    return HttpResponse("".join(response))


class NoteDetails(TemplateView):
    """Note details."""
    
    template_name = "notes/details.html"
    def get_context_data(self, note_id):
        """Return the note data."""
        notes = store.get()
        edit = reverse('notes:edit', args=[note_id])
        return {
            "id": note_id,
            "num_notes": len(notes),
            "note": notes[note_id - 1],
            'edit': edit
        }


def _get_note_items_matching_search(search_term):
    """Return a list of items with notes marching the search."""
    notes = store.get()
    return [f"<li>{note['text']}</li>" for note in notes
            if search_term.lower() in note["text"].lower()]


class SearchView(View):
    
    def get(self, request):
        form = SearchForm(initial={'section':SearchForm.ANY})
        context = {
            'form' : form,
        }
        return render(
                    request, 
                    "notes/search_widget.html",
                    context= context,
                    )
        
    
    def post(self, request):
        
        form = SearchForm(request.POST)
        
        if form.is_valid():
            
            term_of_search = form.cleaned_data['term_of_search']
            
            select = form.cleaned_data['section']
            
            return redirect('notes:search_term', term_of_search, select)


class AddView(View):
    
    def get(self, request):
        
        form = AddForm()
        context = {
            'form': form,
            'form_name': 'AddForm',
        }
        return render(request, 'notes/common.html', context)
    
    
    def post(self, request):
        
        form = AddForm(request.POST)
        
        if form.is_valid():
            
            section = form.cleaned_data['section']
            text = form.cleaned_data['text']
            
            input_item = {
                        'text': text,
                        'section': section
                        }
            notes.append(input_item)
            # input_val = notes
            store.save(notes)
            another_note = reverse('notes:add')
            message = 'The note was added succesfully!'
            context = {
                'another_note': another_note,
                'message': message,
            }
            return render(request, 'notes/add_success.html', context)


class EditView(View):
    
    def get(self, request, note_id):
        
        section = notes[note_id-1]['section']
        text = notes[note_id-1]['text']
        
        form = EditForm(initial={
                                'section': section, 
                                'text': text, 'hidden_section': section,
                                'form_name': 'EditForm',
                                }
                                )
        return render(request, 'notes/common.html', {'form':form})
    
    
    def post(self, request, note_id):
        
        form = EditForm(request.POST)
        
        if form.is_valid():
            
            new_text = form.cleaned_data['text']
            
            notes[note_id-1]['text'] = new_text
            
            store.save(notes)
            
            return redirect('notes:details', note_id)
        
        else:
            return render(request, 'notes/edit.html', {'form':form})