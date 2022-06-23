from django.http import HttpResponse, HttpResponseRedirect
from notes.forms import NotesForm
from .models import Notes
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesDeleteView(DeleteView):
    model = Notes
    template_name = "notes/notes_delete.html"
    success_url = "/smart/notes"

# def detail(request, pk):
#     try:
#         current_note = Notes.objects.get(pk = pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist.  Please try another query.")
#     return render(request, 'notes/notes_detail.html', {'note': current_note})