from tkinter import Frame
from .objects import Grid

class GridUI(Frame):

    HIDE = "#17A1F0"
    SHOW = "#FFFFFF"
    FLAGGED = "#0DDE30"
    BOMB = "#F21B0D"

    def __init__(self, master, frame_size:tuple=(500, 500), grid_size:tuple=(5, 5)):
        self.__master = master
        self.__height, self.__width = frame_size
        self.__rows, self.__columns = grid_size
        
        self.__gridui = []
        
        self.__init_grid()
        self.__init_ui()
        
    def __init_grid(self):
        self.__grid = Grid(
            rows=self.__rows,
            columns=self.__columns
        )
    
    def __init_ui(self):
        super().__init__(
            master=self.__master, 
            height=self.__height, 
            width=self.__width
        )
        
        case_height = self.__height / self.__rows
        case_width = self.__width / self.__columns
        
        for case in self.__grid.grid():
            self.__gridui.append(
                CaseUI(
                    self, 
                    height=case_height, 
                    width=case_width, 
                    color=self.HIDE
                )
            )
            self.__gridui[len(self.__gridui) - 1].add(case.location)
        
    def start(): self.__init_grid()
        
    def add(self):
        self.pack()
        
class CaseUI(Frame):

    def __init__(self, master, **kwargs):
        self.__master = master
        self.__height = kwargs['height']
        self.__width = kwargs['width']
        self.__color = kwargs['color']
        
        self.__init_case()
        
    def __init_case(self):
        super().__init__(
            master=self.__master,
            height=self.__height, 
            width=self.__width,
            bg=self.__color
        )
        
    def add(self, location):
        self.grid(
            row=location.row,
            column=location.column,
            padx=1,
            pady=1
        )