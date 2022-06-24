from tkinter import Tk
from .objectUI import GridUI

class Demineur(Tk):

    def __init__(self, **kwargs):
        self.__height = kwargs["height"]
        self.__width = kwargs["width"]
        
        self.__init_ui()
        
    def __init_ui(self):
        super().__init__()
        self.geometry(f'{self.__width}x{self.__height}')
        
        demineur = GridUI(
            self, 
            frame_size=(self.__height, self.__width),
            grid_size=(5, 5)
        )
        demineur.add()
        
        
    def run(self):
        self.mainloop()