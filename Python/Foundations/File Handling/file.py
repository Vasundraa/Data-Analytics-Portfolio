file=open(r"C:\Users\vasun\OneDrive\Desktop\Vasundraa\Python\Foundations\File Handling\std_details.txt","r+")

# with open(r"C:\Users\vasun\OneDrive\Desktop\Vasundraa\Python\Foundations\File Handling\std_details.txt","a+") as file:
#     content=file.write("Mithi")
#     print(file.read())

#initially file contains:Vasu\n Rithiha 
print("Read Output:\n",file.read())
file.seek(0)

print("Readline Outputy:\n",file.readline())
file.seek(0)