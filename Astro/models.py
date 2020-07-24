from django.db import models
from django.core.validators import RegexValidator


class Prescription(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name + " " + self.surname


class Enquiry(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    customer_name = models.CharField(max_length=30)
    number = models.CharField(max_length=20, blank=True, validators=[alphanumeric])
    email = models.EmailField()
    question = models.TextField()
    reply = models.TextField(default=None, null=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        if self.replied:
            string = self.customer_name + "-" + " replied"
        else:
            string = self.customer_name + "-" + " pending"
        return string


class Order(models.Model):
    buyer_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    product = models.CharField(max_length=30, choices=(('0', 'Choose product..'), ('1', 'Sanitizer'),
                                                       ('2', 'Antibiotics'), ('3', 'Amoxol-23'),
                                                       ('4', 'Hydroxly-Peroxide'), ('5', 'Paracetamol'),
                                                       ('6', 'Heat rub'), ('7', 'Amole'), ('8', 'JK4')),
                               default='0')

    quantity = models.IntegerField(default=0)
    city = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30,
                               choices=(('0', 'Select Your country..'), ('1', 'Zimbabwe'), ('2', 'Zambia'),
                                        ('3', 'South Africa'), ('4', 'Virgin Islands'), ('5', 'Algeria'),
                                        ('6', 'Botswana'), ('7', 'Cameroon'), ('8', 'Germany'),
                                        ('9', 'Other')), default='0')
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.buyer_name
