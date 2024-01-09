#this is the default page!
from mksGame import GoFish


def main():
  #menu function
  #let user choose a game to play
  choice = input("Please select a game to play: \n"
       + "GoFish")
  if choice == "GoFish":
    game = GoFish()
  

  
  #run the selected game
  game.run()
  



if __name__ == "__main__":
  main()