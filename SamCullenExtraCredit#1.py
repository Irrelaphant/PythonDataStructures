#Sam Cullen, COSC-216, Python Data Structures, Professor Segal

#Deques

#A deque is essentially a list that can pop and push onto the left and right side of itself.
#it operates with similar characteristics to a stack in assembly, except you can chose which 
#side to pop and push onto. In python, they offer the flexibility and effeciency of an O(1) time

class MyDeque:


    def __init__(self):
        #list to store the data and fill it with "None"
        #this, to my understanding, "None" is the same as "Null" in java
        self._data = [None]
        #this is the number of elements in deque
        self._n = 0
        #this is supposed to be the capacity of deque
        self._capacity = 1
        #these both point to the first and last element but are initialized as -1 so they are empty
        self._first = -1
        self._last = -1

    def __str__(self):
        #this methods purpose is to return the string representation of the deque
        #this will return a for loop that will loop based off of the size of the list
        #i will make a string that stores the string we want to return

        #this will store the left side of the list when we want to print it 
        string = "|"

        #now we want to loop through each element in the list, and append the to our string
        for i in range(self._first, self._last + 1):
            #we need to convert each element to a string and append
            string += str(self._data[i])

            #Check if it is the last element in the deque it
            #if it is not the last, add a ", "
            if i < self._last:
                string += ", "

        #we are done adding everything to the string now so we can add a closing line
        
        string += "|"

        #return our string
        return string

    def __len__(self):
        #this will return the amount of elements in the deque
        return self._n


    def isEmpty(self):
        #this will check if the deque is empty
        #if the size of the list is equal to 0, its empty
        if self._n == 0:
            return True
        else:
            return False
        
    
    def addFirst(self, element):
        #this will add an element to the front of the deque
        #first step is to check if the size of the deque needs to be increased to fit the element
        #if it does need to be resized, we have a method for that
        
        if self._n + 1 > self._capacity:
            #according to the slides, and from what i've googled online you are supposed 
            #to double the size of the list? and this is to keep the O(1) time, instead of expanding it
            #based off of each element that would be added, which would make it O(n) time.
            self.resize(2 * self._capacity)

        #This will check if it is empty, and if it is empty itll add it to the front
        if self.isEmpty():
            #set first to the front most element, 0
            self._first = self._last = 0
            #this will add whatever element is given, to the index of the first pointer
            self._data[self._first] = element

        else:
            #update the first pointer in order to insert the new element at the front
            self._first = (self._first -1) % self._capacity
            #now lets insert the element at the first position
            self._data[self._first] = element

        #at the very end, we increase the number of elements
        self._n += 1
                

    def addLast(self, element):
        #this is identical to addfirst but at the end we just add the element using the last pointer
        #check if it needs to increase capacity
        if self._n + 1 > self._capacity:
            #resize like in addfirst
            self.resize(2 * self._capacity)
        
        #then check if it's empty, if so then add it to the end 
        if self.isEmpty():
            self._first = self._last = 0
            self._data[self._last] = element
        #if it doesn't need to be resized
            
        else:
            #set the last pointer to the end of the list 
            self._last = (self._last + 1) % self._capacity
            #instert the new element
            self._data[self._last] = element
            
        #now that we are done, increase the elements
        self._n += 1
        

    def deleteFirst(self):
        #first step is to check if deque is empty, if it is we are supposed to error it
        if self.isEmpty():
            raise ValueError("the Deque is empty")
        
        #first thing to do is to get the first element
        element = self._data[self._first]
        #now we set the position to "None" in the deque, removing the value stored
        self._data[self._first] = None
        #now we update the pointer to increase by one, so that old position can't accessed
        self._first = (self._first + 1) % self._capacity
        #now we decrease the amount of elements because we are removing one
        self._n -= 1
        #now we should check again if deque is empty 
        if self.isEmpty():
            #if it is empty, we reset the pointers
            self._first = self._last = -1

        #the instructions say we have to return the element removed
        return element


    def deleteLast(self):
        #once again this is super similar to delete first but we just use the last pointer instead
        #I copied the delete first method and changed the pointers
        if self.isEmpty():
            raise ValueError("the Deque is empty")
        
        #first thing to do is to get the first element
        element = self._data[self._last]
        #now we set the position to "None" in the deque, removing the value stored
        self._data[self._last] = None
        #now we update the pointer to increase by one, so that old position can't accessed
        self._first = (self._last - 1) % self._capacity
        #now we decrease the amount of elements because we are removing one
        self._n -= 1
        #now we should check again if deque is empty 
        if self.isEmpty():
            #if it is empty, we reset the pointers
            self._first = self._last = -1

        #the instructions say we have to return the element removed
        return element
    

    def first(self):
        #check if it is empty
        if self.isEmpty():
            raise ValueError("The Deque is empty")
        
        #since it isn't empty now, we can just return the first value of self._data
        return self._data[self._first]
    

    def last(self):
        #would work the same as first except it returns whatever the last is
        if self._isEmpty():
            raise ValueError("The Deque is empty")
        #return the last element of the list 
        return self._data[self._last]
        

    def resize(self, new_capacity):
        #this will resize the .data list to whatever the new capacity is
        #we can do this just by multiplying it, but we will fill it with "None" which is like null
        #this also needs to reorient the elements so the front of the deque is position 0
        #in order to do that we make a copy of the original list, saving it in a temp one, then placing it in
        #the new list that has been resized

        #set the temp list
        temp_data = self._data
        
        #increase the size of self._data
        self._data = [None] * new_capacity

        #now we need a for loop that will go over each element in the old (temp) list
        #each item will then get copied to the newly sized list
        for i in range(self._n):
            self._data[i] = temp_data[(self._first + i) % self._capacity]

        #now we should change the capacity variable to the new capacity
        self._capacity =  new_capacity
        #set first to the first position at 0
        self._first = 0
        #set last to the size of the deque -1 since zero indexed
        self._last = self._n -1


def main():
    #we have to create the deque
    #then we can add a bunch of numbers to the deque, and print out the elements 
    deque = MyDeque()
    deque.addFirst(14)
    deque.addFirst(17)
    deque.addFirst(6)
    deque.addLast(40)
    deque.addLast(35)

    #print it!
    print("Deque contains: ", deque)






if __name__ == "__main__":
    main()
