from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
# Create your views here.

def homepage(request):
    initial_value={
        'smooth_num':0.01,
    }
    mesg=""
    mesg_class=""
    err=""
    form = InputForm(initial=initial_value)

    if request.method =='POST':
        form = InputForm(request.POST,initial=initial_value)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            smooth_factor = form.cleaned_data['smooth_num']
            start_letter = form.cleaned_data['start_letter']
            print(sentence+" "+start_letter)
            print(smooth_factor)

    if err:
        mesg = err
        mesg_class='is-danger'
    else:
        mesg = "Your Predictions"
        mesg_class='is-success'
    return render(request, 'home.html',{'forms':form})
