
import lb
import turtle as trtl
import random as rand
leaderboard_file_name = "lb.txt"
player_name = input ("Please enter your name: ")
print("You made the leaderboard")
i=1
while(i==1):
  if(input("'start' to start: ")=="start"):
    i=0
color = "pink"
shape = "circle"
size = 2
def update_score(s):score_writer.clear();score_writer.write("Score: "+str(s+1), font=font_setup);return s
spot = trtl.Turtle()
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(150,150)
counter = trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-150,150)
font_setup = ("Arial", 20, "normal")
spot.shape(shape)
spot.shapesize(size)
spot.fillcolor(color)
spot.penup()
timer = 7
counter_interval = 1000
timer_up = False
s=7
def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 150)
  spot.goto(new_xpos,new_ypos)
def manage_leaderboard():

  global s
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or s >= int(leader_scores_list[4])):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, s)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, s)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, s)
def spot_clicked(x, y):
  global s
  global timer_up
  if(timer_up!=True):
    spot.hideturtle()
    change_position()
    update_score(s)
    s+=1
    spot.showturtle()
  else:
    spot.hideturtle()
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor("green")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()

































#import os
#os.system("cd jellyide&&python -m jellyide.jelly fun ../jelly.jel 'test'")
#int compression
#ḃ250ịØJ”“;;”’ṄV