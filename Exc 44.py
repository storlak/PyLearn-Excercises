# Create two new variables that contain just the lower and upper case letters of `s` respectively, in the correct
# alphabetical order, i.e:
# "ABCDEF"
# "abcdef"

s = 'FfEeDdCcBbAa'
reversed_s = s[::-1]
print(reversed_s[::2])
print(reversed_s[1::2])
