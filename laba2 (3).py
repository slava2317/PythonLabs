def out_even_number(max_number: int): # 1 задание
    for x in range(2,max_number,2):
        print(x, end = " ")
        
        
def calc_arithmetic_mean(lst: list): # 2 задание
    arithm_mean = 0
    for i in lst:
        arithm_mean += i
    arithm_mean /= len(lst)
    print(arithm_mean)


def find_shared_keys(first_dict: dict, second_dict: dict): # 3 задание
    for i in first_dict:
        if i in second_dict:
           print(
                f"shared key: {i}\n"
                f"Value in first dictionary: {first_dict[i]}\n"
                f"Value in second dictionary: {second_dict[i]}\n"
                )
           
           
def find_number_of_divisors(number: int): # 4 задание
    if number == 1:
        d = 1
    else:
        d = 2
        for i in range(2, int(number/2)+1): 
            if number % i == 0:
                d += 1
    print(d)
            
            
def find_shortest_word(lst: list): # 5 задание
    sh_word = len(lst[0])
    sh_index = 0
    for i in range(1,len(lst)):
        if len(lst[i]) < sh_word:
            sh_word = len(lst[i])
            sh_index = i
    print(lst[sh_index])
    
    
def delete_repetitive_elem(lst: list): # 6 задание
    lst_copy = set(lst)
    lst_copy = list(lst_copy)
    print(lst_copy)
    
    
def create_dict(max_number: int): # 7 задание
    dictionary = {k:k ** 2 for k in range(max_number)}
    print(dictionary)
    
    
def delete_in_tuple(tup: tuple): # 8 задание
    tmp = []
    for i in tup:
        if i % 3 != 0:
            tmp.append(i)
    tmp = tuple(tmp)
    print(tmp)
    
    
def check_sets(first_set: set, second_set: set): # 9 задание
    if first_set & second_set == first_set or first_set & second_set == second_set:
        print("Yes")
    else:
        print("No")
        
        
def out_numbers(max_number: int): # 10 задание
    for i in range(max_number,0,-1):
        print(i,end = " ")
        
        
if __name__ == "__main__":
    calc_arithmetic_mean([1,2,3])