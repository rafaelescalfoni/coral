from django.shortcuts import render

def login(request):
    # general_error = ""

    # if request.POST:
    #     form = AuthenticationForm(request=request, data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(username=username, password=password)

    #         if user is not None:
    #             auth_login(request, user)
    #             general_error = f"Você já está logado(a) como {username}"
    #             return redirect("/story")
    #         else:
    #             general_error = "Usuário ou senha inválidos"
    #     else:
    #         general_error = "Usuário ou senha inválidos"

    # form = AuthenticationForm()
    return render(request, "auth/login.html")#, {"form": form, "general_error": general_error})