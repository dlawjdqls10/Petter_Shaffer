from django.db import models


class Show(models.Model):
    author = models.CharField(max_length=50, verbose_name="작가")
    title = models.CharField(max_length=200, verbose_name="제목")
    poster = models.ImageField(upload_to='poster/', verbose_name="포스터", blank=True)
    running_time = models.TimeField(verbose_name="러닝타임")
    date = models.DateTimeField(verbose_name="공연날짜")
    place = models.CharField(max_length=300, verbose_name="공연장소")
    cast_set = models.ManyToManyField('Cast', verbose_name="참여인원")
    circle = models.ForeignKey('Circle', on_delete=models.CASCADE, blank=True)
    summary = models.TextField(verbose_name="내용설명", blank=True, null=True)
    price = models.CharField(max_length=20, verbose_name="가격", blank=True, null=True)

    def __str__(self):
        return self.title


class Circle(models.Model):
    name = models.CharField(max_length=50, verbose_name="동아리명")

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=50, verbose_name="이름")
    image = models.ImageField(upload_to='image/', verbose_name="사진", blank=True)

    def __str__(self):
        return self.name
