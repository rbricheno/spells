# Get a timezone aware version of the current time
# without previously knowing the timezone

from datetime import datetime

tz = datetime.now().astimezone().tzinfo
now = datetime.now(tz)
