from wordlist import *
import math,string,random



if __name__ == '__main__' :
    count = 0
    ans = random.choice(word_list)
    # print(ans)
    list_ans = list(ans)
    print("Enter a 5 letter word:")
    while(1):
        if(count == 6):
            print(u"Out of tries:( But the word was\u001b[32m %s\u001b[0m " % ans)
            break

        word = input()
        if(word not in word_list):
            print("Word is not valid")
            continue
        list_in = list(word)

        if(len(word) == 5):
            for k in list_in:
               if(k in list_ans):
                   in_i = list_in.index(k)
                   ans_i = list_ans.index(k)
                   if(in_i == ans_i):
                       print(u"\u001b[32m %s\u001b[0m" % k,end='')
                   else:
                       print(u"\u001b[33m %s\u001b[0m" % k,end='')
               else:
                   print(" %s" % k,end='')
            print("",end='\n')         
            if(word == ans):
                count+=1
                print("Congrats")
                break
            else:
                count+=1
                # print("nope")

        else:
            print("Word needs to exactly 5 letters long")
            continue

        
        
        
            