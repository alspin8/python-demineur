from dataclasses import dataclass, field
import random

@dataclass
class Location:
    row: int
    column: int
    
    def is_around(self, base):
        if abs(self.row - base.row) <= 1 and abs(self.column - base.column) <= 1:
            return True
        else:
            return False

    def is_in_grid(self, grid_size:tuple):
        if self.row >= 0 and self.row < grid_size[0] and self.column >= 0 and self.column < grid_size[1]:
            return True
        else: return False

    def left(self): return Location(row=self.row, column=self.column - 1)

    def right(self): return Location(row=self.row, column=self.column + 1)

    def top(self): return Location(row=self.row - 1, column=self.column)

    def bottom(self): return Location(row=self.row + 1, column=self.column)

@dataclass
class Case:
    is_bomb: bool
    is_hidden: bool = field(init=False, default=True)
    value: int = field(init=False, default=0)
    location: Location
    

class Grid:

    def __init__(self, rows:int = 5, columns:int = 5): 
        self.rows = rows
        self.columns = columns
        self.loose = False
        self.win = False

        self.__grid = []
        
        self.__fill_bomb()
        self._fill_case_value()
         
    def __fill_bomb(self):
        for _row in range(self.rows):
            for _column in range(self.columns):
                rnd = random.randint(1, 5)
                self.__grid.append(Case(
                    is_bomb=(True if rnd == 1 else False), 
                    location=Location(
                        row=_row, 
                        column=_column
                    )
                ))
                
    def _fill_case_value(self):
        for case in self.__grid:
            if case.is_bomb:
                for _case in self.__grid:
                    if _case.location.is_around(case.location):
                        _case.value += 1
                    elif case.location.row - _case.location.row < -1 :
                        break
                    else: pass
            else: pass
           
    # Getters
    def grid(self): return self.__grid
            
    def case(self, location:Location): return [case for case in self.__grid if case.location.row == location.row and case.location.column == location.column][0]
    
    def case_index(self, location:Location): return [self.__grid.index(case) for case in self.__grid if case.location.row == location.row and case.location.column == location.column][0]
    
    def case_value(self, location:Location): return self.case(location).value
    
    def is_bomb_on_case(self, location:Location):
        if location.row >= 0 and location.row < self.rows and location.column >= 0 and location.column < self.columns:
            return self.case(location).is_bomb
        else: return True
    
    def is_case_hidden(self, location:Location): return self.case(location).is_hidden
    
    # Setters
    def hide_case(self, location:Location): self.grid[self.case_index(location)].is_hidden = True
    
    def show_case(self, location:Location): 
        if not self.loose:
            case = self.case(location)
            self.__grid[self.case_index(location)].is_hidden = False
            if case.is_bomb:
                self.loose = True
            else:
                self.__start_propagation(location)
        
    # Propagation
    
    def __start_propagation(self, location:Location):
        self.__propagation(location.left())
        self.__propagation(location.right())
        self.__propagation(location.bottom())
        self.__propagation(location.top())
    
    def __propagation(self, location:Location):
        if location.is_in_grid((self.rows, self.columns)) and self.is_case_hidden(location) and not self.is_bomb_on_case(location):
            case = self.case(location)
            if( 
                (not self.is_bomb_on_case(location.left())) and 
                (not self.is_bomb_on_case(location.right())) and 
                (not self.is_bomb_on_case(location.bottom())) and 
                (not self.is_bomb_on_case(location.top())) ):
                self.__grid[self.__grid.index(case)].is_hidden = False
                self.__start_propagation(case.location)