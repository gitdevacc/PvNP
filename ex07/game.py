from linked_list import LinkedList
from queue import Queue
from stack import Stack
from wave import Wave
from non_plant import Non_Plant
from plant import Plant
from card import Card 
import random 
class Game:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.cash, self.height, self.width = [int(x) for x in f.readline().split(' ')]
            self.waves = LinkedList()
            self.waves_num = 0 #This is the amount of waves left, not current wave number
            for line in iter(f.readline, ''):
                self.waves.add(Wave(*[int(x) for x in line.split(' ')]))
                self.waves_num += 1
        self.board=Queue() #Incomplete, supposed to create Queue of width and height of read-in file
        addme={}
        for row in range(self.height):
            for column in range(self.width):
                addme.update({(row,column):None})
        self.board.enqueue(addme)
        self.gameover=False
        self.turn=0
        self.nonplants_amt=0
        self.deck=Stack() #Completish, please bugtest, supposed to initialize powerup card deck
        for i in range(100):
            self.deck.push(random.randint(0,5))
    def draw(self):
        print("Cash: $", self.cash, "\nWaves: ", self.waves_num, sep = '')
        s = ' '.join([str(i) for i in range(self.width - 1)])
        print(' ', s)
        for row in range(self.height):
            s = []
            for col in range(self.width):
                if self.is_plant(row, col):
                    char = 'P'
                elif self.is_nonplant(row, col):
                    size = self.board[row][col].size()
                    char = str(size) if size < 10 else "#"
                else:
                    char = '.'
                s.append(char)
            print(row, ' ', ' '.join(s), '\n', sep='')
    def is_nonplant(self,row, col):
        dict1=self.board[0]
        if isinstance(dict1[(row, col)], Non_Plant):
            return True
        else:
            return False
    def is_plant(self, row, col):
        dict1=self.board[0]
        if isinstance(dict1[(row, col)], Plant):
            return True
        else:
            return False
    def remove(self, row, col): #May need fixing 
        if self.is_nonplant(row, col):
            self.cash+=20
            dict1=self.board[0]
            del dict1[(row, col)]
            self.board[0]=dict1
        else:
            dict1=self.board[0]
            del dict1[(row, col)]
            self.board[0]=dict1
    def place_nonplant(self, row): #### FIX ME!!!
        new_nonplant=Non_Plant()
        dict1=self.board[0]
        dict1[(row, )]
    def place_plant(self, row, col):
        dict1=self.board[0]
        new_plant=Plant(35, 10)
        assert self.cash>=0
        self.cash-=new_plant.cost
        assert dict1[(row, col)]==None
        #Add functionality here to ensure that plants cannot be placed in rightmost column
    def place_wave(self):
        assert self.turn==self.waves_num*-1
        self.place_nonplant(self.waves.head.c.row)
        self.waves.head(self.waves.head.n)
        self.waves_num-=1
   





        
        
        