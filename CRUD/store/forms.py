from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from .models import ContactTable


class Contact(forms.ModelForm):
    class Meta:
        model = ContactTable
        fields = ['first_name', 'last_name', 'email', 'phone', 'membership']
        # Define validators for fields here
        validators = {
            'first_name': [MinLengthValidator(limit_value=4), MaxLengthValidator(limit_value=20)],
            'last_name': [MinLengthValidator(limit_value=4), MaxLengthValidator(limit_value=20)],
            'email': [MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=30)],
            'phone': [MinLengthValidator(limit_value=11), MaxLengthValidator(limit_value=15)],
        }

    first_name = forms.CharField(
        label='First Name',
        error_messages={'required': 'Please Enter Your first NAme'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Please Enter first Name',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        error_messages={'required': 'Please Enter Your Last Name'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Please Enter Last Name',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        initial='xyz@gmail.com',
        error_messages={'required': 'Please Enter Your Email'},
        widget=forms.TextInput(attrs={
            'placeholder': 'xyz@gmail.com',
            'class': 'form-control'
        })
    )

    phone = forms.CharField(label='Phone No', initial='12345678921', error_messages={
        'required': 'Please Enter Your Phone No'
    }, label_suffix='!', widget=forms.TextInput(attrs={
        'placeholder': '+923075239903',
        'class': 'form-control'
    }))

    membership = forms.ChoiceField(
        label='Please Choose Membership',
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
        choices=ContactTable.MEMBERSHIP_CHOICES
    )


# class Contact(forms.Form):
#     @staticmethod
#     def validate_name(value):
#         if not value[0].isupper():
#             raise ValidationError(
#                 'First letter Must start with a Capital Letter')
#         if not value.isalpha():
#             raise ValidationError('Name must only contain letters.')

#     @staticmethod
#     def validate_custom_email(value):
#         if '@' not in value or '.' not in value.split('@')[1]:
#             raise ValidationError(
#                 'Email must contain "@" and at least one "." in the domain.')

#     first_name = forms.CharField(
#         label='First Name',
#         max_length=50,
#         error_messages={
#             'required': 'Please Enter First Name',
#         }, label_suffix=':', widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Enter First Name',
#                 'class': 'form-control'
#             }
#         ), validators=[
#             MinLengthValidator(limit_value=4),
#             MaxLengthValidator(limit_value=30),
#             validate_name
#         ]
#     )

#     last_name = forms.CharField(
#         label='Last Name',
#         max_length=50,
#         error_messages={
#             'required': 'Please Enter Last Name',
#         }, label_suffix='::::', widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Enter Last Name',
#                 'class': 'form-control'
#             }
#         ), validators=[
#             MinLengthValidator(limit_value=4),
#             MaxLengthValidator(limit_value=30),
#             validate_name
#         ]
#     )

#     email = forms.EmailField(
#         label='Email', error_messages={
#             'required': 'Please Enter Your Email'
#         }, widget=forms.TextInput(attrs={
#             'placeholder': 'xyz@gmail.com',
#             'class': 'form-control'
#         }), validators=[validate_custom_email,
#                         MinLengthValidator(limit_value=10),
#                         MaxLengthValidator(limit_value=30)]
#     )

#     phone_no = forms.CharField(label='Phone No', error_messages={
#         'required': 'Please Enter Your Phone No'
#     }, label_suffix='!', widget=forms.TextInput(attrs={
#         'placeholder': '+923075239903',
#         'class': 'form-control'
#     }), validators=[
#         MinLengthValidator(limit_value=11),
#         MaxLengthValidator(limit_value=15)
#     ])
