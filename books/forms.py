from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text_review', 'stars')

        widgets = {
            'text_review': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Напишите отзыв...'}),
            'stars': forms.Select(attrs={'class': 'form-select'}),
        }
