from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .generateurs.excel import export_paiements_excel
from .generateurs.pdf import export_paiements_pdf
from datetime import date

@login_required
def index_rapports(request):
    return render(request, 'rapports/index.html')

@login_required
def rapport_excel(request):
    d1 = request.GET.get('debut')
    d2 = request.GET.get('fin')
    return export_paiements_excel(d1, d2)

@login_required
def rapport_pdf(request):
    d1 = request.GET.get('debut')
    d2 = request.GET.get('fin')
    return export_paiements_pdf(d1, d2)
