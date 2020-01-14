import  time
## This decorator mesure the time for a function to executed

def timeit(method):
    def timed(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()
        print(f"Time to Excute: {end - start}")
        return result
    return timed
