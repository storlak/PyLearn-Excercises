course = "Python for beginners"
another = course[:]
mokoko = "Today the weather is nice."
print(course[0])
print(course[-1])
print(course[:-3])
print(course[6:10])
print(another)
print(len(course))
print(mokoko.find("T"))
print(mokoko.find("weather"))
print(
    mokoko.replace("nice", "bad")
)  # bu çok önemli. method anlık etki ediyor. bir sonraki satırda print mokoko
# bize yine aynısını verecek. cümleyi değiştirmiyor sadece yazıldığı satırda!!!
