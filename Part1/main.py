# Cheung Kai Cun Ronald, 202670M , IT2153-02
from stock import Stock
from bubble import bubbleSort
from selection import selectionSort
from insertion import insertionSort
from linear import sequentialSearch
from binary import binarySearch
itemsList = []

while True:
    print('------------------MENU--------------------')
    print('(1). Add items into stock inventory')
    print('(2). Update selected item')
    print('(3). Remove items from stock inventory')
    print('(4). Display items in the stock inventory')
    print('(5). Sort items')
    print('(6). Search item')
    print('(7). Exit application')
    print('-----------------------------------------')
    choice = input('Enter action [1-7]:')

    # Add item
    if choice == '1':
        try:
            # user input
            user_desc = input('Enter item description:')
            if not user_desc:
                print('\nDescription cannot be empty!\n')
                continue
            # user_price = '{:.2f}'.format(round(float(input('Enter item selling price:$')),2))
            user_price = float(input('Enter item selling price:$'))
            user_level = int(input('Enter item stock level:'))
            user_amount = int(input('Enter amount of items:'))
            user_expDate = int(input('Enter days till item expiry date:'))
            # set index as key, object as value
            # index increases every object initialization
            itemsList.append(Stock(Stock.count,user_desc,user_price,user_level,user_amount,user_expDate))
            print('\nItem Index',Stock.count, 'added!\n')
            # print data stored in dictionary
            # print('Storage:',itemsdict)
        except ValueError:
            print('\nWrong Value Type!\n')
        except TypeError:
            print('\nExceeded Item limit of 20!\n')

    # Update selected item using index
    elif choice == '2':
        if len(itemsList) >= 1:
            try:
                update = int(input('Enter index of item you want to update:'))
                for i in itemsList:
                    if i.get_index() == update:
                        # user input
                        new_user_desc = input('Enter item description:')
                        if not new_user_desc:
                            print('\nDescription cannot be empty!\n')
                            continue
                        # new_user_price = '{:.2f}'.format(round(float(input('Enter item selling price:$')),2))
                        new_user_price = float(input('Enter item selling price:$'))
                        new_user_level = int(input('Enter item stock level:'))
                        new_user_amount = int(input('Enter amount of items:'))
                        new_user_expDate = int(input('Enter days till item expiry date:'))
                        # setter
                        i.set_desc(new_user_desc)
                        i.set_price(new_user_price)
                        i.set_level(new_user_level)
                        i.set_amount(new_user_amount)
                        i.set_expDate(new_user_expDate)
                        print('\nItem Index', update, 'updated!\n')
            except ValueError:
                print('\nWrong Value Type!\n')
            except IndexError:
                print('\nIndex error\n')
        else:
            print('\nNo items to update!\n')

    # Remove selected item using index
    elif choice == '3':
        if len(itemsList) >= 1:
            try:
                remove = int(input('Enter index of item you want to remove:'))
                for i in itemsList:
                    if i.get_index() == remove:
                        itemsList.remove(i)
                        print('\nItem Index', remove, 'removed!\n')
            except ValueError:
                print('\nWrong Value Type\n')
        else:
            print('\nNo items to remove!\n')

    # Display all items
    elif choice == '4':
        if len(itemsList) >= 1:
            print('\n-------Display---------\n')
            try:
                for i in itemsList:
                    print(i,'\n')
            except IndexError:
                print('\nIndex error\n')
            except KeyError:
                print('\nKey Error\n')
        else:
            print('\nNo items to display!\n')

    # Sort items based on price in ascending order
    elif choice == '5':
        if len(itemsList) > 1:
            print('\n---SORT ITEMS BY PRICE---\n')
            print('(B). Bubble Sort')
            print('(S). Selection Sort')
            print('(I). Insertion Sort')
            sortchoice = input('Enter type of sort [B,S or I]:').upper()
            print('\n')
            try:
                templist = []
                for i in itemsList:
                    templist.append(i.get_price())
                sortedlist = []
                if sortchoice == 'B':
                    sortedlist = bubbleSort(templist)
                    print(sortedlist)
                elif sortchoice == 'S':
                    sortedlist = selectionSort(templist)
                    print(sortedlist)
                elif sortchoice == 'I':
                    sortedlist = insertionSort(templist)
                    print(sortedlist)
                else:
                    print('\nInvalid sort choice!\n')

                if len(sortedlist) > 1:
                    newItemList = []
                    for price in sortedlist:
                        for item in itemsList:
                            if item.get_price() == price:
                                newItemList.append(item)
                    itemsList = newItemList
            except IndexError:
                print('\nIndex error\n')
            except KeyError:
                print('\nKey Error\n')
        else:
            print('\nNo items to sort!\n')

    # Search item based on price
    elif choice == '6':
        if len(itemsList) >= 1:
            print('\n---SEARCH ITEMS BY PRICE---\n')
            print('(L). Linear Search')
            print('(B). Binary Search')
            try:
                searchchoice = input('Enter type of search [L or B]:').upper()
                target = float(input('Enter target price:$'))
                print('\n')
                templist = []
                for i in itemsList:
                    templist.append(i.get_price())
                # sort the list before searching
                templist = sorted(templist)

                if searchchoice == 'L':
                    print('\n',sequentialSearch(templist,target),'\n')
                    # retrieve the target object
                    for j in itemsList:
                        if target == j.get_price():
                            current = j
                            print(current,'\n')
                elif searchchoice == 'B':
                    print('\n',binarySearch(templist,target),'\n')
                    # retrieve the target object
                    for j in itemsList:
                        if target == j.get_price():
                            current = j
                            print(current,'\n')
                else:
                    print('\nInvalid search choice!\n')

            except IndexError:
                print('\nIndex error\n')
            except KeyError:
                print('\nKey Error\n')
            except ValueError:
                print('\nWrong Value Type!\n')
        else:
            print('\nNo items to search!\n')

    # Exit program
    elif choice == '7':
        exit()

    else:
        print('\nInvalid action!\n')
