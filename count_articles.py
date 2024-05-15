import csv
def count_article_types(csv_file):
    category_counts = {
        "Arts": 0,
        "Campus Life": 0,
        "News": 0,
        "Opinion": 0,
        "Science": 0,
        "Sports": 0
    }
    i=1
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if row:
                # find any articles that were mislabeled (category label on article
                # is different from the section of the website that the article
                # was found under) on the original website
        
                if (i<=1926): # article was found in Arts section
                    if (row[0].strip().split('\n')[0]!="Arts"):
                        print(row[0])
                        print(i)
                        print("----------------------------------")
                elif (i>1926 and i<=3072): # article was found in Campus Life section
                    if (not row[0].strip().startswith("Campus Life")):
                        print(row[0])
                        print(i-1926)
                        print("----------------------------------")
                elif (i>3072 and i<=9022): # article was found in News section
                    if (row[0].strip().split('\n')[0]!="News"):
                        print(row[0])
                        print(i-3072)
                        print("----------------------------------")
                elif (i>9022 and i<=10934): # article was found in Opinion section
                    if (row[0].strip().split('\n')[0]!="Opinion"):
                        print(row[0])
                        print(i-9022)
                        print("----------------------------------")
                elif (i>10934 and i<=11014): # article was found in Science section
                    if (row[0].strip().split('\n')[0]!="Science"):
                        print(row[0])
                        print(i-10934)
                        print("----------------------------------")
                else: # article was found in Sports section
                    if (row[0].strip().split('\n')[0]!="Sports"):
                        print(row[0])
                        print(i-11014)
                        print("----------------------------------")

                # count frequency of scraped articles under each category    
                if row[0].strip().startswith("Campus Life"):
                    category_counts["Campus Life"]+=1
                else:
                    category_counts[row[0].strip().split('\n')[0]]+=1
            i+=1
    return category_counts

csv_file = 'export.csv'
print(count_article_types(csv_file))
