import turtle

colors = ["red", "yellow", "green", "blue", "purple", "orange"]

turtle.speed(500)
turtle.bgcolor("black")

def draw_spiral(x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  
  for i in range(360):
    
    turtle.pencolor(colors[i % 6]) # % é o resto da divisão
    turtle.width(i // 100 + 1) # // é uma divisão que ignora quebrados e usa inteiros
    turtle.forward(i)
    turtle.left(59)

turtle.getscreen().onclick(draw_spiral) #o clique só funciona direito pq ta identado aqui

turtle.mainloop()