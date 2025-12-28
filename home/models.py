from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now
# Create your models here.
SELECT_CATEGORY_CHOICES =[
    ("Food", "Food"),
    ("Travel", "Travel"),
    ("Shopping", "Shopping"),
    ("Necessities", "Necessities"),
    ("Entertainment", "Entertainment"),
    ("Other", ("Other"))
]

ADD_EXPENSE_CHOICES =[ 
    ("Expense", "Expense"),
    ("Income", "Income")
]

PROFESSION_CHOICES =[
    ("Employee", "Employee"),
    ("Business", "Business"),
    ("Student", "Student"),
    ("Other", "Other")
]

class Addmoney_info(models.Model):
    user = models.ForeignKey(User, default =1, on_delete = models.CASCADE)
    add_money = models.CharField(max_length = 255, choices =ADD_EXPENSE_CHOICES)
    date = models.DateField(default = now)
    quantity =models.BigIntegerField()
    category = models.CharField(max_length = 255, choices =SELECT_CATEGORY_CHOICES, default ='Food' )

    class Meta:
        db_table = 'addmoney'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length =255, choices= PROFESSION_CHOICES)
    savings = models.IntegerField(null =True, blank =True)
    income = models.BigIntegerField(null =True, blank =True)
    image = models.ImageField(upload_to='profile_image', blank =True)

    def __str__(self):
        return self.user.username 
