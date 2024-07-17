from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.views.generic import FormView
from .forms import ContactFormModel, ContactForm
from .models import Contact

# Create your views here.
def exito(request):
    return render(request, 'exito.html', {})

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})

def contacto(request):
    if request.method =='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_form = Contact.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactForm()
        
    return render(request, 'contactform.html', {'form': form})

class ContactView(FormView):
    form_class = ContactFormModel
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("customer_email")
        subject = form.cleaned_data.get("customer_name")
        message = form.cleaned_data.get("message")

        return super(ContactView, self).form_valid(form)
    
    def post(self,request):
        form = ContactFormModel(request.POST)
        form.save()

        return redirect("/")
