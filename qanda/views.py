from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(max_length=255)

def index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            return render_to_response('qanda/answers.html', {})
    else:
        form = QuestionForm()
    
    return render_to_response('qanda/index.html', {'form': form})
