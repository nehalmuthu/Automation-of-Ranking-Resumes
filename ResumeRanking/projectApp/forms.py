# import form class from django 
from django import forms 
   
# import GeeksModel from models.py 
from .models import GeeksModel, JobDescription 
   
# create a ModelForm 
class GeeksForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = GeeksModel 
        fields = "__all__"



class JDForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ('title', 'document')