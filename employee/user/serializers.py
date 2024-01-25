from rest_framework  import serializers


from user.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('userName', 'passWord','firstName','lastName','email','isAdmin','birthday','position','departmentName','describe','phoneNumber')


