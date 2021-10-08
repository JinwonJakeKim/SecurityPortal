from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Model_laws_data, Model_regulation, Model_SKTL_policy, Model_guide, Model_trend, FileUpload, Model_magazine
from django.utils import timezone
from .forms import QuestionForm, AnswerForm, FileUploadForm, laws_Form, laws_AnswerForm, regulation_AnswerForm, SKTL_policy_AnswerForm, guide_AnswerForm, trend_AnswerForm, regulation_Form, SKTL_policy_Form, guide_Form, trend_Form, magazine_Form, magazine_AnswerForm
from django.core.paginator import Paginator

import urllib
import os
from django.http import HttpResponse, Http404
import mimetypes

def home(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/home.html')

def laws_data(request):
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    laws_list = Model_laws_data.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(laws_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'laws_list': page_obj}
    return render(request, 'pybo/laws_list.html', context)

def regulation_data(request):
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    regulation_list = Model_regulation.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(regulation_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'regulation_list': page_obj}
    return render(request, 'pybo/regulation_list.html', context)

def SKTL_policy_data(request):
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    SKTL_policy_list = Model_SKTL_policy.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(SKTL_policy_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'SKTL_policy_list': page_obj}
    return render(request, 'pybo/SKTL_policy_list.html', context)

def guide_data(request):
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    guide_list = Model_guide.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(guide_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'guide_list': page_obj}
    return render(request, 'pybo/guide_list.html', context)

def trend_data(request):
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    trend_list = Model_trend.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(trend_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'trend_list': page_obj}
    return render(request, 'pybo/trend_list.html', context)

def magazine_data(request):
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    magazine_list = Model_magazine.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(magazine_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'magazine_list': page_obj}
    return render(request, 'pybo/magazine_list.html', context)

def index(request):
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    question_list = Question.objects.order_by('-create_date')


    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #id에 해당하는 Quesiton 객체를 get
    context = {'question': question} #위에서 get한 question 객체를 text 화
    return render(request, 'pybo/question_detail.html', context)

def laws_detail(request, laws_id):
    laws_detail = get_object_or_404(Model_laws_data, pk=laws_id) #id에 해당하는 Model_laws_data 객체를 get
    context = {'laws_detail': laws_detail} #' ' 안의 변수를 그대로 .html 파일에서 변수 사용(변수명 동일 필수)
    return render(request, 'pybo/laws_detail.html', context)

def regulation_detail(request, regulation_id):
    regulation_detail = get_object_or_404(Model_regulation, pk=regulation_id) #id에 해당하는 Model_laws_data 객체를 get
    context = {'regulation_detail': regulation_detail} #' ' 안의 변수를 그대로 .html 파일에서 변수 사용(변수명 동일 필수)
    return render(request, 'pybo/regulation_detail.html', context)

def SKTL_policy_detail(request, SKTL_policy_id):
    SKTL_policy_detail = get_object_or_404(Model_SKTL_policy, pk=SKTL_policy_id) #id에 해당하는 Model_laws_data 객체를 get
    context = {'SKTL_policy_detail': SKTL_policy_detail} #' ' 안의 변수를 그대로 .html 파일에서 변수 사용(변수명 동일 필수)
    return render(request, 'pybo/SKTL_policy_detail.html', context)

def guide_detail(request, guide_id):
    guide_detail = get_object_or_404(Model_guide, pk=guide_id) #id에 해당하는 Model_laws_data 객체를 get
    context = {'guide_detail': guide_detail} #' ' 안의 변수를 그대로 .html 파일에서 변수 사용(변수명 동일 필수)
    return render(request, 'pybo/guide_detail.html', context)

def trend_detail(request, trend_id):
    trend_detail = get_object_or_404(Model_trend, pk=trend_id) #id에 해당하는 Model_laws_data 객체를 get
    context = {'trend_detail': trend_detail} #' ' 안의 변수를 그대로 .html 파일에서 변수 사용(변수명 동일 필수)
    return render(request, 'pybo/trend_detail.html', context)

def magazine_detail(request, trend_id):
    trend_detail = get_object_or_404(Model_magazine, pk=trend_id) #id에 해당하는 Model_laws_data 객체를 get
    context = {'magazine_detail': trend_detail} #' ' 안의 변수를 그대로 .html 파일에서 변수 사용(변수명 동일 필수)
    return render(request, 'pybo/magazine_detail.html', context)

def question_create(request):
    """
    pybo  질문 등록, 맨처음 이 페이지에 질문을 등록하기위해 진입할때는 GET 방식으로 진입되어 Else 문이 실행되고
    해당 form 에서 submit을 누르면 POST 방식으로 요청되어 데이터가 저장된다.
    if == POST -> 입력후 실행부분 , if == GET -> 입력전 실행부분
    """
    if request.method == 'POST': #저장하기, 입력후 실행부
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.imgfile = request.FILES["imgfile"] #!!! 반드시 files 은 이처럼 따로 request의 files 을 따로 모델속성에 저장해줘야한다.
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
            #question_form.html에서 입력한 값을 POST 보내서 위 코드로 저장이 되면 index 함수를 호출시켜서 결국 question_list.html 보여지도록 Redirection
    else:
        # request.method 가 'GET'인 경우 호출됨, 질문등록하기, 입력전 실행부
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'pybo/question_form.html', context)

def laws_create(request):
    """
    pybo  질문 등록, 맨처음 이 페이지에 질문을 등록하기위해 진입할때는 GET 방식으로 진입되어 Else 문이 실행되고
    해당 form 에서 submit을 누르면 POST 방식으로 요청되어 데이터가 저장된다.
    if == POST -> 입력후 실행부분 , if == GET -> 입력전 실행부분
    """
    if request.method == 'POST': #저장하기, 입력후 실행부
        form = laws_Form(request.POST, request.FILES)#laws_Form 에서 정의된 인자는 1개(forms.ModelForm) 이더라도 request.FILES 따로 받을 수 있음
        if form.is_valid():
            laws = form.save(commit=False)
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    laws.filename = request.FILES['upload_files'].name
            #laws.upload_files = request.FILES["upload_files"] #!!! 반드시 files 은 이처럼 따로 request의 files 을 따로 모델속성에 저장해줘야한다.
            laws.create_date = timezone.now()
            laws.save()
            return redirect('pybo:laws_data')
            #question_form.html에서 입력한 값을 POST 보내서 위 코드로 저장이 되면 index 함수를 호출시켜서 결국 question_list.html 보여지도록 Redirection
    else:
        # request.method 가 'GET'인 경우 호출됨, 질문등록하기, 입력전 실행부
        form = laws_Form()
    context = {
        'form': form
    }
    return render(request, 'pybo/laws_form.html', context)

def regulation_create(request):
    """
    pybo  질문 등록, 맨처음 이 페이지에 질문을 등록하기위해 진입할때는 GET 방식으로 진입되어 Else 문이 실행되고
    해당 form 에서 submit을 누르면 POST 방식으로 요청되어 데이터가 저장된다.
    if == POST -> 입력후 실행부분 , if == GET -> 입력전 실행부분
    """
    if request.method == 'POST': #저장하기, 입력후 실행부
        form = regulation_Form(request.POST, request.FILES)#regulation_Form 에서 정의된 인자는 1개(forms.ModelForm) 이더라도 request.FILES 따로 받을 수 있음
        if form.is_valid():
            regulation = form.save(commit=False)
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    regulation.filename = request.FILES['upload_files'].name
            #regulation.upload_files = request.FILES["upload_files"] #!!! 반드시 files 은 이처럼 따로 request의 files 을 따로 모델속성에 저장해줘야한다.
            regulation.create_date = timezone.now()
            regulation.save()
            return redirect('pybo:regulation_data')
            #question_form.html에서 입력한 값을 POST 보내서 위 코드로 저장이 되면 index 함수를 호출시켜서 결국 question_list.html 보여지도록 Redirection
    else:
        # request.method 가 'GET'인 경우 호출됨, 질문등록하기, 입력전 실행부
        form = regulation_Form()
    context = {
        'form': form
    }
    return render(request, 'pybo/regulation_form.html', context)

def SKTL_policy_create(request):
    """
    pybo  질문 등록, 맨처음 이 페이지에 질문을 등록하기위해 진입할때는 GET 방식으로 진입되어 Else 문이 실행되고
    해당 form 에서 submit을 누르면 POST 방식으로 요청되어 데이터가 저장된다.
    if == POST -> 입력후 실행부분 , if == GET -> 입력전 실행부분
    """
    if request.method == 'POST': #저장하기, 입력후 실행부
        form = SKTL_policy_Form(request.POST, request.FILES)#SKTL_policy_Form 에서 정의된 인자는 1개(forms.ModelForm) 이더라도 request.FILES 따로 받을 수 있음
        if form.is_valid():
            SKTL_policy = form.save(commit=False)
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    SKTL_policy.filename = request.FILES['upload_files'].name
            #SKTL_policy.upload_files = request.FILES["upload_files"] #!!! 반드시 files 은 이처럼 따로 request의 files 을 따로 모델속성에 저장해줘야한다.
            SKTL_policy.create_date = timezone.now()
            SKTL_policy.save()
            return redirect('pybo:SKTL_policy_data')
            #question_form.html에서 입력한 값을 POST 보내서 위 코드로 저장이 되면 index 함수를 호출시켜서 결국 question_list.html 보여지도록 Redirection
    else:
        # request.method 가 'GET'인 경우 호출됨, 질문등록하기, 입력전 실행부
        form = SKTL_policy_Form()
    context = {
        'form': form
    }
    return render(request, 'pybo/SKTL_policy_form.html', context)

def guide_create(request):
    """
    pybo  질문 등록, 맨처음 이 페이지에 질문을 등록하기위해 진입할때는 GET 방식으로 진입되어 Else 문이 실행되고
    해당 form 에서 submit을 누르면 POST 방식으로 요청되어 데이터가 저장된다.
    if == POST -> 입력후 실행부분 , if == GET -> 입력전 실행부분
    """
    if request.method == 'POST': #저장하기, 입력후 실행부
        form = guide_Form(request.POST, request.FILES)#guide_Form 에서 정의된 인자는 1개(forms.ModelForm) 이더라도 request.FILES 따로 받을 수 있음
        if form.is_valid():
            guide = form.save(commit=False)
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    guide.filename = request.FILES['upload_files'].name
            #guide.upload_files = request.FILES["upload_files"] #!!! 반드시 files 은 이처럼 따로 request의 files 을 따로 모델속성에 저장해줘야한다.
            guide.create_date = timezone.now()
            guide.save()
            return redirect('pybo:guide_data')
            #question_form.html에서 입력한 값을 POST 보내서 위 코드로 저장이 되면 index 함수를 호출시켜서 결국 question_list.html 보여지도록 Redirection
    else:
        # request.method 가 'GET'인 경우 호출됨, 질문등록하기, 입력전 실행부
        form = guide_Form()
    context = {
        'form': form
    }
    return render(request, 'pybo/guide_form.html', context)

def trend_create(request):
    """
    pybo  질문 등록, 맨처음 이 페이지에 질문을 등록하기위해 진입할때는 GET 방식으로 진입되어 Else 문이 실행되고
    해당 form 에서 submit을 누르면 POST 방식으로 요청되어 데이터가 저장된다.
    if == POST -> 입력후 실행부분 , if == GET -> 입력전 실행부분
    """
    if request.method == 'POST': #저장하기, 입력후 실행부
        form = trend_Form(request.POST, request.FILES)#trend_Form 에서 정의된 인자는 1개(forms.ModelForm) 이더라도 request.FILES 따로 받을 수 있음
        if form.is_valid():
            trend = form.save(commit=False)
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    trend.filename = request.FILES['upload_files'].name
            #trend.upload_files = request.FILES["upload_files"] #!!! 반드시 files 은 이처럼 따로 request의 files 을 따로 모델속성에 저장해줘야한다.
            trend.create_date = timezone.now()
            trend.save()
            return redirect('pybo:trend_data')
            #question_form.html에서 입력한 값을 POST 보내서 위 코드로 저장이 되면 index 함수를 호출시켜서 결국 question_list.html 보여지도록 Redirection
    else:
        # request.method 가 'GET'인 경우 호출됨, 질문등록하기, 입력전 실행부
        form = trend_Form()
    context = {
        'form': form
    }
    return render(request, 'pybo/trend_form.html', context)

def magazine_create(request):
    """
    pybo  질문 등록, 맨처음 이 페이지에 질문을 등록하기위해 진입할때는 GET 방식으로 진입되어 Else 문이 실행되고
    해당 form 에서 submit을 누르면 POST 방식으로 요청되어 데이터가 저장된다.
    if == POST -> 입력후 실행부분 , if == GET -> 입력전 실행부분
    """
    if request.method == 'POST': #저장하기, 입력후 실행부
        form = magazine_Form(request.POST, request.FILES)#magazine_Form 에서 정의된 인자는 1개(forms.ModelForm) 이더라도 request.FILES 따로 받을 수 있음
        if form.is_valid():
            magazine = form.save(commit=False)
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    magazine.filename = request.FILES['upload_files'].name
            #magazine.upload_files = request.FILES["upload_files"] #!!! 반드시 files 은 이처럼 따로 request의 files 을 따로 모델속성에 저장해줘야한다.
            magazine.create_date = timezone.now()
            magazine.save()
            return redirect('pybo:magazine_data')
            #question_form.html에서 입력한 값을 POST 보내서 위 코드로 저장이 되면 index 함수를 호출시켜서 결국 question_list.html 보여지도록 Redirection
    else:
        # request.method 가 'GET'인 경우 호출됨, 질문등록하기, 입력전 실행부
        form = magazine_Form()
    context = {
        'form': form
    }
    return render(request, 'pybo/magazine_form.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def laws_answer_create(request, laws_id):
    laws_detail = get_object_or_404(Model_laws_data, pk=laws_id)
    if request.method == "POST":
        form = laws_AnswerForm(request.POST)
        if form.is_valid():
            laws_answer = form.save(commit=False)
            laws_answer.create_date = timezone.now()
            laws_answer.laws_data = laws_detail
            laws_answer.save()
            return redirect('pybo:laws_detail', laws_id=laws_detail.id)
    else:
        form = laws_AnswerForm()
    context = {'laws_detail': laws_detail, 'form': form}
    return render(request, 'pybo/laws_detail.html', context)

def regulation_answer_create(request, regulation_id):
    regulation_detail = get_object_or_404(Model_regulation, pk=regulation_id)
    if request.method == "POST":
        form = regulation_AnswerForm(request.POST)
        if form.is_valid():
            regulation_answer = form.save(commit=False)
            regulation_answer.create_date = timezone.now()
            regulation_answer.regulation = regulation_detail
            regulation_answer.save()
            return redirect('pybo:regulation_detail', regulation_id=regulation_detail.id)
    else:
        form = regulation_AnswerForm()
    context = {'regulation_detail': regulation_detail, 'form': form}
    return render(request, 'pybo/regulation_detail.html', context)

def SKTL_policy_answer_create(request, SKTL_policy_id):
    SKTL_policy_detail = get_object_or_404(Model_SKTL_policy, pk=SKTL_policy_id)
    if request.method == "POST":
        form = SKTL_policy_AnswerForm(request.POST)
        if form.is_valid():
            SKTL_policy_answer = form.save(commit=False)
            SKTL_policy_answer.create_date = timezone.now()
            SKTL_policy_answer.SKTL_policy = SKTL_policy_detail
            SKTL_policy_answer.save()
            return redirect('pybo:SKTL_policy_detail', SKTL_policy_id=SKTL_policy_detail.id)
    else:
        form = SKTL_policy_AnswerForm()
    context = {'SKTL_policy_detail': SKTL_policy_detail, 'form': form}
    return render(request, 'pybo/SKTL_policy_detail.html', context)

def guide_answer_create(request, guide_id):
    guide_detail = get_object_or_404(Model_guide, pk=guide_id)
    if request.method == "POST":
        form = guide_AnswerForm(request.POST)
        if form.is_valid():
            guide_answer = form.save(commit=False)
            guide_answer.create_date = timezone.now()
            guide_answer.Guide = guide_detail
            guide_answer.save()
            return redirect('pybo:guide_detail', guide_id=guide_detail.id)
    else:
        form = guide_AnswerForm()
    context = {'guide_detail': guide_detail, 'form': form}
    return render(request, 'pybo/guide_detail.html', context)

def trend_answer_create(request, trend_id):
    trend_detail = get_object_or_404(Model_trend, pk=trend_id)
    if request.method == "POST":
        form = trend_AnswerForm(request.POST)
        if form.is_valid():
            trend_answer = form.save(commit=False)
            trend_answer.create_date = timezone.now()
            trend_answer.trend = trend_detail
            trend_answer.save()
            return redirect('pybo:trend_detail', trend_id=trend_detail.id)
    else:
        form = trend_AnswerForm()
    context = {'trend_detail': trend_detail, 'form': form}
    return render(request, 'pybo/trend_detail.html', context)

def magazine_answer_create(request, magazine_id):
    magazine_detail = get_object_or_404(Model_magazine, pk=magazine_id)
    if request.method == "POST":
        form = magazine_AnswerForm(request.POST)
        if form.is_valid():
            magazine_answer = form.save(commit=False)
            magazine_answer.create_date = timezone.now()
            magazine_answer.magazine = magazine_detail
            magazine_answer.save()
            return redirect('pybo:magazine_detail', magazine_id=magazine_detail.id)
    else:
        form = magazine_AnswerForm()
    context = {'magazine_detail': magazine_detail, 'form': form}
    return render(request, 'pybo/magazine_detail.html', context)

def laws_download_view(request, pk):
    laws = get_object_or_404(Model_laws_data, pk=pk) #pk 값을 key값으로 하여 객체를 얻음
    url = laws.upload_files.url[1:] #jj, 첨부된 파일의 경로 저장
    file_url = urllib.parse.unquote(url) #&인코딩된 텍스트를 되돌리기 위해 변환 후 file_url에 저장

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(laws.filename.encode('utf-8')) #&인코딩으로 변환
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404

def regulation_download_view(request, pk):
    regulation = get_object_or_404(Model_regulation, pk=pk) #pk 값을 key값으로 하여 객체를 얻음
    url = regulation.upload_files.url[1:] #jj, 첨부된 파일의 경로 저장
    file_url = urllib.parse.unquote(url) #&인코딩된 텍스트를 되돌리기 위해 변환 후 file_url에 저장

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(regulation.filename.encode('utf-8')) #&인코딩으로 변환
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404

def SKTL_policy_download_view(request, pk):
    SKTL_policy = get_object_or_404(Model_SKTL_policy, pk=pk) #pk 값을 key값으로 하여 객체를 얻음
    url = SKTL_policy.upload_files.url[1:] #jj, 첨부된 파일의 경로 저장
    file_url = urllib.parse.unquote(url) #&인코딩된 텍스트를 되돌리기 위해 변환 후 file_url에 저장

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(SKTL_policy.filename.encode('utf-8')) #&인코딩으로 변환
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404

def guide_download_view(request, pk):
    guide = get_object_or_404(Model_guide, pk=pk) #pk 값을 key값으로 하여 객체를 얻음
    url = guide.upload_files.url[1:] #jj, 첨부된 파일의 경로 저장
    file_url = urllib.parse.unquote(url) #&인코딩된 텍스트를 되돌리기 위해 변환 후 file_url에 저장

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(guide.filename.encode('utf-8')) #&인코딩으로 변환
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404

def trend_download_view(request, pk):
    trend = get_object_or_404(Model_trend, pk=pk) #pk 값을 key값으로 하여 객체를 얻음
    url = trend.upload_files.url[1:] #jj, 첨부된 파일의 경로 저장
    file_url = urllib.parse.unquote(url) #&인코딩된 텍스트를 되돌리기 위해 변환 후 file_url에 저장

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(trend.filename.encode('utf-8')) #&인코딩으로 변환
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404

def magazine_download_view(request, pk):
    magazine = get_object_or_404(Model_magazine, pk=pk) #pk 값을 key값으로 하여 객체를 얻음
    url = magazine.upload_files.url[1:] #jj, 첨부된 파일의 경로 저장
    file_url = urllib.parse.unquote(url) #&인코딩된 텍스트를 되돌리기 위해 변환 후 file_url에 저장

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(magazine.filename.encode('utf-8')) #&인코딩으로 변환
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST=['content']
        img = request.FILES["imgfile"]
        fileupload = FileUpload(
            title = title,
            content = content,
            imgfile = img,
        )
        fileupload.save()
        return redirect('fileupload')
    else:
        # forms.py 에서 작성한 form 의 틀을 우선 import 한 뒤 여기서 fileuploadForm 객체에다가 치환시킨다.
        # 치환 시킨 form 객체는 context 에 저장되어 form 자체가 template 로 전달된다.
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'pybo/fileupload.html', context)