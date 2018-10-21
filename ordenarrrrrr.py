import random
import time

class Lista(object):
    def __init__(self, tam, ordem, porcentagem):        #recebe como parametro do objeto o (tamanho da lista, o tipo de ordem <Aleatorio,Crescente> etc, e quantos % já ordenado)
        self.lista = []
        self.Tamanho = tam
        self.Ordenado = False
        for i in range(tam):
            self.lista.append(random.randrange(10 * tam))

        if (ordem == "Decrescente"):
            if (porcentagem == 0):
                self.lista = sorted(self.lista, reverse=True)
            else:
                num = (self.Tamanho * porcentagem) // 100
                aux1 = sorted(self.lista)                              #1.0 uso um auxiliar para guardar a lista ordenada
                aux = aux1[:num]                                       #1.1 uso outro auxiliar para pegar somente a porcentagem ja ordenada
                aux2 = sorted(aux1[num:], reverse=True)                #1.2 em outro auxiliar jogo os números que não fazem parte da porcentagem já ordenada,porém ja em ordem decrescente
                self.lista = aux + aux2                                #junto os 2 auxiliares usados em (1.1) e (1.2) na self.lista

        if (ordem == "Crescente"):
            self.lista = sorted(self.lista)

        if (ordem == "Aleatoria"):
            if (porcentagem != 0):
                num = (self.Tamanho * porcentagem) // 100
                aux1 = sorted(self.lista)
                aux = aux1[:num]
                aux2 = aux1[num:]
                random.shuffle(aux2)        # da mesma forma feita em Ordem Decrescente, porém a mudança ocorre que em vez de ordenar em forma decrescente os números que não fazem
                self.lista = aux + aux2     # parte da porcentagem já ordenada, eu embaralho a lista para ficar de forma aleatória

    def __str__(self):
        c = 0
        string = ":\n"
        string += '['
        for i in self.lista:
            if c != (self.Tamanho - 1):
                string += (str(i) + ', ')
                c += 1
            else:
                string += (str(i) + '] ')
        return string

    def selectSort (self):
        inicio = time.time()
        for i in range(self.Tamanho-1):
            i_min = i
            for j in range(i+1,self.Tamanho):
                if (self.lista[j] < self.lista[i_min]):         #o primeiro passo é pegar o menor item da lista e coloca-lo na primeira posição, depois desse passo não há mais
                    i_min = j                                   #comparações com o primeiro elemento, ficando assim (num de elementos-1), o processo se repete até sobrar aoenas um elemento

            if (self.lista[i] != self.lista[i_min]):               #quando acha o menor elemento realiza a troca
                aux = self.lista[i]
                self.lista[i] = self.lista[i_min]
                self.lista[i_min] = aux
        self.Ordenado = True
        fim = time.time()
        print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))

    def insertSort(self):
        inicio = time.time()
        for i in range(1, len(self.lista)):         #ordena sempre deixando os elementos da esquerda em ordem crescente
            chave = self.lista[i]
            k = i
            while k > 0 and chave < self.lista[k - 1]:
                self.lista[k] = self.lista[k - 1]
                k -= 1
            self.lista[k] = chave

        self.Ordenado = True
        fim = time.time()
        print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))
    def shellSort(self):                                    # é um tipo de inserção direta so que em vez de usar a lista para ser ordenada como um único segmento, ele usa vários segmentos
        inicio = time.time()
        h = 1
        while h > 0:
            for i in range(h, self.Tamanho):
                key = self.lista[i]

                j = i
                while j >= h and key <= self.lista[j - h]:
                    self.lista[j] = self.lista[j - h]
                    j -= h
                    self.lista[j] = key
            h = h // 2
        self.Ordenado = True
        fim = time.time()
        print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))
    def mergeSort(self):
        inicio = time.time()
        self.mergeRecursive(self.lista)
        self.Ordenado = True
        fim = time.time()
        print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))
    def mergeRecursive(self, lista):
        middle = len(lista) // 2                            # pega o elemento do meio da lista
        left = lista[:middle]                               # divide a lista com elementos da esquerda
        right = lista[middle:]                              # divide a lista com elementos da direita

        if len(lista) > 1:
            self.mergeRecursive(
                left)                                       # usa a Ordenação dividir-para-conquistar, dividindo a sequência em 2 subsequências n/2
            self.mergeRecursive(
                right)                                      # depois ordena as 2 subsequências recursivamente utilizando ordenação por intercalação

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
    def quickSort(self):
        inicio = time.time()
        self.quickSortHelper(self.lista,0, len(self.lista)-1)       #
        self.Ordenado = True
        fim = time.time()
        print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))
    def quickSortHelper(self,lista, first, last):
        if first < last:
            splitpoint = self.partition(lista, first, last)

            self.quickSortHelper(lista, first, splitpoint - 1)
            self.quickSortHelper(lista, splitpoint + 1, last)

    def partition(self, lista , first, last):
        pivotvalue = lista[first]                                #valor do pivot

        leftmark = first + 1                                     #seta da esquerda
        rightmark = last                                         #seta da direita

        done = False
        while not done:

            while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = lista[leftmark]
                lista[leftmark] = lista[rightmark]
                lista[rightmark] = temp

        temp = lista[first]
        lista[first] = lista[rightmark]
        lista[rightmark] = temp

        return rightmark

    def maxHeapfy(self, root, tam):
        maior = root
        left = 2 * root + 1          #root= raiz // left=filho da esquerda // right= filho da direita
        right = 2 * root + 2


        if left < tam and self.lista[left] > self.lista[root]:
            maior = left


        if right < tam and self.lista[right] > self.lista[maior]:
            maior = right


        if maior != root:
            aux = self.lista[root]
            self.lista[root] = self.lista[maior]
            self.lista[maior] = aux

            self.maxHeapfy(maior, tam)

    def heapSort(self):
        inicio = time.time()
        for i in range(self.Tamanho, -1, -1):
            self.maxHeapfy(i, self.Tamanho)


        for i in range(self.Tamanho - 1, 0, -1):

            aux = self.lista[i]
            self.lista[i] = self.lista[0]
            self.lista[0] = aux

            self.maxHeapfy(0, i)
        self.Ordenado = True
        fim = time.time()
        print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))
    def countSort(self):
        inicio = time.time()
        mx = max(self.lista)
        n1 = [0 for i in range(mx + 1)]                                 #vetor com tamanho do número máximo do self.lista
        r1 = []
        for i in self.lista:                                            #incrementa +1 no valor que a posição do vetor equivale ao número contido na lista
            n1[i] += 1
        for i in range (len(n1)):
            if n1[i] !=0:
                r1 += [i for n in range (n1[i])]
        for i in range (self.Tamanho):
            self.lista[i]=r1[i]
        self.Ordenado = True
        fim = time.time()
        print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))
    def radixSort(self):
        inicio = time.time()
        RADIX = 10
        maxLength = False
        tmp, placement = -1, 1

        while not maxLength:
            maxLength = True

            buckets = [list() for _ in range(RADIX)]                    #o bucket começa vazio com tamanho do valor de RADIX

            for i in self.lista:
                tmp = i / placement

                buckets[int(tmp % RADIX)].append(i)                     #adiciona a lista bucket os elementos de acordo algarismo
                if maxLength and tmp > 0:
                    maxLength = False

            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    self.lista[a] = i
                    a += 1

            placement *= RADIX                                  # o placement é incrementado para extrair o próximo algarismo do número
        self.Ordenado = True
        fim = time.time()
        print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))