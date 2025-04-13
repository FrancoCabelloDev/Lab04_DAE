from django import forms
from .models import BookLoan, Reservation

class BookLoanForm(forms.ModelForm):
    class Meta:
        model = BookLoan
        fields = ['copy', 'borrower', 'checkout_date', 'due_date']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['book', 'user', 'branch']
