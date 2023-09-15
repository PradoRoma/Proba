from django import forms

class UserForm(forms.Form):
    header = forms.CharField(label = "Название темы", initial= "Как вам мой сайт?", widget = forms.TextInput(attrs = {"class":"myfield"}))
    name = forms.CharField(label="Имя", help_text="Введите ваше имя", min_length = 2, max_length = 20, widget = forms.TextInput(attrs = {"class":"myfield"}))
    age = forms.IntegerField(label = "Возраст", help_text="Введите ваш возраст", required= False, min_value = 1, max_value = 120, widget = forms.TextInput(attrs = {"class":"myfield"}))
    email = forms.EmailField(label= "Почта", help_text= "Введите вашу почту", required = False, min_length = 10, widget = forms.TextInput(attrs = {"class":"myfield"}))
    weight = forms.DecimalField(label="Масса тела", min_value = 3, max_value = 200, decimal_places = 2, widget = forms.TextInput(attrs = {"class":"myfield"}))
    comment = forms.CharField(label = "Комментарий", widget= forms.Textarea(attrs = {"class":"myfield"}), min_length = 1, max_length = 250)
    required_css_class = "field"
    error_css_class = "error"
    ield_order = ["header", "name", "age", "weight", "email", "comment"]