"""Write a Python program that accepts a
hyphen-separated sequence of words as input and
prints the words in a hyphen-separated sequence
after sorting them alphabetically.
"""
def sort_words(mylist):
    items=[n for n in mylist]
    items.sort()
    return(items)

list1=input("Enter hyphen separated list").split('-')
i1=sort_words(list1)
print('-'.join(i1))
