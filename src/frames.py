from tkinter import HIDDEN, Frame, Canvas

class GameResult(Canvas):

    def __init__(self, master, frame_size:list):
        self.__master = master
        self.__height, self.__width = frame_size

        self.__init_ui()

    def __init_ui(self):
        super().__init__(
            self.__master,
            height=self.__height,
            width=self.__width,
        )

        self.__text = self.create_text(
            ((self.__width / 2), (self.__height / 2)), 
            text=''
        )

        self.bind("<Button-1>", self.remove)

    def add(self, text):
        self.itemconfigure(self.__text, text=text)
        self.pack()

    def remove(self, event=None):
        self.pack_forget()