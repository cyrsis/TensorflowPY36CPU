import multiprocessing

N_WORKERS = multiprocessing.cpu_count()

print("You have CPU core n ", N_WORKERS)
