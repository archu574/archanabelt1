# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app1.models import User
from django.db import models
from django.db.models import Count


# Create your models here.
class PokeManager(models.Manager):

    def addpoke(self,uid,id):
        print "adding a poke"
        userpoked=User.objects.get(id=id)
        userpoking= User.objects.get(id=uid)
        countvar=userpoked.poked.count()
        pokes,created=self.update_or_create(countvar=countvar,personpoking=userpoking,personpoked=userpoked)
        return pokes

class Poke(models.Model):
    countvar=models.IntegerField(blank=False, default=0, null=True)
    personpoking = models.ForeignKey(User, related_name="poking")
    personpoked = models.ForeignKey(User, related_name="poked")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= PokeManager()
