from django.urls import path
from .views import homepage, login_view, signup_view, logout_view, book_table, my_bookings, delete_booking, edit_booking


urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('book-table/', book_table, name='book_table'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('delete-booking/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('edit-booking/<int:booking_id>/', edit_booking, name='edit_booking'),
]   