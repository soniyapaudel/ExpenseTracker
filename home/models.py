from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now


# Category Choices

# Expense / Income
ADD_EXPENSE_CHOICES =[ 
    ("Expense", "Expense"),
    ("Income", "Income")
]
EXPENSE_CATEGORY_CHOICES =[
    ("Groceries", "Groceries"),
    ("Shopping", "Shopping"),
    ("Rent", "Rent"),
    ("Internet", "Internet"),
    ("Medicines", "Medicines"),
    ("Savings", "Savings"),
    ("Laundry", "Laundry"),
    ("Outing", "Outing"),
    ("Necessities", "Necessities"),
    ("Other", ("Other"))
]



INCOME_CATEGORIES =[
    ("Salary", "Salary"),
    ("Bonus","Bonus"),
    ("Gift", "Gift"),
    ("ROI", "ROI"),
    ("Other", "Other")
]

#---Add Expense ----
class Addmoney_info(models.Model):
    user = models.ForeignKey(User, default =1, on_delete = models.CASCADE)
    add_money = models.CharField(max_length = 255, choices =ADD_EXPENSE_CHOICES)
    date = models.DateField(default = now)
    amount =models.BigIntegerField()
    category = models.CharField(max_length = 255, default ='' )
    description = models.CharField(max_length=255, default='', blank =True )
    class Meta:
        db_table = 'addmoney'

    def __str__(self):
        return f"{self.user.username} - {self.add_money} - {self.amount}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    savings = models.IntegerField(null =True, blank =True)
    income = models.BigIntegerField(null =True, blank =True)
    image = models.ImageField(upload_to='profile_image', blank =True)

    def __str__(self):
        return self.user.username 


    def clean(self):
        from django.core.exceptions import ValidationError
        if self.add_money == "Expense" and self.category not in dict(EXPENSE_CATEGORY_CHOICES):
            raise ValidationError("Select a valid expense Category")
        elif self.add_money == "Income" and self.category not in dict(INCOME_CATEGORIES):
            raise ValidationError("Select a valid income category")
