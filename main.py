import flower_shop as fs
import solo as fc
import shop as sh
print('---------------------------------------------------------------')
print('Welcome to the FlowerShop Simulator!')
print('---------------------------------------------------------------')
# initial setting
balance = 7500
shop1 = sh.shop()
round = int(input('How many months would you like to run the game for?'))
for i in range(round):
    print(f'\nMonth {i+1} \n')
    balance,shop1 = fc.one_run(balance,shop1)
    i+=1
    print('---------------------------',end='\n')
print('*******************************')
print('Congratulations! You have completed the simulation!')
print('final balance',balance)