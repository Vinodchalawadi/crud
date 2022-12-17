from rest_framework import serializers
from authapp.models import user

class userserializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = user
        fields = '__all__'
        # exclude = ['active']

    def  get_len_name(self, object):
        return len(object.name)



# class userserializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length = 20)
#     role  = serializers.CharField(max_length = 20)
#     company = serializers.CharField(max_length = 20)
#     discription = serializers.CharField(max_length = 20)
#     active =serializers.BooleanField()
    
    def create(self, validated_data):
        return user.objects.create(**validated_data)

    
    


    def update(self, instanse, validated_data):
        instanse.name = validated_data.get('name', instanse.name)
        instanse.role = validated_data.get('role', instanse.role)
        instanse.company = validated_data.get('company', instanse.company)
        instanse.discription = validated_data.get('discription', instanse.discription)
        instanse.active = validated_data.get('active', instanse.active)
        instanse.save()
        return instanse

    def  validate(self, data):
        if data['role'] == data['discription']:
            raise serializers.ValidationError('Role and description should be diffrent')
        else:
            return data
     
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('Nmae should be at leat 4 characters')
        else:
            return value

    
         