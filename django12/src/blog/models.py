from django.db import models
#카테고리
class PostType(models.Model):
     name=models.CharField('카테고리', max_length=20)
     def __str__(self):
         return self.name
from django.conf import settings     
#글(제목,글쓴이,글내용,작성일, 카테소리 외래키
# Create your models here.
class Post(models.Model):
    type = models.ForeignKey(PostType, on_delete=models.PROTECT)
    headline= models.CharField('제목', max_length=200)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content=models.TextField('내용', null = True, blank =True)
    pub_date=models.DateTimeField('작성일',auto_now_add=True)
    class Meta:
        ordering=['-id']
class PostImage(models.Model):
    post=models.ForeignKey(Post, on_delete =models.CASCADE)
    image=models.ImageField('이미지파일',upload_to='images/%Y/%m/%d')
    #객체 삭제시 호출되는
    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)
#파일(글-외래키, 파일)
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file =models.FileField('첨부파일',upload_to='files/%Y/%m/%d') 
    #FileField:파일 (이미지, 실행파일, 액셀,워드, 등)의 경로를 저장하는 공간
    def delete(self, using=None, keep_parents=False):  
        self.file.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)