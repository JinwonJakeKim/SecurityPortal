from django.urls import path
from . import views


app_name = 'pybo'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('laws_data/', views.laws_data, name='laws_data'),
    path('regulation_data/', views.regulation_data, name='regulation_data'),
    path('SKTL_policy_data/', views.SKTL_policy_data, name='SKTL_policy_data'),
    path('guide_data/', views.guide_data, name='guide_data'),
    path('trend_data/', views.trend_data, name='trend_data'),
    path('magazine_data/', views.magazine_data, name='magazine_data'),
    path('', views.index, name='index'),
    path('laws/<int:laws_id>/', views.laws_detail, name='laws_detail'),
    path('regulation_detail/<int:regulation_id>/', views.regulation_detail, name='regulation_detail'),
    path('SKTL_policy_detail/<int:SKTL_policy_id>/', views.SKTL_policy_detail, name='SKTL_policy_detail'),
    path('guide_detail/<int:guide_id>/', views.guide_detail, name='guide_detail'),
    path('trend_detail/<int:trend_id>/', views.trend_detail, name='trend_detail'),
    path('magazine_detail/<int:magazine_id>/', views.magazine_detail, name='magazine_detail'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('laws_answer/create/<int:laws_id>/', views.laws_answer_create, name='laws_answer_create'),
    path('regulation_answer/create/<int:regulation_id>/', views.regulation_answer_create, name='regulation_answer_create'),
    path('SKTL_policy_answer/create/<int:SKTL_policy_id>/', views.SKTL_policy_answer_create, name='SKTL_policy_answer_create'),
    path('guide_answer/create/<int:guide_id>/', views.guide_answer_create, name='guide_answer_create'),
    path('trend_answer/create/<int:trend_id>/', views.trend_answer_create, name='trend_answer_create'),
    path('magazine_answer/create/<int:magazine_id>/', views.magazine_answer_create, name='magazine_answer_create'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('fileupload/', views.fileUpload, name='fileupload'),
    path('laws/create', views.laws_create, name='laws_create'),
    path('regulation/create', views.regulation_create, name='regulation_create'),
    path('SKTL_policy/create', views.SKTL_policy_create, name='SKTL_policy_create'),
    path('guide/create', views.guide_create, name='guide_create'),
    path('trend/create', views.trend_create, name='trend_create'),
    path('magazine/create', views.magazine_create, name='magazine_create'),
    path('download/<int:pk>', views.laws_download_view, name="laws_download"),
    path('download/<int:pk>', views.regulation_download_view, name="regulation_download"),
    path('download/<int:pk>', views.SKTL_policy_download_view, name="SKTL_policy_download"),
    path('download/<int:pk>', views.guide_download_view, name="guide_download"),
    path('download/<int:pk>', views.trend_download_view, name="trend_download"),
    path('download/<int:pk>', views.magazine_download_view, name="magazine_download"),

    #<int: >안에 들어가는 변수명은 view 에서 받는 함수의 () 인자명과 일치해야해
    #answer_create 가 views.answer_create 를 호출하고 <int:quesiton_id>를 넘깁니다.
    #view.answer_create 함수에는 "def answer_create(request, question_id):" 와 같이 () 안의 인자명과 일치해야함
]
