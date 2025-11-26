import flower_shop as fs
import solo as fc
print('---------------------------------------------------------------')
print('Welcome to the FlowerShop Simulator!')
print('---------------------------------------------------------------')
# initial setting
balance = 7500
round = int(input('How many months would you like to run the game for?'))
for i in range(round):
    print(f'\nMonth {i+1} \n')
    balance = fc.one_run(balance)
    i+=1
    print('---------------------------',end='\n')
print('final balance',balance)