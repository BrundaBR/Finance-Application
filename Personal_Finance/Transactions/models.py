
from django.db import models
from User_Authentication.models import User

# Bank details concerned to User
class Bank(models.Model):
    bank_id=models.IntegerField()
    bank_name=models.CharField(max_length=100)
    acc_no=models.IntegerField()
    acc_type=models.CharField(max_length=50)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class ExpenseType(models.Model):
    expense_type_id=models.IntegerField()
    expense_type=models.CharField(max_length=100)

class Expense(models.Model):
    expense_id=models.IntegerField(primary_key=True)
    expense_type_id=models.ForeignKey(ExpenseType,on_delete=models.CASCADE)


# Recent transactions made by user
class Transactions(models.Model):
    transaction_id=models.IntegerField(primary_key=True)
    transaction_date=models.DateField()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    bank_id=models.ForeignKey(Bank,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    credit=models.FloatField()
    debit=models.FloatField()
    merchant=models.CharField(max_length=100)
    expense_id=models.ForeignKey(Expense,on_delete=models.CASCADE)

class AssestType(models.Model):
    assest_type_id=models.IntegerField()
    assests_type=models.CharField(max_length=100)

class Assests(models.Model):
    assest_id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    assest_name=models.CharField(max_length=100)
    assest_type=models.ForeignKey(AssestType,on_delete=models.CASCADE)
    uom=models.CharField(max_length=100)
    quantity=models.IntegerField()

class LiabilitesType(models.Model):
    liabilites_type_id=models.IntegerField()
    liabilites_type=models.CharField(max_length=100)

class Liabilites(models.Model):
    liablities_id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    liablities_name=models.CharField(max_length=100)
    liablities_type=models.ForeignKey(LiabilitesType,on_delete=models.CASCADE)
    uom=models.CharField(max_length=100)
    quantity=models.IntegerField()
    
#Data to recognize the bank behaviour and bank type
class BankInfo(models.Model):
    bank_info_id=models.IntegerField()
    recepient=models.EmailField()
    bank_id=models.ForeignKey(Bank,on_delete=models.CASCADE)

