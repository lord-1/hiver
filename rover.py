class Position:
    """
    Position Generic class
    """
    ANGLED_FACE_LEFT = {
        "North": "West",
        "West": "South",
        "South": "East",
        "East": "North"
    }

    ANGLED_FACE_RIGHT = {
        "West": "North",
        "South": "West",
        "East": "South",
        "North": "East"
    }

    FACE_DICT = {
        "L": ANGLED_FACE_LEFT,
        "R": ANGLED_FACE_RIGHT
    }

    def __init__(self, x=0, y=0, face='North'):
        self.__x = x
        self.__y = y
        self.__current_face = face

    def __movement(self):
        """
        Function to make changes in x coordinate and
        y coordinate based on direction the rover is
        facing
        :return:
        """
        if self.__current_face == 'North':
            self.__y += 1
        elif self.__current_face == 'South':
            self.__y -= 1
        elif self.__current_face == 'East':
            self.__x += 1
        else:
            self.__x -= 1

    def set(self, face=None, movement=False):
        """
        Function to accept either the movement or the face
        for the rover
        :param face: to change the face based on direction
        :param movement: to move the rover forward towards the face
        :return: None
        """
        if movement:
            self.__movement()
        else:
            self.__current_face = self.FACE_DICT[face][self.__current_face]

    def get(self):
        """
        getter for the class
        :return: x coord, y coord, current facing direction
        """
        return self.__x, self.__y, self.__current_face


class Rover:
    """
    Class for the rover
    """
    ALLOWED = ['M', 'L', 'R', '?', 'Q']

    def __show_position(self):
        """
        Function to show position of the rover
        :return:
        """
        print(self.current_pos.get())

    def __init__(self, x=0, y=0, face="North"):
        self.current_pos = Position(0, 0)
        self.__show_position()

        self.ALLOWED_FUNCTIONS = {
            "L": self.__turn_left,
            "R": self.__turn_right,
            "M": self.__move_forward,
            "Q": exit}

    def __move_forward(self):
        """
        function to acknowledge movement
        :return: None
        """
        self.current_pos.set(movement=True)
        self.__show_position()

    def __turn_right(self):
        """
        function to acknowledge change of face towards
        right of current direction
        :return: None
        """
        self.current_pos.set(face="R")
        self.__show_position()

    def __turn_left(self):
        """
        function to acknowledge change of face towards
        right of current direction
        :return: None
        """
        self.current_pos.set(face="L")
        self.__show_position()

    def start_movement(self):
        """
        function to start the rover inputs
        :return: None
        """
        while True:
            x = input()
            self.ALLOWED_FUNCTIONS.get(x)()


if "__name__" == "__main__":
    Rover().start_movement()

"""
Assumptions 
1. Only M, L, Q, R, ? are allowed
2. Current position is (0,0, North)
3. Bi axial Movement 
"""