import itertools, PySignal
from unittest import signals
from tkinter import HIDDEN, Canvas, Frame
from tkinter.font import NORMAL
from .grid import Grid, Location

class GridUI(Frame):

    BLACK = "#000000"

    PADDING = 1

    def __init__(self, master, frame_size:tuple=(500, 500), grid_size:tuple=(5, 5)):
        self.__master = master
        self.__height, self.__width = frame_size
        self.__rows, self.__columns = grid_size
        
        self.__gridui = []

        self.signals = PySignal.SignalFactory()
        self.signals.register('loose')
        self.signals.register('win')
        
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
            width=self.__width,
            bg=self.BLACK
        )
        
        case_height = (self.__height / self.__rows) - 2 * self.PADDING
        case_width = (self.__width / self.__columns) - 2 * self.PADDING
        
        for case in self.__grid.grid():
            self.__gridui.append(
                CaseUI(
                    self, 
                    location=case.location,
                    height=case_height, 
                    width=case_width, 
                    value=('X' if case.is_bomb else case.value)
                )
            )
            self.__gridui[len(self.__gridui) - 1].bind(
                "<Button-1>", 
                lambda event, location=case.location:self.__on_click(event, location) 
            )

    def __on_click(self, event, location):
        self.__grid.show_case(location)
        self.__refresh()
        if self.__grid.loose:
            self.signals['loose'].emit()
        elif self.__grid.win:
            self.signals['win'].emit()
        else: pass

    def __refresh(self):
        for case, caseUI in itertools.zip_longest(self.__grid.grid(), self.__gridui):
            if not case.is_hidden:
                caseUI.show()
        
    def start(self): self.__init_grid()
        
    def add(self):
        self.pack()

    def remove(self):
        self.pack_forget()
        
class CaseUI(Canvas):

    HIDE = "#17A1F0"
    SHOW = "#FFFFFF"
    BLACK = "#000000"

    def __init__(self, master, location:Location, **kwargs):
        self.__master = master
        self.location = location
        self.__height = kwargs['height']
        self.__width = kwargs['width']
        self.__value = kwargs['value']
        
        self.__init_case()
        self.__add()
        
    def __init_case(self):
        super().__init__(
            master=self.__master,
            height=self.__height, 
            width=self.__width,
            bg=self.HIDE,
            highlightthickness=0
        )
        self.text = self.create_text(
            ((self.__width / 2), (self.__height / 2)), 
            text=self.__value,
            fill=self.BLACK,
            state=HIDDEN
        )

    def show(self):
        self.config(background=self.SHOW)
        if self.itemcget(self.text, 'state') == HIDDEN:
            self.itemconfigure(self.text, state=NORMAL)
            
        
    def __add(self):
        self.grid(
            row=self.location.row,
            column=self.location.column,
            padx=1,
            pady=1
        )