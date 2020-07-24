from django import forms
from .models import Enquiry, Prescription, Order


class ModalEnquiry(forms.ModelForm):
    class Meta:
        model = Enquiry

        fields = {
            'customer_name',
            'number',
            'email',
            'question',

        }

        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Customer name'

            }),

            'number': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Customer number'

            }),

            'email': forms.EmailInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Email'

            }),

            'question': forms.Textarea(attrs={
                'content': 'Textarea',
                'class': "form-control inp",
                'placeholder': 'Enquiry'

            }),
        }


class ModalPrescription(forms.ModelForm):
    class Meta:
        model = Prescription

        fields = {
            'name',
            'surname',
            'email',
            'description'

        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Your name'

            }),

            'surname': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Your surname'

            }),

            'email': forms.EmailInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Your Email'

            }),

            'description': forms.Textarea(attrs={
                'content': 'Textarea',
                'class': "form-control inp",
                'placeholder': 'Describe what you are feeling here...'

            }),
        }


class ModalOrder(forms.ModelForm):
    class Meta:
        model = Order

        fields = {
            'buyer_name',
            'email',
            'address',
            'product',
            'quantity',
            'city',
            'country',
            'confirmed'

        }

        widgets = {
            'buyer_name': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Your name'

            }),

            'email': forms.EmailInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Your Email'

            }),

            'address': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Your address'

            }),

            'quantity': forms.NumberInput(attrs={
                'class': "form-control inp",

            }),

            'city': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'City'

            }),

        }
