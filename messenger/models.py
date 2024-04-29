from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content  = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name ='threads')
    messages = models.ManyToManyField(Message)

#Señal 
def messages_changed(sender, **kwarg):
    #Recuperamos los datos 
    instance = kwarg.pop("instance",None)
    action = kwarg.pop("action",None)
    pk_set = kwarg.pop("pk_set",None)
    print(instance ,action,pk_set)

    false_pk_set = set()
# Intercepta usuarios que no esten en el hilo e intente enviar mensajes 
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("Ups,({}) no forma parte del hilo".format(msg.user) )
                false_pk_set.add(msg_pk)
    
    #Buscar los mensajes de false_pk_set que si estan en pk_set y los borramos de pk_set

    pk_set.difference_update(false_pk_set)

#Conectamos la seña con los cambios que puedan suceder en el campo many to many field de messages
m2m_changed.connect(messages_changed, sender= Thread.messages.through)