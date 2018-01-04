from __future__ import unicode_literals
from datetime import date
from django.utils.timezone import datetime
from ..app1.models import User
from ..app2.models import Poke
from django.shortcuts import render,redirect
from django import forms
from django.db.models import Count



# Create your views here.
def contextfunc(request):
    userz = User.objects.all().exclude(id=request.session['id'])
    pokez = Poke.objects.all()
    user = User.objects.get(id=request.session['id'])
    usercount_pokes = Poke.objects.all().filter(personpoked=request.session['id'])
    counting=Poke.objects.all().exclude(personpoking=request.session['id'])
    userlist = Poke.objects.filter(personpoked=request.session['id']).exclude(id=request.session['id'])
    # setofusers = Poke.objects.all().exclude(id=request.session['id']
    #
    # set1=set(usercount_pokes)
    # set2=set(setofusers)



    context = {
        'downbox':userz,
        'pokes_of_people_to_poke':pokez,
        'usercount_pokes': usercount_pokes,
        'counting':counting,
        'pokez':pokez,
        'userlist':userlist,
        # 'setofusers':setofusers,
              }
    return render(request,'app2/mainpage.html',context)



def addpokes(request,id):
    print "adding pokes func"
    uid=request.session['id']
    entry=Poke.objects.addpoke(uid,id)
    return redirect('/main')

def logout(request):
    return redirect('/')
