# def alphabetspam(string):
#     upperCase = 0
#     lowerCase = 0
#     whiteSpace = 0
#     sym = 0
#     for i in string:
#         if ord(i) >= 97 and ord(i) <= 122:
#             lowerCase += 1
#         elif ord(i) >= 65 and ord(i) <= 90:
#             upperCase += 1
#         elif ord(i) == 95:
#             whiteSpace += 1
#         else:
#             sym += 1
#     return whiteSpace/len(string),lowerCase/len(string),upperCase/len(string),sym/len(string)
#

# def findingana(string):
#     for i in range(0 , len(string)):
#         if string[i] == "a":
#             return string[i:]

# string = "Welcome_NWERC_participants!"
# print(alphabetspam(string))