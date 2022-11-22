

# try:
#     file = open("C:/Users/befor/jobs.txt", 'w')
#     file.write('Applied at Thinkcell\n')
#     file.write('Applied at Debeka\n')
#     file.write('Applied at Lancom\n')
#     file.write('Applied at Pair finance\n')
#     file.write('Did not apply anymore\n')
#     file.close()
# except:
#     print('file not found')
# else:
#     print('Lines added')
# try:
#     file = open("C:/Users/befor/jobs.txt", 'a')
#     file.write('Will apply again in December\n')
#     file.write('year 2023\n')
#     file.close()
#     file = open("C:/Users/befor/jobs.txt", 'r')
#     print(file.readlines())
# except:
#     print('lines not added/could not read')

file = open("C:/Users/befor/jobs.txt", 'r')
print(file.read())
file.close()