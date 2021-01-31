import math
 
MAX, MIN = 1000, -1000
 
def alphabeta(depth, idx, maximize, vals, alpha, beta): 
    if depth == int(math.log(len(vals), 2)): # checking if leaf node
        return values[idx] 
 
    if maximize: 
        best = MIN
        for i in range(0, 2): 
            val = alphabeta(depth + 1, idx * 2 + i, False, vals, alpha, beta) # calling next recursion
            best = max(best, val)  
            if best < beta : 
                alpha = max(alpha, best) # updating alpha value
        return best 
 
    else: 
        best = MAX
        for i in range(0, 2): 
            val = minimax(depth + 1, idx * 2 + i, True, vals, alpha, beta) # calling next recursion
            best = min(best, val) 
            if best > alpha: 
                 beta = min(beta, best) # updating beta  
        return best 
 
if __name__ == "__main__": 
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print(f"Result = {alphabeta(0, 0, True, values, MIN, MAX)}") 
