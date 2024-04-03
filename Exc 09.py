data = [
    {"open": 100, "high": 120, "low": 90, "close": 110},
    {"open": 110, "high": 130, "low": 80, "close": 120},
    {"open": 120, "high": 140, "low": 70, "close": 130},
    {"open": 130, "high": 150, "low": 60, "close": 140},
]
ranges = []
for d in data:
    ranges.append(d["high"] - d["low"])


ranges = [d["high"] - d["low"] for d in data]
print(ranges)
