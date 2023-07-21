from .libraries import *


@login_required
def update_description_view(request, pk):
    user = request.user
    cover = CoverLetter.objects.get(pk=pk)
    text = Pagetext.objects.get(pk=1)
    form = CoverLetterForm(request.POST or None, instance=cover)
    context = {"form": form, "user": user, "cover": cover, "text": text}
    load_context = {"form": form, "user": user, "cover": cover, "text": text}
    if user != cover.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    # else:
    elif request.method == "POST":
        if form.is_valid():
            form.instance.user_id = request.user
            wait_to_save = form.save(commit=False)
            wait_to_save.save()
            print(wait_to_save.description_text)
            messages.add_message(request, messages.INFO, "Job Description Updated!")
            # return render(request, "resumes/create.html", context)
            return HttpResponseRedirect(
                reverse("resumes:trigger_and_list", args=(cover.id,))
            )
        else:
            return render(request, "resumes/form_template.html", context)

    return render(request, "resumes/form_template.html", context=load_context)
