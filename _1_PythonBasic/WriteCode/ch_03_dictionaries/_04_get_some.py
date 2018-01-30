from collections import defaultdict

data = {"year": 2001, "country": "USA", "title": "Johnny 5", "duration": "119 min"}

data = defaultdict(lambda: "MISSING", data)
print('accept default value instead style')
print(data['year'])
print(data['rating'])
print()
