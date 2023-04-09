#!/usr/bin/python3
"""method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    # """se recorren las posiciones de las cajas que se pueden abrir"""
    # for j in range(len(boxes)):
    #     if boxes[j]:
    #         continue
    #     else:
    #         if (j < len(boxes) - 1):
    #             return False
    # return True

    lista_v = [0]
    for i in lista_v:
        for j in boxes[i]:
            if j < len(boxes) and j not in lista_v:
                lista_v.append(j)
        if len(lista_v) == len(boxes):
            return True
    return False
