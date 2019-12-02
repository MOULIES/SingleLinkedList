from Data_structure.SingleLinkeList.Merge_Output_Display import Merge_Output_Print
from Data_structure.SingleLinkeList.SingleLinkedList import SingleLinkedList


def main():
    list = SingleLinkedList()
    list.create_list()
    while True:

        print("1.Display list")
        print("2.Count the number of nodes")
        print('3.Search for an element')
        print('4.Insert in empty list/Insert in beginning fo the list')
        print('5.Insert a node at the end of the list')
        print('6. Insert a node after a specified node')
        print('7. Insert a node before a specified node')
        print('8. Insert a node at a given position')
        print('9. Delete first node')
        print('10. Delete last node')
        print('11.Delete any node')
        print('12. Reverse the list')
        print('13. Bubble sort by exchanging data')
        print('14. Bubble sort by exchanging links')
        print('15.Merge sort by exchanging data and rearranging link')
        print('16.Merge sort')
        print('17.Insert cycle')
        print('18.Detect cycle')
        print('19. Remove cycle')
        print('20.Quit')
        option = int(input('Enter your choice:'))
        if option == 1:
            list.display_list()
        elif option == 2:
            list.count_nodes()
        elif option == 3:
            data = int(input('enter the element to be searched: '))
            list.search(data)
        elif option == 4:
            data = int(input('enter the element to be inserted: '))
            list.insert_in_beginning(data)
        elif option == 5:
            data = int(input('enter the element to be inserted: '))
            list.insert_at_end(data)
        elif option == 6:
            data = int(input('enter the element to be inserted: '))
            x = int(input('Enter the element after which to insert: '))
            list.insert_after(data, x)
        elif option == 7:
            data = int(input('enter the element to be inserted: '))
            x = int(input('Enter the element before which to insert: '))
            list.insert_before(data, x)
        elif option == 8:
            data = int(input('enter the element to be inserted: '))
            k = int(input('Enter the positon at which to insert : '))
            list.insert_at_position(data, k)
        elif option == 9:
            list.delete_first_node()
        elif option == 10:
            list.delete_last_node()
        elif option == 11:
            data = int(input('enter the element to be deleted: '))
            list.delete_node(data)
        elif option == 12:
            list.reverse_list()
        elif option == 13:
            list.bubble_sort_exdata()
        elif option == 14:
            list.bubble_sort_exlinks()
        elif option == 15:
            # list.merge_sort()

            a = Merge_Output_Print()
        elif option == 16:
            list.merge_sort()
        elif option == 17:
            data = int(input('enter the element at which the cycle to be inserted: '))
            list.insert_cycle(data)
        elif option == 18:
            if list.has_cycle():
                print('List has a cycle')
            else:
                print('List does not have a cycle')
        elif option == 19:
            list.remove_cycle()

        elif option == 20:
            break
        else:
            print('Wrong option')
        print()


if __name__ == '__main__':
    main()
