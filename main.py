import flower_shop as fs
import solo as fc


# initial setting
balance = 7500
round = int(input('Enter the number of operation months'))
for i in range(round):
    print(f'The {i+1} month operation\n')
    balance = fc.one_run(balance)
    i+=1
    print('---------------------------',end='\n')
print('final balance',balance)