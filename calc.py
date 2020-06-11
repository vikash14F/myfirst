def add(x,y):
    if x>0 and y>0:
        print('Addition', x+y)

def sub(x,y):
    if x>y:
        print('substaction ',x-y)
    else:
        print('Invalid Substraciton')
        
def mul(x,y):
    if x>0 and y>0:
        print('Multiplication ',x*y)
    else:
        print
        
def div(x,y):
    if x>0 and y>0:
        print('Division ',x/y)
    else:
        print('Invalid Division')
        
x  =int(input('Enter 1st number\n'))
y = int(input('Enter 2nd number\n'))

action = int(input('Please Enter you action\n'))
if action >0 and action < 5:
    pass
else:
    print('Note: Invalid action. Dfault action addition is taken!')
    action = 1
    
    



def cal(x,y,action):
    if action == 1:
        add(x,y)
    if action == 2:
        sub(x,y)
    if action == 3:
        mul(x,y)
    if action == 4:
        div(x,y)


cal(x,y,action)
