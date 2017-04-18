from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        # Ensure that a username is set
        #if not kwargs.get('username'):
        if not username:
            raise ValueError('Users must have a valid username')

        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        if not password:
            raise ValueError('Users must have a valid password')

        """
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')
        """
        # guest = Guest.objects.create()
        user = self.model(
            username= username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(username, email, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


# Create your models here.
class Address(models.Model):
    # id = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length = 80)
    address2 = models.CharField(max_length = 40)
    city = models.CharField(max_length = 80)
    company_name = models.CharField(max_length = 100)
    email_address = models.CharField(max_length = 254)
    fax = models.CharField(max_length = 20)
    is_active = models.BooleanField()
    is_default = models.BooleanField()
    postal_code = models.CharField(max_length= 10)
    primary_phone = models.CharField(max_length= 20)
    secondary_phone = models.CharField(max_length= 20)
    state = models.CharField(max_length= 20)
    building_address = models.CharField(max_length=80)
    road_address = models.CharField(max_length=80)
    # customer_address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        abstract = True

class CustomerAddress(Address):
    TYPE_CHOICES=(
        ('MAIN', 'MAIN'),
        ('SUB', 'SUB')
    )
    # id = models.AutoField(primary_key=True)
    address_name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

class User(AbstractUser):
    SEX_CHOICES = (
        ('FEMALE', 'FEMALE'),
        ('MALE', 'MALE')
    )
    address = models.OneToOneField("users.CustomerAddress", null=True, blank=True)
    type = models.CharField(max_length=30)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, blank= True)
    last_name = models.CharField(max_length=50, blank= True)
    name = models.CharField(max_length=100)
    cell_phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    authenticated = models.BooleanField(default = False)
    account_lock = models.BooleanField(default = False)

    users = UserManager()