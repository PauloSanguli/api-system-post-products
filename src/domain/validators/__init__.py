import re

PATTERN_EMAIL = r"^([a-z0-9\+_\-]+)(\.[a-z0-9\+_\-]+)*@([a-z0-9\-]+\.)+[a-z]{2,6}$"
PATTERN_PHONE = r"^(?:(\+244|00244))?(9)(1|2|3|4|9)([\d]{7,7})$"

result = re.search(PATTERN_PHONE, "+244908123546")
print(result)