
def bin_to_dec(binary):
    numbers2 = []
    while binary > 0 :
        if binary % 2 ==0:
            numbers2.append("0")
        else: 
            numbers2.append("1")
        binary = binary//2
    numbers2.reverse()
    returner = "".join(numbers2)
    return(returner)


def dec_to_bin(x):
    y,i = 0,0
    while(x!=0):
        dec = x % 10
        y = y+dec *pow(2,i)
        x = x//10
        i+= 1
    return(y)

def ip_to_bin(ip2): 
    split = ip2.split(".")
    newsplit = []
    for number2 in split:
        number2 = int(number2)
        newsplit.append(bin_to_dec(number2))

    return ".".join(newsplit)

binip = ip_to_bin("255.255.255.255")
print(binip)



def ip_to_dec(ip10):
    split = ip10.split(".")
    newsplit = []
    for number10 in split:
        number10 = int(number10)
        newsplit.append(dec_to_bin(number10))
    
    return ".".join(newsplit)
decip = ip_to_dec("1111.1111.1111.1111")
print(decip)

# penis