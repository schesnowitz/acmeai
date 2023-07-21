from .libraries import *

@login_required
def user_job_profile_view(request, pk):
    job_profile = UserJobProfile.objects.get(pk=pk)
    user = request.user

    if user.job_profile.full_name == "":
        path = "resumes/user_job_initial_use.html"
        form = UserJobProfileNameForm(request.POST or None, instance=job_profile)
    else:
        path = "resumes/user_job_initial_use.html"
        form = UserJobProfileForm(request.POST or None, instance=job_profile)
    context = {"user": user, "form": form}
    if user != job_profile.user:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    if request.method == "GET":
        return render(request, path, context)

    if request.method == "POST":
        if form.is_valid():
            wait_to_save = form.save(commit=False)
            wait_to_save.save()
            messages.add_message(
                request, messages.INFO, "Your personal job info has been updated"
            )
            return HttpResponseRedirect(reverse("resumes:index"))
        else:
            messages.add_message(
                request, messages.INFO, "there was a problem saving personal job info"
            )
            return render(request, path, context)
    return render(request, path, context)

@login_required
def user_job_profile_pdf_view(request, pk, id):
    job_profile = UserJobProfile.objects.get(pk=pk)
    pdf = PdfContent.objects.get(pk=id)
    user = request.user
    form = UserJobProfileForm(request.POST or None, instance=job_profile)
    context = {"user": user, "form": form, "pdf": pdf}
    if user != job_profile.user:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    if request.method == "GET":
        return render(request, "resumes/user_job_profile_pdf_form.html", context)

    if request.method == "POST":
        if form.is_valid():
            wait_to_save = form.save(commit=False)
            wait_to_save.save()
            messages.add_message(
                request, messages.INFO, "Your personal job info has been updated"
            )

            return redirect("resumes:pdf_html", pdf.id)
        else:
            messages.add_message(
                request, messages.INFO, "there was a problem saving personal job info"
            )
            return render(request, "resumes/user_job_profile_pdf_form.html", context)
    return render(request, "resumes/user_job_profile_pdf_form.html", context)

@login_required
def user_job_profile_form_view(request, pk):
    user = request.user
    job_profile = UserJobProfile.objects.get(user=user)
    
    form = UserJobProfileForm(request.POST or None, instance=job_profile)
    context = {"user": user, "form": form}
    if user != job_profile.user:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    # else:
    if request.method == "GET":
        return render(request, "resumes/user_job_profile_form.html", context)

    if request.method == "POST":
        if form.is_valid():
            wait_to_save = form.save(commit=False)
            wait_to_save.save()
            messages.add_message(
                request, messages.INFO, "Your personal job info has been updated"
            )

            return HttpResponseRedirect(reverse("resumes:index"))
        else:
            messages.add_message(
                request, messages.INFO, "there was a problem saving personal job info"
            )
            return render(request, "resumes/user_job_profile_form.html", context)
    return render(request, "resumes/user_job_profile_form.html", context)