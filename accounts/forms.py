#returns the user model that's currently active in the project
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# when user is ready to sign up, will will call usercreationform from auth.form
class UserCreateForm(UserCreationForm):

    class Meta:
        #these fields come with the authorization user models
        fields = ('username', 'email', 'password1', 'password2')
        #allows us to get the current model of who's accessing the website
        model = get_user_model()

        #label is up labels like in the form html but here.  not needed.  only for customization
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'