from django.shortcuts import render
from accounts.models import User, Profile
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from accounts.forms import ProfileForm
from django.http import HttpResponseRedirect
from accounts.models import Profile
# Create your views here.
@login_required
def edit_user(request):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    user_form = ProfileForm(instance=user)
 
    #ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('activation_key', 'key_expires'))
    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('userid','surname','firstname','sex','title','birth_date','mobile','address','address2','city','state','zipcode','country'))
    formset = ProfileInlineFormset(instance=user)
 
    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = ProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile')
 
        return render(request, "accounts/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

@login_required
def profiles_list(request):
    profiles = Profile.objects.all()
    return render(request, 'accounts/profiles_list.html', {'profiles': profiles})


@login_required
def profile_detail(request):
    u = User.objects.get(pk=request.user.pk)
    profile = Profile.objects.filter(user=u)
    #print (profile[0].activation_key)
    print (profile[0].birth_date)
    return render(request, 'accounts/profile_detail.html', {'profile': profile[0]})
#======

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from accounts.forms import SignUpForm
from accounts.tokens import account_activation_token
from django.http import HttpResponse
from django.core.mail import EmailMessage

@login_required
def home(request):
    return render(request, 'home.html')

import requests 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data.get('email')
            response = requests.get(
                "http://api.quickemailverification.com/v1/verify?email=" + to_email + "&apikey=7304da5f8417d4a865dc14bc1122b0e7349b65a2b0333a7e3fda0e8c8427")
            response = response.json()
            if (response['result'] == "valid"):
                user = form.save(commit=False)
                #user.is_active = False
                user.active = False
                user.save()

                current_site = get_current_site(request)
                mail_subject = 'Activate Your Library Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    #'domain': current_site.domain,
                    'domain': 'localhost:8000',
                    #'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                #user.email_user(subject, message)
                #to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                #return redirect('account_activation_sent')
                return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        #uid = force_str(urlsafe_base64_decode(uidb64)).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        #user.is_active = True
        user.active = True
        #user.profile.email_confirmed = True
        user.email_confirmed = True
        user.save()
        #login(request, user)
        return redirect('account_update')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return render(request, 'account_activation_invalid.html')

#=======
"""
def register_user(request):
if request.method == 'POST':
        register = RegisterForm(request.POST, prefix='register')
        usrprofile = ProfileForm(request.POST, prefix='profile')
        if register.is_valid() * usrprofile.is_valid():
            user = register.save()
            usrprof = usrprofile.save(commit=False)
            usrprof.user = user
            usrprof.set_token()
            #usrprof.subscribed = '1'
            
            usrprof.save()
            return HttpResponse('congrats')
        else:
            return HttpResponse('errors')
else:
    userform = RegisterForm(prefix='register')
    userprofileform = ProfileForm(prefix='profile')
    return render(request, 'registration/register_form.html', {'userform': userform, 'userprofileform': userprofileform})

"""
