



import re
pattern = r'(\d{1,3})(,\d{3})(.\d+)?'
matches = re.findall(pattern,"This string contains numbers like 1,545, 5,212,565, and 454,453,632. It also has decimal numbers like 1,545.123 and 5,212,565.456." )
match = [''.join(match) for match in matches]
print(' '.join(match))