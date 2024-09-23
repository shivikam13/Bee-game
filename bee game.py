import pgzrun,random 

WIDTH=600
HEIGHT=500
TITLE="BEE GAME"
bee=Actor('bee',(0,0))
bee.pos=150,150
flower=Actor("flower")
flower.pos=250,250
def draw():
   screen.blit("background",(0,0))
   bee.draw()
   flower.draw()

def draw():
   screen.blit('background',(0,0))
   bee.draw()
   flower.draw()
def update():      
   if keyboard.left:
      bee.x=bee.x-2
   if keyboard.right:
      bee.x=bee.x+2 


pgzrun.go()

