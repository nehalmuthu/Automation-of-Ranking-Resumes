
# import the standard Django Model 
# from built-in library 
from django.db import models 
   
# declare a new model with a name "GeeksModel" 
class GeeksModel(models.Model): 
  
    # fields of the model 
    title = models.CharField(max_length = 200) 
    description = models.TextField() 
  
    # renames the instances of the model 
    # with their title name 
    def __str__(self): 
        return self.title 
    
    
  
# declare a new model with a name "GeeksModel" 
class myModel(models.Model): 
        # fields of the model 
    title = models.CharField(max_length = 200) 
    description = models.TextField() 
    last_modified = models.DateTimeField(auto_now_add = True) 
    img = models.ImageField(upload_to = "images/") 
  
        # renames the instances of the model 
        # with their title name 
    def __str__(self): 
        return self.title 
    
    

# declare a new model with a name "GeeksModel" 
class JobDescription(models.Model): 
    # fields of the model 
    title = models.CharField(max_length = 200) 
    document = models.FileField(upload_to='documentsJD/')
    
            # renames the instances of the model 
        # with their title name 
    def __str__(self): 
        return self.title 