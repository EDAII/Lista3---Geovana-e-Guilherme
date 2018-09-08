## Busca e Ordenação
### Gerenciador do Matrícula Web

##### Alunos

| Matrícula | Nome |
|--|--|
| 16/0122180 | Geovana Ramos Sousa Silva |
| 16/0123186 | Guilherme Guy de Andrade |

##### Para rodar
```sh
$ python3 lista3.py
```

##### Descrição
A pasta do projeto contém um arquivo chamado **codMat.txt**, o qual inclui todas as disciplinas da UnB da oferta 2018.1 no formato:

*< CÓDIGO >-< NOME DA DISCIPLINA >*

Além disso, a pasta **mwsresult** possui subpastas para cada disciplina existente no txt descrito acima, as quais contêm outros txts com as informações da disciplina e todas as turmas referentes a ela. 

Estes arquivos foram gerados por um [script](https://gitlab.com/atlasds/ds2017) criado por uma equipe de outra disciplina do curso de Engenharia de Software, composta também pela dupla que realizou este projeto de EDA2.

O programa em Python irá ler o codMat.txt e carregar todas as disciplinas no programa. A partir disso o usuário poderá:

- Ordenar por código - QuickSort 
    - Irá ordenar o conjunto de matérias por seu código usando o QuickSort como método de ordenação.
- Ordenar por código - MergeSort 
    -  Irá ordenar o conjunto de matérias por seu código usando o MergeSort como método de ordenação.
- Embaralhar
    - Irá desordenar o conjunto de matérias.
-  Status (ordenado ou não)
    - Informa se as matérias estão ordenadas.
- Imprimir tudo
    - Irá imprimir no terminal todas as matérias.
-  Mostrar detalhes de disciplina 
    - Pede o código da disciplina e informa suas turmas, horários, professores e créditos. Esses dados serão buscados na subpasta da disciplina dentro da pasta mwsresult. 
- Busca por nome
    - Pede uma entrada de texto e busca todas as disciplinas que contenham esse texto no seu nome.
- Sair
    - Encerra o programa


##### Busca
A busca utilizada foi a Busca Binária.

##### Ordenação
A ordenação utilizada foi o MergeSort e o QuickSort.
