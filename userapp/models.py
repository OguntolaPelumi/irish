from django.db import models

# Create your models here.
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    countries=[
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("UK", "UK"),
        ("USA", "USA"),
    ]

    states=[
        ("Alabama", "Alabama"),
        ("Alaska", "Alaska"),
        ("Arizona", "Arizona"),
        ("Arkansas", "Arkansas"),
        ("California", "California"),
        ("Colorado", "Colorado"),
        ("Connecticut", "Connecticut"),
        ("Delaware", "Delaware"),
        ("Florida", "Florida"),
        ("Georgia", "Georgia"),
        ("Hawaii", "Hawaii"),
        ("Idaho", "Idaho"),
        ("Illinois", "Illinois"),
        ("Indiana", "Indiana"),
        ("Iowa", "Iowa"),
        ("Kansas", "Kansas"),
        ("Kentucky", "Kentucky"),
        ("Louisiana", "Louisiana"),
        ("Maine", "Maine"),
        ("Maryland", "Maryland"),
        ("Massachusetts", "Massachusetts"),
        ("Michigan", "Michigan"),
        ("Minnesota", "Minnesota"),
        ("Mississippi", "Mississippi"),
        ("Missouri", "Missouri"),
        ("Montana", "Montana"),
        ("Nebraska", "Nebraska"),
        ("Nevada", "Nevada"),
        ("New Hampshire", "New Hampshire"),
        ("New Jersey", "New Jersey"),
        ("New Mexico", "New Mexico"),
        ("New York", "New York"),
        ("North Carolina", "North Carolina"),
        ("North Dakota", "North Dakota"),
        ("Ohio", "Ohio"),
        ("Oklahoma", "Oklahoma"),
        ("Oregon", "Oregon"),
        ("Pennsylvania", "Pennsylvania"),
        ("Rhode Island", "Rhode Island"),
        ("South Carolina", "South Carolina"),
        ("South Dakota", "South Dakota"),
        ("Tennessee", "Tennessee"),
        ("Texas", "Texas"),
        ("Utah", "Utah"),
        ("Vermont", "Vermont"),
        ("Virginia", "Virginia"),
        ("Washington", "Washington"),
        ("West Virginia", "West Virginia"),
        ("Wisconsin", "Wisconsin"),
        ("Wyoming", "Wyoming"),
        ("District of Columbia", "District of Columbia"),
        ("American Samoa", "American Samoa"),
        ("Northern Mariana Islands", "Northern Mariana Islands"),
        ("Puerto Rico", "Puerto Rico"),
        ("United States Minor Outlying Islands", "United States Minor Outlying Islands"),
        ("Virgin Islands, U.S.", "Virgin Islands, U.S."),
        
        
    ]
    position = [
        ("CEO", "CEO"),
        ("GMD", "GMD"),
        ("CTO", "CTO"),
        ("Supervisor", "Supervisor"),
        ("Accountant", "Accountant"),
        ("Marketer", "Marketer"),
        ("Cashier", "Cashier"),
        ("Driver", "Driver"),
        ("Customer care", "Customer care")
    
    ]

    marital_status = [
        ("Single", "Single"),
        ("Engaged", "Engaged"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
        ("Complicated", "Complicated"),
        ("Widow", "Widow"),
    ]

    user_status = [
        ("Active", "Active"),
        ("Retired", "Retired"),
        ("Suspended", "Suspended"),
        ("Freeze", "Freeze"),
        ("On Leave", "On Leave"),
    ]

    sex = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]



    profile = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(unique=False, null=True, max_length=20)
    email = models.EmailField(unique=True, null=True, max_length=50)
    date_of_birth = models.DateField(unique=False, null=True, max_length=20, blank=True)
    phone_number = models.CharField(unique=True, max_length=11, null=True)
    sex = models.CharField(choices=sex, max_length=20, null=True, unique=False)
    nationality = models.CharField(choices=countries, unique=False, max_length = 50, null=True)
    state = models.CharField(choices=states, unique=False, max_length=50, null=True)
    city = models.CharField(unique=False, max_length=50, null=True)
    address = models.CharField(unique=False, max_length=100, null=True)
    occupation = models.CharField(unique=False, null=True, max_length=50)
    profile_passport = models.ImageField(upload_to='userimage/', unique=False, null=True)
    position = models.CharField(choices=position, unique=False, max_length=20, null=True)
    marital_status = models.CharField(choices=marital_status, unique=False, max_length=20, null=True)
    staff = models.BooleanField(default=False, unique=False, null=True)
    user_status = models.CharField(choices=user_status, unique=False, max_length=20, null=True)




    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
