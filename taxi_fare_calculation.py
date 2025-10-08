def calculate_fare(distance_km):
    BASE_FARE = 50
    RATE_PER_KM = 10
    fare = BASE_FARE + (distance_km * RATE_PER_KM)
    return fare
trips = [5, 10, 3]
total_fare = 0.0
print("--- Trip Breakdown ---")
for i, distance in enumerate(trips):
    trip_fare = calculate_fare(distance)
    total_fare += trip_fare
    print(f"Trip {i + 1}: ${int(trip_fare)}")
print("\n--- Summary ---")
print(f"Total Fare: ${int(total_fare)}")