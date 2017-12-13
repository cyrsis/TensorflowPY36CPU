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
            self._room1 = None          # declare private members
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
        print('Room: ', self._roomNumber)
        print('Room is of Type: ', self.__class__)
                
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


# Extend MazeFactory
class EnchantedMazeFactory(MazeFactory):        
    @classmethod            # decorator
    def MakeRoom(cls, n):   # n = roomNumber
        return EnchantedRoom(n, cls.CastSpell())    # pass in roomNo, create a spell      
        
    @classmethod                # decorator
    def MakeDoor(cls, r1, r2):  # r1, r2 = two rooms
        return DoorNeedingSpell(r1, r2)     # door between rooms
    
    @classmethod
    def CastSpell(cls):
        return Spell()  
    

class EnchantedRoom(Room):
    def __init__(self, roomNo, aSpell):
        super(EnchantedRoom, self).__init__(roomNo)
        print('The spell is: ', aSpell)
        
class Spell():    
    def __repr__(self):                 # overwrite string representation
        return '"A hard-coded spell"'

class DoorNeedingSpell(Door):    
    def __init__(self, r1, r2):
        super(DoorNeedingSpell, self).__init__(r1, r2)
        self.spell = Spell()

    def Enter(self):
        print('    + This door needs a Spell...', self.spell)
        if self._isOpen: print('    **** You have passed through this door...')
        else: print('    ** This door needs to be opened before you can pass through it...')

    
# Extend MazeFactory
class BombedMazeFactory(MazeFactory):
    @classmethod            # decorator
    def MakeWall(cls): 
        return BombedWall()
       
    @classmethod            # decorator
    def MakeRoom(cls, n):   # n = roomNumber
        return RoomWithABomb(n)    # pass in roomNo, create a spell

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
    # Abstract Factory
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
    
    # Note: Base-class Wall has no Clone method, so we add it to this subclass    
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
    