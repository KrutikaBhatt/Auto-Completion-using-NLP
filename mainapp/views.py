from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
import pickle
# Create your views here.

def homepage(request):
    initial_value={
        'smooth_num':1.00,
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
            tokenized = sentence.split(' ')
            print(tokenized)
            suggestions = get_suggestions(tokenized,start_letter,smooth_factor)
            print(suggestions)
    if err:
        mesg = err
        mesg_class='is-danger'
    else:
        mesg = "Your Predictions"
        mesg_class='is-success'
    return render(request, 'home.html',{'forms':form})

def get_suggestions(tokenized,start_letter,smooth_factor):
    n_gram_list = pickle.load(open('C:/Users/User/auto_completion/auto_completion/mainapp/data/en_counts.txt', 'rb'))
    vocabulary = pickle.load(open('C:/Users/User/auto_completion/auto_completion/mainapp/data/vocab.txt', 'rb'))
    suggestions = get_predictions(tokenized,n_gram_list,vocabulary,k=smooth_factor,start_with=start_letter)
    return suggestions

def get_predictions(tokens,n_gram_list,vocab,k=1.0,start_with=None):
    count = len(n_gram_list)
    print("In get predictions :")
    suggest =[]
    for i in range(count-1):
        n_gram_counts = n_gram_list[i]
        nplus1_gram_count = n_gram_list[i+1]

        suggestions = auto_complete(tokens, n_gram_counts,nplus1_gram_count, vocab,k=k, start_with=start_with)
        suggest.append(suggestions)

    return suggest

def auto_complete(previous_token,n_gram_count,nplus1_gram_count,vocab,k=1.0,start_with=None):
    n  = len(list(n_gram_count.keys())[0])
    previous_n_gram = previous_token[-n:]
    probablities = probs(previous_n_gram,n_gram_count,nplus1_gram_count,vocab,k=k)

    suggestions = None
    max_prob =0

    for word,prob in probablities.items():
        if start_with!=None:
            if not word.startswith(start_with):
                continue

        if prob>max_prob:
            suggestions = word
            max_prob = prob

    print("Auto Completion function done")
    return suggestions,max_prob

def probs(previous_n_gram,n_gram_count,nplus1_gram_count,vocab,k=1.0) ->'dict':
    previous_n_gram = tuple(previous_n_gram)
    vocab = vocab + ["<e>", "<unk>"]
    vocab_size = len(vocab)
    probablities ={}
    for word in vocab:
        probab = get_single_probablity(word,previous_n_gram,n_gram_count,nplus1_gram_count,vocab_size,k=k)
        probablities[word] = probab
    
    print("The Probs function done")
    return probablities

def get_single_probablity(word,previous_n_gram,n_gram_count,nplus1_gram_count,vocab_size,k=1.00) -> 'float':
    previous_n_gram = tuple(previous_n_gram)
    previous_n_gram_count = n_gram_count[previous_n_gram] if previous_n_gram in n_gram_count else 0

    #Denominator
    denom = previous_n_gram_count + k*vocab_size

    nplus1_gram = previous_n_gram +(word,)

    nplus1_gram_count = nplus1_gram_count[nplus1_gram] if nplus1_gram in nplus1_gram_count else 0

    #Numerator
    numerator = nplus1_gram_count + k

    return (numerator/denom)
