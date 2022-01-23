from django.urls import path 
  

# importing views from views..py 
from .views import chooseJD2,chooseJD,model_form_upload,home_view , geeks_view,list_viewjd, list_view,search_view,search_view_ver2
  
urlpatterns = [ 
    path('', home_view ),
    path('docupload', model_form_upload ),
    path('choose', chooseJD ),
    path('choose2', chooseJD2 ,name='choose2'),
    path('sample1', geeks_view ),
    
    path('search', search_view ),
    path('search2', search_view_ver2),
    
    path('list', list_view ),
    
    path('listjd', list_viewjd, name='listjd' ),
] 