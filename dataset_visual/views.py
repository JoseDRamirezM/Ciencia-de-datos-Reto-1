from django.shortcuts import render
from django.urls import path
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from . import util


# Create your views here.

def index(request):
    return render(request, "dataset_visual/visualizar.html",
                  {'dates': util.get_date_limits(util.get_df()),
                   'df': util.query_pais_viajado_por_departamento()})
