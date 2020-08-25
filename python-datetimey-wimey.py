# Get a timezone aware version of the current time
# without previously knowing the timezone

import datetime

# Yes, really.
tz = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
now = datetime.datetime.now(tz)
