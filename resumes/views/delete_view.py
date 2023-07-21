from .libraries import *

@login_required
def delete_view(request, pk):
    text = Pagetext.objects.get(pk=1)
    object = get_object_or_404(Resume, id=pk)
    context = {"object": object, "text": text}
    if request.user != object.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if request.method == "POST":
            object.delete()
            messages.add_message(request, messages.INFO, "Resume deleted")
            return redirect("resumes:index")

        return render(request, "resumes/delete.html", context)
    

@login_required
def delete_cover_letter_view(request, pk):
    text = Pagetext.objects.get(pk=1)
    object = get_object_or_404(CoverLetter, id=pk)
   
    context = {"object": object, "text": text}
    if request.user != object.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if request.method == "POST":
            object.delete()
            messages.add_message(request, messages.INFO, "Cover Letter deleted")
            return redirect("resumes:create", object.resume_id.id)

        return render(request, "resumes/delete.html", context)
