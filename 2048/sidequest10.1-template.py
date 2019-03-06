#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    mat=[]
    for i in range(n):
        t=[]
        for i in range(n):
            t+=[0]
        mat+=[t]
    return  mat
def has_zero(mat):
    for item in mat:
        if 0 in item:
            return True
    return False
def add_two(mat):
    y=0
    temp=[]
    for item in mat:
        x=0
        for i in item:
            if i==0:
                temp+=[[x,y],]
            x+=1
        y+=1
    if len(temp)>0:
        print(temp)
        tempint=randint(0,len(temp)-1)
        final_x=temp[tempint][0]
        final_y=temp[tempint][1]
        mat[final_y][final_x]=1024
    return mat

###########
# Task 2  #
###########



def transpose(mat):
    temp=[]
    for i in range(len(mat[0])):
        temp+=[list(map(lambda x:x[i],mat)),]
    return temp
def not_adjacent(mat):
    for item in mat:
        for i in range(len(mat)-2):
            if item[i]==item[i+1]:
                return False
    for item in transpose(mat):
        for i in range(len(mat)-2):
            if item[i]==item[i+1]:
                return False
    return True
def game_status(mat):
    if 2048 in flatten(mat):
        return "win"
    elif not has_zero(mat) and not_adjacent(mat):
        return "lose"
    else:
        return "not over"
def transpose(mat):
    temp=[]
    for i in range(len(mat[0])):
        temp+=[list(map(lambda x:x[i],mat)),]
    return temp
###########
# Task 3b #
###########
def reverse_row(lst):
    new_row=[]
    for i in range(len(lst)-1,-1,-1):
        new_row+=[lst[i]]
    return new_row
def reverse(mat):
    return list(map(reverse_row,mat))

def merge_left_row(original_lst):
    n=len(original_lst)
    lst=[]
    new_lst=[]
    for i in original_lst:
        if i ==0:
            continue
        else:
            lst.append(i)    
    score_increment_row=[0]
    def helper(lst):
        for i in range(len(lst)):
            if lst[i]!=0:
                if i==len(lst)-1:
                    new_lst.append(lst[i])
                    return new_lst
                if lst[i+1]==lst[i]:
                    new_lst.append(lst[i]//2)
                    score_increment_row[0]+=2*lst[i]
                    return helper(lst[i+2:])
                if lst[i+1]!=lst[i]:
                    new_lst.append(lst[i])
                    return helper(lst[i+1:])
    if len(lst)!=0:
        helper(lst)
    new_lst.extend([0]*(n-len(new_lst)))
    return [new_lst,score_increment_row]
    
def merge_left(mat):
    new_mat=[]
    score_increment=0
    for item in mat:
        temp=merge_left_row(item)
        new_mat.append(temp[0])
        score_increment+=temp[1][0]
        if not new_mat==mat:
            is_valid=True
        else:
            is_valid=False
    return (new_mat,is_valid,score_increment)

def merge_right(mat):
    temp=(merge_left(reverse(mat)))
    return (reverse(temp[0]),temp[1],temp[2])
    
def merge_up(mat):
    temp=(merge_left(transpose(mat)))
    return (transpose(temp[0]),temp[1],temp[2])
def merge_down(mat):
    temp=(merge_right(transpose(mat)))
    return (transpose(temp[0]),temp[1],temp[2])

############
# Task 3ci #
############


###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
   
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print(mat)     
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return
def make_state(matrix, total_score):
    return [matrix,total_score]
def get_matrix(state):
    return state[0]
  
def get_score(state):
    return state[1]
def make_new_game(n):
    return make_state(add_two(add_two(new_game_matrix(n))),0)
def helper(f,state):
    temp=f(get_matrix(state))
    temp_score=get_score(state)
    if temp[1]:
        final_matrix=add_two(temp[0])
    else:
        final_matrix=temp[0]
    final_state=make_state(final_matrix,temp[2]+temp_score)
    return (final_state,temp[1])
    
def left(state):
    return helper(merge_left,state)
def right(state):
    return helper(merge_right,state)
def up(state):
    return helper(merge_up,state)
def down(state):
    return helper(merge_down,state)


# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer:
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return [matrix,total_score]
def get_matrix(state):
    return state[0]
  
def get_score(state):
    return state[1]
def make_new_game(n):
    return make_state(add_two(add_two(new_game_matrix(n))),0)
def helper(f,state):
    temp=f(get_matrix(state))
    temp_score=get_score(state)
    if temp[1]:
        final_matrix=add_two(temp[0])
    else:
        final_matrix=temp[0]
    final_state=make_state(final_matrix,temp[2]+temp_score)
    return (final_state,temp[1])
    
def left(state):
    return helper(merge_left,state)
def right(state):
    return helper(merge_right,state)
def up(state):
    return helper(merge_up,state)
def down(state):
    return helper(merge_down,state)



# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
gamegrid = GameGrid(game_logic)




