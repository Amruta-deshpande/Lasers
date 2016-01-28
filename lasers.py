__author__ = 'dell'
"""
This is lab assignment to implement a laser which is placed on one square of the grid and covers three of the
four horizontally or vertically adjacent square and to cover the highest sum of numbers possible.
Author: 1. Amruta Deshpande (asd8933@rit.edu)
        2. Shreya Joshi (saj3899@rit.edu)

"""
import collections
import sortFile
# the initial constants
newList=[]
results=[]

def openFile():
    """
    openFile function is used to open a given file and then splits the line using delimiter
    :param data : Splits line using delimiter
    :param results : Creating a list using list comprehensions
    :param newList : Creates list of list
    """
    filename = input('File name please:')
    try:
        with open(filename) as fname:
            for line in fname:
                line = line.strip()
                data = line.split(' ')
                results = [int(iter) for iter in data]
                newList.append(results)
    except FileNotFoundError as e:
        print(e)

def theLasers(Num):
    """
    theLasers function give the positions and orientations for the solution and calculates the sum for the laser
    :param Lasers : collections for namedtuple
    :param listSum : is a list used to store the sum of the laser
    :param finalListLaser: is a list used to store the final list
    :param endCol: is the last column of the grid
    :param endRow: is the last row of the grid
    :param sumS: is the sum of south orientation of the laser
    :param sumN: is the sum of north orientation of the laser
    :param sumE: is the sum of east orientation of the laser
    :param sumW: is the sum of west orientation of the laser
    """
    Lasers=collections.namedtuple('Lasers','row column orientation sum')
    listSum=[]
    listLasers=[]
    finalListLaser=[]
    endCol=(len(newList[0]))-1
    endRow=len(newList)-1
    for index in range(len(newList)):
        for jindex in range(len(newList[0])):
            if (index==0 and jindex==0) or (index==0 and jindex==endCol) or (index==endRow and jindex==0) or (index==endRow and jindex==endCol):
                continue
            elif index==0 and jindex!=(len(newList[0])-1) and jindex!=0:
                sumS=newList[index+1][jindex]+newList[index][jindex+1]+newList[index][jindex-1]
                listSum.append(sumS)
                laserS=Lasers(column=index,row=jindex,orientation='south',sum=sumS)
                listLasers.append(laserS)
            elif index==endRow and (jindex!=(len(newList[0])-1)) and jindex!=0:
                sumN=newList[index-1][jindex]+newList[index][jindex+1]+newList[index][jindex-1]
                listSum.append(sumN)
                laserN=Lasers(column=index,row=jindex,orientation='north',sum=sumN)
                listLasers.append(laserN)
            elif jindex==0 and index!=0 and index!=(len(newList)-1):
                sumE=newList[index+1][jindex]+newList[index-1][jindex]+newList[index][jindex+1]
                listSum.append(sumE)
                laserE=Lasers(column=index,row=jindex,orientation='east',sum=sumE)
                listLasers.append(laserE)
            elif jindex==endCol and index!=0 and index!=(len(newList)-1):
                sumW=newList[index+1][jindex]+newList[index-1][jindex]+newList[index][jindex-1]
                listSum.append(sumW)
                laserW=Lasers(column=index,row=jindex,orientation='west',sum=sumW)
                listLasers.append(laserW)
            else:
                sumS=newList[index+1][jindex]+newList[index][jindex+1]+newList[index][jindex-1]
                sumN=newList[index-1][jindex]+newList[index][jindex+1]+newList[index][jindex-1]
                sumE=newList[index+1][jindex]+newList[index-1][jindex]+newList[index][jindex+1]
                sumW=newList[index+1][jindex]+newList[index-1][jindex]+newList[index][jindex-1]
                newMax=max(sumS,sumN,sumE,sumW)
                listSum.append(newMax)
                if newMax==sumS:
                    laserS=Lasers(column=index,row=jindex,orientation='south',sum=sumS)
                    listLasers.append(laserS)
                elif newMax==sumN:
                    laserN=Lasers(column=index,row=jindex,orientation='north',sum=sumN)
                    listLasers.append(laserN)
                elif newMax==sumE:
                    laserE=Lasers(column=index,row=jindex,orientation='east',sum=sumE)
                    listLasers.append(laserE)
                elif newMax==sumW:
                    laserW=Lasers(column=index,row=jindex,orientation='west',sum=sumW)
                    listLasers.append(laserW)

    finalList=sortFile.mergesort(listSum)
    lastList=finalList[::-1]
    checked=[]
    for eiter in lastList:
       if eiter not in checked:
           checked.append(eiter)

    for iter in range(Num):
        sortSum=checked[iter]
        for jiter in range(len(listLasers)):
            if listLasers[jiter].sum==sortSum:
                finalListLaser.append(listLasers[jiter])

    for iter in range(Num):
        print(finalListLaser[iter])

def main():
    """
    The main function calls the openFile method and take number of lasers from the user.
    :return: None
    """
    openFile()
    Num=int(input('Enter the number of lasers:'))
    theLasers(Num)

if __name__ == '__main__':
    main()