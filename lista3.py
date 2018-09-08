# -*- coding: utf-8 -*-
import math
import os
import random

from quicksort import QuickSorter


class Subject:
    
    def __init__(self, code, name ):
        self.code = code
        self.name = name

    def __str__(self):
        return 'Código: ' + str(self.code) + ' - Nome: ' + self.name


def search_by_code(code_to_search, subjects):

    lower_index = 0
    upper_index = subjects.__len__() - 1

    while lower_index <= upper_index:

        middle_index = math.floor((upper_index + lower_index) / 2)

        current_subject =  subjects[middle_index]

        if current_subject.code == code_to_search:
            return  current_subject

        elif current_subject.code > code_to_search:
            upper_index = middle_index - 1

        else:
            lower_index = middle_index + 1

    return None


def search_by_name(name_to_search, subjects):

    for subject in subjects:
        if name_to_search.upper() in subject.name:
            print(subject)

def find_subject_path(search_result):

    for folder in os.listdir('mwsresult/'):
        folder_code_name = folder.split('-')
        folder_code = int(folder_code_name[0].rstrip())
        if folder_code == search_result.code:
            return folder

    return None

def read_subject_folder(path):
    
    for file in os.listdir('mwsresult/' + path):
   
        if file != "info.txt":
            print("##### TURMA ######")
        else:
            print("##### INFORMAÇÕES DA MATÉRIA ######")
        read_file('mwsresult/' + path + '/' + file)    


def read_file(path):
    
    file = open(path, 'r')
    for line in file:
        print(line)
    file.close()

def print_subjects(data):
    for subject in data:
        print(subject)

def is_sorted(data, key):

    current_check = data[0]

    for item in data:
        
        if getattr(item, key) >= getattr(current_check, key):
            current_check = item
        else:
            return False

    return True

def mergeSort(subjects):
    # left = starting index of left array
    # mid = ending index of left array 
    # right = ending index of right array
    # merge() = joins left[] and right[] arrays into one array[left...right]
    # sub_array_size = size of left or right array 

    sub_array_size = 1

    while sub_array_size < len(subjects) - 1:
         
        left = 0

        while left < len(subjects)-1:
            
            # (False result,True result) [Condition] 
            mid = ( ( left + sub_array_size - 1, len(subjects) - 1) [ left + sub_array_size - 1 > len(subjects)-1])
         
            # (False result,True result) [Condition] 
            right = ( (2 * sub_array_size + left - 1, len(subjects) - 1) [2 * sub_array_size + left - 1 > len(subjects)-1])
             
            merge(subjects, left, mid, right)
            left = left + sub_array_size*2
             
        sub_array_size = 2 * sub_array_size
    
    return subjects
 
def merge(subjects, left, mid, right):
    # n1 = number of elements in left array
    # n2 = number of elements in right array

    n1 = mid - left + 1 
    n2 = right - mid

    L = [None] * n1    # fill with zeros
    R = [None] * n2    # fill with zeros

    # copy elements
    for i in range(0, n1):
        L[i] = subjects[left + i]
    for i in range(0, n2):
        R[i] = subjects[mid + i + 1]
 
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i].code > R[j].code:
            subjects[k] = R[j]
            j += 1
        else:
            subjects[k] = L[i]
            i += 1
        k += 1
 
    while i < n1:
        subjects[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        subjects[k] = R[j]
        j += 1
        k += 1


########################### MAIN ####################################

file = open("codMat.txt", "r")

subjects = []

for line in file:
    if line.strip():
        subject_code_name = line.split('-')
        code = int(subject_code_name[0].rstrip())
        name = subject_code_name[-1].rstrip()
        subjects.append(Subject(code, name))

file.close()

while True:
    
    choice = int(input("""
        Escolha uma opção:
        (1) Ordenar por código - QuickSort 
        (2) Ordenar por código - MergeSort 
        (3) Embaralhar
        (4) Status (ordenado ou não)
        (5) Imprimir tudo
        (6) Mostrar detalhes de disciplina 
        (7) Busca por nome
        (0) Sair           
    """))
    
    if choice == 0:
        break

    elif choice == 1:
        qSort = QuickSorter()
        subjects = qSort.sort(subjects, key='code')

    elif choice == 2:
        subjects = mergeSort(subjects)

    elif choice == 3:
        random.shuffle(subjects)

    elif choice == 4:
        print('Por código: ' + str(is_sorted(subjects, 'code')))
        print('Por nome: ' + str(is_sorted(subjects, 'name')))
    
    elif choice == 5:
        print_subjects(subjects)
    
    elif choice == 6:
        code_to_search = int(input("Digite o código da matéria: "))
        if not is_sorted(subjects, 'code'):
            qSort = QuickSorter()
            subjects = qSort.sort(subjects, key='code')
        search_result = search_by_code(code_to_search, subjects)
        path = find_subject_path(search_result)
        read_subject_folder(path)

    elif choice == 7:
        name_to_search = input('Digite o nome da disciplina: ')
        search_by_name(name_to_search, subjects)

    else:
        print("Opção inexistente!") 
    

