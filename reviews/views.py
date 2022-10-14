from django.shortcuts import render, redirect

import reviews
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def create(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")

    else:
        form = ReviewForm()

    context={
        'form':form
    }
    return render(request,'reviews/create.html',context)

def index(request):
    
    review = Review.objects.order_by('pk')

    context = {
        'review':review
    }   

    return render(request,'reviews/index.html',context)

def detail(request,pk):

    review = Review.objects.get(pk=pk)

    context = {
        'review' : review
    }

    return render(request,'reviews/detail.html', context)

def update(request,pk):
    review = Review.objects.get(pk=pk)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:detail", review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context={
        "review":review,
        'review_form' : review_form,
    }

    return render(request,'reviews/update.html',context)