from django.urls import path
from . import views


app_name = 'pybo'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('laws_data/', views.laws_data, name='laws_data'),
    path('regulation_data/', views.regulation_data, name='regulation_data'),
    path('SKTL_Policy/', views.SKTL_Policy, name='SKTL_Policy'),
    path('GuideManual/', views.GuideManual, name='GuideManual'),
    path('Trend/', views.Trend, name='Trend'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('fileupload/', views.fileUpload, name='fileupload'),
    path('laws/create', views.laws_create, name='laws_create'),
]
