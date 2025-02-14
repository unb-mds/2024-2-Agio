from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class ProductTable(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    amount = models.IntegerField()
    category = models.CharField(max_length=255, default="Sem categoria")
    description = models.CharField(max_length=255, default="Sem descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name


class UserTable(models.Model):
    id = models.AutoField(primary_key=True)  # Ajusta para um campo AutoField
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Evitar duplicatas
    password = models.CharField(max_length=255)

    # Função para proteger a senha
    def save(self, *args, **kwargs):
        # Protege a senha apenas na criação ou atualização direta
        if not self.pk or 'password' in kwargs.get('update_fields', []):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
