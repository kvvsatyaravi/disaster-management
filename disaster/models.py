from django.db import models

class main(models.Model):
#safeplaces
    yourlocation = models.CharField(max_length=200,default='null')
    safeplacesname = models.CharField(max_length=200,default='kkd')
    safeplacesdistance = models.IntegerField(default='23')
    safeplacescapacity = models.IntegerField(default='200')
    safeplacescontact = models.IntegerField(default='5679')

#transport
    transportname = models.CharField(max_length=200,default='orange travels')
    transporttypeof = models.CharField(max_length=200,default='bus')
    transportcontact = models.IntegerField(default='5679')
    
#rescue
    rescueteamtype = models.CharField(max_length=200,default='navy')
    rescueteammembers = models.IntegerField(default='5')
    rescuecontact =models.IntegerField(default='420420')

#hospital
    
class login(models.Model):
    question = models.CharField(max_length=100,default="testing")
    answer = models.CharField(max_length=100,default="testing")
    username=models.CharField(max_length=200,default='null')
    password=models.CharField(max_length=200,default='null')


class givealert(models.Model):
    alertinfo  = models.CharField(max_length=50,default="testing")
    



