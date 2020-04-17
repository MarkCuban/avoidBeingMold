def ismatch(s: str, p: str):
    ret = True
    j = 0
    i = 0
    ch = 0

    while i < len(p) and j < len(s):
        try:
            print('p[i] is ', p[i], ' ', s[j])
        except:
            pass    
        
        if (p[i] >= 'a' and p[i] <= 'z') or p[i] == '.':
            try:
                if p[i+1] == '*':
                    ch = p[i]
                else:
                    ch = 0
            except:
                pass
                
            if s[j] >= 'a' and s[j] <= 'z':
                if s[j] == p[i] or p[i] == '.':
                    if ch != 0:
                        while s[j] == p[i] or p[i] == '.':
                            if j < len(s)-1:
                                j += 1
                            else:
                                j += 1
                                break
                    else:
                        j += 1
                else:
                    if ch == 0:
                        ret = False
                        break
            else:
                ret = False
                break

            if ch == 0:
                pass  
            else:
                i += 2
                ch = 0
                continue
            
            i += 1

    if j != len(s):
        ret = False

    if i != len(p):
        ret = False

                             
    return ret

def prehandler(s, p):
    oring_p = p
    oring_s = s
    try:
        if p[0] == s[0] and p[1] != '*':
            while p[0] == s[0] and p[1] != '*':
                flag = True
                p = p[1:]
                s = s[1:]          
        if p[-1] == s[-1] and p[-1] != '*':
            while p[-1] == s[-1]:
                flag = True
                p = p[:-1]
                s = s[:-1] 
        return s, p
    except:
        return oring_s, oring_p

def reducepattern(p, i):

    j = 0
    ret = ''
    try:
        p_list = p.split('*')

        if len(p_list) > 1:
            for j in range(0, len(p_list)):
                if i == j:
                    if j != len(p_list) - 1:
                        tmp = p_list[j]
                        tmp = tmp[0:-1]
                        ret += p_list[j][:-1]
                    else:
                        ret = None
                else:
                    if j != len(p_list) - 1:
                        ret += p_list[j]
                        ret += '*'
                    else:
                        ret += p_list[j]
        else:
            ret = None
                  
    except:
        pass

    return ret

def isMatchWhile(s, p):

    orgin = p
    orgin_s = s
    idx = 0
    ret = False

    while True:
        s, p = prehandler(s, p)
        if s == None or p == None :
            if s == None and p == None:
                ret = True
                break       
        ret = ismatch(s, p)

        if ret == True:
            break
        else:
            p = reducepattern(orgin, idx)
            s = orgin_s
            idx += 1
            if s == None or p == None :
                break
    return ret
            




s = "aaa"
p = "a*a"

ret = isMatchWhile(s, p)
print('ret is ', ret)

