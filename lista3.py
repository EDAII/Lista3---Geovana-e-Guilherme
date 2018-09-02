# -*- coding: utf-8 -*-
import math
import os


class Subject:
    
    def __init__(self, code, name ):
        self.code = code
        self.name = name


def search(code_to_search, subjects):

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
    # Estou usando busca binária então tem que estar ordenado por código
    choice = int(input("""
        Escolha o método e o parâmetro de ordenação:
        (1) Método 1 - por código
        (2) Método 1 - por matéria
        (3) Método 2 - por código
        (4) Método 2 - por matéria 
        (5) Sair           
    """))

    if choice == 1:
        break
    elif choice == 2:
        break
    elif choice == 3:
        break
    elif choice == 4:
        break
    elif choice == 5:
        break
    else:
        print("Opção inexistente!") 
    

code_to_search = int(input("Digite o código da matéria: "))

search_result = search(code_to_search, subjects)

path = find_subject_path(search_result)

read_subject_folder(path)