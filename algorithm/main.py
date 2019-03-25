import random, copy
from Classes import Group, Professor, CourseClass, Room, Slot
from math import ceil, log2
import math

Slot.slots = [Slot("9:00", "11:00", "Mon"), Slot("11:00", "13:00", "Mon"), Slot("13:00", "15:00", "Mon"),
              Slot("9:00", "11:00","Tue"), Slot("11:00", "13:00", "Tue"), Slot("13:00", "15:00", "Tue"),
              Slot("9:00", "11:00","Wed"), Slot("11:00", "13:00", "Wed"), Slot("9:00", "11:00","Thu"), 
              Slot("11:00", "13:00", "Thu"), Slot("13:00", "15:00", "Thu"), Slot("9:00", "11:00","Fri"),
              Slot("11:00", "13:00", "Fri")]

max_score = None

cpg = []
slots = []
CourseClass.classes = []
Professor.professors = []
Group.groups = []
Room.rooms = []
bits_needed_backup_store = {}  # to improve performance

inputls = [["CSE1", "Natalie", "Cl02", "CC11"], ["CSE1", "David", "Cl03", "CC11"], ["CSE1", "Natalie", "Cl01", "CC12"],\
           ["CSE2", "Natalie", "Cl02", "CC11"], ["CSE2", "David", "Cl03", "CC11"], ["CSE2", "Natalie", "Cl01", "CC12"],\
           ["ESC1", "Sun Jun", "Cl02", "CC11"], ["ESC1", "Sun Jun", "Cl03", "CC11"], ["ESC1", "Sun Jun", "Cl01", "CC12"],\
           ["ESC2", "Sun Jun", "Cl02", "CC11"], ["ESC2", "Sun Jun", "Cl03", "CC11"], ["ESC2", "Sun Jun", "Cl01", "CC12"],\
           ["ESC3", "Sun Jun", "Cl02", "CC11"], ["ESC3", "Sun Jun", "Cl03", "CC11"], ["ESC3", "Sun Jun", "Cl01", "CC12"],\
           ["P&S1", "Tony", "Cl02", "CC12"], ["P&S1", "Tony", "Cl03", "CC12"], ["P&S1", "Tony", "Cl01", "CC12"]]
           
def input_info(): 

    for e in inputls:
        if CourseClass.find(e[0]) == -1:
            CourseClass.classes.append(CourseClass(e[0]))
        if Professor.find(e[1]) == -1:
            Professor.professors.append(Professor(e[1]))
        if Group.find(e[2]) == -1:
            Group.groups.append(Group(e[2]))  
        if Room.find(e[3]) == -1:
            Room.rooms.append(Room(e[3]))

   
def get_cpg():
    input_info()
    len1 = len(inputls)
    for i in range(len1):
        
       cpg.append(CourseClass.find(inputls[i][0]))
       cpg.append(Professor.find(inputls[i][1]))
       cpg.append(Group.find(inputls[i][2]))
       cpg.append(Room.find(inputls[i][3]))


def bits_needed(x):
    global bits_needed_backup_store
    r = bits_needed_backup_store.get(id(x))
    if r is None:
        r = int(ceil(log2(len(x))))
        bits_needed_backup_store[id(x)] = r
    return max(r, 1)


def join_cpg_pair(_cpg):
    res = []
    for i in range(0, len(_cpg), 4):
        res.append(_cpg[i] + _cpg[i + 1] + _cpg[i + 2] + _cpg[i + 3])
    return res


def convert_input_to_bin():
    global cpg, slots, max_score, inputls
    input_info()
    cpg.clear()
    '''
    cpg = [CourseClass.find("CSE"),Professor.find("Natalie"),Group.find("Cl02"),
           CourseClass.find("CSE"),Professor.find("David"),Group.find("Cl03"),
           CourseClass.find("CSE"),Professor.find("Natalie"),Group.find("Cl01")]
    '''
    get_cpg()
    print(type(cpg))
    print(cpg)
    for _c in range(len(cpg)):
        #print(type(_c))
        
        if _c % 4 == 0:  # CourseClass
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(CourseClass.classes), '0')       
        elif _c % 4 == 1:  # Professor
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Professor.professors), '0')
        elif _c % 4 == 2:  # Group
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Group.groups), '0')
        else:
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Room.rooms), '0')
    print("here")
    print(cpg)

    cpg = join_cpg_pair(cpg)
    print("there")
    print(cpg)


    for t in range(len(Slot.slots)):
        slots.append((bin(t)[2:]).rjust(bits_needed(Slot.slots), '0'))

    max_score = (len(cpg) - 1) * 3 + len(cpg) * 3


def course_bits(chromosome):
    i = 0

    return chromosome[i:i + bits_needed(CourseClass.classes)]


def professor_bits(chromosome):
    i = bits_needed(CourseClass.classes)

    return chromosome[i: i + bits_needed(Professor.professors)]


def group_bits(chromosome):
    i = bits_needed(CourseClass.classes) + bits_needed(Professor.professors)

    return chromosome[i:i + bits_needed(Group.groups)]

def lt_bits(chromosome):
    i = bits_needed(CourseClass.classes) + bits_needed(Professor.professors) + \
        bits_needed(Group.groups)

    return chromosome[i:i + bits_needed(Room.rooms)]

def slot_bits(chromosome):
    i = bits_needed(CourseClass.classes) + bits_needed(Professor.professors) + \
        bits_needed(Group.groups) + bits_needed(Room.rooms)

    return chromosome[i:i + bits_needed(Slot.slots)]


def slot_clash(a, b):
    if slot_bits(a) == slot_bits(b):
        return 1
    return 0


# checks that a faculty member teaches only one course at a time.
def faculty_member_one_class(chromosome):
    scores = 0
    for i in range(len(chromosome) - 1):  # select one cpg pair
        clash = False
        for j in range(i + 1, len(chromosome)):  # check it with all other cpg pairs
            if slot_clash(chromosome[i], chromosome[j])\
                    and professor_bits(chromosome[i]) == professor_bits(chromosome[j]):
                clash = True
                # print("These prof. have clashes")
                # print_chromosome(chromosome[i])
                # print_chromosome(chromosome[j])
        if not clash:
            scores = scores + 1
    return scores

def room_member_one_class(chromosome):
    scores = 0
    for i in range(len(chromosome) - 1):
        clash = False
        for j in range(i + 1, len(chromosome)):
            if slot_clash(chromosome[i], chromosome[j])\
                and lt_bits(chromosome[i]) == lt_bits(chromosome[j]):
                clash = True
                break
        if not clash:
            scores = scores + 1
    return scores
# check that a group member takes only one class at a time.
def group_member_one_class(chromosomes):
    scores = 0

    for i in range(len(chromosomes) - 1):
        clash = False
        for j in range(i + 1, len(chromosomes)):
            if slot_clash(chromosomes[i], chromosomes[j]) and\
                    group_bits(chromosomes[i]) == group_bits(chromosomes[j]):
                # print("These classes have slot/lts clash")
                # print_chromosome(chromosomes[i])
                # print_chromosome(chromosomes[j])
                # print("____________")
                clash = True
                break
        if not clash:
            # print("These classes have no slot/lts clash")
            # print_chromosome(chromosomes[i])
            # print_chromosome(chromosomes[j])
            # print("____________")
            scores = scores + 1
    return scores



def evaluate(chromosomes):
    global max_score
    score = 0
    score = score + faculty_member_one_class(chromosomes)
    score = score + room_member_one_class(chromosomes)
    score = score + group_member_one_class(chromosomes)
    return score / max_score

def cost(solution):
    # solution would be an array inside an array
    # it is because we use it as it is in genetic algorithms
    # too. Because, GA require multiple solutions i.e population
    # to work.
    return 1 / float(evaluate(solution))

def init_population(n):
    global cpg, slots
    chromosomes = []
    for _n in range(n):
        chromosome = []
        for _c in cpg:
            chromosome.append(_c + random.choice(slots))
        chromosomes.append(chromosome)
    return chromosomes


# Modified Combination of Row_reselect, Column_reselect
def mutate(chromosome):
    # print("Before mutation: ", end="")
    # printChromosome(chromosome)

    rand_slot = random.choice(slots)

    a = random.randint(0, len(chromosome) - 1)
    
    chromosome[a] = course_bits(chromosome[a]) + professor_bits(chromosome[a]) +\
        group_bits(chromosome[a]) + lt_bits(chromosome[a]) + rand_slot

    # print("After mutation: ", end="")
    # printChromosome(chromosome)


def crossover(population):
    a = random.randint(0, len(population) - 1)
    b = random.randint(0, len(population) - 1)
    cut = random.randint(0, len(population[0]))  # assume all chromosome are of same len
    population.append(population[a][:cut] + population[b][cut:])
    

def selection(population, n):
    population.sort(key=evaluate, reverse=True)
    while len(population) > n:
        population.pop()


def print_chromosome(chromosome):
    print(CourseClass.classes[int(course_bits(chromosome), 2)], " | ",
          Professor.professors[int(professor_bits(chromosome), 2)], " | ",
          Group.groups[int(group_bits(chromosome), 2)], " | ",
          Room.rooms[int(lt_bits(chromosome), 2)], " | ",
          Slot.slots[int(slot_bits(chromosome), 2)])

# Simple Searching Neighborhood
# It randomly changes timeslot of a class/lab
def ssn(solution):
    rand_slot = random.choice(slots)

    
    a = random.randint(0, len(solution) - 1)
    
    new_solution = copy.deepcopy(solution)
    new_solution[a] = course_bits(solution[a]) + professor_bits(solution[a]) +\
        group_bits(solution[a]) + lt_bits(solution[a]) + rand_slot 
    return [new_solution]

# Swapping Neighborhoods
# It randomy selects two classes and swap their time slots
def swn(solution):
    a = random.randint(0, len(solution) - 1)
    b = random.randint(0, len(solution) - 1)
    new_solution = copy.deepcopy(solution)
    temp = slot_bits(solution[a])
    new_solution[a] = course_bits(solution[a]) + professor_bits(solution[a]) +\
        group_bits(solution[a]) + lt_bits(solution[a]) + slot_bits(solution[b])

    new_solution[b] = course_bits(solution[b]) + professor_bits(solution[b]) +\
        group_bits(solution[b]) + lt_bits(solution[b]) + temp 
    # print("Diff", solution)
    # print("Meiw", new_solution)
    return [new_solution]

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / temperature)

def simulated_annealing():
    alpha = 0.9
    T = 1.0
    T_min = 0.00001
    print ("here")
    convert_input_to_bin()
    population = init_population(1) # as simulated annealing is a single-state method
    old_cost = cost(population[0])
    # print("Cost of original random solution: ", old_cost)
    # print("Original population:")
    # print(population)

    for __n in range(500):
        new_solution = swn(population[0])
        new_solution = ssn(population[0])
        new_cost = cost(new_solution[0])
        ap = acceptance_probability(old_cost, new_cost, T)
        if ap > random.random():
            population = new_solution
            old_cost = new_cost
        T = T * alpha
    # print(population)
    # print("Cost of altered solution: ", cost(population[0]))
    print("\n------------- Simulated Annealing --------------\n")
    for lec in population[0]:
        print_chromosome(lec)
    print("Score: ", evaluate(population[0]))

def genetic_algorithm():
    generation = 0
    convert_input_to_bin()
    population = init_population(3)

    # print("Original population:")
    # print(population)
    print("\n------------- Genetic Algorithm --------------\n")
    while True:
        
        # if termination criteria are satisfied, stop.
        if evaluate(max(population, key=evaluate)) == 1 or generation == 500:
            print("Generations:", generation)
            print("Best Chromosome fitness value", evaluate(max(population, key=evaluate)))
            print("Best Chromosome: ", max(population, key=evaluate))
            for lec in max(population, key=evaluate):
                print_chromosome(lec)
            break
        
        # Otherwise continue
        else:
            for _c in range(len(population)):
                crossover(population)
                selection(population, 5)
                
                # selection(population[_c], len(cpg))
                mutate(population[_c])

        generation = generation + 1
        # print("Gen: ", generation)

    # print("Population", len(population))


def main():
    random.seed()
    genetic_algorithm()
    simulated_annealing()

main()