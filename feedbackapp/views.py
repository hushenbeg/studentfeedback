from django.shortcuts import render
from feedbackapp.forms import FeedBackForm, SignupForm

# Create your views here.

def feedback_view(request):
    form = FeedBackForm()
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printing information')
            print('Name:', form.cleaned_data['name'])
            print('Roll No:', form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:', form.cleaned_data['feedback'])
        
    return render(request, 'feedbackapp/feedback.html', {'form':form})

def sigup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print('Basic validation Completed and Printing data')
            print('Name :', form.cleaned_data['name'])
            print('password:', form.cleaned_data['password'])
            print('email:', form.cleaned_data['email'])
    
    return render(request, 'feedbackapp/signup.html', {'form':form})
