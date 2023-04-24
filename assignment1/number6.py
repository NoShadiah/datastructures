countryCapitals = {
    'USA': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'Mexico': 'Mexico City',
    'UK': 'London',
    'France': 'Paris',
    'Germany': 'Berlin',
    'India': 'New Delhi',
    'China': 'Beijing',
    'Japan': 'Tokyo',
    'Australia': 'Canberra',
    'Uganda':'Kampala'
}

# Prompting a user
country = input('Enter a country name: ')
capital = countryCapitals.get(country)

if capital:
    print(f"The capital of {country} is {capital}.")
else:
    print(f"Sorry, I don't have information on the capital of {country}.")