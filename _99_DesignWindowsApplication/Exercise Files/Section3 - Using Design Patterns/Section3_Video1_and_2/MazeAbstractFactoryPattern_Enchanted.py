from enum import Enum

class MapSite():
    def Enter(self):
        raise NotImplementedError('Abstract Base Class method')
    
class Direction(Enum):
    North = 0
    East  = 1
    South = 2
    West  = 3
    
class Room(MapSite):
    def __init__(self, roomNo):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)
        
    def GetSide(self, Direction):
        return self._sides[Direction]
    
    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite
        
    def Enter(self):
        print('    You have entered room: ' + str(self._roomNumber))
        
class Wall(MapSite):
    def Enter(self):
        print('    * You just ran into a Wall...')    

class Door(MapSite):
    def __init__(self, Room1=None, Room2=None):
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False
        
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

class MazeGame():   
    # Abstract Factory
    def CreateMaze(self, factory=MazeFactory):
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
# Self-testing section    
#==================================================================
if __name__ == '__main__':
    # common code moved into function
    def find_maze_rooms(maze_obj):      # pass object into function
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
    num_of_stars = 44
    print('*' * num_of_stars)
    print('*** The Maze Game - MazeFactory ***')
    print('*' * num_of_stars)
    
    # creating the original Maze passing it in as a Factory
    factory = MazeFactory       # pass in class directly
#     factory = MazeFactory()     # pass in instance of class; no __init__(self)
    print(factory)
    print('=' * num_of_stars)
     
    maze_obj = MazeGame().CreateMaze(factory)
    find_maze_rooms(maze_obj)

    print('\n')
    print('*' * num_of_stars)
    print('*** The Maze Game - EnchantedMazeFactory ***')
    print('*' * num_of_stars)
    
    ############################################
    
    factory = EnchantedMazeFactory
    print(factory)
    print('=' * num_of_stars)
    
    maze_obj = MazeGame().CreateMaze(factory)
    find_maze_rooms(maze_obj)     

    