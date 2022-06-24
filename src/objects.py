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
    def grid(self): 
        print(self.__grid)
        return self.__grid
            
    def case(self, row, column): return [case for case in self.__grid if case.location.row == row and case.location.column == column][0]
    
    def case_index(self, row, column): return [self.__grid.index(case) for case in self.__grid if case.location.row == row and case.location.column == column][0]
    
    def case_value(self, row, column): return self.case(row, column).value
    
    def is_bomb_on_case(self, row, column): return self.case(row, column).is_bomb
    
    def is_case_hidden(self, row, column): return self.case(row, column).is_hidden
    
    # Setters
    def hide_case(self, row, column): self.grid[self.case_index(row, column)].is_hidden = True
    
    def show_case(self, row, column): self.__start_propagation(row, column)
        
    # Propagation
    
    def __start_propagation(row, column):
        self.__propagation(row + 1, column + 1)
        self.__propagation(row + 1, column - 1)
        self.__propagation(row - 1, column + 1)
        self.__propagation(row - 1, column - 1)
    
    def __propagation(row, column):
        case = self.case(row, column)
        if( not self.case(row + 1, column + 1).is_bomb and
            not self.case(row + 1, column - 1).is_bomb and
            not self.case(row - 1, column + 1).is_bomb and
            not self.case(row - 1, column - 1).is_bomb ):
            self.__grid[self.grid.index(case)].is_hidden = False
            return self.__start_propagation(case.location.row, case.location.column)
        else: return
            