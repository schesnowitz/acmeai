from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from chats.models import Instruction, Chat
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from pages.models import Profile, Pagetext
from chats.functions import chat_llm
from django.core.files.base import ContentFile
from chats.forms import InstructionForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
import csv

class IndexView(LoginRequiredMixin, ListView):
    model = Instruction
    fields = ["description", "prompt", "data"]
    context_object_name = "instructions"
    template_name = "chats/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["text"] = Pagetext.objects.get(pk=1)
        return context

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(user_id=self.request.user)




@login_required
def delete_view(request, pk):
    text = Pagetext.objects.get(pk=1)
    object = get_object_or_404(Instruction, id = pk)
    context ={"object" : object, "text" : text}
    if request.user != object.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if request.method =="POST":
            object.delete()
            messages.add_message(request, messages.INFO, "Chatter deleted")
            return redirect("chats:index")
    
        return render(request, "chats/delete.html", context)
@login_required
def chat_session_view(request, pk):
    instructions = Instruction.objects.get(pk=pk)

    chats = Chat.objects.filter(instruction_id=pk)
    user = request.user
    profile = Profile.objects.get(user=user)
    # OPENAI_API_KEY = profile.open_api_key
    # print(f" ---- {profile.open_api_key}")
    data_file = request.build_absolute_uri(instructions.data_text.url)
    prompt = instructions.prompt
    text = Pagetext.objects.get(id=1)
    context = {
        "instructions": instructions,
        "chats": chats,
        "text": text,
    }
    if user != instructions.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if (
            request.method == "POST"
            or None
            and (
                request.POST.get("form_type") == "chatInteract"
                and request.POST.get("query")
            )
        ):
            query = request.POST.get("query")

            if query == "":
                messages.add_message(
                    request,
                    messages.INFO,
                    "You tried to send an empty query!  this is not allowed.",
                )
                return render(request, "chats/chat_session.html", context)
            else:
                # chat_llm(prompt=prompt, data_file_url=instructions.data_text.url, query=query, instruction_id=instructions, user=request.user)
                try:
                    chat_llm(
                        prompt=prompt,
                        data_file_url=instructions.data_text.path,
                        query=query,
                        instruction_id=instructions,
                        user=request.user,
                    )

                except Exception as e:
                    if e:
                        messages.add_message(
                            request,
                            messages.INFO,
                            "An empty response was returned.  check your API key",
                        )

                    else:
                        messages.add_message(
                            request,
                            messages.INFO,
                            "Try your request again, as there was a problem getting a response from the AI.",
                        )
                        return render(request, "chats/chat_session.html", context)

                return render(request, "chats/chat_session.html", context)

        return render(request, "chats/chat_session.html", context)


@login_required
def create_view(request):
    text = Pagetext.objects.get(id=1)

    form = InstructionForm(request.POST)

    if request.method == "POST":
        current_user = request.user
        if form.is_valid():
            wait_for_text = form.save(commit=False)
            file = ContentFile(
                wait_for_text.data,
                name=f"data_text_user{current_user.id}dt{datetime.now()}.txt",
            )
            wait_for_text.data_text = file
            wait_for_text.user_id = current_user
            wait_for_text.save()
            messages.add_message(request, messages.INFO, "Your Prompt has been saved.")
            return redirect("chats:index")
        else:
            messages.add_message(
                request, messages.INFO, "There was a problem saving your data."
            )
            return render(request, "chats/index.html", {"form": form, "text": text})

    return render(request, "chats/create.html", {"form": form, "text": text})


@login_required
def update_view(request, pk):
    instruction = Instruction.objects.get(pk=pk)
    chats = Chat.objects.filter(instruction_id=pk)

    form = InstructionForm(request.POST or None, instance=instruction)
    if request.user != instruction.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if request.method == "POST":
            current_user = request.user
            if form.is_valid():
                wait_for_text = form.save(commit=False)
                file = ContentFile(
                    wait_for_text.data,
                    name=f"data_text_user{current_user.id}dt{datetime.now()}.txt",
                )
                wait_for_text.data_text = file
                wait_for_text.user_id = current_user

                wait_for_text.save()
                messages.add_message(
                    request, messages.INFO, "LLM Instructions have been updated."
                )
                return redirect("chats:chat", instruction.id)
            else:
                messages.add_message(
                    request, messages.INFO, "There was a problem saving your data."
                )
                return render(
                    request, "chats/update.html", {"form": form, "instruction": instruction}
                )
        return render(
            request, "chats/update.html", {"form": form, "instruction": instruction}
        )

@login_required
def chat_csv_view(request, pk):
    instruction = Instruction.objects.get(pk=pk)
    chats = Chat.objects.filter(instruction_id=instruction)
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="chatter.csv"'},
    )
    website = "acmeai.io"
    email = "AI@acmeAI.io"
    writer = csv.writer(response)
    writer.writerow([f"Time", f"Input", "Response"])
    for data in chats:
        writer.writerow([f"{data.time}", f"{data.input}", f"{data.response}"])
    writer.writerow([])

    writer.writerow([f"#End of output#", f""])
    writer.writerow([f"File", f"Created On", f"Description"])
    writer.writerow(
        [
            f"{instruction.description}",
            f"{instruction.prompt}",
            f"{instruction.data}",
        ]
    )
    writer.writerow([])
    writer.writerow([])
    writer.writerow([f"##############", f""])
    writer.writerow([f"{email}", f"{website}"])
    return response
