from enum import Enum
from copy import deepcopy

class MapSite():
    def Enter(self):
        raise NotImplementedError('Abstract Base Class method')
    
class Direction(Enum):
    North = 0
    East  = 1
    South = 2
    West  = 3

#===================================================================
# Prototype definition of Door
#===================================================================
class Door(MapSite):
    def __init__(self, other=None):
        self._isOpen = False
        if other:                       # copy constructor
            self._room1 = other._room1      
            self._room2 = other._room2
        else:
            self._room1 = None          # private members
            self._room2 = None

    def Initialize(self, r1, r2):
        self._room1 = r1                # initialize private members
        self._room2 = r2
    
    def Clone(self):
        return Door(self)
    
    def OtherSideFrom(self, Room):
        print('\tDoor obj: This door is a side of Room: {}'.format(Room._roomNumber))
        if 1 == Room._roomNumber: 
            other_room = self._room2
        else: 
            other_room = self._room1        
        return other_room
        
    def Enter(self):
        if self._isOpen: print('    **** You have passed through this door...')
        else: print('    ** This door needs to be opened before you can pass through it...')
   
#===================================================================
# Prototype definition of Room
#===================================================================    
class Room(MapSite):
    def __init__(self, roomNo=0):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)
                
    def GetSide(self, Direction):
        return self._sides[Direction]
    
    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite
        
    def Enter(self):
        print('    You have entered room: ' + str(self._roomNumber))
            
    def Clone(self):
        return deepcopy(self)  
    
    def Initialize(self, roomNo):  
        self._roomNumber = int(roomNo)
                 
#===================================================================
# Prototype definition of Wall
#===================================================================    
class Wall(MapSite):
    def Enter(self):
        print('    * You just ran into a Wall...')   

    def Clone(self):
        return deepcopy(self)         
              
class Maze():
    def __init__(self):
        # dictionary to hold room_number, room_obj <key, value> pairs
        self._rooms = {}
    
    def AddRoom(self, room):
        # use roomNumber as lookup value to retrieve room object
        self._rooms[room._roomNumber] = room    
    
    def RoomNo(self, room_number):
        return self._rooms[room_number]    
    
class MazeFactory():   
    @classmethod            # decorator
    def MakeMaze(cls):      # cls, not self
        return Maze()       # return Maze instance 
    
    @classmethod            # decorator
    def MakeWall(cls):
        return Wall()
    
    @classmethod            # decorator
    def MakeRoom(cls, n):   # n = roomNumber
        return Room(n)
        
    @classmethod                # decorator
    def MakeDoor(cls, r1, r2):  # r1, r2 = two rooms
        return Door(r1, r2)     # door between rooms   
  
#===================================================================
# Prototype definition of BombedWall
#=================================================================== 
class BombedWall(Wall):
    def __init__(self, other=None):
        self.wall_is_damaged = False    # True if bomb exploded
        self._bomb = None
        
        if other:                       # copy constructor
            self._bomb = other._bomb
            
    def Clone(self):
        return deepcopy(self)  
    
class RoomWithABomb(Room):
    def __init__(self, roomNo=0):
        super(RoomWithABomb, self).__init__(roomNo)
        self.has_bomb = True
        self.bomb_exploded = False        

class MazeGame():   
    # Abstract Factory Pattern - did not change
    def CreateMaze(self, factory=MazeFactory):  # pass in a concrete Factory
        aMaze = factory.MakeMaze()
        r1 = factory.MakeRoom(1)
        r2 = factory.MakeRoom(2)
        aDoor = factory.MakeDoor(r1, r2)
        
        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)
        
        r1.SetSide(Direction.North.value, factory.MakeWall())
        r1.SetSide(Direction.East.value, aDoor)
        r1.SetSide(Direction.South.value, factory.MakeWall())
        r1.SetSide(Direction.West.value, factory.MakeWall())
        
        r2.SetSide(Direction(0).value, factory.MakeWall())
        r2.SetSide(Direction(1).value, factory.MakeWall())
        r2.SetSide(Direction(2).value, factory.MakeWall())
        r2.SetSide(Direction(3).value, aDoor)
        
        return aMaze

#==================================================================
# *** Here starts the Prototype Pattern
#==================================================================
class MazePrototypeFactory(MazeFactory):     # subclass MazeFactory
    # C++ ctor: MazePrototypeFactory(Maze*, Wall*, Room*, Door*)    
    # in Python we use __init__:
    def __init__(self, m, w, r, d):
        # initialize prototypes // C++ 'private members' 
        # these variables hold class instances of Mazes, Walls etc.
        self._prototypeMaze = m
        self._prototypeWall = w
        self._prototypeRoom = r
        self._prototypeDoor = d
        
        self.prototype_manager_registry = {}   # store of created objects
    
    def register_prototype(self, key, prototype):
        self.prototype_manager_registry[key] = prototype    # add to store
        
    def unregister_prototype(self, key):
        del self.prototype_manager_registry[key]            # delete from store
   
    def MakeWall(self):
        return self._prototypeWall.Clone()  # call Clone() method on prototype
    
    def MakeDoor(self, r1, r2):
        door = self._prototypeDoor.Clone()  # call Clone() method on Door
        door.Initialize(r1, r2)             # initialize rooms between door
        return door
        
    def MakeRoom(self, n):
        room = self._prototypeRoom.Clone()  # call Clone() method on Room
        room.Initialize(n)                  # initialize room number
        return room      
    
#==================================================================
# Self-testing section    
#==================================================================
if __name__ == '__main__':
    # common code moved into function
    def find_maze_rooms(maze_obj):      # pass object into function
        print()
        # find its rooms
        maze_rooms = []
        for room_number in range(5):
            try: 
                # get the room number
                room = maze_obj.RoomNo(room_number)
                print('\n^^^ Maze has room: {}'.format(room_number, room))
                print('    Entering the room...')
                room.Enter()
                # append rooms to list
                maze_rooms.append(room)
                for idx in range(4):
                    side = room.GetSide(idx) 
                    side_str = str(side.__class__).replace("<class '__main__.", "").replace("'>", "")  
                    print('    Room: {}, {:<15s}, Type: {}'.format(room_number, Direction(idx), side_str))
                    print('    Trying to enter: ', Direction(idx))
                    side.Enter()
                    if 'Door' in side_str:
                        door = side                    
                        if not door._isOpen:
                            print('    *** Opening the door...')
                            door._isOpen = True
                            door.Enter()
                        print('\t', door)                    
                        # get the room on the other side of the door
                        other_room = door.OtherSideFrom(room)
                        print('\tOn the other side of the door is Room: {}\n'.format(other_room._roomNumber))                    
                
            except KeyError:
                print('No room:', room_number)
        num_of_rooms = len(maze_rooms)
        print('\nThere are {} rooms in the Maze.'.format(num_of_rooms))       
        print('Both doors are the same object and they are on the East and West side of the two rooms.')

    ##########################################################################################################
    def play_game(aProtoFactory, num_of_stars=44, explode_bomb=False):
        print('\n')
        print('*' * num_of_stars)
        print('*** The Maze Game ***')
        print('*' * num_of_stars)
            
        factory = aProtoFactory
        print(factory)
        print('=' * num_of_stars)
        
        game = MazeGame()
        maze = game.CreateMaze(factory)
        find_maze_rooms(maze)     
    
        if explode_bomb:
            print('\n*** Bomb exploded - walls are damaged! ***')
            maze._rooms[1].bomb_exploded = True
            for side in range(4):
                cur_side = maze._rooms[1]._sides[side]
                if 'BombedWall' in str(cur_side):
                    cur_side.wall_is_damaged = True
                    print('Wall is damaged:', cur_side, cur_side.wall_is_damaged)
            
    ############################################

    # create a prototypical/default maze factory
    # initialize with basic maze component objects
    simpleMazeFactory = MazePrototypeFactory(
        Maze(), Wall(), Room(), Door()             # pass in instances of components
    )
              
    # pass the prototype into the game
    play_game(simpleMazeFactory)
  
      
    # change type of maze by initializing the MazePrototypeFactory
    # with a different set of prototypes
    bombedMazeFactory = MazePrototypeFactory(
        Maze(), BombedWall(),
        RoomWithABomb(), Door()
    )
           
    # pass the prototype into the game
    play_game(bombedMazeFactory)
     
    
    # Create a maze that will consist of 100 rooms with 400 walls
    complexMazeFactory = MazePrototypeFactory(
        Maze(), Wall(), Room(), Door()              # pass in instances of components
    )
    
    game = MazeGame()
    maze = game.CreateMaze(complexMazeFactory)      # creates 2 rooms with a door in between

    # print current maze objects
    from pprint import pprint
    pprint(maze._rooms)
    print()
    
    # Create 98 more rooms and add them to the maze -- they are not connected to each other
    for roomNo in range(3, 101):                    # create 98 more rooms
        new_room = Room()                           # create new room
        new_room.Initialize(roomNo)                 # give room unique number
        maze.AddRoom(new_room)                      # add room to maze        
        
    pprint(maze.__dict__)                   # print maze objects
    print()
    pprint(complexMazeFactory.__dict__)     # print complexMazeFactory objects
    
    print()
    print(maze.RoomNo(99))
    print(maze.RoomNo(99).GetSide(0))                       # 0 = North
    print(maze.RoomNo(99).GetSide(Direction(0).value))      # 0 = North
    print(maze.RoomNo(99).GetSide(Direction.South.value))   # Room has neither Door nor Wall
    print()
    
    # Create 400 walls and add them to the 100 rooms
    for room in range(3, 101):                              # Room1 and Room2 are already build
        for site_dir in range(4):
            new_wall = Wall()
            maze.RoomNo(room).SetSide(site_dir, new_wall)   
            print(maze.RoomNo(room).GetSide(site_dir))
    print()
    # print out the 4 sides of some rooms (any room between 1 - 100)
    for side in range(4):
        print('Room: ' + '12', Direction(side), maze.RoomNo(12).GetSide(side))
        
    print()
    for side in range(4):
        print('Room: ' + '100', Direction(side), maze.RoomNo(100).GetSide(side))       
        
    print()                
    
    # We are building a maze consisting of 100 rooms with walls.
    # We use this as a Prototype to build different mazes, all consisting of 100 rooms 
    # but with doors that can be located in different directions of any room.
    # They can also have different types of Rooms and of Walls (bombed).

    # Now that we have created an expensive object, let us register this prototype maze
    complexMazeFactory.register_prototype('100_Rooms', maze)
    print(maze)                                                 # same objects
    print()
    print(complexMazeFactory.prototype_manager_registry)
    
    # clone maze
    # We are creating a copy of the already created maze object
    original = complexMazeFactory.prototype_manager_registry['100_Rooms']
    print('\nproto Maze:', original, original.__class__)
    
    clone = deepcopy(original)
    print('clone Maze:', clone, clone.__class__)    # same class, different object in memory
    
    print()
    print(clone.RoomNo(100).GetSide(3))
    
    clone.RoomNo(100).SetSide(3, BombedWall())      # change the type of Wall
    print(clone.RoomNo(100).GetSide(3))
    
    
    # helper function to find rooms that have doors
    def find_doors(the_clone, first_room, last_room):
        for room_number in range(first_room, last_room):                         
            for room_direction in range(4):
                site = the_clone.RoomNo(room_number).GetSide(room_direction)
                if 'Door' in str(site):
                    print('Room: ' + str(room_number), Direction(room_direction), site)    
#                     print('Room: ' + str(room_number), site)        
    
    print('\nDoors in Rooms 1 to 100')        # Clone has one door between Room1 and Room2
    find_doors(clone, 1, 101)
    
    # Add a door to Room2
    new_door = Door()
    clone.RoomNo(2).SetSide(Direction.East.value, new_door)
    clone.RoomNo(3).SetSide(Direction.West.value, new_door)
    
    print('\nDoors in Rooms 1 to 10')
    find_doors(clone, 1, 10)
    
    # make another clone from the prototype manager registry
    another_clone = deepcopy(original)
    print('\nanother_clone:', another_clone, another_clone.__class__)    # same class, different object
    
    # Add a door to Room2
    new_door = Door()
    another_clone.RoomNo(2).SetSide(Direction.North.value, new_door)
    another_clone.RoomNo(3).SetSide(Direction.South.value, new_door)
    
    print('\nDoors in Rooms 1 to 10')
    find_doors(another_clone, 1, 10)    
    
    