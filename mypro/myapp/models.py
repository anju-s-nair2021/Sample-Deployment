from django.db import models

# Create your models here.
class State(models.Model):
    sname=models.CharField(max_length=20)
class District(models.Model):
    dname=models.CharField(max_length=20)
    sid=models.ForeignKey(State,on_delete=models.CASCADE) #on_delete tells Django how to handle the deletion of a related object to maintain referential integrity in the database.
    # model.CASCADE: Deletes the related objects when the referenced object is deleted.
    # models.PROTECT
    # model.SET_DEFALUT: Sets the foreign key to NULL if the referenced object is deleted. 

class Reg(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=5)
    dob=models.DateField()
    qual=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phno=models.BigIntegerField()
    addr=models.TextField()
    loc=models.CharField(max_length=20)
    image=models.FileField(upload_to='file')

class Login(models.Model):
    uname=models.CharField(max_length=20)
    pswd=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)
    uid=models.ForeignKey(Reg,on_delete=models.CASCADE)
