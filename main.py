from wordlist import *
from PyDictionary import PyDictionary
import math,string,random,time,sys

dictionary=PyDictionary()

if __name__ == '__main__' :
    count = 0
    ans = random.choice(word_list)
    list_ans = list(ans)
    print("Enter a 5 letter word:")
    while(1):        
        if(count == 6):
            print(u"Out of tries:( But the word was\u001b[32m %s\u001b[0m\n " % ans)
            # print(dictionary.meaning(ans))
            break
        
        word = input()
        list_in = list(word)
        sys.stdout.write(u"\u001b[A")
        # if(list_in [0]== "-"):
        #     print(dictionary.meaning(ans))
        #     time.sleep(3.5)
        #     print ("\033[A                             \033[A")
        #     continue
        if(len(word) == 5):
            if(word not in word_list):
                print(word +" is not valid")
                time.sleep(1.5)
                print ("\033[A                             \033[A")
                continue  

            for i in range(len(list_in)):
                if(list_in[i] == list_ans[i]):
                    print(u"\u001b[32m %s\u001b[0m" % list_in[i],end='')
                elif(list_in[i] in list_ans):
                    print(u"\u001b[33m %s\u001b[0m" % list_in[i],end='')
                else:
                    print(" %s" % list_in[i],end='')

            print("",end='\n')         
            
            if(word == ans):
                count += 1
                print("Congrats\n")
                # print(dictionary.meaning(ans))
                break
            else:
                count += 1
                

        else:
            print("Word needs to exactly 5 letters long")
            time.sleep(1.5)
            print ("\033[A                                                    \033[A")
            continue
        #count2 += 1
        
        
        
            