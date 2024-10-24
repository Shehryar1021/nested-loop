string =input("PLEASE ENTER YOUR OWN WORD :")
char =input("PLEASE ENTER YOUR OWN CHARACTER :")
i=0
count=0
while(i < len(string)):
    if(string[i]  ==char):
        count = count + 1
        i=i+1
        print("THE TOTAL NUMBER OF TIMES", char,"has OCCURED =", count)