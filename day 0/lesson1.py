from turtle import*

width("6")

#house

color("dark blue")
forward (200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#door

forward(75)
color("yellow")
begin_fill()
left(90)
forward (85)
right(90)
forward(45)
right(90)
forward(85)
end_fill()

#window 1

color("purple")
penup()
goto(20,120)
pendown()
begin_fill()
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

#window 2

penup()
goto(120, 120) 
pendown()
begin_fill()
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()


#roof

penup()
goto(200,200)
pendown()
color("dark blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

exitonclick()