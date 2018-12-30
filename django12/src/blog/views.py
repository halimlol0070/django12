from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
#제네릭뷰 사용시 문서 확인 어떤 변수 메소드를 수정할수 있는지 파악 해야함
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from django.urls.base import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

#게시물 목록(index)
class Index(ListView):
    template_name='blog/index.html'#HTML 
    model = Post
    context_object_name='post_list'#템플릿 키값
    paginate_by=5
    
#상세 페이지(detail)
class Detail(DetailView):
    template_name='blog/index.html'
    model=Post
    context_object_name= 'obj'
#글 등록  페이지
from .forms import  *
class PostRegister( LoginRequiredMixin ,FormView):
    template_name='blog/postregister.html'
    form_class=PostForm
    context_object_name='form'
    #is_valid()함수가 True를 반환했을 떼에  form_valid()함수를 오버라이딩해서 구현
    def form_valid(self, form):
        #사요자입력에대한 겍체 생성 처리
        #author변수에 값이 채워져 있지 않다.
        #뷰함수의 request매개변수를 뷰클래스에서 사용할때 
        obj=form.save(commit=False)#obj: Post(database 저장)
        obj.author=self.request.user
        obj.save()#Db에 객체 저장
        return FormView.form_valid(self, form)
        #사용자가 업로드한 이미지... 파일을 데이터 베이스에 객체로 저장
        for f in self.request.FILES.getlist('images'):
            image=PostImage(post=obj,image=f)
            image.save()
        #image=PostImage()
        #image=post=obj
        #image.image=f
        image.save()#데이터 베이스에 새로운 포스트 이미지 객체가 저장
        for f in self.request.FILES.getlist('files'):
            file=PostFile(post=obj,file=f)
            file.save()

        return HttpResponseRedirect(reverse('blog:detail',args=(obj.id,)))
class Searchp(FormView):    
    template_name='blog/serchP.html'
    form_class=SearchForm
    context_object_name='form'
    #유효성 검사를 통과한 요청들을 처리하기위해 form_valid 함수 overriding
    def form_valid(self,form):
        search_word=form.cleaned_data['search_word']
        #(post headline변수)
        #Post.objects.filter(변수 __필터링 =값)
        #변수를 비교한후 만족하는 객체를 추출하는 함수
        #contains:해당변수가 우변값을 포함한경우 추출하겠다는 설정
        #추출된 결과를 HTML로 전달(검색결과+재 전
        post_list=Post.objects.filter(headline__contains=search_word)
        return render(self.request,self.template_name,{'form':form,'search_word':search_word,'postlist':post_list})
    
#ListView:객체 목록
#DetailView:객체 한개
