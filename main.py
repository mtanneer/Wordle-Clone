from wordlist import *
import math,string,random,time,sys

def loading(a_list):
    #print "Loading..."
    #for i in range(len(a_list)):
    time.sleep(0.1)
    sys.stdout.write(u"\u001b[1000D") 
    sys.stdout.write(str(a_list))
    sys.stdout.flush()
    print()

if __name__ == '__main__' :
    count = 0
    count2 = 0
    a_list = list(string.ascii_lowercase)
    ans = random.choice(word_list)
    #ans = "speed"
    #print(ans)
    list_ans = list(ans)
    print("Enter a 5 letter word:")
    #sys.stdout.write(u"\u001b[B")
    while(1):
        #sys.stdout.write(u"\u001b[1000D") 
        # sys.stdout.write(u"\u001b["+ str(count2) +"A") 

        
        if(count == 6):
            print(u"Out of tries:( But the word was\u001b[32m %s\u001b[0m " % ans)
            break
        
        word = input()
        list_in = list(word)
        #sys.stdout.write(u"\u001b["+str(count2)+"A")
        sys.stdout.write(u"\u001b[A")
        
        #print(word)
        if(len(word) == 5):
            if(word not in word_list):
                count2 += 1
                print(word +" is not valid")
                continue  
            if(count):
                loading(a_list)
            count2 = 0
            for i in range(len(list_in)):
                if(list_in[i] == list_ans[i]):
                    print(u"\u001b[32m %s\u001b[0m" % list_in[i],end='')
                elif(list_in[i] in list_ans):
                    print(u"\u001b[33m %s\u001b[0m" % list_in[i],end='')
                else:
                    print(" %s" % list_in[i],end='')
                    if(list_in[i] in a_list):
                        a_list.remove(list_in[i])

            print("",end='\n')         
            
            if(word == ans):
                count += 1
                print("Congrats")
                break
            else:
                count += 1
                

        else:
            print("Word needs to exactly 5 letters long")
            continue
        #count2 += 1
        
        
        
            