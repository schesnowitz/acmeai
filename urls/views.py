from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from urls.models import Url, Urlsession
from urls.functions import url_llm_qa
from urls.forms import UrlForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from pages.models import Pagetext
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView 

from django.contrib.auth.decorators import login_required


@login_required
def url_index_view(request):
    urls = Url.objects.order_by("-time").filter(user_id=request.user)

    form = UrlForm(request.POST, request.FILES)
    text = Pagetext.objects.get(pk=1)
    context = {
        "form": form,
        "user": request.user,
        "urls": urls,
        "text": text,
    }
    load_context = {
        "user": request.user,
        "urls": urls,
        "text": text,
    }
    if request.method == "POST":
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
            messages.add_message(request, messages.INFO, 
                                     "URL saved and ready to go!")
            return redirect("urls:index")
        else:
            form = UrlForm()
            return render(request, "urls/index.html", context)

    return render(request, "urls/index.html", context=load_context)

@login_required
def interaction_view(request, pk):
    urls = Url.objects.get(pk=pk)
    sessions = Urlsession.objects.filter(url_id=pk)
    session_user = Url.objects.filter(user_id=request.user)
    text = Pagetext.objects.get(pk=1)
    context = {"urls": urls, "sessions": sessions, "text": text}
    current_user = request.user

    # file_url = request.build_absolute_uri(document.path_to_file.url)
    url_request = urls.url_path
    if current_user != urls.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if (
            request.method == "POST"
            or None
            and (
                request.POST.get("form_type") == "urlInteract" and request.POST.get("query")
            )
        ):
            query = request.POST.get("query")
            if query == "":
                messages.add_message(
                    request,
                    messages.INFO,
                    "You tried to send an empty query! this is not allowed.",
                )
                return render(request, "urls/interactions.html", context)
            else:
                try:
                    url_llm_qa(
                        url_path=url_request, query=query, url_model=urls, user=request.user
                    )
                except Exception as e:
                    if e:
                        messages.add_message(
                            request,
                            messages.INFO,
                            "An empty response was returned. check your API key",
                        )

                    else:
                        return render(request, "urls/interactions.html", context)

        return render(request, "urls/interactions.html", context)


@login_required
def delete_view(request, pk):
    
    text = Pagetext.objects.get(pk=1)
    object = get_object_or_404(Url, id = pk)
    context ={"object" : object, "text" : text}
    if request.user != object.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if request.method =="POST":
            object.delete()
            messages.add_message(request, messages.INFO, "Url deleted")
            return redirect("urls:index")
    
        return render(request, "urls/delete.html", context)
    

@login_required
def url_csv_view(request, pk):
    document = Url.objects.get(pk=pk)
    sessions = Urlsession.objects.filter(url_id=document)
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="url.csv"'},
    )
    website = "acmeai.io"
    email = "AI@acmeAI.io"
    writer = csv.writer(response)
    writer.writerow([f"Time", f"Input", "Response"])
    for data in sessions:
        writer.writerow([f"{data.time}", f"{data.input}", f"{data.response}"])
    writer.writerow([])

    writer.writerow([f"#End of output#", f""])
    writer.writerow([f"File", f"Created On", f"Description"])
    writer.writerow(
        [
            f"{document.url_path}",
            f"{document.time}",
            f"{document.description}",
        ]
    )
    writer.writerow([])
    writer.writerow([])
    writer.writerow([f"##############", f""])
    writer.writerow([f"{email}", f"{website}"])
    return response
