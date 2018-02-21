import os

count = 0
tr = 0

def main():
	f = open("doc.txt","r")
	a = []
        for l in f:
            count++
            a.append(l)

        tr += 1
	rec = count
        c = str(a[-1])
        b = "whats up\n"

        if count == tr:
            con = True
            count = 0
        else:
            con = False
			count = 0

        if con :

            if c==b:
                os.system('echo "We are up sir" | festival --tts')

            else:
                print("We are not done yet")
        tr = rec

if __name__ == "__main__":
        while True:
                main()

