from django.contrib import admin
from .models import LibraryBranch, BookCopy, BookLoan, Reservation

@admin.register(LibraryBranch)
class LibraryBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)

@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('inventory_number', 'book', 'branch', 'condition', 'is_available')
    list_filter = ('branch', 'condition', 'is_available')
    search_fields = ('inventory_number', 'book__title')

@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ('copy', 'borrower', 'checkout_date', 'due_date', 'status')
    list_filter = ('status',)
    search_fields = ('copy__inventory_number', 'borrower__username')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'branch', 'status', 'request_date')
    list_filter = ('status',)
    search_fields = ('book__title', 'user__username')
