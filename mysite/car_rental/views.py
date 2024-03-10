from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.


def rental_review(request):

    #if the user passes a post request >> Check form content >> if ok >> thank you page

    if request.method=="POST":
        form  = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect(reverse('car_rental:thankyou'))
    else:
        form =  ReviewForm()
        print("Here is the problem")
    return render(request, 'car_rental/rental_review.html', context={'form':form})


    #else render the form

    


def thankyou(request):


    return render(request, 'car_rental/thankyou.html')
