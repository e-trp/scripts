#!/usr/bin/python3
# -*- coding: utf-8 -*-

# проверка списка
def checklist(list):
    for i in range(0,len(list)-1):
        if list[i]>list[i+1]:
            return False
    return True


# бинарный поиск
def binsearch(list,number):
    left=0
    right=len(list)-1
    while left!=right:
        mid=(left+right)//2
        if number==list[mid]:
            return mid
        if number>list[mid]:
            left=mid-1
        if number<list[mid]:
            right=mid+1
    return None

# поиск наименьшего числа
def searchsmaller(list):
    small=list[0]
    index=0
    for i in range(1,len(list)):
        if small>list[i]:
            small=list[i]
            index=i
    return index

# сортировка выбором
def selectionsort(list):
    li=[]
    for i in range(0, len(list)):
        smaller=searchsmaller(list)
        li.append(list.pop(smaller))
    return li

def non_mutable_selectionsort(list):
    ordli=[]
    for i in range(0,len(list)):
        min=list[i]
        index=i
        for l in list[i:]:    
            if min>list[l]:
                min=list[l]
                index=l
        list[index]=list[i]
        ordli.append(min)
    return ordli

# быстрая сортировка
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
    return quicksort(less)+[pivot]+quicksort(greater)


def bubblesort(list):
    for i in range(0,len(list)):
        for o in range(0,len(list)):
            if list[i]<list[o]:
                (list[i],list[o])=(list[o],list[i])
    return list

