
#lists are enclosed within square brackets
#courses = ['history', 'math', 'science', 'compsci' ]
#print(courses)


#prints amount of values in list
#courses = ['history', 'math', 'science', 'compsci' ]
#print(len(courses))



#square brackets after courses allows you to acces a specific index within your list
#courses = ['history', 'math', 'science', 'compsci' ]
#print(courses[0])



#pringting a -1 will display the last item in your list
#courses = ['history', 'math', 'science', 'compsci' ]
#print(courses[-1])



#print everything from the second index on
#courses = ['history', 'math', 'science', 'compsci' ]
#print(courses[2:])



#the append option allow you to add values to an existing list
#courses = ['history', 'math', 'science', 'compsci' ]
#courses.append('art')
#print(courses)



#using the insert fuction it allows you to insert values into an existing list, location must first be specified
#courses = ['history', 'math', 'science', 'compsci' ]
#courses.insert(0, 'art')
#print(courses)



#using the extend function this allows you to append an existing list to a list you already have created
#courses = ['history', 'math', 'science', 'compsci' ]
#courses2 = ['art', 'education']
#courses.extend(courses2)
#print(courses)



#this removes specific values from an existing list
#courses = ['history', 'math', 'science', 'compsci' ]
#courses.remove('math')
#print(courses)



#removes the last value from your list
#courses = ['history', 'math', 'science', 'compsci' ]
#courses.pop()
#print(courses)



#when using the popped function it stores the value in a seperate place
#courses = ['history', 'math', 'science', 'compsci' ]
#popped = courses.pop()
#print(popped)
#print(courses)



#using the reverse function with sort the list backwards
#courses = ['history', 'math', 'science', 'compsci' ]
#courses.reverse()
#print(courses)



#this sorts lists in ascending order
#courses = ['history', 'math', 'science', 'compsci' ]
#nums = [1, 3, 7, 2, 5, 9]
#courses.sort()
#nums.sort()
#print(courses)
#print(nums)



#this sorts lists in descending order
courses = ['history', 'math', 'science', 'compsci' ]
nums = [1, 3, 7, 2, 5, 9]
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)