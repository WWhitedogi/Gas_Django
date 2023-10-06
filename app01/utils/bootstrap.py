from django import forms

class Bootstrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 如果 "class" 属性不存在，添加它
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
            # 如果 "placeholder" 属性不存在，添加它
            if 'placeholder' not in field.widget.attrs:
                field.widget.attrs['placeholder'] = field.label

class BootStrapModelForm(Bootstrap,forms.ModelForm):
    pass

class BootStrapForm(Bootstrap,forms.Form):
    pass