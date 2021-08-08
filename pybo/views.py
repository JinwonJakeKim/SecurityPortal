from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Model_laws_data, Model_SKTL_Policy, Model_GuideManual, Model_Trend, FileUpload
from django.utils import timezone
from .forms import QuestionForm, AnswerForm, FileUploadForm
from django.core.paginator import Paginator

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
    return render(request, 'pybo/laws_data.html', context)

def regulation_data(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/regulation_data.html')

def SKTL_Policy(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/SKTL_Policy.html')

def GuideManual(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/GuideManual.html')

def Trend(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/Trend.html')

def index(request):
    """
    pybo 목록 출력
    """
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
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id) #id에 해당하는 Quesiton 객체를 get
    context = {'question': question} #위에서 get한 question 객체를 text 화
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
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
            question.imgfile = request.FILES["imgfile"]
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index') #question_form.html에서 입력한 값을 POST 보내서 위 코드로 저장이 되면 index 함수를 호출시켜서 결국 question_list.html 보여지도록 Redirection
    else:
        # request.method 가 'GET'인 경우 호출됨, 질문등록하기, 입력전 실행부
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'pybo/question_form.html', context)