from datetime import datetime, timedelta

# Define the date format
date_format = "%d-%m-%Y"

# Parse the given dates
start_date = datetime.strptime("22-01-2011", date_format)
end_date = datetime.strptime("05-02-2011", date_format)

# Generate the list of dates between the given dates
date_list = [start_date + timedelta(days=x) for x in range(1, (end_date - start_date).days)]

# Format the dates back to strings
formatted_dates = [date.strftime(date_format) for date in date_list]
print(formatted_dates)
