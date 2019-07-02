from django.db.models import Model, TextField


class SimpleModel(Model):
    name = TextField()
