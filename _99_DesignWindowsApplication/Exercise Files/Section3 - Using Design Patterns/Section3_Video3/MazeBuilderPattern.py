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


# interface
class MazeBuilder():
    def __init__(self):
        pass                                # constructor-like initializer
    
    def BuildMaze(self):                    # build a Maze
        pass                                # empty, can be overwritten; not raising an exception
    
    def BuildRoom(self, room):              # build a Room with a number
        pass                                # empty, can be overwritten
    
    def BuildDoor(self, roomFrom, roomTo):  # place a door between existing rooms
        pass                                # empty, can be overwritten
    
    def GetMaze(self):                      # get the Maze
        return None                         # overwrite to return a Maze
    
    
class MazeGame():   
    # Builder Design Pattern
    def CreateMaze(self, builder):          # pass in a MazeBuilder
        builder.BuildMaze()

        builder.BuildRoom(1)
        builder.BuildRoom(2)
        builder.BuildDoor(1, 2)
                                            # there is no BuildWall...                           
        return builder.GetMaze()
    
    
    def CreateComplexMaze(self, builder):   # pass in a MazeBuilder
        builder.BuildRoom(1)
        # ...
        builder.BuildRoom(1001)             # 1,000 rooms, no doors, using same MazeBuilder interface
        
        return builder.GetMaze()

    
# C-like .h interface definition
class Interface_StandardMazeBuilder(MazeBuilder):
    def __init__(self): pass
    
    def BuildMaze(self): pass                            
    def BuildRoom(self, n): pass        
    def BuildDoor(self, roomFrom, roomTo): pass                                
    
    def GetMaze(self): return Maze
  
    # private      
    def CommonWall(self, Room1, Room2): return Direction    
    _currentMaze = Maze
        

# implementation        
class StandardMazeBuilder(MazeBuilder):
    def __init__(self):  
        self._currentMaze = None                # member to hold a Maze
    
    def BuildMaze(self): 
        self._currentMaze = Maze() 
                                       
    def BuildRoom(self, n): 
        try: self._currentMaze.RoomNo(n)
        except: 
            print('Room {} does not exist - building this room.'.format(n))
            room = Room(n)
            self._currentMaze.AddRoom(room)
            
            room.SetSide(Direction.North.value, Wall())   # all sides are Walls
            room.SetSide(Direction.South.value, Wall())
            room.SetSide(Direction.East.value, Wall())
            room.SetSide(Direction.West.value, Wall())
            
                                        
    def BuildDoor(self, n1, n2):
        r1 = self._currentMaze.RoomNo(n1)
        r2 = self._currentMaze.RoomNo(n2) 
        d = Door(r1, r2)
        
        r1.SetSide(self.CommonWall(r1, r2), d)  # Door replaces Wall
        r2.SetSide(self.CommonWall(r2, r1), d)  # Door replaces Wall
        
        print()
        for side in range(4):
            if 'Door' in str(r1._sides[side]):
                print('Room1: ', r1._sides[side], Direction(side))
            if 'Door' in str(r2._sides[side]):
                print('Room2: ', r2._sides[side], Direction(side))
            
    
    def GetMaze(self):
        return self._currentMaze                            
          
    def CommonWall(self, aRoom, anotherRoom):
        # layout: room1, room2 etc. from left (West) to right (East)
        if aRoom._roomNumber < anotherRoom._roomNumber:
            return Direction.East.value       # other room on East
        else:
            return Direction.West.value       # other room on West
    
    
# C-like .h interface definition
class Interface_CountingMazeBuilder(MazeBuilder):
    
    def __init__(self): 
        # private        
        self._doors     # leading '_' is a naming convention for private
        self._rooms
    
    def BuildMaze(self): pass                            
    def BuildRoom(self, n): pass        
    def BuildDoor(self, r1, r2): pass       
    def AddWall(self, n, Direction): pass
    
    def GetCounts(self): return tuple()
  

# implementation        
class CountingMazeBuilder(MazeBuilder):
    def __init__(self):  
        self._rooms = 0
        self._doors = 0

    def BuildRoom(self, n): 
        self._rooms += 1
        
    def BuildDoor(self, r1, r2):
        self._doors += 1    

    def GetCounts(self): 
        return self._rooms, self._doors


#==================================================================
# Self-testing section    
#==================================================================
if __name__ == '__main__':
    print('*' * 21)
    print('*** The Maze Game ***')
    print('*' * 21)
    
    maze = Maze
    game = MazeGame()
    builder = StandardMazeBuilder()

    game.CreateMaze(builder)
    maze = builder.GetMaze()
    
       
    print('\n' * 2)
    print('*' * 21)
    print('*** The Counting Maze Game ***')
    print('*' * 21)
     
    game = MazeGame()
    builder = CountingMazeBuilder()
 
    game.CreateMaze(builder)
    rooms, doors = builder.GetCounts()
     
    print('The maze has {} rooms and {} doors'.format(rooms, doors))
     
    
    