#####
# This file contains the views needed to generate pdf reports from html, using WeasyPrint
#####
import base64
import os
import tempfile

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.shortcuts import render

from Panacea.decorators import group_required
from Panacea.utilities import find_user_organization
from .models import cover_sheet, tax_rates, organization


@login_required(login_url='/Panacea/login')
@group_required('Summary reporter', 'WSDOT staff')
def cover_sheet_report(request, pdf=None):
    user_org = find_user_organization(request.user.id)
    org_cover_sheet = cover_sheet.objects.get(organization_id=user_org.id)
    agency_type = user_org.summary_organization_classifications.name
    print(agency_type)
    try:
        base64_logo = base64.encodebytes(org_cover_sheet.organization_logo).decode("utf-8")
    except:
        base64_logo = ""
    if agency_type != "Community provider" or agency_type != "Medicaid broker":
        tax_description, created = tax_rates.objects.get_or_create(organization_id=user_org.id)
        tax_description = tax_description.tax_rate_description
    if pdf == 'pdf':
        html_report = render_to_string('../templates/reports/cover_sheet.html', {'cover_sheet': org_cover_sheet,
                                                                                 'agency_type': agency_type,
                                                                                 'organization': user_org,
                                                                                 'tax_description': tax_description,
                                                                                 'base64_logo': base64_logo})
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=coversheet.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        HTML(string=html_report).write_pdf(response)

        return response
    else:
        return render(request, '../templates/reports/cover_sheet.html', {'cover_sheet': org_cover_sheet,
                                                                         'agency_type': agency_type,
                                                                         'organization': user_org,
                                                                         'tax_description': tax_description,
                                                                         'base64_logo': base64_logo})

def save_report(org_id, path='./cover_sheets/'):
    org = organization.objects.get(id=org_id)
    org_cover_sheet = cover_sheet.objects.get(organization_id=org.id)
    agency_type = org.summary_organization_classifications.name
    print(agency_type)
    try:
        base64_logo = base64.encodebytes(org_cover_sheet.organization_logo).decode("utf-8")
    except:
        base64_logo = ""
    if agency_type != "Community provider" or agency_type != "Medicaid broker":
        tax_description, created = tax_rates.objects.get_or_create(organization_id=org.id)
        tax_description = tax_description.tax_rate_description

    html_report = render_to_string('../templates/reports/cover_sheet.html', {'cover_sheet': org_cover_sheet,
                                                                             'agency_type': agency_type,
                                                                             'organization': org,
                                                                             'tax_description': tax_description,
                                                                             'base64_logo': base64_logo})

    pdf = HTML(string=html_report).write_pdf()
    f = open(os.path.join(path, org.name + '.pdf'), 'wb')
    f.write(pdf)
    f.close()


def generate_all_coversheets(start_with_org_name=None):
    if start_with_org_name:
        skip = True
    else:
        skip = False

    for org in organization.objects.all():
        print(org.name)
        if org.name == start_with_org_name:
            skip = False
        if not skip:
            if org.name not in ['Washington State Department of Transportation',
                                'Lower Elwha Klallam Tribe',
                                'Nooksack Indian Tribe',
                                'Quileute Nation',
                                'Colville Confederated Tribes',
                                'Heckman Motors, Inc']:
                save_report(org.id)
