from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from pythonsdk.lib.meli import Meli
from .models import Sucursal
import json

def login(request):
    meli = Meli(client_id=8741598323122588, client_secret="cuaIibeYZPRVaCy7alSIqF4QhgTHqlsf")
    redirectUrl = meli.auth_url(redirect_URI='http://localhost:8000/redirect')
    response = HttpResponseRedirect(redirectUrl)
    return response

def redirect(request):
    code = request.GET.get('code')
    context = {
        'creado': True
    }
    meli = Meli(client_id=8741598323122588, client_secret="cuaIibeYZPRVaCy7alSIqF4QhgTHqlsf")
    meli.authorize(code=code, redirect_URI='http://localhost:8000/redirect')
    sucursal = Sucursal.objects.get(nom="Kia Zamora")
    sucursal.meli_token = meli.access_token
    sucursal.meli_refresh_token = meli.refresh_token
    sucursal.expiration_token_date = meli.expires_in
    sucursal.save(update_fields=['meli_token','meli_refresh_token','expiration_token_date'])
    
    return render(request, 'redirect.html', context)
