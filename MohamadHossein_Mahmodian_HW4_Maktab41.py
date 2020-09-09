from random import randint 
import functools as f

table = [[0,0,0,],[0,0,0,],[0,0,0,]]

def view_table(table):
    for row in table:
        print(row)

def set_cpu():
    i ,j = randint(0,2),randint(0,2)
    while table[i][j] != 0:
        multi =[f.reduce(lambda a,b: a*b,i)for i in table]
        print(multi)
        if 0 in multi:
            i ,j = randint(0,2),randint(0,2)
        else:
            result = master(table)
            return result
    else:
        table[i][j] = -1
        return table


def set_user(i,j):
    while table[i][j] != 0:
        print('Oops select empty cell')
        return False
    else:
        table[i][j] = 1
        return table

def validator(sumx):
    if sumx == 3:
        return True
    elif sumx == -3:
        return False

def rows(page):
    for sublist in page:
        sumx = sum(sublist)
        if validator(sumx) == True:
            return 'You Win'         
        elif validator(sumx) == False:  
            return 'CPU Win'

def column(page):
    for counter in range(3):
        sumx = 0
        for sublist in page:
            sumx += sublist[counter]
            if validator(sumx) == True:
                return 'You Win'
            elif validator(sumx) == False:  
                return 'CPU Win'

def orib(page):
    x = 0
    for sublist in page:
        sumx = sublist[x]
        x += 1
        if validator(sumx) == True:
            return 'You Win'
        elif validator(sumx) == False:  
            return 'CPU Win'

def xorib(page):
    x = 2
    sumx = 0
    for sublist in page:
        sumx += sublist[x]
        x -= 1
        if validator(sumx) == True:
            return 'You Win' 
        elif validator(sumx) == False:  
            return 'CPU Win' 

def master(page):
    if rows(page) != None:
        return rows(page)
    elif column(page) != None:
        return column(page)
    elif orib(page) != None:
        return orib(page)
    elif xorib(page) != None:
        return xorib(page)
    else:
        return False


view_table(table)


while True:
    i,j = map(int,input('Give me i, j:').split())
    stat = set_user(i,j)
    if stat == False:
        continue
    stat = set_cpu()
    if stat == False:
        view_table(table)
        print('Nobody win !!!')
        break
    else:
        view_table(table)
        result = master(table)
    if result == 'You Win' or result == 'CPU Win':
        print(result)
        break
#_______________________________________________________________________________________


