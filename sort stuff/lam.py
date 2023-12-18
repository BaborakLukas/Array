def optimal_lamps(s):
    n = len(s)
    res = ["O"] * n  
    off_count = 0  
    last_off = -1  
    for i in range(n):
        if s[i] == "X": 
            res[i] = "X"
            off_count = 0  
        elif i == 0 or i == n - 1:  
            off_count = 0 
        elif s[i-1] == "O" and s[i+1] == "O": 
            res[i] = "-"
            off_count += 1  
            last_off = i  
            if off_count >= 2:  
                res[last_off] = "-"
                off_count = 1  
                last_off = i  
        else:  
            off_count = 0  
    return "".join(res)


s = "OOOXOXOOOOOO"
print(optimal_lamps(s))