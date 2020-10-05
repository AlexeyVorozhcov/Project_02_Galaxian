import pickle
import glb

# записать геймеров в файл
def write_bd_gamers():
    with open('out.txt', 'wb') as out:
        pickle.dump(bd_gamers, out)

# прочитать геймеров из файла
def  read_bd_gamers():
    with open('out.txt', 'rb') as inp:
        bd_gamers = pickle.load(inp)
    return bd_gamers

bd_gamers = read_bd_gamers()


# bd_gamers={'ALEX':{}, 'Tamara':{}, 'bimax':{}, 'Катя':{}}

# прочитать последнего игрока
def  read_last_gamer():
    with open('last_gamer.txt', 'rb') as inp:
        glb.num_gamer = pickle.load(inp)
        print(glb.num_gamer)


read_last_gamer()

def add_new_gamer(name):
    bd_gamers[name] = {}
    write_bd_gamers()
    glb.num_gamer=len(bd_gamers)-1
    print(glb.num_gamer)
    print(bd_gamers)

def del_gamer_from_base(name):
    trash = bd_gamers.pop(name)
    write_bd_gamers()
    glb.num_gamer = len(bd_gamers) - 1
    print(glb.num_gamer)
    print(bd_gamers)

# add_new_gamer('NNNNN')
# записать последнего игрока
def write_last_gamer():
    with open('last_gamer.txt', 'wb') as out:
        pickle.dump(glb.num_gamer, out)


# write_last_gamer()




#Получить тройку лидеров по очкам уровня n
def get_liders(n):
    result=[]
    temp = []
    for gamer, table in bd_gamers.items():
        for lev_n, lev_p in table.items():
            if lev_n == n:
                temp.append([gamer, lev_p])
    temp.sort(key=lambda i:i[1], reverse=True)
    # print(temp)
    k=0
    for i in temp:
        k+=1
        result.append(i)
        if k==3: break
    # print(result)
    return result

#получить текущего игрока
def get_now_gamer():
    return get_all_gamers()[glb.num_gamer]

# получить список всех игроков
def get_all_gamers():
    result = []
    for gamer, table in bd_gamers.items():
        if gamer not in result:
            result.append(gamer)
    # print(result)
    return result

# получить количество очков у текущего игрока на определенном уровне
def get_points_of_gamer_on_level(num_level):
    result = 0
    if bd_gamers[get_now_gamer()].get(num_level) != None:
        result = bd_gamers[get_now_gamer()][num_level]
    return result

#get_liders(6)
#get_now_gamer()


#write_last_gamer()