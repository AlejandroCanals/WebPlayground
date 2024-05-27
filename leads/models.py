from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Lead(models.Model):
    LOW = 'Baja'
    MEDIUM = 'Media'
    HIGH = 'Alta'

    CHOICES_PRIORITY = {
        (LOW, 'Baja'),
        (MEDIUM, 'Media'),
        (HIGH, 'Alta'),

    }

    NEW = 'Nuevo'
    CONTACTED = 'Contactado'
    WON = 'Completado'
    LOST = 'Perdido'

    CHOICES_STATUS = {
        (NEW, 'Nueva'),
        (CONTACTED, 'Contactado'),
        (WON, 'Completado'),
        (LOST, 'Perdido'),

    }

    name = models.CharField(max_length=255, verbose_name="Nombre")
    email = models.EmailField(max_length=100, verbose_name="Email")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM, verbose_name="Prioridad")
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW, verbose_name="Estado")
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE, verbose_name="Creado por")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado a las")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Modificado a las ")
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name
