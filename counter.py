#This program prints the number of pairs in an array
from collections import Counter #I need this to count

pairs = [] #This list will hold the value a certain number/element occurs
            #this is the way I know to get number of pairs. Feel free to upgrade this
def  findNumOfPairs(my_array):
        count_my_array = Counter(my_array) #count the number of occurence of each element
        for v in count_my_array.values(): #loops through the values 
            get_each_pair = v//2         #divides each value and returns the actual result
            pairs.append(get_each_pair)  #all values go into list 'pairs'
    
number = (1,1,1,1,3,33,5,5,6,6,2,2,2,33,22,2,22,8,8,88,8,8,88,8) #array to work on
findNumOfPairs(number)
print(sum(pairs)) #print the sum of all the elements in pairs

