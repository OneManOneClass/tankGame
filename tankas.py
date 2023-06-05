class Tankas:
    def __init__(self, position=None, direction="Šiaurė", total_shots=0, score=0, fuel=150):
        if position is None:
            position = {'X': 0, 'Y': 0}
        self.position = position
        self.direction = direction
        self.total_shots = total_shots
        self.shots_info = {"Šiaurė": 0, "Pietūs": 0, "Rytai": 0, "Vakarai": 0}
        self.score = score
        self.fuel = fuel

    def move_up(self):
        self.direction = "Šiaurė"
        self.position["Y"] += 1
        self.fuel -= 10

    def move_down(self):
        self.direction = "Pietūs"
        self.position["Y"] -= 1
        self.fuel -= 10

    def move_left(self):
        self.direction = "Vakarai"
        self.position["X"] -= 1
        self.fuel -= 10

    def move_right(self):
        self.direction = "Rytai"
        self.position["X"] += 1
        self.fuel -= 10

    def shoot(self, enemy_pos):
        self.total_shots += 1
        self.shots_info[self.direction] += 1
        if self.hit(enemy_pos):
            self.fuel += 20
            self.score += 1
            return True
        else:
            self.fuel -= 10
            return False

    def hit(self, enemy_pos):
        match self.direction:
            case ("Šiaurė"):
                if enemy_pos['X'] == self.position['X'] and enemy_pos['Y'] > self.position['Y']:
                    return True
            case ("Pietūs"):
                if enemy_pos['X'] == self.position['X'] and enemy_pos['Y'] < self.position['Y']:
                    return True
            case ("Vakarai"):
                if enemy_pos['Y'] == self.position['Y'] and enemy_pos['X'] < self.position['X']:
                    return True
            case ("Rytai"):
                if enemy_pos['Y'] == self.position['Y'] and enemy_pos['X'] > self.position['X']:
                    return True

        return False

    def info(self):
        return f"Pozicija: {self.position}\nKryptis: {self.direction}\n" \
               f"Šūviai: {self.total_shots}\nŠūvių kryptys: {self.shots_info}\nSunaikinti taikiniai: {self.score}"

    def __repr__(self):
        return f"Pozicija: {self.position} Kryptis: {self.direction} Kuras: {self.fuel}"
