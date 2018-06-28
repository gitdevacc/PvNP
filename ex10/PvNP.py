import sys
from game import Game

if __name__=="__main__":
    if len(sys.argv)==2:
        game=Game(sys.argv[1])
        game.place_wave()
        game.draw()
        game.get_input()
        while game.gameover==False:
            game.run_turn()
            if game.gameover==False:
                game.draw()
                game.get_input
        print("Game Over!!!")