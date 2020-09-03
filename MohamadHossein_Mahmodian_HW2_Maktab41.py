import random

# chance = 10
# answer = random.randint(1,100)
# while True:
#     guess = input(f'Input your Guess "1 - 100" and {chance} chance left:')

#     if chance > 1:
#         try:
#             guess_type = type(eval(guess))
#             if guess_type == int:
#                 chance -= 1
#                 guess = int(guess)
#                 if guess == answer:
#                     print('**** You win :) ****')
#                     break

#                 elif guess > answer:
#                     print('Too High +')

#                 else:
#                     print('Too low -')

#             else:
#                 print(f'<<your entry is {guess_type.__name__} please give me integer>>')

#         except NameError:
#             print(f'<<your entry is string please give me integer>>')
#         print('')

#     else: 
#         print("No chance \nxxxx You lose :( xxxx")
#         break



# -------------------------------------------------------------------------------------
def range_test(start = 0, stop = 0 ,step = 1):
    range_list = []
    __generator = start

    if stop == 0 :
        __generator = 0
        stop = start
        while True:
            if __generator < stop: 
                range_list.append(__generator)
                __generator = __generator + step
            else: 
                break
        return range_list

    else:
        if start > stop :
            while True:
                if __generator != stop:
                    range_list.append(__generator)
                    __generator = __generator + step
                else: 
                    break
            return range_list
                    
        else:
            while True:
                if __generator < stop:
                    range_list.append(__generator)
                    __generator = __generator + step
                else: 
                    break
            return range_list            

print(range_test(4))
print(range_test(2,5))
print(range_test(5,10,2))
print(range_test(10,1,-3))