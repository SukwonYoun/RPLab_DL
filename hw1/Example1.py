#hw1 Ex1

def pair_count(input_list):
    count=0
    for i in range(0,len(input_list)-1):
        for j in range(i+1,len(input_list)):
            s1=set(input_list[i])
            s2=set(input_list[j])
            if len(s1 & s2)==2:
                count=count+1
            else:
                count=count+0

    return count
        
