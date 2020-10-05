import fileinput

def xsat_3sat(SAT, n, nvars, x):
    aux = []
    for clause in SAT:
        if n==1: 
            aux.append([clause[0], nvars+1, nvars+2])
            aux.append([clause[0], nvars+1, -1*(nvars+2)])
            aux.append([clause[0], -1*(nvars+1), nvars+2])
            aux.append([clause[0], -1*(nvars+1), -1*(nvars+2)])
            nvars+=2
        elif n==2:
            aux.append([clause[0], clause[1], nvars+1])
            aux.append([clause[0], clause[1], -1*(nvars+1)])
            nvars+=1
        elif n==3:
            aux.append(clause)
        else:
            aux.append([clause[0], clause[1], nvars+1])
            for i in range(2, n-2):
                aux.append([ -1*(nvars+1), clause[i], nvars+2])
                nvars+=1
            aux.append([ -1*(nvars+1), clause[n-2], clause[n-1]])
            nvars+=1

    return xsat_increment(aux, 3, nvars, x)

def xsat_increment(SAT, n, nvars, x):
	
	aux = []
	
	for i in range(x - n):
		for j in range(len(SAT)):
			nvars += 1
			p = SAT[j][:]
			q = SAT[j][:]
			
			p.append(nvars)
			aux.append(p)
			
			q.append(-1 * nvars)
			aux.append(q)
			
		SAT = aux[:]
		aux = []
	
	return (SAT, nvars)

def reducer(SAT, nclauses, nvars, x):
	# assuming SAT is >= 3
	new_sat = []
	
	for clause in SAT:
		n = len(clause)
		if (x >= n):
			if (x >= 3): 
				res, vars_new = xsat_increment([clause], n, nvars, x)
			else:
				res, vars_new = xsat_3sat([clause], n, nvars, x)
		else:
			res, vars_new = xsat_3sat([clause], n, nvars, x)
		nvars = vars_new 
		for j in range(len(res)):
			new_sat.append(res[j])
	
	return (new_sat, len(new_sat), nvars)


def printDimacs(new_sat, nclauses, nvars):
	print("p cnf "+str(nvars)+" "+str(nclauses))
	out = ""
	for i in range(nclauses):
		for j in range(len(new_sat[i])):
			out += str(new_sat[i][j]) + " "
		out += str(0)
		out += "\n"
	print(out)

def main():
	
	nvars = 0
	nclauses = 0
	SAT = []
	x = 5
	for line in fileinput.input():
		if(line[0:5] == 'p cnf'):
			b = line.split()
			nvars = int(b[2])
			nclauses = int(b[3])
		elif(line[0] != "c"):
			l = line.split()
			c = [int(l[e]) for e in range(len(l) - 1)]
			SAT.append(c)

	# print(nvars, nclauses)
	# print(SAT)
	new_sat, nclauses, nvars = reducer(SAT, nclauses, nvars, x)
	printDimacs(new_sat, nclauses, nvars)

main()	