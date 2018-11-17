from django import forms

class MessageForm_Form(forms.Form):

    name=forms.CharField(max_length=50, widget=forms.TextInput
                        (attrs={'class':'mes_form_input',
                                'name':'name',
                                'id':'name',
                                'placeholder':'Ф.И.О.',
                                'required':True}))

    telephone=forms.CharField(max_length=50, widget=forms.TextInput(
                            attrs={'class':'mes_form_input',
                                     'type':'text',
                                     'name':'telephone',
                                     'id':'phone',
                                     'placeholder':'+38 (___) ___-__-__',
                                     'required':True}))

    email=forms.EmailField(max_length=50, required=False, widget=forms.EmailInput(
                            attrs={'class':'mes_form_input',
                                     'type':'email',
                                     'id':'email',
                                     'placeholder':'Example@email.com'
                                     }))

    text_message = forms.CharField(widget=forms.Textarea(
                                attrs={'class': 'mes_form_area',
                                       'id': 'text_message',
                                       'placeholder': 'Ваше сообщение:',
                                       'required': True,
                                       'cols':'0',
                                       'rows':'0'}))

