from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.TextField
    user_name = models.TextField
    user_password = models.TextField
    email = models.EmailField(unique=True)
    cr_date = models.DateTimeField(auto_now_add=True)


class CurrencySign(models.Model):
    cur_sign = models.CharField()
    sign = models.CharField()

    def __str__(self):
        return self.sign

class CurrencyPrice(models.Model):
    cur_desc = models.CharField()
    cur_price = models.DecimalField(max_digits=5, decimal_places=2)

    #def __str__(self):
       # return self.cur_price

class Tags(models.Model):
    name = models.CharField()
    desc = models.CharField()
    #cr_date = models.DateTimeField(auto_now_add=True)
    # cr_user = models.ForeignKey(Users, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name



class Currencies(models.Model):
    cur_id = models.TextField()
    cur_name = models.TextField()
    cur_desc = models.CharField(null=True)
    cur_sign = models.ForeignKey(CurrencySign, on_delete=models.PROTECT, null=True)
    cur_tag = models.ManyToManyField(Tags)
    cr_date = models.DateTimeField(auto_now_add=True)
    #cr_user = models.ForeignKey(Users, on_delete=models.PROTECT)


class Curr_Tags(models.Model):
    cur_id = models.ForeignKey(Currencies, on_delete=models.PROTECT, null=True)
    tag_id = models.ForeignKey(Tags, on_delete=models.PROTECT, null=True)

