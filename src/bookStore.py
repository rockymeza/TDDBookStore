class BookStore(object):
    
    
    def __init__(self):
        pass

    
    def buy(self, counts):
        counts.sort()
        
        discount = [0.75, 0.8, 0.9, 0.95, 1]
        cost = counts[0] * 8 * 5 * 0.75  
        
        for index in range(1, 5):            
            cost += (counts[index] - counts[index - 1]) * 8 * (5 - index) * discount[index]
        
        return cost
            
    
    
    
    
    


