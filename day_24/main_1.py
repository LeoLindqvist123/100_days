'''with open("my_file.txt") as f:
    contents = f.read()
    print(contents)
'''
# mode = "a" for append and "w" for write

'''with open("my_file.txt", mode="a") as file:
    file.write("\nNew text")'''

with open("new_file.txt", mode="w") as file:
    file.write("Tjenare mannen")