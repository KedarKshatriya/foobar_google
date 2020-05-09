def solution(s):    
    right = 0
    sal = 0
    for l in s:
        if(l == '>'):
            right += 1
        if(l == '<' and right > 0):
            sal += 2 * right        
    return sal
