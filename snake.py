import turtle as t

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__ (self):
        self.segments = []
        self.positions = [(0,0),(-20,0),(-40,0)]
        for pos in self.positions:
            self.add_segment(pos)
    
    def add_segment(self, position):
        new_seg = t.Turtle()
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x_cor = self.segments[seg_num -1].xcor()
            y_cor = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.segments[0].forward(20)
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)                        