from django.http import HttpResponse
from django.template.loader import render_to_string
from apps.paiements.models import Paiement

def export_paiements_pdf(date_debut=None, date_fin=None):
    qs = Paiement.objects.select_related('moto').order_by('-date')
    if date_debut:
        qs = qs.filter(date__gte=date_debut)
    if date_fin:
        qs = qs.filter(date__lte=date_fin)

    paiements = list(qs)
    total_attendu = sum(p.montant_attendu for p in paiements)
    total = sum(p.montant_verse for p in paiements)
    total_manque = sum(p.manque_a_gagner() for p in paiements)

    html = render_to_string('rapports/pdf_paiements.html', {
        'paiements': paiements,
        'total_attendu': total_attendu,
        'total': total,
        'total_manque': total_manque,
        'date_debut': date_debut,
        'date_fin': date_fin,
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport_paiements.pdf"'

    try:
        from xhtml2pdf import pisa
        pisa.CreatePDF(html, dest=response)
    except ImportError:
        response = HttpResponse(html, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="rapport_paiements.html"'

    return response
