from datetime import datetime, date, time, timedelta

start_date = date(2018, 9, 1)
end_date = date.today()
counter = start_date
while counter <= end_date:
    print(counter)
    counter += timedelta(days=1)