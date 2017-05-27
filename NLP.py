import re
import sys
from collections import Counter

#matrix for sentence one
matrix1_unsmooth_count = [[0 for x in range(9)] for y in range(9)]
matrix1_add_1_smooth_count = [[0 for x in range(9)] for y in range(9)]
matrix1_good_turing_count = [[0 for x in range(9)] for y in range(9)]
matrix1_unsmooth_probability = [[0 for x in range(9)] for y in range(9)]
matrix1_add_1_smooth_probability = [[0 for x in range(9)] for y in range(9)]
matrix1_good_turing_probability = [[0 for x in range(9)] for y in range(9)]

#matrix for sentence two
matrix2_unsmooth_count = [[0 for x in range(10)] for y in range(10)]
matrix2_add_1_smooth_count = [[0 for x in range(10)] for y in range(10)]
matrix2_good_turing_count = [[0 for x in range(10)] for y in range(10)]
matrix2_unsmooth_probability = [[0 for x in range(10)] for y in range(10)]
matrix2_add_1_smooth_probability = [[0 for x in range(10)] for y in range(10)]
matrix2_good_turing_probability = [[0 for x in range(10)] for y in range(10)]

words = re.findall('\S+', open('corpus.txt').read())
c = (Counter(zip(words, words[1:])))

# unique word count
u = 0
yourtext =open('corpus.txt').read()
somecount = 0
#count of individual unique words
unique = Counter(yourtext.split())
V = len(Counter(yourtext.split()))
print("Unique Bigram Count of the corpus")
for count in c:
    print(count, c[count]) # List of bigram along with it's count

#sentence one
sen1 = "the president has relinquished his control of company's board."
sen1 = sen1.split(" ")
sen2 = []

for i in sen1:
    for j in sen1:
        sen2.append(i + " " + j)
counter = []
for i in sen2:
    counter.append(len(re.findall(i, open('corpus.txt').read())))

# sentence two
sen02 = "the chief executive officer said last year revenue was good."
sen02 = sen02.split(" ")
sen3 = []

for i in sen02:
    for j in sen02:
        sen3.append(i + " " + j)
counter2 = []
for i in sen3:
    counter2.append(len(re.findall(i, open('corpus.txt').read())))

print("\n")

print("Bigram Count for SENTENCE ONE")
print("\n")
print("Bigram count without smoothing")

k = 0
for i in range(9):
        for j in range(9):
            matrix1_unsmooth_count[i][j] = float("{0:4f}".format(counter[k]))
            k+=1
s = [[str(e) for e in row] for row in matrix1_unsmooth_count]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
print("\n")

print("Bigram count with add 1 smoothing")
k = 0
for i in range(9):
        for j in range(9):
            matrix1_add_1_smooth_count[i][j] = float("{0:4f}".format(((counter[k] + 1)*29326)/(29326 + V)))
            k+=1
s = [[str(e) for e in row] for row in matrix1_add_1_smooth_count]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
print("\n")

NC = Counter(counter)

print("Bigram count with good turing")

k = 0
for i in range(9):
        for j in range(9):
            matrix1_good_turing_count[i][j] = float("{0:4f}".format((((counter[k] + 1)*NC[counter[k]+1])/NC[counter[k]])))
            k+=1
s = [[str(e) for e in row] for row in matrix1_good_turing_count]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
print("\n")
print("\n")
this_word = len(re.findall("this", open('corpus.txt').read()))
print("\n")
################################################################################
# SENTENCE TWO
print("Bigram Count of SENTENCE TWO")
print("Bigram Count without smoothing")

k = 0
for i in range(10):
        for j in range(10):
            matrix2_unsmooth_count[i][j] = float("{0:4f}".format(counter2[k]))
            k+=1
s = [[str(e) for e in row] for row in matrix2_unsmooth_count]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
print("\n")

print("Bigram count with add 1 smoothing")
k = 0
for i in range(10):
        for j in range(10):
            matrix2_add_1_smooth_count[i][j] = float("{0:4f}".format(((counter2[k] + 1)*29326)/(29326 + V)))
            k+=1
s = [[str(e) for e in row] for row in matrix2_add_1_smooth_count]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
print("\n")

print(" Bigram count with good turing")
NC2 = Counter(counter2)
k = 0
for i in range(10):
        for j in range(10):
            matrix2_good_turing_count[i][j] = float("{0:4f}".format((((counter2[k] + 1)*NC2[counter2[k]+1])/NC2[counter2[k]])))
            k+=1
s = [[str(e) for e in row] for row in matrix2_good_turing_count]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
print("\n")
print("\n")

##############################################################
print("Bigram Probability of SENTENCE ONE")

print("Bigram probability without smoothing")
k=0
l=0
for i in sen1:
    for j in range(9):
        if unique[i] > 0:
            matrix1_unsmooth_probability[l][j]= float("{0:4f}".format(counter[k]/unique[i]))
        else:
            matrix1_unsmooth_probability[l][j] = 0
        k +=1
    l+=1
s = [[str(e) for e in row] for row in matrix1_unsmooth_probability]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))

print("\n")
print("Bigram probability with add 1 smoothing")

k=0
l=0
for i in sen1:
    for j in range(9):
        matrix1_add_1_smooth_probability[l][j]= float("{0:4f}".format((counter[k]+1)/(unique[i]+V)))
        k +=1
    l+=1
s = [[str(e) for e in row] for row in matrix1_add_1_smooth_probability]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))


N = 0
for i in NC:
    N += NC[i]
print("\n")

print("Bigram probability with good turing")
k = 0
for i in range(9):
        for j in range(9):
            matrix1_good_turing_probability[i][j] =  float("{0:4f}".format(matrix1_good_turing_count[i][j]/N))

s = [[str(e) for e in row] for row in matrix1_good_turing_probability]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))

print("\n")



###########################################################################################################
#Sentence TWO - PROBABILITY
print("Bigram Probability of SENTENCE TWO")
print("\n")
print("Bigram probability without smoothing")
k=0
l=0
for i in sen1:
    for j in range(10):
        if unique[i] > 0:
            matrix2_unsmooth_probability[l][j]= float("{0:4f}".format(counter2[k]/unique[i]))
        else:
            matrix2_unsmooth_probability[l][j] = 0
        k +=1
    l+=1
s = [[str(e) for e in row] for row in matrix2_unsmooth_probability]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
print("\n")
print("Bigram probability with add 1 smoothing")

k=0
l=0
for i in sen02:
    for j in range(10):
        matrix2_add_1_smooth_probability[l][j]= float("{0:4f}".format((counter2[k]+1)/(unique[i]+V)))
        k +=1
    l+=1
s = [[str(e) for e in row] for row in matrix2_add_1_smooth_probability]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))


N2 = 0
for i in NC2:
    N2 += NC2[i]
print("\n")

print("Bigram probability with good turing")
k = 0
for i in range(10):
        for j in range(10):
            matrix2_good_turing_probability[i][j] =  float("{0:4f}".format(matrix2_good_turing_count[i][j]/N2))

s = [[str(e) for e in row] for row in matrix2_good_turing_probability]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '      '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))

print("\n")
print("\n")

###########################################################################################################
print("Total probability of sentence ONE ")
print("\n")
tp = 1
for i in range(9):
    tp*= matrix1_unsmooth_probability[i][i]
print("P(Sentence without smothing) = ",tp)

tp = 1
for i in range(9):
    tp*= matrix1_add_1_smooth_probability[i][i]
print("P(Sentence with ADD-1 smothing) = ",tp)

tp = 1
for i in range(9):
    tp*= matrix1_good_turing_probability[i][i]
print("P(Sentence with Good-Turing) = ",tp)
############################################################################
print("\n")
print("\n")
print("Total probability of sentence TWO ")
print("\n")
tp = 1
for i in range(10):
    tp*= matrix2_unsmooth_probability[i][i]
print("P(Sentence without smothing) = ",tp)

tp = 1
for i in range(10):
    tp*= matrix2_add_1_smooth_probability[i][i]
print("P(Sentence with ADD-1 smothing) = ",tp)

tp = 1
for i in range(10):
    tp*= matrix2_good_turing_probability[i][i]
print("P(Sentence with Good-Turing) = ",tp)

