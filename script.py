from RandomWordGenerator import RandomWord
#import random
import time




class Script:

    
    def __init__(self):
        self.accuracy = 0
        self.time = 0
        self.times = []
        self.precisions = []

        print("Welcome to the Reaction Typer! ")
        time.sleep(0.2)
        playing = True 
        while playing: 
            self.number = input('Please type in the amount of words that you would like to type: ')
            if self.number == "/quit":
                break

            if self.table() == None:
                break

            self.table()
       

    def time_converter_string(self, sec):
        self.mins = sec // 60
        self.sec = sec % 60 
        self.string_times.append(self.sec)
        

    def time_converter(self, sec):
        seconds = sec % 60 
        self.times.append(round(seconds))
    
    def table(self):
        rw = RandomWord(max_word_size=20, constant_word_size=False)

        words = rw.getList(int(self.number))

        for i in words:
            print("-" * 6)
            print(i)
            print("-" * 6)
            self.string = i 
            time.sleep(0.2)
            start_time = time.time()
            prompt = input()
            end_time = time.time()

            if prompt == "/quit":
                break
            current_string_list = []
            user_prompted_words = []
            for k in i:
                current_string_list.append(k)

            for j in current_string_list:
                for l in prompt:
                    if l == j:
                        user_prompted_words.append(l)
                    prompt = prompt[1:]
                    break
                    
            
            precision = len(user_prompted_words) / len(current_string_list)
            self.precisions.append(precision * 100)

            
            time_difference = end_time - start_time
            self.time_converter(time_difference)
        
        self.ending()

    def ending(self):
        try:
            print("Here is the summary of your session: ")
            self.string_times = []
            for i in self.times:
                self.time_converter_string(i)
            dictionary = {key: value for key, value in zip(self.string_times, self.precisions)}

            sorted_times = self.merge_sort(self.times)
            fastest_time = sorted_times[0]
            slowest_time = sorted_times[-1]
            count = 1
            for k,l in dictionary.items():
                print("""Word no.{count}: 
                
                Time: {time} seconds
                Accuracy: {accuracy}%

                """.format(count=count, time=k, accuracy=l))
                count += 1
            
            for i in self.times:
                self.time += i
            for i in self.precisions:
                self.accuracy += i
            
            print("----------------------------------")
            print(""" 
            Total Session Summary: 

                Average Time Taken: {time} seconds
                Average Accuracy: {accuracy}%
                Fastest Time: {fast} seconds
                Slowest Time: {slow} seconds

                """.format(time=round(self.time / len(self.times)), accuracy=int(self.accuracy / len(self.precisions)), fast=fastest_time, slow=slowest_time))
        except IndexError:
            print("The user has quit the program! ")
            return 
            
    def merge_sort(self,lst):
        if len(lst) <= 1:
            return lst 
        else:
            middle_index = len(lst) // 2
            left_split = lst[:middle_index]
            right_split = lst[middle_index:]
            left_sorted = self.merge_sort(left_split)
            right_sorted = self.merge_sort(right_split)
            return self.merge(left_sorted, right_sorted)

    def merge(self,left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        if left:
            result += left 
        elif right:
            result += right 
        return result








test = Script()
print(test)
