from django.shortcuts import render,redirect
from .models import song ,Favourite,Download
from .forms import SignupForm,AuthenticateForm,UserProfileForm,AdminProfileForm,ChangePasswordForm,CrudForm,ContactUsForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
# payment
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse


def index(request):
        songs = song.objects.all()
        return render(request,'MusicX/index.html',{'songs':songs})


    
def Songs(request):
    songs = song.objects.all()
    return render(request,'MusicX/Songs.html',{'songs':songs})

def Songpost(request,id):
    songs=song.objects.filter(song_id=id).first()
    return render(request,'MusicX/Songpost.html',{'songs':songs})

def about(request):
    return render(request,"MusicX/about.html")

def ContactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus')
    else:
        form = ContactUsForm()

    return render(request, 'MusicX/contactUs.html',{'form':form})

def favourite(request):
    return render(request, 'MusicX/favourite.html')


def treanding_song(request):
    songs = song.objects.filter(categories="TREANDING")
    return render(request,'MusicX/treanding.html',{'songs':songs})

def hindi_song(request):
    songs = song.objects.filter(categories="HINDI")
    return render(request,'MusicX/hindi.html',{'songs':songs})

def marathi_song(request):
    songs = song.objects.filter(categories="MARATHI")
    return render(request,'MusicX/marathi.html',{'songs':songs})

def english_song(request):
    songs = song.objects.filter(categories="ENGLISH")
    return render(request,'MusicX/english.html',{'songs':songs})

def devotional_song(request):
    songs = song.objects.filter(categories="DEVOTIONAL")
    return render(request,'MusicX/devotional.html',{'songs':songs})

def signup(request):
    if request.method == "POST":
        mf=SignupForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/login/')
    else:
        mf=SignupForm()
    return render(request, 'MusicX/signup.html', {'mf':mf})
     

def log_in(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':       
            mf = AuthenticateForm(request,request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            mf = AuthenticateForm()
        return render(request,'MusicX/login.html',{'mf':mf})
    else:
        return redirect('/') 
    
def profile(request):
    if request.user.is_authenticated:  # This check wheter user is login, if not it will redirect to login page
        if request.method == 'POST':
            if request.user.is_superuser == True:
                mf = AdminProfileForm(request.POST,instance=request.user)
            else:
                mf = UserProfileForm(request.POST,instance=request.user)
            if mf.is_valid():
                mf.save()
        else:
            if request.user.is_superuser == True:
                mf = AdminProfileForm(instance=request.user)
            else:
                mf = UserProfileForm(instance=request.user)
        return render(request,'MusicX/profile.html',{'name':request.user,'mf':mf})
    else:                                            # request.user returns the username
        return redirect('login')
    


def logout_user(request):
    logout(request)
    return redirect('index')


def changepassword(request):                           # Password ChangeForm               
    if request.user.is_authenticated:                  # Include old password 
        if request.method == 'POST':                               
            mf =ChangePasswordForm(request.user,request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('profile')
        else:
            mf = ChangePasswordForm(request.user)
        return render(request,'MusicX/changepassword.html',{'mf':mf})
    else:
        return redirect('login')
    

def favourite(request):
    if request.method == "POST":
        user=request.user
        music_id=request.POST['music_id']

        # Check if the song is already in the user's favorites
        music = Favourite.objects.filter(user=user, music_id=music_id)
        if music.exists():
            message='Your song is already added.'
        else:
            # Add the song to the user's favorites
            favourite = Favourite(user=user, music_id=music_id)
            favourite.save()
            message='Your song is successfully added.'

        # Get the song object and pass it to the template   
        songs = song.objects.filter(song_id=music_id).first()
        return render(request, 'MusicX/Songpost.html', {'songs': songs, 'message': message})

    # Get the user's favorites and pass them to the template
    fev = Favourite.objects.filter(user=request.user)
    fav_musics = [f.music_id for f in fev]
    songs = song.objects.filter(song_id__in=fav_musics)
    return render(request, 'MusicX/favourite.html', {'songs': songs})
 


# ....................CRUD..................

# Create your views here.
def crud(request):
    # if request.method == 'POST':
    #     cf =CrudForm(request.POST)
    #     if cf.is_valid():
    #         cf.save()
    #     sm =song.objects.all()        
    #     cf= CrudForm()
    # else:
    sm =song.objects.all()
    # cf =CrudForm()
    return render(request, 'MusicX/crud.html',{'sm':sm})


def delete(request,id):
    if request.method == 'POST':
        de = song.objects.get(pk=id)
        de.delete()
    return redirect('crud')
    

def update(request,id):
    if request.method == 'POST':
        um = song.objects.get(pk=id)
        cf = CrudForm(request.POST, instance=um)
        if cf.is_valid():
            cf.save()
        cf = CrudForm()
    else:
        um =song.objects.get(pk=id)
        cf =CrudForm(instance=um)
    return render(request, 'MusicX/update.html',{'cf':cf})


def add_song(request):
    if request.method == 'POST':
        cf =CrudForm(request.POST)
        if cf.is_valid():
            cf.save()      
        cf= CrudForm()
    else:
        cf =CrudForm()
    return render(request, 'MusicX/add_song.html',{'cf':cf})





@login_required
def buynow_payment(request, id):
    songs = song.objects.get(pk=id)
    final_price = songs.price

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': final_price,
        'item_name': 'MusicX',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('buynowpaymentsuccess', args=[id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    return render(request, 'MusicX/payment.html', {'final_price': final_price, 'paypal': paypal_payment})

@login_required
def buynow_payment_success(request, id):
    user = request.user
    songs = song.objects.get(pk=id)
    Download(user=user, songs=songs, quantity=1).save()

    # Serve the song file as a response to the user
    response = HttpResponse(songs.Song.read(), content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{songs.name}.mp3"'
    return response


def payment_failed(request):
    return render(request,'MusicX/payment_failed.html')






