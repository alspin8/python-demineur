from tkinter import Tk

from .frames import GameResult
from .gridUI import GridUI

class Demineur(Tk):

    def __init__(self, **kwargs):
        self.__height = kwargs["height"] if "height" in kwargs else 500
        self.__width = kwargs["width"] if "width" in kwargs else 500
        self.__rows = kwargs["rows"] if "rows" in kwargs else 5
        self.__columns = kwargs["columns"] if "columns" in kwargs else 5
        
        self.__init_ui()

        self.demineur.signals['loose'].connect(self.loose)
        self.demineur.signals['win'].connect(self.win)
        
    def __init_ui(self):
        super().__init__()
        self.title("Démineur")
        self.geometry(f'{self.__width}x{self.__height}')
        
        self.demineur = GridUI(
            master=self, 
            frame_size=(self.__height, self.__width),
            grid_size=(self.__rows, self.__columns)
        )
        self.demineur.add()

        self.result = GameResult(
            master=self,
            frame_size=(self.__height, self.__width)
        )

    def win(self):
        self.result.add("win")
        # self.demineur.remove()

    def loose(self):
        self.result.add("loose")
        self.demineur.remove()
        
    def run(self):
        self.mainloop()