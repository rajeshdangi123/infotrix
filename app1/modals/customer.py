from django.db import models

class Customer(models.Model):
    user_name=models.CharField(max_length=30)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_field=models.EmailField()
    phone_number=models.IntegerField()
    password=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.user_name
    
    #@staticmethod
    def register(self):
        self.save()

  
    def isExists(self):
        if Customer.objects.filter(email_field=self.email_field):
            return True
        else:
            return False
    @staticmethod
    def get_customer_by_email(email_field):
        try:
            return Customer.objects.get(email_field=email_field)
        except:
            return False
    


    