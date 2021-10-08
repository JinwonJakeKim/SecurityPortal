from django import forms
from pybo.models import Question, Answer, FileUpload, Model_laws_data, laws_Answer, Model_regulation, regulation_Answer, Model_SKTL_policy, SKTL_policy_Answer, Model_guide, guide_Answer, Model_trend, trend_Answer, Model_magazine, magazine_Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'imgfile']
        labels = {
            'subject':'제목',
            'content':'내용',
            'imgfile':'첨부파일',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }

# form 은 fomrs.Form 을 상속받으면 폼, forms.ModelForm을 상속받으면 모델 폼이라 부른다. 
# 여기서는 form.ModelForm 을 상속받음. 모델 폼은 말 그대로 모델과 연결된 폼이며, 모델폼 객체를 저장하면 연결된 모델의 데이터를 저장
# 즉 별도로 template 에서 DB에 접근하지 않아도 된다.
# Template(.html) - ModelForm - Model(DB) 와 같이 ModelForm 이 html 과 DB 를 연결

class laws_Form(forms.ModelForm):
    class Meta:
        model = Model_laws_data
        fields = ['subject', 'content', 'upload_files']
        labels = {
            'subject':'제목',
            'content':'내용',
            'upload_files':'첨부파일',
        }

class laws_AnswerForm(forms.ModelForm):
    class Meta:
        model = laws_Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }

class regulation_Form(forms.ModelForm):
    class Meta:
        model = Model_regulation
        fields = ['subject', 'content', 'upload_files']
        labels = {
            'subject':'제목',
            'content':'내용',
            'upload_files':'첨부파일',
        }

class regulation_AnswerForm(forms.ModelForm):
    class Meta:
        model = regulation_Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }

class SKTL_policy_Form(forms.ModelForm):
    class Meta:
        model = Model_SKTL_policy
        fields = ['subject', 'content', 'upload_files']
        labels = {
            'subject':'제목',
            'content':'내용',
            'upload_files':'첨부파일',
        }

class SKTL_policy_AnswerForm(forms.ModelForm):
    class Meta:
        model = SKTL_policy_Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }

class guide_Form(forms.ModelForm):
    class Meta:
        model = Model_guide
        fields = ['subject', 'content', 'upload_files']
        labels = {
            'subject':'제목',
            'content':'내용',
            'upload_files':'첨부파일',
        }

class guide_AnswerForm(forms.ModelForm):
    class Meta:
        model = guide_Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }

class trend_Form(forms.ModelForm):
    class Meta:
        model = Model_trend
        fields = ['subject', 'content', 'upload_files']
        labels = {
            'subject':'제목',
            'content':'내용',
            'upload_files':'첨부파일',
        }

class trend_AnswerForm(forms.ModelForm):
    class Meta:
        model = trend_Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }

class magazine_Form(forms.ModelForm):
    class Meta:
        model = Model_magazine  # 사용할 모델
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class magazine_AnswerForm(forms.ModelForm):
    class Meta:
        model = magazine_Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'imgfile', 'content']