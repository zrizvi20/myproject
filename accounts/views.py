##def login(request):
##    if request.method=="POST":
##        form = LoginForm(form.cleaned_data)
##        if form.is_valid():
##            username = form.cleaned_data['username']
##            password = form.cleaned_data['password']
##            user = authenticate(username=username, password=password)
##            if user is not None:
##                login(request.user)
##                return redirect('/')
##            else:
##                error = "Username and password do not match!"
##        else:
##            form = LoginForm()
##            return render(request, 
