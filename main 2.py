# This script is meant to take in 4 variables and return the number of additional people that can sit without violating social distancing protocals

# N = seats in the row 1 to N
# K = social distancing spaces
# M = number of current diners
# S = list[seat number of diners]
# 1 is pre-seated
# 9 is socially distanced
# 2 is newly placed

def getMaxAdditionalDinersCount(N, K, M, S):
    if N >= 1 and N <= 10 ** 15:
        if K >= 1 and K <= N:
            if M >= 1 and M <= 500000:
                if M <= N:
                    if min(S) >= 1 and max(S) <= N:
                        seats = []
                        count = 0
                        #The below code makes a list with 0s in empty spots and 1s in filled seats
                        for i in range(1,N+1):
                            if i in S:
                                seats.insert(i,1)
                            else:
                                seats.insert(i,0)
                        #prints 9s to the left
                        for j in range(0, len(S)):
                            a = 1
                            while a <= K:
                                if S[j] -1 - a >= 0:
                                    seats[S[j] -1 - a] = 9
                                a += 1
                        #print(seats)
                        #prints 9s to the right
                        for j in range(0, len(S)):
                            a = 1
                            while a <= K:
                                if S[j] -1 + a < len(seats):
                                    seats[S[j] -1 + a] = 9
                                a += 1
                        print(seats)
                        #Need to go through and add 2s signifying new people sitting down and their 9s
                        for i in range(0,len(seats)):
                            if seats[i] == 0:
                                seats[i] = 2
                                count += 1
                                a = 1
                                while a <= K:
                                    if i + a < len(seats):
                                        seats[i+a] = 9
                                    a += 1
                        print(seats)



                        return count
                    else:
                        return ("Does not meet constraints")
                else:
                    return ("Does not meet constraints")
            else:
                return ("Does not meet constraints")
        else:
            return ("Does not meet constraints")
    else:
        return ("Does not meet constraints")

print(getMaxAdditionalDinersCount(10, 1, 2, [2,6]))
print(getMaxAdditionalDinersCount(15, 2, 3, [11,6,14]))


