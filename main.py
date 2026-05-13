#Classes
class Player:
    id_generator = 1
    player_list = []
    def __init__(self):
        self.name = input("Ingrese nombre del jugador: ")

        self.player_id = Player.id_generator
        Player.id_generator += 1

        
        self.points = 0
        Player.player_list.append(self)

    def __str__(self):
        return f"Player: {self.name} | ID: {self.player_id} | Points: {self.points}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "player_id" : self.player_id,
            "points" : self.points
        }

jugador = Player()
jugador2 = Player()

for player in Player.player_list:
    print(player)