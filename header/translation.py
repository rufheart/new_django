from dataclasses import field
from re import I
from modeltranslation.translator import translator, TranslationOptions
from header.models import Detail_Product

class MyForm(TranslationOptions):
    fields = ('desc','slug')

translator.register(Detail_Product, MyForm)    