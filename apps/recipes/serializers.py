from rest_framework import serializers
from models import *


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        depth = 1