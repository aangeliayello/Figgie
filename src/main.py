import numpy as np
import itertools
from enum import Enum
import sys
sys.path.append("E:/Documents/_FunAndProfit/Figgie/src/")
import utils


class Suit(Enum):
    SPADES   = 0
    CLUBS    = 1
    DIAMONDS = 2
    HEARTS   = 3
    

DISTRIBUTION = [12, 10, 10, 8]

distribution_permutations = itertools.permutations(DISTRIBUTION)

possible_distributions = [tuple(perm) for perm in itertools.permutations(DISTRIBUTION)]


def calc_probabilities(hand):
    total_count = 0
    dist_count = {dist:0 for dist in possible_distributions}

    for dist in possible_distributions:
        temp_count_arr = utils.PRIME_FACTORIZATION[1]
        
        if np.all([hand[i] <= dist[i] for i in range(len(dist))]):
            for i in range(len(dist)):
                temp_count_arr = utils.multiply(utils.chooseI(dist[i], hand[i]), temp_count_arr)
            
            temp_count_int = utils.int_(temp_count_arr)
        else: 
            temp_count_int = 0
            
        dist_count[dist] += temp_count_int
        total_count += temp_count_int

    # Calculate the probabilities
    probabilities = {
        "SPADES"   : {"total": 0, "ten": 0, "eight": 0},
        "CLUBS"    : {"total": 0, "ten": 0, "eight": 0},
        "DIAMONDS" : {"total": 0, "ten": 0, "eight": 0},
        "HEARTS"   : {"total": 0, "ten": 0, "eight": 0},
    }



    for dist, count in dist_count.items():
        twelve_suit = np.argmax(dist)
        gold_suit = ((twelve_suit+1) % 2) + 2*(twelve_suit // 2)
        probabilities[Suit(gold_suit).name]['total'] += count/total_count
        if dist[gold_suit] == 8:
            probabilities[Suit(gold_suit).name]['eight'] += count/total_count
        else:
            probabilities[Suit(gold_suit).name]['ten'] += count/total_count

    import json
    json_string = json.dumps(probabilities, indent=4)  # indent for pretty printing
    print(json_string)
    
    for key, val in probabilities.items():
        print(key, val["total"])