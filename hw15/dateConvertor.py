# seconds = 0 # -> 0 днів, 00:00:00
# seconds = 224930 # -> 2 дні, 14:28:50
# seconds = 466289 # -> 5 днів, 09:31:29
# seconds = 950400 # -> 11 днів, 00:00:00
# seconds = 1209600 # -> 14 днів, 00:00:00
# seconds = 1900800 # - > 22 дні, 00:00:00
# seconds = 8639999 # -> 99 днів, 23:59:59
# seconds = 22493 # -> 0 днів, 06:14:53
seconds = 7948799 # -> 91 день, 23:59:59

days, remainder = divmod(seconds, 24 * 60 * 60)
hours, remainder = divmod(remainder, 60 * 60)
minutes, seconds = divmod(remainder, 60)

days_message = ''

if days == 0:
    days_message = "днів"
elif days == 1:
    days_message = "день"
elif 2 <= days <= 4:
    days_message = "дні"
else:
    days_message = "днів"


days_str = f"{days} {days_message}" if days > 0 else "0 днів"
time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

print(f"{days_str}, {time_str}")