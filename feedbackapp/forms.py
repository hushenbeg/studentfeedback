from django import forms
from django.core import validators

# def starts_with_h(value):
#     if value[0].lower()!= 'h':
#         raise forms.ValidationError('Name should be starts with h | H')

class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget = forms.Textarea)

    def clean(self):
        print("Total form validation....")
        total_cleaned_data = super().clean()
        input_name = total_cleaned_data['name']
        if input_name[0].lower()!='h':
            raise forms.ValidationError('Name Parameters should starts with h')

        input_rollno = total_cleaned_data['rollno']

        if input_rollno <= 0:

            raise forms.ValidationError('rollno should be Greater than 0')
        
        input_email = total_cleaned_data['email']

        if 'gmail.com' not in input_email:
            raise forms.ValidationError("The email domain should be contains gmail.com")
        
        input_feedback = total_cleaned_data['feedback']

        if len(input_feedback) <= 10:
            raise forms.ValidationError("The feedback content length should be greater than 10 character")

        


    # def clean_name(self):
    #     print('validating name')
    #     input_name = self.cleaned_data['name']
    #     print(len(input_name))
    #     if len(input_name) < 4:
    #         raise forms.ValidationError('The Minimum no of characters in the name field should be 4')
    #     return input_name+'durga'
    # def clean_rollno(self):
    #     print('validating rollno')
    #     input_rollno = self.cleaned_data['rollno']
    #     return input_rollno
    
    # def clean_email(self):
    #     print('validating email')
    #     input_email = self.cleaned_data['email']
    #     if '@' not in input_email:
    #         raise forms.ValidationError('The email should contains "@" symbol')
    #     return input_email
    
    # def clean_feedback(self):
    #     print('Validating feedback field')
    #     input_feedback = self.cleaned_data['feedback']
    #     return input_feedback

class SignupForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label='Reenter Password', widget= forms.PasswordInput)
    email = forms.EmailField()

    def clean(self):
        total_cleaned_data = super().clean()
        pwd = total_cleaned_data['password']
        repwd = total_cleaned_data['repassword']
        if pwd != repwd:
            raise forms.ValidationError('Both Passwords must be same')
