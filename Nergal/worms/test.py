from alive_progress import alive_bar
def compute():
    g = 0
    for i in range(1000000000000000000000000):
        g = g +1
        yield
with alive_bar(1000000000000000000000000) as bar:
    for i in compute():
        bar()
