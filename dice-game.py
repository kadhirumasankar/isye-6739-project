import csv
import math
import random
import statistics
import subprocess
import time

import matplotlib.pyplot as plt
from bashplotlib.histogram import plot_hist


class Player:
    def __init__(self, id, coins):
        self.id = id
        self.coins = coins


def print_scores():
    print("-------------")
    print("| A |Pot| B |")
    print("-------------")
    print(f"| {player_A.coins} | {pot.coins} | {player_B.coins} |")
    print("-------------")


def print_ascii_hist():
    if len(cycle_list) > 0:
        plot_hist(
            cycle_list, pch=".", bincount=math.ceil((max(cycle_list) - min(cycle_list)))
        )
        # print(f"µ = {mu_list[-1]}")


if __name__ == "__main__":
    cycle_list = []
    mu_list = []
    num_trials = 100000
    for i in range(num_trials):
        player_A = Player("A", 4)
        player_B = Player("B", 4)
        pot = Player("pot", 2)
        counter = 0
        while True:
            if counter % 2 == 0:
                current_player = player_A
            else:
                current_player = player_B
            num = random.randint(1, 6)
            if num == 1:
                # print(f"{current_player.id} rolled {num}, and does nothing")
                pass
            elif num == 2:
                current_player.coins += pot.coins
                pot.coins = 0
                # print(f"{current_player.id} rolled {num} and took all the coins from the pot. {current_player.id} has {current_player.coins} coins")
            elif num == 3:
                current_player.coins += pot.coins // 2
                pot.coins -= pot.coins // 2
                # print(f"{current_player.id} rolled {num} and took half of the coins from the pot. {current_player.id} has {current_player.coins} coins")
            else:
                if current_player.coins == 0:
                    # print(f"{current_player.id} rolled {num} but has 0 coins. The game ended on cycle {counter//2 + 1}")
                    cycle_list.append(counter // 2 + 1)
                    break
                current_player.coins -= 1
                pot.coins += 1
                # print(f"{current_player.id} rolled {num} and put one coin in the pot. {current_player.id} has {current_player.coins} coins")
            counter = counter + 1
        if (i + 1) % 2000 == 0:
            subprocess.run(["clear", "-x"])
            print_ascii_hist()
            print(
                f"{i+1} of {num_trials} runs complete ({math.ceil(i/num_trials * 100)}%)"
            )

    file = open("cycle_list.csv", "w+", newline="")
    with file:
        write = csv.writer(file)
        write.writerow([str(r) for r in cycle_list])

    plt.hist(cycle_list, bins=math.ceil((max(cycle_list) - min(cycle_list))))
    plt.xlabel("Cycles")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Cycles (µ = {statistics.mean(cycle_list)})")
    plt.grid(True, axis="y", alpha=0.5)
    plt.show()
