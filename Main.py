from timeit import default_timer as timer
import Cases


def __main__():
    n = 10
    time = 0
    while time < 120:
        start = timer()
        #Cases.worstQCK(n)
        #Cases.worstINSRT(n)
        Cases.bestQCK(n)
        #Cases.bestINSRT(n)
        #Cases.avgQCK(n)
        #Cases.avgINSRT(n)
        end = timer()
        time = end - start
        print "La dimensione dell'array e': ", n
        print "Il tempo impiegato e': ", time
        n *= 10
        n = int(n)


if __name__ == __main__():
    __main__()
