from django.shortcuts import render
from django.views import generic
from django.db.models import Count

from .models import ScholarshipInfo

def index(request):
    universidade_list = ScholarshipInfo.objects \
        .values('nm_instituicao_ensino_superior') \
        .annotate(dcount=Count('nm_instituicao_ensino_superior')) \
        .order_by('nm_instituicao_ensino_superior')

    programa_list = ScholarshipInfo.objects \
        .values('nm_programa') \
        .annotate(dcount=Count('nm_programa')) \
        .order_by('nm_programa')

    ano_list = ScholarshipInfo.objects \
        .values('vl_ano') \
        .annotate(dcount=Count('vl_ano')) \
        .order_by('vl_ano')

    kwargs = {
    }

    universidade = request.POST.get('universidade')
    if universidade == "" or universidade is None:
       universidade = None
    else:
        kwargs['nm_instituicao_ensino_superior'] = universidade

    ano = request.POST.get('ano')
    if ano == "" or ano is None:
       ano = None
    else:
        kwargs['vl_ano'] = ano

    programa = request.POST.get('programa')
    if programa == "" or programa is None:
        programa = None
    else:
        kwargs['nm_programa'] = programa

    bolsa_estudo_list = list()

    context = {'universidade_list': universidade_list, \
               'ano_list': ano_list, \
               'programa_list': programa_list, \
               'universidade': universidade, \
               'ano': ano, \
               'programa': programa}

    if universidade is not None or \
            ano is not None or \
            programa is not None:

        bolsa_estudo_list = ScholarshipInfo.objects \
            .filter(**kwargs) \
            .order_by('vl_ano', 'nm_instituicao_ensino_superior', 'nm_programa', 'nm_programa_fomento', 'nm_area_conhecimento')
    else:
        pesquisar = request.POST.get('pesquisar')
        if pesquisar == "":
            context['error_message'] = "Selecione pelo menos um filtro para realizar pesquisa"

    context['bolsa_estudo_list'] = bolsa_estudo_list
    return render(request, 'pages/index.html', context)