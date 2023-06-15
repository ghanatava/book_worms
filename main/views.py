from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import FormView
from main import forms,models

# Create your views here.
def index(request):
    return render(request,'main/home.html',{})

def about(request):
    return render(request,'main/about_us.html',{})

class ContactUsView(FormView):
    template_name="main/contact_form.html"
    form_class=forms.ContactForm
    success_url="/"

    def form_valid(self,form):
        form.send_mail()
        return super().form_valid(form)

def product_list(request,tag):
    if tag != 'all':
        tag = get_object_or_404(models.ProductTag, slug=tag)

    if tag and tag != 'all':
        products=models.Product.objects.active().filter(tags=tag)
    else:
        products = models.Product.objects.active()
        
    return render(request,'main/product_list.html',{'products':products})
