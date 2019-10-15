import sys
import random
def primary():
  #print("Keep it logically awesome.")
  #f = open("quotes.txt",'w')
##  with open("qts.txt",'r+b') as f:
##    qts = f.readlines()
##    f.seek(0)
##    for qt in qts:
##      qt = f.read()
##      print(qt)
##      #qt='"'+qt+'"'
##      f.write(qt)   
##    #f.close()
  
  a = input('Enter your Quote: "')
  a = '"'+a+'"'
  print(type(a))
  b = input('Do You Want To add This Quote to your List ?')
  
  if b == 'Y' or b == 'y':
    with open("quotes.txt",'a+') as f:
      with open("qts.txt", 'a+') as f2:
        #f.write("\n")
        f.write("\n"+a)
##        f2.write("\n"+a)
        f.close()
##        f2.close()
        
  with open("quotes.txt",'r') as f:
    quotes = f.readlines()
    f.close()
    
  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.write(
  #f.close()
    
  last = len(quotes)
  #rnd = random.randint(0,last)
  #print(quotes[-1])
  #print(quotes[len(quotes)-1])
  #print(quotes[rnd])
  
  for i in range(last):
    #sys.stdout.write("QUOTE {}: {}".format(i+1,quotes[i]))# On Same line to print
    #sys.stdout.flush()                                    # Same use and used along with above line
    #print("QUOTE {}: {}".format(i+1,quotes[i]),end=" ",flush=True)
    print("QUOTE ",(i+1),": ",quotes[i],end='')
#    print()
##  print("\n======")
##  for i in range(len(qts)):
##    print("QUOTE ",(i+1),": ",qts[i],end='')
  

if __name__== "__main__":
  primary()
