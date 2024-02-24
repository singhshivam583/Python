file = open('youtube.txt', 'w')

try:
    file.write("chai aur code")

except FileNotFoundError:
    print("File Not found")

finally:
    file.close()


with open('youtube.txt', 'w') as file:
    file.write('chai aur python')


