import datetime
from django.contrib.auth.models import User
from bookings.models import Vehicle, Booking, Result

user1 = User.objects.create_user(username='user1', email='user1@example.com', password='password123')
user2 = User.objects.create_user(username='user2', email='user2@example.com', password='password123')
user3 = User.objects.create_user(username='user3', email='user3@example.com', password='password123')
user4 = User.objects.create_user(username='user4', email='user4@example.com', password='password123')
user5 = User.objects.create_user(username='user5', email='user5@example.com', password='password123')

vehicle1 = Vehicle.objects.create(name='Toyota Camry', vehicle_type='Sedan', location='NY', date='2021-05-20', time='10:00:00', price=150.00)
vehicle2 = Vehicle.objects.create(name='Ford Explorer', vehicle_type='SUV', location='Cagayan', date='2020-06-15', time='12:00:00', price=200.00)
vehicle3 = Vehicle.objects.create(name='Honda Civic', vehicle_type='Compact', location='Bukidnon', date='2019-07-10', time='09:00:00', price=250.00)

common_booking_time = datetime.time(10, 0)

booking1 = Booking.objects.create(user=user1, vehicle=vehicle1, total_price=150.00, booking_time=common_booking_time, payment_method='Credit Card')
booking2 = Booking.objects.create(user=user2, vehicle=vehicle2, total_price=200.00, booking_time=common_booking_time, payment_method='Cash')
booking3 = Booking.objects.create(user=user3, vehicle=vehicle3, total_price=250.00, booking_time=common_booking_time, payment_method='Credit Card')
booking4 = Booking.objects.create(user=user4, vehicle=vehicle1, total_price=180.00, booking_time=common_booking_time, payment_method='Credit Card')
booking5 = Booking.objects.create(user=user5, vehicle=vehicle2, total_price=220.00, booking_time=common_booking_time, payment_method='Cash')
booking6 = Booking.objects.create(user=user1, vehicle=vehicle3, total_price=130.00, booking_time=common_booking_time, payment_method='Cash')
booking7 = Booking.objects.create(user=user2, vehicle=vehicle1, total_price=170.00, booking_time=common_booking_time, payment_method='Credit Card')
booking8 = Booking.objects.create(user=user3, vehicle=vehicle2, total_price=210.00, booking_time=common_booking_time, payment_method='Credit Card')
booking9 = Booking.objects.create(user=user4, vehicle=vehicle3, total_price=130.00, booking_time=common_booking_time, payment_method='Credit Card')
booking10 = Booking.objects.create(user=user5, vehicle=vehicle1, total_price=150.00, booking_time=common_booking_time, payment_method='Credit Card')

Result.objects.create(booking=booking1, status='success', rating=5, feedback="Excellent service!")
Result.objects.create(booking=booking2, status='success', rating=4, feedback="Good experience.")
Result.objects.create(booking=booking3, status='success', rating=5, feedback="Very satisfied.")
Result.objects.create(booking=booking4, status='success', rating=4, feedback="Nice ride.")
Result.objects.create(booking=booking5, status='failed', rating=1, feedback="Would not recommend.")
Result.objects.create(booking=booking6, status='success', rating=4, feedback="Good value.")
Result.objects.create(booking=booking7, status='success', rating=5, feedback="Loved it!")
Result.objects.create(booking=booking8, status='success', rating=4, feedback="Will book again.")
Result.objects.create(booking=booking9, status='failed', rating=1, feedback="Broken suspension.")
Result.objects.create(booking=booking10, status='failed', rating=1, feedback="Lowly maintained car.")
