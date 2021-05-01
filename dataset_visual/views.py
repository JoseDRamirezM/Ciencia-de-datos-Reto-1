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
                   'df': util.get_df_html()})


def render_query(request):
    if request.method == 'POST':
        queries_no_params = ["query_estado_general",
                             "query_estado_por_departamento", "query_pais_viajado_por_departamento"]

        query = request.POST["query_type"]
        if (query in queries_no_params):
            i = queries_no_params.index(query)
            if (i == 0):
                return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                          'df': util.query_estado_general()})
            elif (i == 1):
                return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                          'df': util.query_estado_por_departamento()})
            else:
                return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                          'df': util.query_pais_viajado_por_departamento()})
    else:
        index(request)


def query_params(request):
    if request.method == 'POST':
        queries_params = ["query_estado_general_departamento"]
        departamento = request.POST['departamento']
        return render(request, "dataset_visual/visualizar.html", {'dates': util.get_date_limits(util.get_df()),
                                                                  'df': util.query_estado_general_departamento(departamento)})

    else:
        return index(request)
