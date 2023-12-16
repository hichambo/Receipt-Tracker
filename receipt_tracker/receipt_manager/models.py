# receipt_manager/models.py
from django.db import models
from django.contrib.auth.models import User

# Receipt class representing a model for storing receipt information
class Receipt(models.Model):
    # A foreign key linking the receipt to a specific user
    # This establishes a relationship with Django's built-in User model.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # A character field to store the name of the store where the purchase was made.
    store_name = models.CharField(max_length=255)
    
    # A date field to store the date of the purchase.
    date_of_purchase = models.DateField()
    
    # A text field to store a simple list of items purchased.
    item_list = models.TextField()
    
    # A decimal field to store the total amount of the purchase.
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # String representation of the Receipt object, returns the store name
    def __str__(self):
        return self.store_name

# UserProfile class representing a model for user profile information
class UserProfile(models.Model):
    # A one-to-one relationship with Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # String representation of the UserProfile object, returns the username
    def __str__(self):
        return self.user.username
