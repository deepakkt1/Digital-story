from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView
from contacts.models import Contact
from django.views.generic import DeleteView
from django.views.generic import DetailView
import forms

class ListContactView(ListView):

    model = Contact
    template_name = 'contact_list.html'
    fields = '__all__'

class SubmissionView(ListView):

    model = Contact
    template_name = 'submission-done.html'
    fields = '__all__'

class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm


    def get_success_url(self):
        return ('submission')

    def get_context_data(self, **kwargs):

        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')

        return context

class UpdateContactView(UpdateView):
    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm
    def get_success_url(self):
        return reverse('contacts-list')
    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('contacts-list')

class ContactView(DetailView):

    model = Contact
    template_name = 'contact.html'
