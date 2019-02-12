## chapter 5
Q: 1. What does the code for an empty dictionary look like?
> dictionary = {}

Q: 2. What does a dictionary value with a key 'foo' and a value 42 look like?
> dictioary = { 'foo', 42 } ( well I guess it is just like other python object)

Q: 3. What is the main difference between a dictionary and a list?
> dictonary is associate array ( k-v as item ) while list is value only with index

Q: 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
> NONE  my test code in python
~~~ python
dict = {'bar': 100}

value = str(dict.get('bar', 0))
print(value)
print(dict.get('foo'))
~~~

Q: 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
>  cat can be used as a key to retrieve value in spam dictionary 

Q: 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
>  cat must be refered by key in spam. or you can't access it 

Q: 7. What is a shortcut for the following code?

if 'color' not in spam:
    spam['color'] = 'black'
> spam.setDefault('color', 'black')
    
Q: 8. What module and function can be used to “pretty print” dictionary values?
> 
~~~python
import pprint
pprint.pprint(dictionary)
~~~

