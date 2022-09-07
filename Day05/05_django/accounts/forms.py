from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
        
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        # 이거만 있으면 온갖게 다 보여짐 -> fields 변경
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
        # 비밀번호는 암호화 문제 -> 따로 처리해야함