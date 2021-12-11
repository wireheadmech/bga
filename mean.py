def mean(value):
    if type(value) == dict:
      the_mean = sum(value.values()) / len(value)
    else:
      the_mean = sum(value) / len(value)
      
    return the_mean
  
# like  print(mean(your_cooked_value)
