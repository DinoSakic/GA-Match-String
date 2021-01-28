import random
import string

GA_Populacija = 2048
GA_Elitizam= 0.10 # stopa elitizma
GA_Mutacija = 0.25 # stopa mutacije
GA_Cilj = "Sretna nova godina! 2021" # String koji zelimo da GA pronadje
GA_Karakteri = string.printable

def randstr():
    return "".join([random.choice(GA_Karakteri) for i in range(len(GA_Cilj))])

def fitness(n):
    return sum([abs(ord(n[j]) - ord(GA_Cilj[j])) for j in range(len(GA_Cilj))])

def ukrstanje(pop, buffer):
    esize = int(GA_Populacija * GA_Elitizam)
    for i in range(esize): # Elitizam
        buffer[i] = pop[i]
    for i in range(esize, GA_Populacija):    # jedna tacka ukrstanja
        i1 = random.randint(0, GA_Populacija / 2)
        i2 = random.randint(0, GA_Populacija / 2)
        spos = random.randint(0, len(GA_Cilj))
        buffer[i] = pop[i1][:spos] + pop[i2][spos:] # ukrstanje i1 i i2
        if random.random() < GA_Mutacija: # Mutacija
            pos = random.randint(0, len(GA_Cilj) - 1)
            buffer[i] = buffer[i][:pos] + random.choice(GA_Karakteri) + buffer[i][pos + 1:]

populacija = [randstr() for i in range(GA_Populacija)]
buffer = [randstr() for i in range(GA_Populacija)]
k = 1
while True:
    populacija = sorted(populacija, key=lambda c: fitness(c))
    print(f"generacija: {k}, fitnes: {fitness(populacija[0])}, {populacija[0]}")
    k += 1
    if not fitness(populacija[0]):
        break
    ukrstanje(populacija, buffer)
    populacija, buffer = buffer, populacija
