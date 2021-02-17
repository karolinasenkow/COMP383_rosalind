from Bio.Seq import Seq


def file_opn(file):                 # opens input file, reads contents into a list, returns list
    f = open(file, 'r')
    itms = f.read().rstrip().split('\n')
    return itms


def split(item, k):             # splits the input item into designated k-mer size
    sp_itms = []
    for i in range(len(item) - k + 1):      # iterates over input item
        sp_itms.append(item[i:i + k])       # adds k-mer to list
    return sp_itms                      # returns list of split items (each of size of k-mer)



def splt_lst(items, k):         # integrates all splits items into a list of nodes
    nod = []
    if k == len(items[0]):
        return items[:]
    for itm in items:                   # for each DNA string
        for sp_itm in split(itm, k):        # split the DNA string and add k-mers to node list
            nod.append(sp_itm)
    return nod


def de_bruijn(spl_lst):         # constructs a de bruijn graph from k-mer list
    edg = []
    for j in rev_comp(spl_lst):         # produces a comprehensive list of k-mers by calling rev_comp()
        edg.append((j[0:-1],j[1:]))     # appends (itm[pre], item[suf])
    return (nodes(edg),edg)


def rev_comp(items):  # converts a a k-mer into its rev comp and produces a comprehensive list
    all_itms = set(items)                   # set avoids repeated nodes
    for i in items:
        rc = str(Seq(i).reverse_complement())
        if rc not in all_itms:          # adds rc to set if not currently in the set
            all_itms.add(rc)
    return all_itms


def nodes(edges):               # makes list of nodes from edges list made by de_bruijn()
    nods = []
    for (pre, suf) in edges:            # checks if prefix and suffix are in list of nodes and adds if they are not
        if pre not in nods:
            nods.append(pre)
        if suf not in nods:
            nods.append(suf)
    return nods


def run(edges):                 # traces through the edges present (preforming eularian walk)
    pre, suf = edges[0]             # prefix, suffix assigned first item in edges
    cyc = [pre]                     # current cycle will keep track of where in the de bruijn graph we are
    while len(suf) > 0:             # while there is a suffix, this loop runs
        cyc.append(suf)                     # now cycle = [pre,suf]
        edges.remove((pre, suf))            # removes [pre, suf] in the current cycle from edges
        pre, suf = neighbor(suf, edges)     # calls neighbor() with the suf (looks for where it is a prefix)
    return cyc, edges


def neighbor(cur_suf, edges):   # searches edges to where the current suffix is a prefix
    for pre, suf in edges:          # pulls new (pre, suf) from edges and compares pre to curr_suf
        if pre == cur_suf:          # searches for a match
            return pre, suf             # if match is found (another iteration is performed)
    else:
        return ([],[])              # if there are no matches --> breaks loop (because suf = [])


def euler_cycle(items):         # walks along all edges once and outputs shortest cycle
    min_cycle = None
    for k in range(len(items[0]),2,-1):     # iterates over different k-mer lengths (from k=len-1 to k=3)
        splt = splt_lst(items, k)               # calls splt_lst() function to split items by k-mer size
        nodes, edges = de_bruijn(splt)          # produces a de bruijn graph from split seqs

        while (len(edges) > 0):                   # moves through edges (removing them as it goes) until there are none
            curr_run, edges = run(edges)               # calls run() which does the edge tracing

            if curr_run[0] == curr_run[-1]:            # if eularian cycle is complete (init(pre,suf) == final(pre,suf))
                cycle = ''
                for r in curr_run[0:-1]:               # assembles superstring from current eularian cycle
                    cycle += r[0]

                if min_cycle == None or len(cycle) < len(min_cycle):    # tracks shortest superstring from a eularian cycle
                    min_cycle = cycle

        if min_cycle != None:       # if everything worked properly
            return min_cycle
    return 'Error: no cycles present'       # if things did not work properly


def output(out, cycle):         # writes edges of de_bruijn graph to output file
    o = open(out, "w")
    o.write(cycle)
    o.close()


# Driver code
items = file_opn('input.txt')

output('Rosalind_15_out.txt', euler_cycle(items))