# from .SingleLinkedList import SingleLinkedList
from Data_structure.SingleLinkeList.SingleLinkedList import SingleLinkedList


class Merge_Output_Print:

    def __init__(self):

        list1 = SingleLinkedList()
        list2 = SingleLinkedList()

        print('Create list1')
        list1.create_list()
        print('Create list2')
        list2.create_list()

        list1.bubble_sort_exdata()
        list2.bubble_sort_exdata()

        print('First List -'); list1.display_list()
        print("Second list "); list2.display_list()

        list3 = list1.merge1(list2)
        print('Merge List - by creating new list'); list3.display_list()

        print('First List -');list1.display_list()
        print("Second list ");list2.display_list()

        list3 = list1.merge2(list2)
        print('Merge List - by rearranging link ');list3.display_list()
        print('First List -');list1.display_list()
        print("Second list ");list2.display_list()
