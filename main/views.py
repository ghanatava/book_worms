from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import FormView
from main import forms, models
from django.core.paginator import Paginator, EmptyPage

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


def product_list(request, tag):

    if tag != 'all':
        tag = get_object_or_404(models.ProductTag, slug=tag)

    if tag and tag != 'all':
        products=models.Product.objects.active().filter(tags__slug=tag)
    else:
        products = models.Product.objects.active()

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    return render(request, 'main/product_list.html', {
        'page_obj':page_obj,
        })


def product_detail(request, slug):
    product=get_object_or_404(models.Product,slug=slug)
    return render(request, 'main/product_detail.html', {
        'product':product,
    })


def add_to_basket(request):
    pass
