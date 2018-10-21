from ordenarrrrrr import Lista
import sys

if (sys.argv[1]=="Ordenar"):                #o sys.argv[x] é o argumento que é recebido da linha de comando
    if (sys.argv[3].isdigit()):             #as comparações são feitas para que a entrada esteja perfeita como o programa requer
        tam= int(sys.argv[3])
        porcentagem = int(sys.argv[5])
        randomList= Lista(tam,sys.argv[4],porcentagem)
        if (sys.argv[2]=="SelectSort"):
            print ("Lista {} {}% já Ordenada {}".format(sys.argv[4],porcentagem, randomList))
            randomList.selectSort()
            print("Lista Ordenada em {} {} ".format(sys.argv[2],randomList))
        elif (sys.argv[2]=="InsertSort"):
            print("Lista {} {}% já Ordenada {}".format(sys.argv[4], porcentagem, randomList))
            randomList.insertSort()
            print("Lista Ordenada em {} {} ".format(sys.argv[2], randomList))
        elif (sys.argv[2]=="ShellSort"):
            print("Lista {} {}% já Ordenada {}".format(sys.argv[4], porcentagem, randomList))
            randomList.shellSort()
            print("Lista Ordenada em {} {} ".format(sys.argv[2], randomList))
        elif (sys.argv[2]=="MergeSort"):
            print("Lista {} {}% já Ordenada {}".format(sys.argv[4], porcentagem, randomList))
            randomList.mergeSort()
            print("Lista Ordenada em {} {} ".format(sys.argv[2], randomList))
        elif (sys.argv[2]=="QuickSort"):
            print("Lista {} {}% já Ordenada {}".format(sys.argv[4], porcentagem, randomList))
            randomList.quickSort()
            print("Lista Ordenada em {} {} ".format(sys.argv[2], randomList))
        elif (sys.argv[2]=="CountSort"):
            print("Lista {} {}% já Ordenada {}".format(sys.argv[4], porcentagem, randomList))
            randomList.countSort()
            print("Lista Ordenada em {} {} ".format(sys.argv[2], randomList))
        elif (sys.argv[2]=="RadixSort"):
            print("Lista {} {}% já Ordenada {}".format(sys.argv[4], porcentagem, randomList))
            randomList.radixSort()
            print("Lista Ordenada em {} {} ".format(sys.argv[2], randomList))
        elif (sys.argv[2]=="HeapSort"):
            print("Lista {} {}% já Ordenada {}".format(sys.argv[4], porcentagem, randomList))
            randomList.heapSort()
            print("Lista Ordenada em {} {} ".format(sys.argv[2], randomList))
        else:
            print("Tente Novamente Usando : Ordenar <algoritmo> <quantidade> <TipoDeOrdem> <PorcentagemJaOrdenada>")
    else:
        print("Tente Novamente Usando : Ordenar <algoritmo> <quantidade> <TipoDeOrdem> <PorcentagemJaOrdenada>")
else:
    print("Tente Novamente Usando : Ordenar <algoritmo> <quantidade> <TipoDeOrdem> <PorcentagemJaOrdenada>")
