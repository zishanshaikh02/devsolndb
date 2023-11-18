from .models import Blog
from rest_framework.serializers import ModelSerializer 



class BlogSerializer(ModelSerializer):

    class Meta :

        model = Blog
        fields = "__all__"


# from .models import Contact

# class ContactSerializer(ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = '__all__'

from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
