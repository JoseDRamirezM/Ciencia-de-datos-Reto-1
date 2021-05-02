from django.shortcuts import render
from django.urls import path
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from . import util


# Create your views here.
registros = 1000


def index(request):
    return render(request, "dataset_visual/visualizar.html",
                  {'dates': util.get_date_limits(util.get_df()),
                   'df': util.get_df_html(), 'tipo_contagio': util.get_tipo_contagio()})


def render_query(request):
    if request.method == 'POST':
        queries_no_params = ["query_estado_general",
                             "query_estado_por_departamento", "query_pais_viajado_por_departamento"]

        query = request.POST["query_type"]
        if (query in queries_no_params):
            i = queries_no_params.index(query)
            if (i == 0):
                return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                          'df': util.query_estado_general(), 'tipo_contagio': util.get_tipo_contagio()})
            elif (i == 1):
                return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                          'df': util.query_estado_por_departamento(), 'tipo_contagio': util.get_tipo_contagio()})
            else:
                return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                          'df': util.query_pais_viajado_por_departamento(), 'tipo_contagio': util.get_tipo_contagio()})
    else:
        index(request)


def query_params_1(request):
    if request.method == 'POST':
        departamento = request.POST['departamento']
        return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                  'df': util.query_estado_general_departamento(departamento),
                                                                  'tipo_contagio': util.get_tipo_contagio()})

    else:
        return index(request)


def query_params_2(request):
    if request.method == 'POST':
        tipo_contagio = request.POST["tipo_contagio"]
        departamento = request.POST["departamento"]
        return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                  'df': util.query_tipo_de_contagio_en_departamento(tipo_contagio, departamento),
                                                                  'tipo_contagio': util.get_tipo_contagio()})
    else:
        return index(request)


def query_params_3(request):
    if request.method == 'POST':
        tipo_contagio = request.POST["tipo_contagio"]
        return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                  'df': util.query_tipo_de_contagio_por_departamento(tipo_contagio),
                                                                  'tipo_contagio': util.get_tipo_contagio()})
    else:
        return index(request)
