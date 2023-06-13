from django.db import models as db

# Create your models here.
class Favorite(db.Model):
    client_id = db.ForeignKey('Client', on_delete=db.CASCADE)
    produto_id = db.IntegerField()

class Client(db.Model):
    name = db.CharField(max_length=100)
    # outros campos relevantes para o client