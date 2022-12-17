from rest_framework import serializers

class userserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    role  = serializers.CharField()
    company = serializers.CharField()
    discription = serializers.CharField()
    active =serializers.BooleanField()