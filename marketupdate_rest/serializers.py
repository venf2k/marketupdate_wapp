from rest_framework import serializers
from marketupdate_model.models import Update, Category, Symbol, Value, all_last_update_v


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = [ 'pk', 'notes_text', 'pub_date', 'pub_hour', ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'pk', 'name', 'description', 'update', ]

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = [ 'pk', 'name', 'description', 'category', ]



class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = [ 'pk', 'value', 'unit', 'precision', 'val_format', 'val_sequence', 'description', 'symbol', ]


class AllLastUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_last_update_v
        val_unit_display = serializers.CharField(source='get_val_unit_display')
        fields = ['val_value', 'val_unit', 'val_precision', 'val_format', 'val_sequence', 'val_description', 'sym_name', 'sym_des', 'cat_name', 'cat_des', 'pub_date', 'pub_hour',]
