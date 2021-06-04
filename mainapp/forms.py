from django import forms

class InputForm(forms.Form):
    sentence = forms.CharField(required=True,max_length=100,min_length=5,widget= forms.TextInput(attrs={'class':'custom_textbox','id':'custom_textbox_id'}))
    smooth_num = forms.FloatField(required=False,max_value=1.00,min_value=0.01,widget=forms.NumberInput(attrs={'class':'form-control input-number','id':'k-smooth-input', 'step': "0.01"}))
    start_letter = forms.CharField(required=False,max_length=1,min_length=0,widget=forms.TextInput(attrs={'class':'custom_textbox'}))
    