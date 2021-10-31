import random
import subprocess, platform



pop = []
numb = 0

def clear():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine
    else: #Linux and Mac
        print("\033c", end="")


def main():
    #x = int(input("number: "))
    x = 10
    generPop(x)
    print(f"first{pop}")
    life(x)




def parameters():
    radLife = 20
    radReprod = 10


def generPop(x: int):
    for _ in range(0, x):
        pop.append(int(random.randint(1, 100)))


def life(x):
    global numb
    i = 0
    numb_rep = 0
    while i+1 < x:
        if pop[i] == 0:
            print(pop)
            i += 1
        else:
            pos_chance = 100 - abs(pop[i] - pop[i+1])
            rand_chance = random.randint(0, 100)
            if pos_chance >= rand_chance:
                new_ell = int((pop[i] + pop[i+1]) / 2)
                info = f"  {pop[i]} {pop[i+1]} | chance: {pos_chance}/{rand_chance} | new: {new_ell}"
                pop[i] = new_ell
                pop[i+1] = 0
                numb += 1
            else:
                info = ""
            print(pop, info)
            i += 1
    print(f"\nnumber of reproduction: {numb}")
    for _ in range(0, pop.count(0)):
        pop.remove(0)
    print(pop)


main()
i = 1
while numb != 0:
    clear()
    pop = []
    numb = 0
    main()
    i += 1
print(i)
