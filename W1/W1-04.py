def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

print(binary_search("Halloworld","a"))

#Setting initial value of the counter to zero
rowcount  = 0
#iterating through the whole file
with open("contacts.csv", mode='r', encoding="utf-8") as file:
    for row in file:
        rowcount+= 1
    #printing the result
    print("Number of lines present:-", rowcount)

# wc -l "contact.csv"
# head -15 contact.csv
# tail -25 contact.csv
head -50 contacts.csv | ./import.py --server test
head -50 contacts.csv | head -25 | ./import.py --server test
head -50 contacts.csv | tail -25 | ./import.py --server test
head -50 contacts.csv | tail -25 | head -13| ./import.py --server test
head -50 contacts.csv | tail -25 | tail -12| head -6 | ./import.py --server test
head -50 contacts.csv | tail -25 | tail -12| head -6 | head -3 |  ./import.py --server test