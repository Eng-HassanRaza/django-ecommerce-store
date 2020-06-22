from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from allauth.account.forms import SignupForm
from core.models import VendorProfile

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

CATEGORY_CHOICES = (
    ('C', 'Cat'),
    ('D', 'Dog'),
    ('P', 'Parrot')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)

class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['shop'] = forms.CharField(required=True)
    def save(self, request):
        shop = self.cleaned_data.pop('shop')
        user = super(MyCustomSignupForm, self).save(request)


class ShopForm(forms.Form):
    shop_name = forms.CharField(required=False)
    shop_log = forms.CharField(required=False)
    shop_category = forms.ChoiceField(
        widget=forms.Select(choices=CATEGORY_CHOICES)
    )
    shop_desc = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))



class VendorSignupForm(SignupForm):
    shop_name = forms.CharField(max_length=50, required=True, strip=True,widget=forms.TextInput(
    attrs={
           'placeholder': 'Shop Name'}))
    def save(self, request):
        user = super(VendorSignupForm, self).save(request)
        vendor_profile = VendorProfile(
            user=user,
            shop_name=self.cleaned_data.get('shop_name')
        )
        vendor_profile.save()
        return vendor_profile.user
