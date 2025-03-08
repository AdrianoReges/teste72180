from django.contrib import admin
from .models import (
    Curso, 
    Entrega,
    Professor, 
    Estudante,
)

admin.site.register(Curso)
admin.site.register(Entrega)
admin.site.register(Estudante)
admin.site.register(Professor)
# Register your models here.
