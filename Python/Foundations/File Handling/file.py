file=open(r"C:\Users\vasun\OneDrive\Desktop\Vasundraa\Python\Foundations\File Handling\std_details.txt","r")
print(file.read())

with open(r"C:\Users\vasun\OneDrive\Desktop\Vasundraa\Python\Foundations\File Handling\std_details.txt","a+") as file:
    content=file.write("Mithi")
    print(file.read())