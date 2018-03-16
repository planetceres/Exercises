def fn(prev_line):
    x_prev= None
    x_next = []
    count = 1
    last = len(prev_line)-1
    
    for i, x in enumerate(prev_line):
                    
        # Increment Count
        if x == x_prev:
            count += 1

        # Reset Count
        elif x_prev is not None:
            x_next.extend([count, x_prev])
            count = 1
        
        # If last index is reached append the count and current value
        if i == last:  
            x_next.extend([count, x])
            
        # Set the current x to be the previous x
        x_prev = x
        
    return x_next

iters = 10
prev_line = [1]
for i in range(0, iters):
    prev_line = fn(prev_line)
    print(prev_line)