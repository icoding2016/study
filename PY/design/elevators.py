"""
Elevator System Design

The core 'single elevator' problem  can be extended in many different directions, making it an ideal problem to see how the candidate thinks. 
It’s easy to make it an object-oriented design problem. 
It can be used to discuss different data structures that will help in the implementation. 
If needed, it can be made even more complicated by adding multiple elevators serving the building, where a request button summons the most appropriate elevator. 

Requirements:
It's important to understand the requirement.
- The use case,  
- The key concern (e.g. wait-time, overall wait-time, total transfer time, etc.)
- dimensions: num of zones/floors/elevators/passangers, max load/num-of-passangers, moving speed
           e.g 4 zones, (50 floors and 20 elevators/zone,)
- special functions,  e.g. Alarm/break/emergency..

Object/Use Case:
  Users:  Elevator, Passager, ElevatorController, 

                                  Floors <>----------------
                    _ _ _ _ _ _ _ _^  ^                    |
                   |                  |                    |
          ElevatorController ----> Elevator(s) <----> Passangers
                  ^                                        |
                  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |


Elevator behavior (FSM): 
  Each elevator action individually based on its own self._dests[], 
    There are 2 source of dest requesting: 1) passangers (passanger.dest), 2) controller (summon)
    - Passanger: request 'dest' to the elevator when onboarding.
    - ElevatorController: adding 'dest' to a choson elevator's _dests[] on Summon.

  Status/Action: Move-up / Move-down / Park (door-closed) / Loading (door-open)

    LOADING <---> PARK <----> GOING_UP
                    ^
                    |
                    --------> GOING_DOWN

    Action map:
    Status      on-floor-i
    ----------------------------------------
    PARK        dest[] empty ? Y -> stay Park()
                i in dest[]  ? Y -> Loading() (dest.remove(i) after loading)
                               N -> (scheduling) -> GoUp()/GoDown() / Park
    GOING_UP    dest[] empty? Y -> Park()
                i in dest[] ? Y -> Park() (-> loading())
                              N -> oneLevelUp
    GOING_DOWN  dest[] empty? Y -> Park()
                i in dest[] ? Y -> Park() (-> loading())
                              N -> oneLevelDown
    LOADING     level passanagers
                cur_direction match dest?  Onboard(passanager) & dest.remove(i) -> Park() 


Algorithms:
  1) Elevator Algorithm
     Full trip on single direction
  2) Controller Algorithm
     FCFS (First Come First Serve)
     SSTF (Shortest Seek Time First)
     <etc>

---------------------------

OOP design examle

Elevator:
  attrs:
    capacity: max_person
    floors:   [-2,... 100]




---------------------------
[Example question 1]:
    An elevator is a combination of at least two elevators. 
    The goal is to minimize the waiting time of the user. 
    Make sure you how your design will evolve if a lift is installed on high rise buildings over 20 floors.
    How many lifts you need to server 40 floors with waiting time no less than 30 seconds on average. 
    Think about the parking strategy of your lift, 
    i.e., which floor they should be resting or should they keep going up or down, etc.


"""


from dataclasses import dataclass
from collections import deque
from enum import Enum
from threading import RLock
import random
import time
import threading
import typing as t


_DEBUG = True

def Trace(msg):
    if _DEBUG:
        print(msg)


class NotInitializedError(Exception):
    pass

class InvalidOperation(Exception):
    pass


class Floor():
    def __init__(self, id) -> None:
        self._id = id
        self.passangers = list()
        self._elevator_indicator = {'UP':False, 'DOWN':False}

    def addPassanger(self, passanger:'Passanger'):
        if passanger not in self.passangers:
            self.passangers.append(passanger)
        if passanger.dest > self._id:
            self.updateIndecators(up=True, down=self._elevator_indicator['DOWN'])
        elif passanger.dest < self._id:
            self.updateIndecators(up=self._elevator_indicator['UP'], down=True)

    def delPassanger(self, passanger:'Passanger'):
        if passanger in self.passangers:
            self.passangers.remove(passanger)
        self.updateIndecators()

    def getPassangers(self) -> list['Passanger']:
        return self.passangers

    def setPassangers(self, passangers:list['Passanger']) -> None:
        self.passangers = passangers
        self.updateIndecators()

    def updateIndecators(self, up:bool=None, down:bool=None):
        u = d = False
        if up != None:
            self._elevator_indicator['UP'] = up
            u = True
        if down != None:
            self._elevator_indicator['DOWN'] = down
            d = True
        if u and d:
            return
        for p in self.passangers:
            if not u and p.dest > self._id:
                self._elevator_indicator['UP'] = True
                u = True
            if not d and p.dest < self._id:
                self._elevator_indicator['DOWN'] = True
                d = True
            if u and d:
                return


class Floors():
    def __init__(self, floors:list[int]) -> None:
        self.floors = {i:Floor(id=i) for i in floors}

    def addPassanger(self, floor:int, passanger:'Passanger'):
        if passanger not in self.floors[floor].passangers:
            self.floors[floor].addPassanger(passanger)

    def getPassangers(self, floor:int) -> list['Passanger']:
        try:
            return self.floors[floor].getPassangers()
        except KeyError:
            raise

    def setPassangers(self, floor:int, passangers:list['Passanger']) -> None:
        try:
            return self.floors[floor].setPassangers(passangers)
        except KeyError:
            raise

    def __getitem__(self, id:int) -> Floor:
        return self.floors[id]

    def __setitem__(self, id:int, floor:Floor) -> None:
        self.floors[id] = floor

    def __len__(self):
        return len(self.floors)

    def ids(self) -> list[int]:
        return self.floors.keys()

@dataclass
class Environment():
    floors: Floors
    elevators:  dict[int, 'Elevator']
    elevator_controller: 'ElevatorController' = None


class Passanger():
    _sn = 0

    def __init__(self, env:Environment, start:int = None, dest:int = None) -> None:
        self._env = env
        self._id = self.__class__._sn + 1
        self.__class__._sn += 1
        self.start = start if start else random.choice([k for k in env.floors.ids()])  # .randint(min(env.floors), max(env.floors))
        self.dest = dest if dest else random.choice([f for f in env.floors.ids() if f!=start])

    def direction(self) -> 'Direction':
        return Direction.UP if self.dest > self.start else Direction.DOWN

    def go(self):
        Trace(f"Passanger {self._id} summon from floor {self.start}, {self.direction()} (->{self.dest})")
        self._env.elevator_controller.summon(floor=self.start, passanger=self)

    def id(self) -> int:
        return self._id

    def __str__(self) -> str:
        return f"Passanger-{self.id()} ({self.start}->{self.dest})"


def PassangerGenerator(env:Environment, speed:float=1.0) -> None:
    """Generate passangers.
    Args:
        speed: how many passangers per 10 second
    """
    while True:
        time.sleep(random.randint(7,13)/speed)
        yield Passanger(env)


class Direction(Enum):
    UP = 1
    DOWN = 2


class ElevatorStatus(Enum):
    PARK = 0
    GOING_UP = 1
    GOING_DOWN = 2
    LOADING = 3


@dataclass
class Action():
    act: ElevatorStatus
    data: list[t.Any] = None


class Elevator(threading.Thread):
    _CAPACITY = 12
    _LOADING_TIME = 1    # the time for loading/unloading 1 passanger
    _SPEED = 2           # levels per second

    def __init__(self, id:str, floors:Floors, capacity:int=None, speed:int=None, loading_time:int=None) -> None:
        super().__init__(name=f"Elevator-{id}")
        # attributes
        self._controller = None
        self.id = id
        self._capacity = capacity if capacity else self._CAPACITY
        self._speed = speed if speed else self._SPEED
        self._loading_time = loading_time if loading_time else self._LOADING_TIME
        self._floors = floors
        # dynamic 
        self._door_open = False
        self._cur_floor = 0
        self._cur_direction: Direction = None
        self._passangers = []    # 
        self._dests = deque()    # [dest, ]
        self._onSummon = []
        # self._status = ElevatorStatus.PARK
        self._actions = deque([Action(act=ElevatorStatus.PARK, data=[self._cur_floor])])    # [<actions>] .e.g [move]
        # 
        self._action_tbl = {
            ElevatorStatus.PARK: self.park,       # -> (scheduling) -> going_up/going_down
            ElevatorStatus.GOING_UP: self.up,     # -> onArrive -> (park) -> loading
            ElevatorStatus.GOING_DOWN: self.down, # -> onArrive -> (park) -> loading
            ElevatorStatus.LOADING: self.load,    # -> park
        }
        self._on_duty = True
        self._lock = RLock()

    def linkController(self, controller:'ElevatorController'):
        if not controller:
            raise ValueError()
        self._controller = controller

    def addDest(self, dest:int) -> None:
        """Adding a new task (dest) to this elevator.
           The task could be assigned either by the elevatorController or the loaded passangers.
        """
        with self._lock:
            if dest not in self._dests:
                self._dests.append(dest)
                Trace(f"{self.name} [floor {self._cur_floor}]: assigned new dest (floor {dest})")

    def delDest(self, dest:int) -> None:
        """Remove a task (dest) from the elevator.
           The typical use case is, the elevator arrived at a floor, 
           then unloads some passangers and finishes this task (dest) in its tasks list."""
        with self._lock:
            if dest in self._dests:
                self._dests.remove(dest)
                Trace(f"{self.name}[floor {self._cur_floor}]: finished dest (floor {dest})")
            if dest in self._onSummon:
                self._onSummon.remove(dest)

    def cancelDest(self, dest:int) -> None:
        """The elevatorController cancel a task (dest) for this elevator.
           That's a special case, e.g. emergency. The passangers cannot add the dest back anymore
        """
        with self._lock:
            if dest in self._dests:
                self._dests.remove(dest)
                # what about the passangers to that dest?
            if dest in self._onSummon:
                self._onSummon.remove(dest)

    def onSummon(self, floor:int) -> None:
        with self._lock:
            if floor not in self._onSummon:
                self._onSummon.append(floor)
            if floor not in self._dests:
                self.addDest(floor)

    def cancelSummon(self, floor:int) -> None:
        """Cancel the summon to the given floor.
           The func is called by ElevatorController.
           Note: need to check if there are passangers destinating to that floor before deleting it from the _dest
        """
        with self._lock:
            if floor in self._onSummon:
                self._onSummon.remove(floor)
            if floor not in self._dests:
                for p in self._passangers:
                    if p.dest == floor:
                        return
                if floor in self._dests:
                    self._dests.remove(floor)


    def loadPassangers(self, passangers:list[Passanger], direction:Direction=None) -> tuple[bool, list[Passanger]]:
        """Load passangers into the elevator.
        Args:
            passangers: the incomming passangers
        Return:
            tuple(<success>, <The accepted passangers (per the capacity)>)
        """
        to_load = passangers
        cut = False
        if direction:
            to_load = [p for p in passangers if p.direction() == direction]
        accepted = []
        with self._lock:
            for p in to_load:
                if self.isFull():
                    cut = True
                    break
                self._passangers.append(p)
                self.addDest(p.dest)
                accepted.append(p)
        Trace(f"{self.name}[floor {self._cur_floor}]: Load passangers ({'partially' if cut else 'fully'}): {[p.id() for p in accepted]}")
        self._operationDelay(self._loading_time * len(accepted))
        return (not cut, accepted)

    def unloadPassangers(self) -> list[Passanger]:
        """unload passangers at the current floor.
        Return:
            The unloadd passangers (arrived)
        """
        unloaded = []
        with self._lock:
            for p in self._passangers:
                if p.dest == self._cur_floor:
                    self._passangers.remove(p)
                    unloaded.append(p)
        Trace(f"{self.name} [floor {self._cur_floor}]: Unloading passangers: {[p.id() for p in unloaded]}")
        self._operationDelay(self._loading_time*len(unloaded))
        self._controller.log(f"{self.name} transported passangers: {[str(p) for p in unloaded]}")
        return unloaded

    def isFull(self) -> bool:
        return len(self._passangers) >= self._capacity

    def idle(self) -> bool:
        return not self._dests

    def run(self):
        while self._on_duty or self._dests:   # finish all task before stopping.
            if not self._controller:
                time.sleep(1)
                continue
            act = self._getNextAction()
            if act:
                act_call = self._action_tbl[act.act]
                if act.data:
                    act_call(*act.data)
                else:
                    act_call()
        Trace(f"{self.name}: stopping.")

    def stop(self):
        self._on_duty = False

    def _peekNextAction(self, action, override=False):
        with self._lock:
            if self._actions:
                return self._actions[0]
            else:
                return None

    def _getNextAction(self) -> Action:
        with self._lock:
            act = None
            try:
                act = self._actions.popleft()
            except KeyError:
                pass
        return act
            
    def _setNextAction(self, action:Action, override=True):
        with self._lock:
            if override:
                self._actions = deque([action])
            else:
                self._actions.append(action)

    def _nextDest(self) -> int:
        """Calculate next dest

           If currently is runnig UP/DOWN, then next dest is the furthest of current direction in self._dests.
               if already the furthest, then reset current direction to None --> will decide the dest in next round
           if the is no current direction, the pick a dest from self._dests
           if empty self._dests, then next dest is None
        """
        dst = None
        with self._lock:
            if not self._dests:
                self._cur_direction = None
                return None
            self._dests = sorted(self._dests)
            if self._cur_direction == Direction.UP:
                if self._dests[-1] > self._cur_floor:
                    dst = self._dests[-1]
                else:
                    # self._cur_direction = Direction.DOWN
                    # dst = self._dests[0]
                    self._cur_direction = None
                    dst = None
            elif self._cur_direction == Direction.DOWN:
                if self._dests[0] < self._cur_floor:
                    dst = self._dests[0]
                else:
                    # self._cur_direction = Direction.UP
                    # dst = self._dests[-1]
                    self._cur_direction = None
                    dst = None
            else:  # self._cur_direction == None
                if self._cur_floor == max([f for f in self._floors.ids()]):
                    self._cur_direction = Direction.DOWN
                    dst = self._dests[0]
                elif self._cur_floor == min([f for f in self._floors.ids()]):
                    self._cur_direction = Direction.UP
                    dst = self._dests[-1]
                else:
                    dst = self._dests[0]    # pick the lowest floor (car-park) by default
                    self._cur_direction = Direction.UP if dst > self._cur_floor else Direction.DOWN
        return dst

    def park(self, floor:int):
        """FSM handler: The elevator parks on current floor (door close).
        """
        with self._lock:
            if self._cur_floor in self._dests:
                self._setNextAction(Action(act=ElevatorStatus.LOADING, data=[self._cur_floor]))
                return
            dst = self._nextDest()
            direction = None
            if dst and dst != self._cur_floor:
                direction = Direction.UP if dst > self._cur_floor else Direction.DOWN
            if not dst:
                # Trace(f"{self.name} [floor {self._cur_floor}]: Parking...")
                self._cur_direction = None
                if self._floors.getPassangers(floor):
                    self._setNextAction(Action(act=ElevatorStatus.LOADING, data=[self._cur_floor]))
                else:
                    self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))
                    self._operationDelay(delay=1)
                return
            if self._cur_floor == dst:
                if self.isFull():
                    self.delDest(self._cur_floor)
                    self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))
                else:
                    self._setNextAction(Action(act=ElevatorStatus.LOADING, data=[self._cur_floor]))
            elif dst > self._cur_floor:
                self._setNextAction(Action(act=ElevatorStatus.GOING_UP, data=[dst]))
            elif dst < self._cur_floor:
                self._setNextAction(Action(act=ElevatorStatus.GOING_DOWN, data=[dst]))
        
    def load(self, floor:int):
        """FSM handler: The elevator loading/unloading on current floor (door open).
        """
        with self._lock:
            # unloading
            Trace(f"{self.name} [floor {self._cur_floor}]: Door opens ...")
            self.unloadPassangers()
            # loading
            passangers = self._floors[self._cur_floor].getPassangers()
            loaded = []
            alldone = False
            if self._cur_direction == None:
                alldone, loaded = self.loadPassangers(passangers)
            else:
                alldone, loaded = self.loadPassangers([p for p in passangers if p.direction() == self._cur_direction])
            # elif self._cur_direction == Direction.UP:
            #     ok, loaded = self.loadPassangers([p for p in passangers if p.dest > self._cur_floor])
            # elif self._cur_direction == Direction.DOWN:
            #     ok, loaded = self.loadPassangers([p for p in passangers if p.dest < self._cur_floor])
            Trace(f"{self.name} [floor {self._cur_floor}]: Door close.")
            self._floors[self._cur_floor].setPassangers([p for p in passangers if p not in loaded])
            if alldone:
                self._controller.summonDone(self._cur_floor, self._cur_direction)
                self.delDest(self._cur_floor)
            self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))

    def up(self, dst:int):
        """FSM handler: The elevator going up from current floor (door close).
        """
        with self._lock:
            if self._cur_floor == max(self._floors.ids()):
                Trace(f"{self.name}[floor {self._cur_floor}]: Reach top floor...")
                self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))
                self._operationDelay(delay=1)
                return
            Trace(f"{self.name} [floor {self._cur_floor}]: Going up to {self._cur_floor+1}, dst={dst}...")
            self._cur_floor += 1
            self._operationDelay(1/self._speed)

            if self._cur_floor in self._dests:
                self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))
            else:
                if dst > self._cur_floor:
                    self._setNextAction(Action(act=ElevatorStatus.GOING_UP, data=[dst]))
                else:
                    self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))

    def down(self, dst:int):
        """FSM handler: The elevator going down from current floor (door close).
        """
        with self._lock:
            if self._cur_floor == min(self._floors.ids()):
                Trace(f"{self.name}[floor {self._cur_floor}]: Reach bottom floor...")
                self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))
                self._operationDelay(delay=1)
                return
            Trace(f"{self.name} [floor {self._cur_floor}]: Going down to {self._cur_floor-1}, dst={dst}...")
            self._cur_floor -= 1
            self._operationDelay(1/self._speed)

            if self._cur_floor in self._dests:
                self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))
            else:
                if dst < self._cur_floor:
                    self._setNextAction(Action(act=ElevatorStatus.GOING_DOWN, data=[dst]))
                else:
                    self._setNextAction(Action(act=ElevatorStatus.PARK, data=[self._cur_floor]))

    def _operationDelay(self, delay:float):
        time.sleep(delay)


class ElevatorController(threading.Thread):
    _DEFAULT_ALGO = "FCFS"

    def __init__(self, floors:Floors, elevators:dict[int, Elevator], algo=None) -> None:
        super().__init__()
        if not floors:
            raise ValueError()
        self._floors: Floors = floors
        self._elevators: dict[str, Elevator] = elevators    # {id:elevator, }
        self._summons: dict = {f:{Direction.UP:None, Direction.DOWN:None} for f in floors.ids()}
        self._algo = algo if algo else self._DEFAULT_ALGO
        self._lock = RLock()
        self._active = True
        self._log = []
        self.connectElevators()
        
    def connectElevators(self):
        Trace(f"Controller: connect elevators...")
        for _, e in self._elevators.items():
            e.linkController(self)

    def chooseElevator(self, floor:int, direction:Direction) -> str:
        """Choose an elevator to summon from a floor.
           The choice is based on:
             - direction -- the elevator with the running direction towards this floor has higher priority
             - distance  -- the closer to the floor, the higher priority.
           The logic: (priority high to low)
             - elevator in current floor and in same direction.
             - elevator in same direction and is coming towards current floor.
             - elevator x is free (idle)
             - elevator in different direction, (more likely to turn back and arrive earlier)
             - elevator in same direction,  (already missed this floor)
        """
        candidates = candidates1 = candidates2 = candidates3= []
        chosen_id = None
        for id, e in self._elevators.items():
            if floor == e._cur_floor and e._cur_direction == direction and (e._actions and e._actions[0].act==ElevatorStatus.PARK):
                return id
            if floor <= e._cur_floor and e._cur_direction == Direction.DOWN and direction == Direction.DOWN:
                candidates1.append(id)
            elif floor >= e._cur_floor and e._cur_direction == Direction.UP and direction == Direction.UP:
                candidates1.append(id)
            elif e.idle():
                candidates2.append(id)
            elif direction != e._cur_direction:
                candidates3.append(id)
        if candidates1:
            candidates = candidates1
        elif candidates2:
            candidates = candidates2
        elif candidates3:
            candidates = candidates3
        else:
            candidates = [id for id in self._elevators.keys()]
        chosen_id = min(candidates, key=lambda id: abs(self._elevators[id]._cur_floor - floor))
        return chosen_id

    def summon(self, floor:int, passanger:Passanger):
        if floor not in self._floors.ids():
            raise ValueError(f'invalid floor {floor}')
        direction = passanger.direction()
        eid = self.chooseElevator(floor, direction)
        with self._lock:
            self._floors[floor].addPassanger(passanger)
            # Signal the chosen elevator to take the task, cancel the summon to the obsoleted candicate elevator if the candidate changes 
            if self._summons[floor][direction] and self._summons[floor][direction] != eid:
                elevator = self._elevators[self._summons[floor][direction]]
                elevator.cancelSummon(floor)
                Trace(f"Controller: unsummon elevator {elevator.id}")
            self._summons[floor][direction] = eid
            self._elevators[eid].onSummon(floor)
        Trace(f"Controller: summon elevator {eid}")

    def summonDone(self, floor:int, direction:Direction):
        """The elevator notify the controller the summon is fullfilled."""
        if floor not in self._floors.ids():
            raise ValueError(f'invalid floor {floor}')
        directions = [direction] if direction else [Direction.UP, Direction.DOWN]
        with self._lock:
            for dir in directions:
                eid = self._summons[floor][dir]
                if eid:
                    self._summons[floor][dir] = None
                    # self._elevators[eid].cancelSummon(floor)

    def log(self, info:str):
        self._log.append(info)

    def readLog(self) -> list[str]:
        return self._log

    def run(self):
        print('Elevator controller starts running...')
        while self._active:
            # self.algo.schedule(current job/passager info)
            time.sleep(1)
            pass
        print('Elevator controller shutting down...')

    def stop(self):
        self._active = False


# environment: Environment = None
# def setEnv(env:Environment):
#     environment = env

# def getEnv() -> Environment:
#     global environment
#     return environment

class ElevateSimu(threading.Thread):
    def __init__(self, floor_count:int, elevator_num:int):
        super().__init__()
        floor_ids = [i for i in range(-4, floor_count-4)]
        floors = Floors(floor_ids)
        elevators = {i:Elevator(str(i), floors) for i in range(elevator_num)}
        elevator_controller = ElevatorController(floors=floors, elevators=elevators)
        env = Environment(floors=floors, elevator_controller=elevator_controller, elevators=elevators)
        self.env = env
        # setEnv(env)
        Trace(f"ElevateSimu: start controller")
        elevator_controller.start()
        Trace(f"ElevateSimu: start elevators")
        for _, e in elevators.items():
            e.start()
        self._stop = False
        
    def run(self):
        print("ElevateSimu starts..")
        allpassangers = []
        for p in PassangerGenerator(self.env, speed=1):
            p.go()
            allpassangers.append(str(p))
            if self._stop:
                Trace(f"All passangers: {allpassangers}")
                break

    def stop(self):
        self._stop = True
        for e in self.env.elevators.values():
            e.stop()
        Trace(f"Transported passangers: \n{self.env.elevator_controller.readLog()}")
        self.env.elevator_controller.stop()


def test():
    simu = ElevateSimu(50, 4)
    simu.start()
    time.sleep(120)
    simu.stop()


test()
