f = open("words.txt", "r")
text = f.read()
pre = text.split("\n")
for ele in pre:
    try:
         if(len(ele) == 7 and ele.):
            # if( 't' in ele or 's' in ele or 'n' in ele  ):
                if(ele[0] =='t' and ele[2]=='n' ):        
                    print(ele)
    except:
        print(" ")
