from tkinter import Label

class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is : ")
            p = self.start
            while p is not None:
                print(p.info,' ',end='')
                p = p.link
            print()


    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n +=1
            p = p.link
        print('Number of nodes on the list = ',n)

    def search(self, x):
        position = 0
        p = self.start
        while p is not None:
            position += 1
            if p.info == x:
                print(f'{x} is found at position {position}')
                return True
            p = p.link
        else:
            print(x,' is not found in the list')
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp


    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp



    def create_list(self):
        n = int(input('Enter the no of nodes : '))
        if n==0:
            return
        for i in range(n):
            data = int(input('Enter the element to be inserted : '))
            self.insert_at_end(data)


    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None:
            print(x, ' Not present in the list')
        else:
            temp= Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        # if list is empty
        if self.start is None:
            print('List is empty')
            return

        # x is in first node,  new node is to be inserted before first node
        if x == self.start.info :
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        #find reference to predecessor of node containing x
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
        if p.link is None:
            print(x, ' Not present in the list')
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp



    def insert_at_position(self, data, k):

        if k ==1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        i = 1
        while i < k-1 and p is  not None: #find a reference to k-1 node
            p = p.link
            i += 1
        if p is None:
            print('you can insert upto postion',i)
        else:
            temp =Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, x):
        if self.start is None:
            print('List is empty')
            return

        #deletion of first node
        if self.start.info == x:
            self.start = self.start.link
            return

        #deletion in between or at the end
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print('Element', x, ' not present in the list')
        else:
            p.link = p.link.link

    def delete_first_node(self):
        if self.start is None:
            print('List is empty')
            return
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            print('List is empty')
            return

        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None



    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q= p.link
                if p.info > q.info:
                    p.info, q.info = q.info,p.info
                p = p.link
            end = p

    def bubble_sort_exlinks(self):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p,q = q,p
                r = p
                p = p.link
            end = p

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge1(self, list2): # Merging br creating a new list
        merge_list = SingleLinkedList()
        merge_list.start = self._merge1(self.start,list2.start)
        return merge_list

    def _merge1(self, p1, p2):
        #create a merge list
        if p1.info <= p2.info:
            startM = Node(p1)
            p1 = p1.link
        else:
            startM = Node(p2)
            p2 = p2.link
        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
            pM = pM.link

        #If second list has finished and element left in first class
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link

        # If first list has finished and element left in second class
        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

    def merge2(self, list2): # Merging br rearranging link
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2 (self.start, list2.start)
        return merge_list

    def _merge2(self, p1, p2):
        if p1.info <= p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link
        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                pM = pM.link
                p1 = p1.link
            else:
                pM.link = p2
                pM = pM.link
                p2 = p2.link
        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1
        return startM


    def merge_sort(self):

        self.start = self.merge_sort_rec(self.start)

    def merge_sort_rec(self,list_start):
        #if list empty or list has only element
        if list_start is None or list_start.link is None:
            return list_start

        #if list has one element
        start1 = list_start
        start2 = self._divide_list(list_start)
        start1 = self.merge_sort_rec(start1)
        print('start1 after dividing ')
        s1 = SingleLinkedList()
        s1.start =start1
        s1.display_list()
        start2 = self.merge_sort_rec(start2)
        print('start2 after dividing ')
        s2 = SingleLinkedList()
        s2.start = start2
        s2.display_list()
        startM = self._merge2(start1,start2)
        return startM

    def _divide_list(self, p):
         q = p.link.link
         while q is not None and q.link is not None:
             p = p.link
             q= p.link.link
         start2 = p.link
         p.link = None
         return start2


