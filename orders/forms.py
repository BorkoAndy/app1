from django import forms

class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField()


    
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Enter your first name",
    #         }
    #     )
    # )

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Enter your last name",
    #         }
    #     )
    # )

    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Phone number",
    #         }
    #     )
    # )

    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial=0,
    # )

    # delivery_adreaa = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "id": "delivery-address",
    #             "rows": 2,
    #             "placeholder": "Enter address",
    #         }
    #     )
    # )   

    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #         choices=[
    #             ("0", False),
    #             ("1", True),
    #         ],
    #         initial=0,
    # )