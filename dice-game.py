import random

class Player:
    def __init__(self, id, coins):
        self.id = id
        self.coins = coins

player_A = Player("A", 4)
player_B = Player("B", 4)
pot = Player("pot", 2)

if __name__ == "__main__":
    counter = 0
    while True:
        if counter % 2 == 0:
            current_player = player_A
        else:
            current_player = player_B
        num = random.randint(1, 6)
        if num == 1:
            print(f"{current_player.id} rolled {num}, and does nothing")
        elif num == 2:
            current_player.coins += pot.coins
            pot.coins = 0
            print(f"{current_player.id} rolled {num} and took all the coins from the pot. {current_player.id} has {current_player.coins} coins")
        elif num == 3:
            current_player.coins += pot.coins//2
            pot.coins -= pot.coins//2
            print(f"{current_player.id} rolled {num} and took half of the coins from the pot. {current_player.id} has {current_player.coins} coins")
        else:
            if current_player.coins == 0:
                print(f"{current_player.id} rolled {num} but has 0 coins. The game ended on cycle {counter//2 + 1}")
                break
            current_player.coins -= 1
            pot.coins += 1
            print(f"{current_player.id} rolled {num} and put one coin in the pot. {current_player.id} has {current_player.coins} coins")
        counter = counter + 1