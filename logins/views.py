from django.shortcuts import render, HttpResponse, redirect, reverse
import pyrebase

# Create your views here.
config = {
    'apiKey': "AIzaSyA520VBeHVrhEF1hpJ13S2D1ZD94TlyNOE",
    "authDomain": "software-engineering-6e9a7.firebaseapp.com",
    'databaseURL': "https://software-engineering-6e9a7.firebaseio.com",
    'projectId': "software-engineering-6e9a7",
    'storageBucket': "software-engineering-6e9a7.appspot.com",
    'messagingSenderId': "329135496498"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def base(request):
	return render(request, 'base.html')

def login(request, error = ''):
	return render(request,'login/login.html', {"error": error})

def signin(request):
	print('\n\n\n\n\n\n coming')
	return render(request, 'signin/signin.html')

def postsignin(request):
	return render(request, 'base.html')

def postlogin(request):
	email = request.POST.get('email')
	passw = request.POST.get('password')
	try:
	    user = auth.sign_in_with_email_and_password(email,passw)
	except:
	    message="invalid info"
	    return redirect(reverse(login))
	print(user['localId'])
	session_id=user['localId']
	request.session['uid'] = str(session_id)
	return render(request,'base.html',{"e":email})
    
