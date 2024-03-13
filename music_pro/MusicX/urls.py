from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('musicX/Songs/',views.Songs, name='Songs'),
    path('musicX/Songs/<int:id>',views.Songpost, name='Songpost'),
    path('musicX/treanding/',views.treanding_song, name='treanding'),
    path('musicX/Matathi/',views.marathi_song, name='marathi'),
    path('musicX/English/',views.english_song, name='english'),
    path('musicX/Hindi/',views.hindi_song, name='hindi'),
    path('musicX/Devotional/',views.devotional_song, name='devotional'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.log_in, name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout_user',views.logout_user, name='logout_user'),
    path('MusicX/favourite',views.favourite, name='favourite'),
    path('MusicX/About',views.about, name='about'),
    path('MusicX/ContactUs',views.ContactUs, name='contactus'),
    path('changepassword/',views.changepassword, name="changepassword"),
    path('MusicX/CRUD',views.crud, name='crud'),
    path('MusicX/add_song',views.add_song, name='add_song'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('buynow_payment/<int:id>',views.buynow_payment,name='buynowpayment'),
    path('buynow_payment_success/<int:id>',views.buynow_payment_success,name='buynowpaymentsuccess'),
    path('payment_failed/',views.payment_failed,name='paymentfailed'),
    
    
    
]
