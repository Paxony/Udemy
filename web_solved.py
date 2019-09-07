import csv
import os


Udemy_csv=os.path.join(".","resources","web_starter.csv")

title=[]
price=[]
subscribers=[]
reviews=[]
reviews_percent=[]
length=[]

with open(Udemy_csv, "r", encoding="utf-8") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    #test=next(csvreader)
    for row in csvreader:
    #add title
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        percent=round(int(row[6])/int(row[5]),2)
        reviews_percent.append(percent)
        new_length=row[9].split(" ")
        length.append(float(new_length[0]))


#print(reviews_percent)

CleanCsv=zip (title,price,subscribers,reviews,reviews_percent,length)
outputfile=os.path.join("webFinal.csv")

with open(outputfile,"w",newline="\n")as datafile:
    writer=csv.writer(datafile)
    writer.writerow(["title","price","suscribers","reviews","percent of reviews","lenght of course"])
    writer.writerows(CleanCsv)
