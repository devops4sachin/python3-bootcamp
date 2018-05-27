import time


# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time() # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time # end time - start time
 
 
# SUMMING 10,000,000 Digits With List Comprehension 
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time


print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")

# Proof that Generator comprehensions are faster than the Lists comprehensions.

################# output ################
#C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\4_Iterators & Generators>python gen-expression-speed-test.py
#4999999950000000
#4999999950000000
#sum(n for n in range(10000000)) took: 10.355361938476562
#sum([n for n in range(10000000)]) took: 1111.1842634677887
