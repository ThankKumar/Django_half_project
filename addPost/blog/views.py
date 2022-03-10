from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
# Home View. 
def home(request):
    return render (request, 'blog/home.html')

#about
def about(request):
    return render (request, 'blog/about.html')

#Contact
def contact(request):
    return render (request, 'blog/contact.html')

#Dashboard
def dashboard(request):
    return render (request, 'blog/dashboard.html')

#logout
def user_logout(request):
    return HttpResponseRedirect('/')

#signup
def user_signup (request):
    
    return render(request, 'blog/signup.html',{'form':form})
#login 
def user_login(request):
    return render (request, 'blog/login.html') 