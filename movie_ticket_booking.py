import math
def book_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        print(f"--> Booking failed: Seat {seat_number} is already booked.")
        return False
    else:
        booked_seats.add(seat_number)
        print(f"--> Successfully booked Seat {seat_number}.")
        return True

def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"--> Successfully cancelled booking for Seat {seat_number}.")
        return True
    else:
        print(f"--> Cancellation failed: Seat {seat_number} was not marked as booked.")
        return False

def get_available_seats(total_seats, booked_seats):
    available = []
    for seat in range(1, total_seats + 1):
        if seat not in booked_seats:
            available.append(seat)
    return available
total_seats = 10
booked_seats = {2, 5, 7} 
print(f"Initial Booked Seats: {sorted(list(booked_seats))}")
print(f"Total Seats: {total_seats}\n")
book_seat(booked_seats, 3) 
cancel_seat(booked_seats, 5)
final_available_seats = get_available_seats(total_seats, booked_seats)
print(f"\nBooked Seats After Operations: {sorted(list(booked_seats))}")
print(f"Available seats: {final_available_seats}")