from django.shortcuts import render
from django.http import HttpResponse
from myapp import forms
def index(request):
	var=forms.frm(request.POST)
	if var.is_valid():
		var.save(commit=True)
	dic={'key':var}
	return render(request,'myapp/index.html',context=dic)
def relative(request):
	return render(request,'myapp/relative.html')
# Create your views here.
