from django.db import models

# Create your models here.
#准备书籍列表信息的模型类
class BookInfo(models.Model):
    name = models.CharField(max_length=10,verbose_name='书籍名称')
    pub_name = models.DateField(verbose_name='发布年份',null=True)
    readcount = models.IntegerField(verbose_name='阅读量',default=0)
    commentcount = models.IntegerField(verbose_name='评论数',default=0)
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo'  #数据库中显示的表名

    def __str__(self):
        return self.name   #定义每个数据对象的显示信息

class PeopleInfo(models.Model):
    GENDER_CHOICES = ((0,'male'),(1,'female'))
    name = models.CharField(max_length=10,verbose_name='任务名字')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    description = models.CharField(max_length=100,null=True,verbose_name='描述')
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

