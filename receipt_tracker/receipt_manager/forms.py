# receipt_manager/forms.py
from django import forms
from .models import Receipt

# ReceiptForm class, a ModelForm to handle receipt-related forms
class ReceiptForm(forms.ModelForm):
    # Meta class to define metadata for the form
    class Meta:
        # Specifies the model to use for the form
        model = Receipt

        # Specifies the fields to include in the form
        fields = ['store_name', 
                  'date_of_purchase', 
                  'item_list',
                  'total_amount']
