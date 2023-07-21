from .libraries import *
 
@login_required
def trigger_and_list_view(request, pk):
    print('we are here')    
    user = request.user
    cover = CoverLetter.objects.get(pk=pk)
    pdfs = PdfContent.objects.filter(cover_letter=cover)
    text = Pagetext.objects.get(pk=1)
    
    context = {
        "user": user,
        "cover": cover,
        "text": text,
        "pdfs": pdfs,

    }

    load_context = {
        "user": user,
        "cover": cover,
        "text": text,
        "pdfs": pdfs,

    }
    if user != cover.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    if request.method == "GET":
        return render(request, "resumes/trigger_and_list.html", context=load_context)
    


    if (
        request.method == "POST"
        or None
        and (
            request.POST.get("form_type") == "trigger_llm" 
        )
    ):
        
        try:
            # pass
            resume_cover_llm(
                            job_description=cover.description_text,
                            resume_url=cover.resume_id.resume_path.path,
                            trigger_text=text.char_19,
                            user=request.user,
                            cover_letter=cover
                        )
        except Exception as e:
            if e:
                messages.add_message(
                    request,
                    messages.INFO,
                    "An empty response was returned.  check your API key",
                )

            else:
                messages.add_message(request, messages.INFO, "Cover Letter Created!")
                return HttpResponseRedirect(reverse("resumes:trigger_and_list"))
        else:
            return render(request, "resumes/trigger_and_list.html", context)

    return render(request, "resumes/trigger_and_list.html", context=load_context)          






