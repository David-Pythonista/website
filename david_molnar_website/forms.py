from django import forms

subjects = [('Contact','Contact'), ('Job offer','Job offer'),('Greetings','Greetings'), ('Photography','Photography'),('Information','Information')]


class ContactForm(forms.Form):

    name = forms.CharField(max_length=50, required=True, label='', widget=forms.TextInput(attrs={'class': 'name_field','placeholder': 'Your name.'}))
    email = forms.EmailField(required=True, label='', widget=forms.EmailInput(attrs={'class': 'email_field','placeholder': 'Your e-mail address.'}))
    subject = forms.ChoiceField(choices=subjects, required=True, label="Subject",widget=forms.Select(attrs={'class':'subject'}))
    message = forms.CharField(required=True, label='', widget=forms.Textarea(attrs={'class': 'message-box','placeholder': 'Write your message here...'}))