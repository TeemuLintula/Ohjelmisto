class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    floor = 1

    def floor_up(self):
        self.floor += 1
        if self.floor < self.bottom_floor:
            self.floor = self.bottom_floor

    def floor_down(self):
        self.floor -= 1
        if self.floor < self.bottom_floor:
            self.floor = self.bottom_floor

    def go_to_floor(self, newFloor):
        while newFloor < self.floor:
            self.floor_down()
        while newFloor > self.floor:
            self.floor_up()