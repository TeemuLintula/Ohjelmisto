class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    current_floor = 1

    def floor_up(self):
        self.current_floor += 1
        if self.current_floor < self.bottom_floor:
            self.current_floor = self.bottom_floor

    def floor_down(self):
        self.current_floor -= 1
        if self.current_floor < self.bottom_floor:
            self.current_floor = self.bottom_floor

    def go_to_floor(self, newFloor):
        while newFloor < self.current_floor:
            self.floor_down()
        while newFloor > self.current_floor:
            self.floor_up()

class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [
            Elevator(bottom_floor, top_floor)
            for elevator in range(elevators)
        ]

    def run_elevator(self, elevator, target_floor):
        self.elevators[elevator].go_to_floor(target_floor)

building = Building(1, 10, 3)
building.run_elevator(1, 9)
print(building.elevators[0].current_floor)
print(building.elevators[1].current_floor)
print(building.elevators[2].current_floor)