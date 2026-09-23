import json

with open(r"C:\Users\vasun\OneDrive\Desktop\Vasundraa\Python\Foundations\File Handling\std_data.json","r+") as file:
    student=json.load(file)

    #accessing values
    print(student["attendance"])
    print(student["marks"]["Python"])


stds={
    1:{

    }
}
with open(r"C:\Users\vasun\OneDrive\Desktop\Vasundraa\Python\Foundations\File Handling\std_data.json","a") as file:
    student=json.dump(stds,file,indent=2)

    print(student)