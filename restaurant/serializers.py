from rest_framework import serializers
from . models import menu

class MenuSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = menu
      fields = '__all__'

   
