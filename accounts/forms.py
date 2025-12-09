from django import forms 
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User 
class CleanUserCreationForm (UserCreationForm):
  email = forms.EmailField(required = True)
  class Meta(UserCreationForm.Meta):
    model = User
    fields = ("username","email","password1","password2")
    help_texts = {f:"" for f in fields}
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    for f in self.fields.values():
      f.help_text = ""

    self.fields["username"].widget.attrs.update({"placeholder":"Enter Username"})
    self.fields["email"].widget.attrs.update({
      "placeholder":"Enter Email",
      "name": "register_email"})
    self.fields["password1"].widget.attrs.update({
            "placeholder": "New Password"
        })

    self.fields["password2"].widget.attrs.update({
            "placeholder": "Confirm Password"
        })
  def clean_email(self):
    email = self.cleaned_data.get("email")
    if User.objects.filter(email = email).exists():
      raise forms.ValidationError("This email is already in use")
    return email
