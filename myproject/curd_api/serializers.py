from rest_framework import serializers
from .models import Student

# def start_with_101(value):
#     if value[0].lower()!='a':
#         raise serializers.ValidationError("name should be start wiht a")
#     return value

class SerializerStudent(serializers.Serializer):

    name = serializers.CharField(max_length =100)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)
    contect_no = serializers.IntegerField()

# this function are data creation !
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
# # this function are update data !

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll_no = validated_data.get('roll_no',instance.roll_no)
        instance.city = validated_data.get('city',instance.city)
        instance.contect_no = validated_data.get('contect_no',instance.contect_no)

        instance.save()
        return instance
    

#     # filed level validation !

#     def validate_name(self,value):
#         if value != Student.name.lower():
#             raise serializers.ValidationError('Enter the name are lower case')
#         return value
    
#     # object level validation !

#     def validate(self, data):
#         name = data.get("name")
#         roll = data.get("roll")
#         if name == name.lower() and roll <= 200 :
#             raise serializers.ValidationError("roll_no must be gretor then 200")
#         return data


