# --------- 1st Promblem  solution -------------

y = int(input())

village_1_list=list(map(int,input().split(",")))
    
village_2_list =list(map(int,input().split(",")))

result_set = set(village_1_list) & set(village_2_list)

result_list = list(result_set)

print(result_list)

#-----------2nd problem-----------------------
    
nums_list = list(map(int,input().split(",")))
target = int(input())

for index1,num1 in enumerate(nums_list):
    #print(index,num)
    remaining_list = nums_list[index1+1:]
    num2 = target-num1 
    if num2 in remaining_list:
        result = [num1,num2]
        print(result)
        break

#------- 3rd problem ------------------- 


from itertools import permutations   

nums_list = [3,20,34,5,9]
l=len(nums_list)
permutations_list =[]
for p in permutations(nums_list,l):
    temp_char_list = map(str,p)
    permutations_list.append("".join(temp_char_list))

print(max(permutations_list))
    
#------- 4th problem -------------

n= int(input())

result_list = []

for i in range(1,n+1):
    if i % 15 ==0:
        result_list.append("FizzBuzz")
    elif i%3 ==0:
        result_list.append("Fizz")
    elif i%5 ==0:
        result_list.append("Buzz")
    else:
        result_list.append(i)

print(result_list)






