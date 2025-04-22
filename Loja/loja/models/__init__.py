from django.db import models                        #biblioteca padrão do Django
from django.contrib.auth.models import User         #biblioteca padrão do Django
from django.db.models.signals import post_save      #biblioteca padrão do Django
from django.dispatch import receiver                #biblioteca padrão do Django

#Models
from .Fabricante import Fabricante
from .Categoria import Categoria
from .Produto import Produto