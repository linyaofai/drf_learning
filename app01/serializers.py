from rest_framework import  serializers
from app01.models import *

class UserInfoSerializer(serializers.Serializer):
    name = serializers.CharField(label='名字', max_length=11)
    price = serializers.IntegerField(label='价格', required=True)
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

        # def validate_name(self, value):
        #     if len(value) > 9:
        #         raise serializers.ValidationError("名字的长度不能大于9")
        #     return value

        def validate(self, attrs):
            name = attrs['name']
            price = attrs['price']
            if name.isnumeric():
                raise serializers.ValidationError('名字不能有数字')
            if price > 250:
                raise serializers.ValidationError('价格不能太贵')
            return attrs


    class Meta:
        model =Book
        fields = '__all__'

        extra_kwargs = {
            'name': {
                'min_length': 6,
                'max_length': 12,
                'error_messages': {
                    'min_length': '6个字符',
                    'max_length': '12个字符',
                },
            },
            'price': {
                'help_text': '６－８位',
            }
        }
