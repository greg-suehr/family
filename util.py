
def neat_display(rows):
    '''
    neat_display takes a list a tuples and prints a neat table

     pretty please give me tuples of the same size
    '''

    n_cols = len(rows[0])
    w_cols = [0] * n_cols

    # find the longest entry in each column
    for row in rows:
        for i in range(n_cols):
            if len(str(row[i])) > w_cols[i]:
                w_cols[i] = len(str(row[i]))

    # now print!
    for row in rows:
        for i in range(n_cols):
            print str(row[i]).ljust(w_cols[i]),  # TODO: figure out this magic,
        print
        
