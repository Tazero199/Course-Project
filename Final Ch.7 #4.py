series = 0
s_list = []
total = 0
go = "y"

while go == "y":
    for x in range(20):
        series = int(input(f"Enter a number: "))
        s_list.append(series)
        total += series
    s_list.sort()

    print(f"Your list is {s_list}\n")
    print(f"The lowest number in the list is {s_list[0]}\n")
    print(f"The highest number in the list is {s_list[-1]}\n")
    print(f"The total of the numbers in the list is {total}\n")
    print(f"The average of the numbers in your list is {total/len(s_list)}\n")

    go = input("Would you like to enter a new list? input: y/n")

print("Thank you and goodbye!")
