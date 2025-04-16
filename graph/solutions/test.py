def move_st(s, t, parent, adjacency_list):
    start = s
    stop = t
    if len(adjacency_list[stop]) == 1:
        stop = parent[stop]
        while len(adjacency_list[stop]) == 2:
            stop = parent[stop]
    print (start, stop)