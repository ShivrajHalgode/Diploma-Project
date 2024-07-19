#from django.urls import path
#from . import views

#urlpatterns = [
#path('', views.index, name="index"),
#path('paint.py', views.paint.py),
#]
from django.urls import path
import views


app_name = 'Certification_Gen'

urlpatterns = [
    path('', views.your_view_function, name='your_view_function'),
   # path('paint.py', paint.py)
]

