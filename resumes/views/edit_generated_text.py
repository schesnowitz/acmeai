from .libraries import *


@login_required
def edit_generated_text_view(request, pk):
    user = request.user

    pdf = PdfContent.objects.get(pk=pk)
    text = Pagetext.objects.get(pk=1)

    form = EditGeneratedTextForm(request.POST or None, instance=pdf)
    context = {"form": form, "user": user, "pdf": pdf, "text": text}
    load_context = {"form": form, "user": user, "pdf": pdf, "text": text}
    if user != pdf.user:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if request.method == "POST":
            if form.is_valid():
                form.instance.user_id = request.user
                wait_for_doctype = form.save(commit=False)
                wait_for_doctype.save()

                messages.add_message(
                    request, messages.INFO, "Job Cover Letter Content Updated!"
                )
                return redirect("resumes:pdf_html", pdf.id)

            else:
                return render(request, "edit_generated_text_form.html", context)

        return render(
            request, "resumes/edit_generated_text_form.html", context=load_context
        )
