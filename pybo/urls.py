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
    path('laws/<int:laws_id>/', views.laws_detail, name='laws_detail'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('laws_answer/create/<int:laws_id>/', views.laws_answer_create, name='laws_answer_create'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('fileupload/', views.fileUpload, name='fileupload'),
    path('laws/create', views.laws_create, name='laws_create'),
    path('download/<int:pk>', views.laws_download_view, name="laws_download"),

    #<int: >안에 들어가는 변수명은 view 에서 받는 함수의 () 인자명과 일치해야해
    #answer_create 가 views.answer_create 를 호출하고 <int:quesiton_id>를 넘깁니다.
    #view.answer_create 함수에는 "def answer_create(request, question_id):" 와 같이 () 안의 인자명과 일치해야함
]
