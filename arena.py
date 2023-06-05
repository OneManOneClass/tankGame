class Arena:
    def __init__(self, width, height, player_pos, enemy_pos):
        self.width = width
        self.height = height
        self.player_pos = player_pos
        self.enemy_pos = enemy_pos

    def draw(self):
        for y in range(int(self.height / 2), (int(self.height / 2) * -1) - 1, -1):
            for x in range(int(self.width / 2) * -1, int(self.height / 2) + 1):
                if self.player_pos['X'] == x and self.player_pos['Y'] == y:
                    print(" X ", end="")
                elif self.enemy_pos['X'] == x and self.enemy_pos['Y'] == y:
                    print(" O ", end="")
                else:
                    print(" - ", end="")
            print()

        print()
