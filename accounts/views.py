from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.


def redirect_to_3000(request,uid,token):
    print('http://localhost:3000/activate/'+uid+'/'+token)
    return redirect('http://localhost:3000/activate')