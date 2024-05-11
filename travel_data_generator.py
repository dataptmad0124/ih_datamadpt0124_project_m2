import pandas as pd
import numpy as np
from faker import Faker
fake = Faker()

# Define the number of entries
num_customers = 10000
num_agents = 100
num_bookings = 30000
num_flights = 2000
num_hotels = 1500
num_tickets = num_bookings
num_payments = num_bookings
num_destinations = 500
num_promotions = 300
num_reviews = 15000

# Generate Customers table
customers = pd.DataFrame({
    'CustomerID': range(1, num_customers + 1),
    'Name': [fake.name() for _ in range(num_customers)],
    'Email': [fake.email() for _ in range(num_customers)],
    'Phone': [fake.phone_number() for _ in range(num_customers)],
    'Gender': [fake.random_element(['Male', 'Female']) for _ in range(num_customers)],
    'CustumerCountry': [fake.country() for _ in range(num_customers)]
})

# Generate Agents table
agents = pd.DataFrame({
    'AgentID': range(1, num_agents + 1),
    'Name': [fake.name() for _ in range(num_agents)],
    'ContactNumber': [fake.phone_number() for _ in range(num_agents)]
})

# Generate Bookings table
bookings = pd.DataFrame({
    'BookingID': range(1, num_bookings + 1),
    'CustomerID': np.random.choice(customers['CustomerID'], num_bookings),
    'AgentID': np.random.choice(agents['AgentID'], num_bookings),
    'DestinationID': np.random.choice(range(1, num_destinations + 1), num_bookings),
    'HotelID': np.random.choice(range(1, num_hotels + 1), num_bookings),
    'FlightID': np.random.choice(range(1, num_flights + 1), num_bookings),
    'BookingDate': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_bookings)]
})

# Generate Flights table
flights = pd.DataFrame({
    'FlightID': range(1, num_flights + 1),
    'Airline': [fake.company() for _ in range(num_flights)],
    'Origin': [fake.city() for _ in range(num_flights)],
    'Destination': [fake.city() for _ in range(num_flights)],
    'DepartureTime': [fake.date_time_this_year() for _ in range(num_flights)],
    'ArrivalTime': [fake.date_time_this_year() for _ in range(num_flights)],
    'Price': np.random.uniform(50, 1000, num_flights)
})

# Generate Hotels table
hotels = pd.DataFrame({
    'HotelID': range(1, num_hotels + 1),
    'Name': [fake.company() for _ in range(num_hotels)],
    'Location': [fake.city() for _ in range(num_hotels)],
    'Rating': np.random.randint(1, 5, num_hotels),
    'PricePerNight': np.random.uniform(30, 500, num_hotels),
    'HotelCountry': [fake.country() for _ in range(num_hotels)]
})

# Generate Tickets table
tickets = pd.DataFrame({
    'TicketID': range(1, num_tickets + 1),
    'BookingID': bookings['BookingID'],
    'FlightID': bookings['FlightID'],
    'Price': bookings['FlightID'].map(flights.set_index('FlightID')['Price']),
    'TicketDate': [fake.date_this_year() for _ in range(num_tickets)]
})

# Generate Payments table
payments = pd.DataFrame({
    'PaymentID': range(1, num_payments + 1),
    'BookingID': bookings['BookingID'],
    'Amount': bookings['BookingID'].map(bookings['HotelID'].map(hotels.set_index('HotelID')['PricePerNight']) +
                                        tickets['Price']),
    'PaymentDate': [fake.date_this_year() for _ in range(num_payments)],
    'PaymentMethod': [fake.credit_card_provider() for _ in range(num_payments)]
})

# Generate Destinations table
destinations = pd.DataFrame({
    'DestinationID': range(1, num_destinations + 1),
    'Name': [fake.city() for _ in range(num_destinations)],
    'Country': [fake.country() for _ in range(num_destinations)],
    'PopularAttraction': [fake.company() for _ in range(num_destinations)],
    'PopularAttractionType': np.random.choice(['Family','Couple','Honeymoon','Business','Single','Friends'], size=num_destinations)
})

# Generate Promotions table
promotions = pd.DataFrame({
    'PromotionID': range(1, num_promotions + 1),
    'Description': [fake.sentence() for _ in range(num_promotions)],
    'Discount': np.random.uniform(5, 30, num_promotions),
    'ValidFrom': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_promotions)],
    'ValidTo': [fake.date_between(start_date='today', end_date='+1y') for _ in range(num_promotions)]
})

# Generate Reviews table
reviews = pd.DataFrame({
    'ReviewID': range(1, num_reviews + 1),
    'BookingID': np.random.choice(bookings['BookingID'], num_reviews),
    'Rating': np.random.randint(1, 5, num_reviews),
    'Comment': [fake.text(max_nb_chars=200) for _ in range(num_reviews)]
})

# Save to CSV
customers.to_csv('customers.csv', index=False)
agents.to_csv('agents.csv', index=False)
bookings.to_csv('bookings.csv', index=False)
flights.to_csv('flights.csv', index=False)
hotels.to_csv('hotels.csv', index=False)
tickets.to_csv('tickets.csv', index=False)
payments.to_csv('payments.csv', index=False)
destinations.to_csv('destinations.csv', index=False)
promotions.to_csv('promotions.csv', index=False)
reviews.to_csv('reviews.csv', index=False)
