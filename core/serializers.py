from djoser.serializers import UserCreatePasswordRetypeSerializer as BaseUserCreatePasswordRetypeSerializer,UserSerializer as BaseUserSerializer

class UserCreatePasswordRetypeSerializer(BaseUserCreatePasswordRetypeSerializer):
    class Meta(BaseUserCreatePasswordRetypeSerializer.Meta):
        fields = ['id','username','first_name','last_name','password','re_password','phone','email']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','username','first_name','last_name','phone','email']