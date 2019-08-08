from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def renderPdf(template, content={}):
    t = get_template(template)
    send_date = t.render(content)
    result = BytesIO()
    #data='json=1&task=post&board=test&thread=80980710&comment=тест'.encode('utf-8')
    pdf = pisa.pisaDocument(BytesIO(send_date.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return None