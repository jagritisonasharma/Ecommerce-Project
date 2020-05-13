from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Review
from .forms import CreateReviewForm, CreateReviewModelForm
from products.models import Product
from django.views import View

# Create your views here.

class ReviewList(ListView):
    model = Review
    template_name = 'reviews/review-list.html'
    context_object_name='reviews'

def CreateReviewFBV(request):  
    if request.method == "GET": 
        # form = CreateReviewForm
        form = CreateReviewModelForm
        context = {
           'form': form
        }
        return render(request, 'reviews/create-review.html', context)
    
    if request.method == 'POST':
        # rating = request.POST.get('ratings')
        # headline =request.POST.get('headline')
        # review = request.POST.get('review')
        
        # id=request.POST.get('product')
        # item = Product.objects.get(id=id)
       
        # Review.objects.create(
        #     rating = rating,
        #     headline = headline,
        #     review = review,
        #     product = item,
        # )
        form = CreateReviewModelForm(request.POST)
        #model mentioned in meta
        form.save()
        return redirect('reviews: review-list')

class CreateReviewCBV(View):
    def get(self, request, *args, **kwargs):
        form = CreateReviewModelForm
        context = {
           'form': form
        }
        return render(request, 'reviews/create-review.html', context)
    
    def post(self, request, *args, **kwargs):
        form = CreateReviewModelForm(request.POST)
        form.save()
        return redirect('reviews:review-list')

    

class CreateReviewGBV(CreateView):
    model = Review
    fields = ['headline', 'review', 'rating', 'product']
    template_name = 'reviews/create-review.html'
    success_url=reverse_lazy('reviews:review-list')