from pydoc import describe
from django.db import models

class Transactions(models.Model):
    transaction_id=models.IntegerField(primary_key=True,max_length=100000)
    transaction_date=models.DateField()
    user_id=models.ForeignKey()
    bank_id=models.ForeignKey()
    description=models.CharField(max_length=500)
    credit=models.FloatField()
    debit=models.FloatField()
    merchant=models.CharField(max_length=100)
    expense_id=models.ForeignKey()

class Assests(models.Model):
    assest_id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey()
    assest_name=models.CharField(max_length=100)
    assest_type=models.ForeignKey()
    uom=models.CharField(max_length=100)
    quantity=models.IntegerField()

class Liabilites(models.Model):
    liablities_id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey()
    liablities_name=models.CharField(max_length=100)
    liablities_type=models.ForeignKey()
    uom=models.CharField(max_length=100)
    quantity=models.IntegerField()
    
class AssestType(models.Model):
    assest_type_id=models.IntegerField()
    assests_type=models.CharField(max_length=100)

class LiabilitesType(models.Model):
    liabilites_type_id=models.IntegerField()
    liabilites_type=models.CharField(max_length=100)

class ExpenseType(models.Model):
    expense_type_id=models.IntegerField()
    expense_type=models.CharField(max_length=100)

class Bank(models.Model):
    bank_id=models.IntegerField()
    bank_name=models.CharField(max_length=100)
    acc_no=models.IntegerField()
    acc_type=models.CharField(max_length=50)
    user_id=models.ForeignKey()

class BankInfo(models.Model):
    bank_info_id=models.IntegerField()
    recepient=models.EmailField()
    bank_id=models.ForeignKey()

