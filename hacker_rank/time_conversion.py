# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. 
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Example
# s = '12:01:00PM'
# Return '12:01:00'.
# s= '12:01:00AM'
# Return '00:01:00'.

def timeConversion(s):
    # Write your code here
    s = list(s)
    if s[8] == "P":
        hour = s[0] + s[1]
        if hour == "12":
            s.pop(9)
            s.pop(8)
            s=''.join(s)
            return s
        else:
            new_hour = int(hour) + 12
            string_hour = str(new_hour)
            s[0] = string_hour[0]
            s[1] = string_hour[1]
    if s[8] == "A":
        hour = s[0] + s[1]
        if hour == "12":
            s[0] = "0"
            s[1] = "0"
        else:
            pass
    s.pop(9)
    s.pop(8)
    s = ''.join(s)
    return s
