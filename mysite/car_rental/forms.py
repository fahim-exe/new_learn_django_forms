from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
# 
#     first_name = forms.CharField(label='First Name', max_length=40)
#     last_name = forms.CharField(label='Last Name', max_length=40)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please Write your review', widget=forms.Textarea(attrs={'class':'myform', 'rows':'2', 'cols':'2 '}))
# 
# 


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        
        fields = "__all__" #pass in all the model fields as form fields

        labels = {
            'first_name': "YOUR FIRST NAME",
            'last_name': "YOUR LAST NAME",
            'stars':"RVIEW RATING ON SCALE 5"
        }

        error_messages = {

            'stars':{
                'min_value':'Yo!! Min value is 1',
                'max_value':'Yo!! Max Value is 5'
            }

        }