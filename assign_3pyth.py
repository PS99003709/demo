#isogram //
def isogram(word):
    lst = []
    for i in word:
        if i in lst:
            return False
        else:
            lst.append(i)
    return True

#ip string literal into integer literal // (ignore this)
def iptoint(ip):
    s = ""
    
    if type(ip) == str:
        res = ip.split(".")
        for i in res:
            s += i
        return int(s)
    elif type(ip) == int:
         lst = []
         n = ip
         while n > 0:
             if n%1000 > 255:
                 return 0
             else:
                 lst.append(n%1000)
                 n //= 1000
         for i in lst:
             s += str(i) + "."
         return s[::-1]

# ip address to integer

def ip_to_int_vice(st):
    if type(st) == str:
        lst = st.split('.')
        res, k = 0,3
        for i in lst:
            if int(i) <= 255:
                res += pow(256, k) * int(i)
                k -= 1
            else:
                return None
            
        return res
    elif type(st) == int:
        s = ""
        k = 3
        while k >=0:
            s += str((st // pow(256, k))%256) + "."
            k -= 1

        return s[:-1]


#frequency of message //
def word_frequency(message):
    d1 = {}
    for word in message.split(" "):
        if word not in d1:
            d1[word] = 1
        else:
            d1[word] += 1
    return d1

#largest by shuffling //
def lar_shuff(n):
    l1 = []
    num = 0
    while n > 0:
        rem = n % 10
        l1.append(rem)
        n //= 10
    l1.sort(reverse=True)
    k = len(l1)
    for i in l1:
        num += i*pow(10, k-1)
        k -= 1
    return num

        
#malformed time string //
def malf_time(tim_str):
    s = ""
    lst = tim_str.split(":")
    lst2 = []
    for i in lst:
        lst2.append(int(i))
    
    if lst2[2] >= 60:
        lst2[1] += lst2[2] // 60
        lst2[2] %= 60
    if lst2[1] >= 60:
        lst2[0] += lst2[1] // 60
        lst2[1] %= 60
    if lst2[0] > 23:
        return None
    
    for i in lst2:
        s += str(i) + ":"
    return s[:-1]


#malformed date string //
def mal_date(date_str):
    s = ""
    lst = date_str.split("/")
    lst2 = []
    for i in lst:
        lst2.append(int(i))
    if lst2[2] < 0 or lst2[2] > 9999:
        return None
    if lst2[1] > 12:
        lst2[2] += lst2[1] // 12
        lst2[1] %= 12
    if (lst2[0] > 30 and lst2[1] in [4,6,9,11]) or (lst2[0] > 31 and lst2[1] in [1,3,5,7,8,10,12]) or (lst2[0] > 28 and lst2[1] == 2):
        lst2[1] += lst2[0] // 30
        lst2[0] %= 30

    for i in lst2:
        s += str(i) + "/"
    return s[:-1]

    
#largest number by deleting the single digit //
def max_del(num):
    lst = []
    k = str(num)
    for c in k:
        lst.append(int(k.replace(c, '')))

    return max(lst)

#RGB TO HEX //
def rgb_to_hex(val):
    d1 = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    s = "0X"
    flag = 0
    for i in val:
        if i > 255:
            return None
        elif i == 0:
            s += "00"

        while i>0 and i < 256:
            if i < 16 and flag == 0:
                rem = i%16
                if rem >= 10:
                    s += "0" + d1[rem]
                else:
                    s+=  "0" + str(rem)
                i //= 16
            elif i < 256:
                flag = 1
                rem = i%16
                if rem >= 10:
                    s += d1[rem]
                else:
                    s+= str(rem)
                i //= 16
            
    return s

#RGB_TO_HEX using inbuilt function
def rgb_to_hex_inbuilt(val):
    s = "0X"
    for i in val:
        if i < 16:
            s += "0"
        s += hex(i)[2:]
    return s

#accumulated strings //
def accum_str(st):
    s = ""
    k = 0
    for c in st:
        s += c.upper() + c.lower()*k
        s += "-"
        k +=1 
    return s[:-1]

#mexican wave //
def mexican(st):
    lst = []
    for i in range(len(st)):
        c=st[:i].lower() + st[i].upper() + st[i+1:].lower()
        lst.append(c)
    return lst
        
