"""
The following models represent Doctor-related information and custom authentication tokens.
"""

# Import necessary modules and classes
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.core.exceptions import ValidationError
import secrets

# Model for Doctor information
class Doctor(AbstractUser):
    """
    Model representing Doctor information.

    - Inherits from Django's AbstractUser, providing basic user functionality.
    - Defines additional fields specific to Doctor profiles such as first name, last name, gender, etc.
    - Specifies custom validation for the password field to ensure complexity requirements.
    - Includes image field for profile pictures.
    - Defines permissions for viewing users.
    """

    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender_choices = [
        ("M", "Male"),
        ("F", "Female")
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    phone = models.CharField(max_length=20)
    license_number = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    graduation_date = models.DateField()
    university = models.CharField(max_length=255)
    password_validator = RegexValidator(
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        message="Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character."
    )
    password = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(limit_value=8), password_validator]
    )
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def clean(self):
        """
        Custom validation method for Doctor instances.

        - Overrides the clean method to include additional validation for the password field.
        """

        super().clean()
        # Custom password validation
        if not self.password_validator(self.password):
            raise ValidationError("Password does not meet the required criteria.")

    def __str__(self):
        """
        Method to represent Doctor objects as strings.
        """
        return self.email
    class Meta:
        """
        Meta class for Doctor model.
        """
        permissions = [("view_user", "Can view user")]

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="doctor_set",
        related_query_name="doctor",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="doctor_set",
        related_query_name="doctor",
    )

# Model for custom authentication tokens
class CustomToken(models.Model):
    """
    Model representing custom authentication tokens for Doctor users.

    - Stores a unique token associated with a Doctor.
    - Links each token to a Doctor instance.
    - Generates a token using secrets module if not provided.
    - Sets the email field based on the associated Doctor's email.
    """

    key = models.CharField(max_length=64, unique=True, blank=True)
    doctor = models.ForeignKey(Doctor, related_name='custom_tokens', on_delete=models.CASCADE)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'CustomToken'
        verbose_name_plural = 'CustomTokens'

    def save(self, *args, **kwargs):
        """
        Method to save CustomToken instances.

        - Overrides the save method to generate a token and set the email if not provided.
        """
        
        if not self.key:
            self.key = secrets.token_hex(32)
        if not self.email:
            self.email = self.doctor.email
        return super().save(*args, **kwargs)