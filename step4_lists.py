# browsers = []
# print (browsers)
#
# #browsers[0] = 'Chrome'
#
# browsers.append('Chrome')
# browsers.append('Firefox')
# browsers.append('Edge')
# print (browsers)
#
# print(len(browsers))
#
# print(browsers[2])
#
# print(browsers[len(browsers) - 1])


# a = []
# a.append(['Chrome', 'Firefox', 'Edge'])
# print(a)
# print(len(a))

b = []
b.extend(['Chrome', 'Firefox', 'Edge'])
print(b)
b.extend(['Opera'])
print(b)
print(len(b))