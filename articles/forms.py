from .models import *
from django import forms
from django.forms import ClearableFileInput

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title',
            'price',
            'content',
        )
        labels = {
            'title': '제목',
            'price': '가격',
            'content': '내용',
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = (
            'x',
            'y',
            'location',
        )
       

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = [
            'title', 
            'index_image', 
            'detail_image'
        ]

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = [
            'title', 'image'
        ]



class ArticlePhotoForm(forms.ModelForm):
    class Meta:
        model = ArticlePhoto
        fields = ("image",)
        widgets = {
            "image": ClearableFileInput(attrs={"multiple": True}),
        }
        labels = {
            'image': '이미지 업로드',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "grade",
        ]
        labels = {
            'title': '제목',
            'content': '내용',
            'grade' : '별점',
        }

        

class ReviewPhotoForm(forms.ModelForm):
    class Meta:
        model = ReviewPhoto
        fields = ("image",)
        widgets = {
            "image": ClearableFileInput(attrs={"multiple": True}),
        }
        labels = {
            'image': '이미지 업로드',
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "name",
            "check_in",
            "check_out",
        ]
        labels = {
            'name': '이름',
            'check_in': '체크인',
            'check_out' : '체크아웃',
        }