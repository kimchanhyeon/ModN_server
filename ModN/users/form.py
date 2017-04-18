from django import forms
from users.models import (
    User,
    CustomerAddress,
)

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('address', 'type', 'username', 'email', 'password',
                  'first_name', 'last_name', 'name', 'cell_phone', 'sex',
                   'authenticated', 'account_lock',
        )

class CustomerAddressForm(forms.ModelForm):

    class Meta:
        model = CustomerAddress
        fields = ('address1', 'address2', 'city', 'company_name', 'email_address',
                  'fax', 'is_active', 'is_default', 'postal_code', 'primary_phone',
                  'secondary_phone', 'state', 'building_address', 'road_address',
                  'address_name', 'type')
