from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import BookCopy, BookLoan, Reservation
from .forms import BookLoanForm, ReservationForm


@csrf_protect
def management_dashboard(request):
    from .forms import BookLoanForm, ReservationForm
    loan_form = BookLoanForm(request.POST or None, prefix='loan')
    reservation_form = ReservationForm(request.POST or None, prefix='res')

    if request.method == 'POST':
        if 'loan_submit' in request.POST and loan_form.is_valid():
            loan_form.save()
            return redirect('management_dashboard')
        elif 'reservation_submit' in request.POST and reservation_form.is_valid():
            reservation_form.save()
            return redirect('management_dashboard')

    context = {
        'copies': BookCopy.objects.select_related('book', 'branch'),
        'loans': BookLoan.objects.select_related('copy', 'borrower'),
        'reservations': Reservation.objects.select_related('book', 'user', 'branch'),
        'loan_form': loan_form,
        'reservation_form': reservation_form
    }
    return render(request, 'management/dashboard.html', context)
