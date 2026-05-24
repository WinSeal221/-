import tkinter as tk
import tkinter.messagebox
import random
SNAKE = [(15,12),(14,12),(13,12),(12,12)]
APLLE = [(0,0)]
total_com_w = 0
total_com_a = 0
total_com_d = 0
total_com_s = 0
check = 0
apple_eat = 0
apple_eat_2 = 0
speed = 500
id_after = None
win = None
canvas = None
def return_com():
  global speed
  global apple_eat
  global total_com_w
  global total_com_s
  global total_com_d
  global total_com_a
  global win
  global check
  global canvas
  global apple_eat_2
  global apple_eat
  global SNAKE
  global APLLE
  check -= 1
  canvas = None
  SNAKE = [(15,12),(14,12),(13,12),(12,12)]
  APLLE = [(0,0)]
  total_com_a = 0
  total_com_d = 0
  total_com_s = 0
  total_com_w = 0
  apple_eat = 0
  apple_eat = 0
  apple_eat_2 = 0
  speed = 500
  win.destroy()
  win = None
  main()
def text():
  global apple_eat
  global apple_eat_2
  global canvas
  apple_eat += 1
  apple_eat_2 += 1
  canvas.delete('text')
  canvas.create_text(70,15,text=f'Всего яблок сьедено:{apple_eat}',tag='text')
def speed_com():
  global canvas
  global speed
  global apple_eat_2
  global apple_eat
  if apple_eat_2 == 5:
    apple_eat_2 = 0
    speed -= 50
    canvas.delete('text_sp')
    canvas.create_text(405,15,text=f'Всего яблок до ускорения:5/{apple_eat_2}',tag='text_sp')
  else:
    canvas.delete('text_sp')
    canvas.create_text(405,15,text=f'Всего яблок до ускорения:5/{apple_eat_2}',tag='text_sp')
def snake():
  global canvas
  size_snake = 15
  for i,(x,y) in enumerate(SNAKE):
    x_1 = x * size_snake
    y_1 = y * size_snake
    x_2 = x_1 - size_snake
    y_2 = y_1 - size_snake
    color = "#00FF37" if i == 0 else "#000000"
    canvas.create_rectangle(x_1,y_1,x_2,y_2,fill=color, tag='snake' )
def apple_com():
   global canvas
   global APLLE
   size_apple = 15
   APLLE = [(random.randint(1,25),random.randint(1,25))]
   x,y = APLLE[0]
   x *= size_apple
   y *= size_apple
   x_2 = x - size_apple 
   y_2 = y - size_apple
   canvas.create_rectangle(x,y,x_2,y_2,fill="#FF0000",tag='aplle')
def movement_snake():
    global apple_eat
    global check 
    global win
    global speed
    global canvas
    if check == 0:
      global total_com_w
      global total_com_a
      global total_com_d
      global total_com_s
      global id_after
      if total_com_w == 1:
        x,y = SNAKE[0]
        y -= 1
        SNAKE.insert(0,(x,y))
        verble = SNAKE[-1]
        SNAKE.pop()
        canvas.delete('snake')
        snake()
        x,y = SNAKE[0]
        if y == 0:
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об стену',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
        if len(SNAKE) != len(set(SNAKE)):
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об себя же',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
        for x,y in SNAKE:
          if (x,y) == APLLE[0]:
            verible = True
            break
          else:
            verible = False
        if verible:
          SNAKE.append(verble)
          canvas.delete('snake')
          canvas.delete('aplle')
          snake()
          text()
          speed_com()
          apple_com()
        if id_after is not None:
          win.after_cancel(id_after)
          id_after = win.after(speed,movement_snake)
        else:
          id_after = win.after(speed,movement_snake)
          
      elif total_com_a == 1:
         x,y = SNAKE[0]
         x -= 1        
         SNAKE.insert(0,(x,y))
         verble = SNAKE[-1]
         SNAKE.pop()
         canvas.delete('snake')
         snake()
         x,y = SNAKE[0]
         if x == 0:
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об стену',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
         if len(SNAKE) != len(set(SNAKE)):
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об себя же',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
         for x,y in SNAKE:
          if (x,y) == APLLE[0]:
            verible = True
            break
          else:
            verible = False
         if verible:
          SNAKE.append(verble)
          canvas.delete('snake')
          canvas.delete('aplle')
          snake()
          text()
          speed_com()
          apple_com()
         if id_after is not None:
           win.after_cancel(id_after)
           id_after = win.after(speed,movement_snake)
         else:
           id_after = win.after(speed,movement_snake)
           
      elif total_com_d == 1:
        x,y = SNAKE[0]
        x += 1
        SNAKE.insert(0,(x,y))
        verble = SNAKE[-1]
        SNAKE.pop()
        canvas.delete('snake')
        snake()
        x,y = SNAKE[0]
        if x == 34:
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об стену',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
        if len(SNAKE) != len(set(SNAKE)):
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об себя же',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
        for x,y in SNAKE:
          if (x,y) == APLLE[0]:
            verible = True
            break
          else:
            verible = False
        if verible:
          SNAKE.append(verble)
          canvas.delete('snake')
          canvas.delete('aplle')
          snake()
          text()
          speed_com()
          apple_com()
        if id_after is not None:
          win.after_cancel(id_after)
          id_after = win.after(speed,movement_snake)
        else:
          id_after = win.after(speed,movement_snake)
          
      elif total_com_s == 1:
         x,y = SNAKE[0]
         y += 1
         SNAKE.insert(0,(x,y))
         verble = SNAKE[-1]
         SNAKE.pop()
         canvas.delete('snake')
         snake()
         x,y = SNAKE[0]
         if y == 34:
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об стену',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
         if len(SNAKE) != len(set(SNAKE)):
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об себя же',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
         for x,y in SNAKE:
          if (x,y) == APLLE[0]:
            verible = True
            break
          else:
            verible = False
         if verible:
          SNAKE.append(verble)
          canvas.delete('snake')
          canvas.delete('aplle')
          snake()
          text()
          speed_com()
          apple_com()
         if id_after is not None:
            win.after_cancel(id_after)
            id_after = win.after(speed,movement_snake)
         else:
            id_after = win.after(speed,movement_snake)
            
      elif total_com_w == 0 and total_com_a == 0 and total_com_d == 0 and total_com_s == 0:
         x,y = SNAKE[0]
         x += 1
         SNAKE.insert(0,(x,y))
         verble = SNAKE[-1]
         SNAKE.pop()
         canvas.delete('snake')
         snake()
         x,y = SNAKE[0]
         if x == 34:
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об стену',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
         if len(SNAKE) != len(set(SNAKE)):
          canvas.destroy()
          label = tk.Label(win,text='Вы проиграли',font=('arial',30))
          label.pack(side='top')
          label_2 = tk.Label(win,text='Причина смерти: вы столкнулись об себя же',font=('arial',15)) 
          label_2.pack()
          label_3 = tk.Label(win,text='Нажмите \'выйти\' чтоб закончить игру',font=('arial',15))
          label_3.pack()
          label_4 = tk.Label(win,text='Нажмити \'заново\' чтоб начать играть снова',font=('arial',15))
          label_4.pack()
          button = tk.Button(win,text='Выйти',width=15,height=2,command=win.destroy)
          button.pack()
          button_2 = tk.Button(win,text='Заново',width=15,height=2,command=return_com)
          button_2.pack()
          check += 1
          return
         for x,y in SNAKE:
          if (x,y) == APLLE[0]:
            verible = True
            break
          else:
            verible = False
         if verible:
          SNAKE.append(verble)
          canvas.delete('snake')
          canvas.delete('aplle')
          snake()
          text()
          speed_com()
          apple_com()
         if id_after is not None:
          win.after_cancel(id_after)
          id_after = win.after(500,movement_snake)
         else:
          id_after = win.after(500,movement_snake)
    
def w_command(event):
  global check
  if check == 0:
    global total_com_w
    global total_com_a
    global total_com_d
    global total_com_s
    if total_com_w == 0 and total_com_a == 0 and total_com_d == 0 and total_com_s == 0:
       total_com_w += 1
       movement_snake()
    elif total_com_w == 0 and total_com_s == 0 and total_com_a == 1:
      total_com_w += 1
      total_com_a -= 1
      movement_snake()
    elif total_com_w == 0 and total_com_s == 0 and total_com_d == 1:
       total_com_w += 1
       total_com_d -= 1
       movement_snake()
def a_command(event):
  global check
  if check == 0:
    global total_com_a
    global total_com_w
    global total_com_s
    if total_com_a == 0 and total_com_w == 1:
      total_com_a += 1
      total_com_w -= 1
      movement_snake()
    elif total_com_a == 0 and total_com_s == 1:
      total_com_a += 1
      total_com_s -= 1
      movement_snake()
def d_command(event):
  global check
  if check == 0:
    global total_com_w
    global total_com_d 
    global total_com_s
    if total_com_d == 0 and total_com_w == 1:
       total_com_d += 1
       total_com_w -= 1
       movement_snake()
    elif total_com_d == 0 and total_com_s == 1:
        total_com_d += 1
        total_com_s -= 1
        movement_snake()
def s_command(event):
  global check
  if check == 0:
    global total_com_s
    global total_com_w
    global total_com_a
    global total_com_d
    if total_com_s == 0 and total_com_w == 0 and total_com_a == 0 and total_com_d == 0:
      total_com_s += 1
      movement_snake()
    elif total_com_s == 0 and total_com_w == 0 and total_com_a == 1:
      total_com_s += 1
      total_com_a -= 1
      movement_snake()
    elif total_com_s == 0 and total_com_w == 0 and total_com_d == 1:
      total_com_s += 1
      total_com_d -= 1
      movement_snake()
def main():
  global apple_eat
  global win
  global canvas
  win = tk.Tk()
  win.geometry("495x495+100+100")
  win.title("Змейка")
  win.config(cursor='None')
  win.bind("<KeyPress>")
  win.bind("w",w_command)
  win.bind("s",s_command)
  win.bind("a",a_command)
  win.bind("d",d_command)
  win.focus_set()
  canvas = tk.Canvas(win,width=495,height=495,bg='white')
  canvas.pack()
  canvas.create_text(70,15,text=f'Всего яблок сьедено:{apple_eat}',tag='text')
  canvas.create_text(405,15,text=f'Всего яблок до ускорения:5/{apple_eat}',tag='text_sp')
  snake()
  apple_com()
  movement_snake()
  tk.mainloop()
main()