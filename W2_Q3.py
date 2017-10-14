def minutes_to_years_days(minutes):
    cal = 60 * 24 * 365
    years = minutes / cal
    days = minutes % cal / (24 * 60)
    return (years , days)

time = int(raw_input("Enter the number of minutes:"));
y , d = minutes_to_years_days(time)
print time , "minutes is approximately", y , "years and" , d , "days"