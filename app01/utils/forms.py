from app01 import models
from django import  forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.pagination import Pagination
from app01.utils.bootstrap import BootStrapModelForm
class UserModelForm(BootStrapModelForm):
    name=forms.CharField(
        min_length=3,
        label="username",
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account","create_time", "gender", "depart"]


class NumberModelForm(BootStrapModelForm):
# validation1
    mobile=forms.CharField(
        label="phone number",
        validators=[RegexValidator(r'^1[0-9]+$' , 'wrong number format')]
    )
    class Meta:
        model=models.Number_Manage
        fields=["mobile","price","level","status"]
        #all
        # fields="__all__"
        #exclue some item
        # exlude=['level']
#不用了解，知道怎么用就行了
    #validation2
    def clean_mobile(self):#当前

        txt_mobile = self.cleaned_data.get("mobile")

        exists=models.Number_Manage.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise forms.ValidationError("phone number already exists")
    #验证通过返回电话
        return txt_mobile

class EditModelForm(BootStrapModelForm):
    # validation1
    mobile = forms.CharField(
        label="phone number",
        validators=[RegexValidator(r'^1[0-9]+$', 'wrong number format')]
    )
    class Meta:
        model = models.Number_Manage
        fields = ["mobile", "price", "level", "status"]
    # validation2
    def clean_mobile(self):  # 当前
        #pk, primary key, the id of editing row
        #self.instance.pk

        txt_mobile = self.cleaned_data.get("mobile")

        exists = models.Number_Manage.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise forms.ValidationError("number already exists")
        return txt_mobile