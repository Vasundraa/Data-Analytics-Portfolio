import csv

with open(r"C:\Users\vasun\OneDrive\Desktop\Vasundraa\Python\Foundations\File Handling\data.csv","r+",newline="") as file:
    reader=csv.reader(file)

    #this line prints the object. to access actual content we must iterate through it
    print(reader)

    for row in reader:
        print(row)

    #to access the contents as dictionary
    reader=csv.DictReader(file)
    for row in reader:
        print(row["name"])

    #this prints extra new line character
    writer=csv.writer(file)
    writer.writerow(["mithra","ece"])
    writer.writerows([["ram","cse"],["priya","eee"]])

    #using write header
    headerRows=["Name","Dept"]
    writer=csv.DictWriter(file,fieldnames=headerRows)
    writer.writeheader()
    #using DictWriter and not printing newline by mentioning in open()
    writer.writerow({"Name":"geetha","Dept":"mech"})
    writer.writerows([{"Name":"nithya","Dept":"it"},{"Name":"dharsh","Dept":"eee"}])