from .libraries import *


def pdf_as_html_view(request, pk):
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

    return render(request, "resumes/view_pdf_as_html.html", context)
