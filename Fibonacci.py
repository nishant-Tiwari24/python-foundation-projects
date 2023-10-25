def fibonnaci(n):
    if n<2:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)