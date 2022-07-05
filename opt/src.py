import time
N = pow(10,7)

# strat
start_time = time.perf_counter()

# IO
for _ in range(N):
    print('.', end='')
print('')

# end
end_time = time.perf_counter()

# print time
elapsed_time = end_time - start_time
print(elapsed_time)
