import datetime
KST=datetime.timezone(datetime.timedelta(hours=9))
print(datetime.datetime.now(tz=KST).date())