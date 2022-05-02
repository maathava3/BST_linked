"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  Maathav Naganathan
ID:      210621280
Email:   naga1280@mylaurier.ca
Term:    Winter 2022
__updated__ = "2022-02-09"
-------------------------------------------------------
"""
from copy import deepcopy



class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count==0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _List_Node(value,self._front)
        
        
        
        # if empty both rear and front should be node
        if self._front is None:
            self._rear = node
            
            
        self._front = node
        self._count+=1
       
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _List_Node(value,None)
        
        if self._front is None:
            self._front = node
        
        #if list is empty, rear has no 'next' so we only do if there is a rear    
        if self._rear is not None:
            self._rear._next = node
            
        self._rear = node
        self._count +=1
        
        
        
        # your code here
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
       
        if i == 0 or i <= (self._count * -1):
            self.prepend(value)
        elif i >= self._count:
            self.append(value)
    
        else:
            curr_node = self._front
            end = i-1
            if i<0:
                start = self._count*-1
            else:
                start = 0
    
            for i in range(start,end):
                curr_node = curr_node._next
        
            node = _List_Node(value,curr_node._next)
            curr_node._next = node
            self._count+=1
                
            
        
        # your code here
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        index=0
        
        while index<self._count and current._value!=key:
            previous = current
            current = current._next
            index+=1
            
        if index==self._count:
            index = -1
            
        # your code here
        return previous,current,index
    
    

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, i = self._linear_search(key)
        
        if i>-1:
            self._count -= 1
            if i>0:
                previous._next = current._next
            elif i==0:
                self._front = current._next
            if i == self._count:
                self._rear = previous
            
            value = current._value
        else:
            value = None
                
        # your code here
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        # your code here
        if self._count==1:
            value = self._front._value
            self._rear = None
            self._front = None
            self._count-=1
        else:
            value = self._front._value
            self._front = self._front._next
            self._count-=1
            
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        previous, current, i = self._linear_search(key)
        while i!=-1:
            if i>-1:
                self._count -= 1
                if i>0:
                    previous._next = current._next
                elif i==0:
                    self._front = current._next
                if i == self._count:
                    self._rear = previous
                
                value = current._value
            else:
                value = None
            previous, current, i = self._linear_search(key)   
        # your code here
        
        # your code here
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, i = self._linear_search(key)
        value = None
        if current is not None:
            value = deepcopy(current._value)
        # your code here
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        value = deepcopy(self._front._value)

        # your code here
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        *_,i = self._linear_search(key)
        # your code here
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        curr_node = self._front
        end = i
        if i<0:
            start = self._count*-1
        else:
            start = 0
        for x in range(start,end):
            curr_node = curr_node._next
            
        value = deepcopy(curr_node._value)   

        # your code here
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        curr_node = self._front
        end = i
        if i<0:
            start = self._count*-1
        else:
            start = 0
        for x in range(start,end):
            curr_node = curr_node._next
            
        curr_node._value = deepcopy(value)

        # your code here
        return curr_node._value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        *_, value = self._linear_search(key)
        # your code here
        return value>-1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        max_data = 0
        current = self._front
        for i in range(self._count):
            
            if current._value>max_data:
                max_data = deepcopy(current._value)
            current = current._next
            

        # your code here
        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        min_data = 1000
        current = self._front
        for i in range(self._count):
            
            if current._value<min_data:
                min_data = deepcopy(current._value)
            current = current._next
            

        # your code here
        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        current = self._front
        number = 0
        while current is not None:
            
            if current._value==key:
                number+=1
            current = current._next
            

        # your code here
        
        # your code here
        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._rear = self._front
        previous = None
        current = self._front

        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp

        self._front = previous
        # your code here
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        if self._front is not None:
            self._reverse_r_aux(self._front, None )
            self._front, self._rear = self._rear, self._front
        
        # your code here
        return
    
    def _reverse_r_aux(self, current, previous ):
        
        if current._next is  None:
            current._next = previous
        else:
            x = current._next
            current._next = previous
            
            previous = current
            
            self._reverse_r_aux(x,previous)
        
        
        return


    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        while current is not None:
            _, c, _ = self._linear_search(current._value)
            if c != current:
                previous._next = current._next
                self._count -= 1
                if current == self._rear:
                    self._rear = previous
            else:
                previous = current
            current = current._next
        return
        
        # your code here
        

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return

        # your code here
       

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (iterative version)
        Use: b = lst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical
        # your code here
        

    def is_identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        identical = True 
        if self._count != other._count:
            identical = False
            
        else:
            identical = self.identical_r_aux(other,self._front,other._front)
        
        return identical

    def identical_r_aux(self,other,value,value_o):
        identical = True
        current = value
        current_o = value_o
        
        if self._front is None:
            identical = True
        
            
        
        if current is not None:
            if current_o._value !=current._value:
                identical = False
            else:
                identical = self.identical_r_aux(other,current._next,current_o._next)
            
        # your code here
        return identical

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        # Split
        middle = self._count // 2 + self._count % 2
        prev = None
        curr = self._front

        for _ in range(middle):
            prev = curr
            curr = curr._next

        if prev is not None:
            # Break the source list between prev and curr
            prev._next = None

        # Define target1
        target1._count = middle
        target1._front = self._front
        target1._rear = prev

        # Define target2
        target2._count = self._count - middle
        target2._front = curr

        if target2._count > 0:
            target2._rear = self._rear

        # Clean up source
        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2
            
                
            
        
        # your code here
        

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left

        return target1, target2
      

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()
        value = self._front
        if_even = True
        self._split_alt_r_aux(even, odd, if_even, value)
        return even, odd
        
        # your code here
        
        
    def _split_alt_r_aux(self, target1, target2, if_even, value):
        
        if value is not None:
            if if_even:
                target1.append(value._value)
            else:
                target2.append(value._value)
            even = not if_even
            self._count-=1
            
            
           
            self._split_alt_r_aux(target1, target2, even,value._next)
        self._front = None 
        self._rear = None 
        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        
        
        value = self._front
        index = 0
        previous = None
        current = None
        
        if self._count ==0:
            index = -1
        
        
        elif value is not None and value._value ==key:
            current = value
            
         
        else:
            previous,current,index = self._search(key,value,index)
        
        
  
        # your code here
        return previous,current,index
    
    def _search(self,key,value,index):
            index += 1
            previous = value
            
            
            if value._next is not None and value._next._value == key:
                
                current = value._next
            
            elif value._next is None:
                index = -1
                previous = None
                current = None
            else:
                previous,current,index = self._search(key,value._next,index)
            
            return previous,current,index
        # your code here
        

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
            # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                # Value does not appear in target list.
                    node = _List_Node(value,None)
        
                    if self._front is None:
                        self._front = node
                    
                    #if list is empty, rear has no 'next' so we only do if there is a rear    
                    if self._rear is not None:
                        self._rear._next = node
                        
                    self._rear = node
                    self._count +=1

            source1_node = source1_node._next

        # your code here
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"
        self.intersection_aux(source1._front,source2._front,source2)

        # your code here
        return
    
    def intersection_aux(self, value1, value2, source2):
        if value1 is not None and value2 is not None:
            _, current, _ = source2._linear_search(value1._value)
            _, current2, _ = self._linear_search(value1._value)
            if current is not None and current2 is None:
                self.append(current._value)
            self.intersection_aux(value1._next,value2,source2)
            
            
        

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"
        

        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                node = _List_Node(value,None)
        
                if self._front is None:
                    self._front = node
                
                #if list is empty, rear has no 'next' so we only do if there is a rear    
                if self._rear is not None:
                    self._rear._next = node
                    
                self._rear = node
                self._count +=1
        
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                node = _List_Node(value,None)
        
                if self._front is None:
                    self._front = node
                
                #if list is empty, rear has no 'next' so we only do if there is a rear    
                if self._rear is not None:
                    self._rear._next = node
                    
                self._rear = node
                self._count +=1
        

            source2_node = source2_node._next
        return
        # your code here
        

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"
        self.union_r_aux(source1._front,source2._front)
        

        # your code here
        return
    def union_r_aux(self,value1, value2):
        temp,temp2=None,None
        """
        if value1 is not None and value2 is not None:
            _, current, _ = self._linear_search(value1._value)
            _, current2, _ = self._linear_search(value1._value)
            if current is None and current2 is None and current!=current2:
                self.append(current._value)
            self.intersection_aux(value1._next,value2,source2)
        """
            
        if value1 is not None or value2 is not None:
            
            if value1 is not None:
                _, current, _ = self._linear_search(value1._value)
                
                if current is None:
                    self.append(value1._value)
                    
            if value2 is not None:
                _, current2, _ = self._linear_search(value2._value)
                
                
                if current2 is None:
                    self.append(value2._value)
            
            
            if value1 is not None:
                temp = value1._next
            
            if value2 is not None:
                temp2 = value2._next
                
            
            self.union_r_aux(temp, temp2)
            

            
        

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()

        while self._front is not None:

            if self._front._value < key:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
        return target1, target2

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        new_list = List()
        curr = self._front
        while curr is not None:
            node = _List_Node(curr._value,None)
        
            if new_list._front is None:
                new_list._front = node
            
            #if list is empty, rear has no 'next' so we only do if there is a rear    
            if new_list._rear is not None:
                new_list._rear._next = node
                
            new_list._rear = node
            new_list._count +=1
            curr = curr._next
        
            
        # your code here
        return new_list

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        # your code here
        return

    def _move_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the rs List to the front
        of the current List. Private helper method.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the rs List and
            its count is updated. The rs List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"
        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        node._next = self._front
        self._front = node

        if self._rear is None:
            # Target list is empty
            self._rear = node
        self._count += 1
        return    

        # your code here
        

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"
      
        while source1._front is not None and source2._front is not None:
            self._move_front_to_rear(source1)
            self._move_front_to_rear(source2)

        if source1._front is not None:
            self._append_list(source1)

        if source2._front is not None:
            self._append_list(source2)
            

        # your code here
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return
    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        node._next = None
        self._rear = node
        self._count += 1
        return
    def _append_list(self, source):
        """
        -------------------------------------------------------
        Helper method to append the entire source list to the rear of the target list.
        The source list becomes empty.
        Use: target._append_list(source)
        -------------------------------------------------------
        Parameters:
            source - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        # Update the target queue
        if self._rear is None:
            # Current queue is empty.
            self._front = source._front
        else:
            self._rear._next = source._front

        self._rear = source._rear
        self._count += source._count
        # Empty the source queue.
        source._front = None
        source._rear = None
        source._count = 0
        return




    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next