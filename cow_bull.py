from posixpath import split


num=1420
num2=int(input("enter numbers of tries:"))
i=0
while i<num2:
    guess=int(input("enter your guess"))
    if len(str(guess))>len(str(num)):
        print("enter four digit number:")
    conguess=str(guess)
    f=list(conguess)
    conno=str(num)
    g=list(conno)
    if len(str(guess))<len(str(num)):
        print("enter four digit number")
    if len(str(guess))==len(str(num)):
        # conguess=str(guess)
        # f=list(conguess)
        # conno=str(a)
        # g=list(conno)
        cow=0
        bull=0
        j=0
        while j<len(f):
            if f[j] in g:
                 cow+=1
            if g[j]==f[j]:
                 bull+=1
            j+=1
        print(bull,"bull",cow,"cow")
    if f==g:
        print("you are winner")
        print("game finish")
        break
    i=i+1