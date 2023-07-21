from .libraries import *


def pdf_view(request, pk):
    template_path = "resumes/view_pdf.html"
    # current date and time
    date = datetime.now().strftime("%B %d, %Y")
    pdf = PdfContent.objects.get(pk=pk)
    text = Pagetext.objects.get(pk=1)
    user_job_info = UserJobProfile.objects.get(user=request.user)
    user = request.user

    context = {
        "pdf": pdf,
        "text": text,
        "user": user,
        "company_name": pdf.cover_letter.company_name,
        "hiring_manager_info": pdf.cover_letter.content,
        "user_job_info": user_job_info,
        "date": date,
    }
    file_name = (f"{user_job_info.full_name}_{pdf.cover_letter.company_name}.pdf")
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'filename="{file_name}"'
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


def pdf_download(request, pk):
    template_path = "resumes/pdf_download.html"
    # current date and time
    date = datetime.now().strftime("%B %d, %Y")
    pdf = PdfContent.objects.get(pk=pk)
    text = Pagetext.objects.get(pk=1)
    user_job_info = UserJobProfile.objects.get(user=request.user)
    user = request.user

    context = {
        "pdf": pdf,
        "text": text,
        "user": user,
        "company_name": pdf.cover_letter.company_name,
        "hiring_manager_info": pdf.cover_letter.content,
        "user_job_info": user_job_info,
        "date": date,
    }
    file_name = (f"{user_job_info.full_name}_{pdf.cover_letter.company_name}.pdf")
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    # response["Content-Disposition"] = 'filename="report.pdf"'
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response

