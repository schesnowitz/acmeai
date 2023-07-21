from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from documents.models import Document, Session
from documents.forms import DocumentForm
from django.views.generic.edit import DeleteView
from documents.functions import document_llm_qa
import csv
from django.http import HttpResponse
from pages.models import Pagetext
import pathlib


@login_required
def document_csv_view(request, pk):
    document = Document.objects.get(pk=pk)
    sessions = Session.objects.filter(document=document)
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="docdata.csv"'},
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
            f"{document.path_to_file.name}",
            f"{document.uploaded_on}",
            f"{document.description}",
        ]
    )
    writer.writerow([])
    writer.writerow([])
    writer.writerow([f"##############", f""])
    writer.writerow([f"{email}", f"{website}"])
    return response

@login_required
def index_view(request):
    user = request.user

    documents = Document.objects.order_by("-uploaded_on").filter(
        created_by=request.user
    )
    text = Pagetext.objects.get(pk=1)

    form = DocumentForm(request.POST, request.FILES)
    context = {"form": form, "user": user, "documents": documents, "text": text}
    load_context = {"user": user, "documents": documents, "text": text}
    if request.method == "POST":

        if form.is_valid():
            form.instance.created_by = request.user
            wait_for_doctype = form.save(commit=False)
            file_extension = pathlib.Path(str(wait_for_doctype.path_to_file)).suffix
            print("File Extension: ", (file_extension))

            if file_extension == ".txt" or file_extension == ".pdf":
                print("File Extension: ", (file_extension))
                wait_for_doctype.save()
                messages.add_message(request, messages.INFO, 
                                     "Document uploaded and ready to go!")
                return redirect("documents:index")
            else:
                print(wait_for_doctype.path_to_file) 
                messages.add_message(request, messages.INFO, 
                                     "Document type not supported, its gotta be a PDF or txt file.")
                return redirect("documents:index")
        else:
            form = DocumentForm()
            return render(request, "documents/index.html", context)

    return render(request, "documents/index.html", context=load_context)

@login_required
def document_interact_view(request, pk):
    text = Pagetext.objects.get(pk=1)
    document = Document.objects.get(pk=pk)
    doc_sessions = Session.objects.filter(document=document)
    user = request.user
    context = {
        "document": document,
        "doc_sessions": doc_sessions,
        "text": text,
    }
    # file_url = request.build_absolute_uri(document.path_to_file.url)
    file_url = document.path_to_file.path
    if user != document.created_by:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if (
            request.method == "POST"
            or None
            and (
                request.POST.get("form_type") == "docInteract" and request.POST.get("query")
            )
        ):
            query = request.POST.get("query")
            if query == "":
                messages.add_message(
                    request,
                    messages.INFO,
                    "You tried to send an empty query!  this is not allowed.",
                )
                return render(request, "documents/document_interactions.html", context)
            # document_llm_qa(file_url, query, document, user)
            try:
                document_llm_qa(file_url, query, document, user)
            except Exception as e:
                if e:
                    messages.add_message(
                        request,
                        messages.INFO,
                        "An empty response was returned.  check your API key",
                    )

                else:
                    return render(request, "documents/document_interactions.html", context)

        return render(request, "documents/document_interactions.html", context)

    
@login_required
def delete_view(request, pk):
    
    text = Pagetext.objects.get(pk=1)
    object = get_object_or_404(Document, id = pk)
    context ={"object" : object, "text" : text}
    if request.user != object.created_by:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if request.method =="POST":
            object.delete()
            messages.add_message(request, messages.INFO, "Document deleted")
            return redirect("documents:index")
    
        return render(request, "documents/delete.html", context)
