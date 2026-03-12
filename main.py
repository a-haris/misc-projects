import random

# Note: all coordinates in (row, col) format

WORLDSIZE = 5
CHARACTER_ICON = '@'

class world():

    def __init__(self, size):
        self.size = size
        self.objects = []
        self.map = []
        for i in range(size):
            self.map.append(['_']*size)

    def display(self):
        for row in range(self.size):
            for col in range(self.size):
                if col != self.size - 1:
                    print(self.map[row][col], end=' ')
                else:
                    print(self.map[row][col])

    def update(self):
        # reset map
        for row in range(self.size):
            for col in range(self.size):
                self.map[row][col] = '_'

        for object in self.objects:
            row = object.coords[0]
            col = object.coords[1]
            self.map[row][col] = object.icon


class entity():

    def __init__(self, icon, coords, objects):
        self.icon = icon
        self.coords = coords
        objects.append(self)


class player(entity):

    def __init__(self, icon, coords, objects):
        super().__init__(icon, coords, objects)

    def get_move(self):
        move = input("Enter WASD keys to move: ")
        if move.lower() == 'w':
            if self.coords[0] != 0:
                self.coords[0] -= 1
        elif move.lower() == 'a':
            if self.coords[1] != 0:
                self.coords[1] -= 1
        elif move.lower() == 's':
            if self.coords[0] != WORLDSIZE - 1:
                self.coords[0] += 1
        elif move.lower() == 'd':
            if self.coords[1] != WORLDSIZE - 1:
                self.coords[1] += 1
        else:
            print('Move not recognised.')
            return False

    
def main():
    world1 = world(WORLDSIZE)

    player1 = player(CHARACTER_ICON, [2,2], world1.objects)

    world1.update()
    world1.display()

    while True:
        player1.get_move()

        world1.update()
        world1.display()

main()