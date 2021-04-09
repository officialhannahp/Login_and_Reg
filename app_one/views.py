from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def main(request):
    return render(request, 'main.html')


def create(request):
    #reg errors
    errors = User.objects.user_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')

    #password hashing
    pw = request.POST['pw']
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
    print(pw_hash)

    #creating a new user
    print(request.POST)
    new_user =  User.objects.create(
        f_name = request.POST['f_name'],
        l_name = request.POST['l_name'],
        email = request.POST['email'],
        pw = pw_hash
    )
    request.session['user_id'] = new_user.id
    return redirect('/success')

def login(request):
    matching_email = User.objects.filter(email=request.POST['email']).first()
    print(matching_email)

    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')

    request.session['sEmail'] = request.POST['email']

    if matching_email is not None:
        if bcrypt.checkpw (request.POST['pw'].encode(), matching_email.pw.encode()):
            request.session['user_id'] = matching_email.id

            return redirect('/success')
        else:
            print('pw incorrect')
            return redirect('/')
    else:
        print ('no user found')
        return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')



    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user
    }

    return render(request, 'success.html', context)

# def wipeDB(request):
#     User.objects.all().delete()
#     return redirect('/')