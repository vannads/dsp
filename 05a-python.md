# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Similarity is that lists and tuples are sequences in Python. The main difference is - **lists are mutable**, the elements are usually homogeneus that are accessed by iterating over the list -- whereas **tuples are immutable**, the elements usually contain a heterogenous sequence of elements that are accessed via unpacking or indexing. Though tuples may seem similar to lists, they are oftne used in different situations and for different purposes. Index in a tuple has an implied sematic, but not in lists as it is mutable. Tuples are usable as dictionary keys, while lists are not. The reason is Python dictionary implementation requires that key objects provide a "hash" implementation. The hash implementation uses a hash value calculated from the key value to find the key. If the key were a mutable object (lists in this case), its value could change, and its hash value. This can lead to unexpected results in dictionary look up. 
---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Similarity is that lists and sets are Python collections - sequences of arbitray items. The main difference is that a list is an ordered collection which can have duplicate elements, where as a set is an unordered collection with NO duplicate elements. In terms of performance - sets are significantly faster when it comes to membership testing, especially for large sets. That is because the set uses a hash function to map to a bucket. Since Python automatically resize the hash table the speed can be constant irrespective of the size of the set. for membership testing in lists Python has to compare every single member for equality (sequential lookup) and it can be slower.At the same time sets are slower than lists when it comes to iterating over its contents.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is an anonymous function expressed as a single statement.
'''
#Example
#2016 Sales figures of Top 5 sales person across 4 regions in USA 
# Each sales_person record is a tuple, elements are: salesPersonName, region, sales_in_$M
#...................................................
sales_2016 = [('Kathy', 'NW', 24), ('John', 'EC', 18), 
              ('Adam', 'SW', 28), ('Paul', 'NW', 20), ('Kate', 'EC', 29)]
sortedList = sorted(sales_2016, key=lambda sales: sales[2], reverse = True)
print(sortedList)

#-Outout-
[('Kate', 'EC', 29), ('Adam', 'SW', 28), ('Kathy', 'NW', 24), ('Paul', 'NW', 20), ('John', 'EC', 18)]
'''
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> In Python, a comprehension is a compact way of creating data structures from one or more iterators. They make it easy to combine loops and conditional tests with minimal syntax.

List comprehension is an elegant way to define and create lists in Python. If defined well, it is a complete substitute for the **lambda** function as wells as the functions **map(), filter(), and reduce()**

#Using list Comprehension
odd_numbers = [x for x in range(1,10) if x % 2 == 1]
print(odd_numbers)
#-Outout-
[1, 3, 5, 7, 9]

#Using filter() and lambda()
odd_numbers = list(filter(lambda x: x % 2, range(1,10)))
print(odd_numbers)
#-Outout-
[1, 3, 5, 7, 9]

#Using map()
def odd(x):
    if (x % 2 == 1):
        return x
        
odd_numbers = list(map(odd, range(1,10)))
print(odd_numbers)
#-Outout-
[1, None, 3, None, 5, None, 7, None, 9]
Here it maps all values, return value if it is odd, and 'None' for even. It's a bit tricky to use map function in this case as function returns 'None' for false condictions.

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





