import os

tr = 0

def main():
    global tr
    f = open("doc.txt","r")
    a = []
    count = 0
    for l in f:
        count += 1
        a.append(l)
    tr += 1
    rec = count
    c = str(a[-1])
    b = "OPEN PI\n"
    e = "WHAT IS YOUR NAME\n"
    f = "WHO ARE YOU\n"
    g = "WHERE IS RUET\n"
    h = "ABBREVIATION OF RUET\n"
    i = "WHO IS THE PRIME MINISTER OF BANGLADESH\n"
    ii = "WHO IS THE PRESIDENT OF BANGLADESH\n"
    j = "WHO IS THE CHANCELLOR OF RUET\n"
    k = "WHO IS THE VICE CHANCELLOR OF RUET\n"
    l = "WHO IS THE DEPARTMENT HEAD OF MTE\n"
    m = "WHO IS THE DEPARTMENT HEAD OF MECHATRONICS ENGINEERING\n"
    n = "WHO IS SHEIKH HASINA\n"
    o = "WHAT IS MECHATRONICS ENGINEERING\n"
    p = "TELL ME SOMETHING  ABOUT DIGITAL BANGLADESH\n"
    q = "WHAT DO YOU KNOW ABOUT MECHATRONICS ENGINEERING\n"
    r = "TELL ME SOMETHING  ABOUT DIGITAL BANGLADESH"
    s = "WHAT DO YOU KNOW ABOUT ENGINEERING\n"
    t = "WHAT IS ENGINEERING\n"
    u = "WHO IS THE VC OF RUET\n"
    v = "WHAT DO YOU EAT\n"
    w = "TELL ME YOUR FUNCTIONS\n"
    x = "WHAT ARE YOUR FUNCTIONS\n"
    y = "WHAT IS THE NAME OF VC OF RUET\n"
    z = "WHAT IS YOUR OPINION ABOUT BANGLADESHI POLITICS\n"
    aa = "HOW ARE YOU\n"
    ab = "WHEN DID BANGLADESH BECOME AN INDEPENDENT COUNTRY\n"
    ac = "DO YOU KNOW BANGABANDHU SHEIKH MUJIBOR RAHMAN\n"
    ad = "WHICH IS THE SECOND COUNTRY TO RECOGNIZE BANGLADESH\n"
    ae = "WHAT IS THE OFFICIAL NAME OF BANGLADESH\n"
    af = "WHO IS THE FOUNDER OF BANGLADESH\n"
    ag = "WHO WROTE THE NATIONAL ANTHEME OF BANGLADESH\n"
    ah = "WHAT IS THE CAPITAL OF BANGLADESH\n"
    ai = "WHICH DAY IS WEEKLY HOLIDAY IN BANGLADESH\n"
    aj = "WHAT IS THE CURRENCY USED IN BANGLAESH\n"
    ak = "WHAT IS THE NATIONAL GAME OF BANGLADESH\n"
    al = "WHAT IS THE TOTAL AREA OF BANGLADESH\n"
    am = "WHAT IS THE POPULATION OF BANGLADESH\n"
    an = "NATIONAL TREE IN BANGLADESH\n"
    ao = "WHAT IS THE NATIONAL FRUIT OF BANGLADESH\n"
    ap = "WHAT IS THE NATIONAL ANIMAL OF BANGLADESH\n"
    aq = "WHAT IS THE NAME OF NATIONAL PARLIAMENT OF BANGLADESH\n"
    ar = "ARE YOU INTELLIGENT\n"
    at = "HOW OLD ARE YOU\n"
    au = "WHAT IS YOUR SIZE\n"
    av = "CAN YOU STOP TIME\n"
    aw = "WHAT IS YOUR FAVOURITE COLOR\n"
    ax = "CAN YOU SING\n"
    ay = "CAN TOU DANCE\n"
    az = "WHAT IS YOUR FAVOURITE MOVIE\n"
    ba = "IS JOHN SNOW DEAD\n"
    bb = "WHAT IS YOUR SEX\n"
    bc = "WHAT IS YOUR GENDER\n"
    bd = "WHAT CAME FIRST CHICKEN OR EGG\n"
    be = "WHO IS THE FATHER OF NATION OF BANGLADESH\n"
    bf = "WHAT IS THE NATIONAL FLOWER OF BANGLADESH\n"
    bg = "WHAT IS THE MAIN REGION OF BANGLADESH\n"
    bh = "ON WHICH CONTINENT IS BANGLADESH LOCATED\n"
    if count == tr:
        con = True
        count = 0
    else:
        con = False
        count = 0
    if con :
        if c==e:
            os.system('echo "my name is mechatro" | festival --tts')
        elif c==f:
            os.system('echo "i am mechatro" | festival --tts')
        elif c==g:
            os.system('echo "ruet is located in rajshahi" | festival --tts')
        elif c==h:
            os.system('echo "rajshahi university of engineering and technilogy" | festival --tts')
        elif c==i:
            os.system('echo "honorable prime minister sheikh haasina" | festival --tts')
        elif c==ii or c==j:
            os.system('echo "president abdul hamid khan" | festival --tts')
        elif c==l or c==m:
            os.system('echo "professor doctor mohammad emdadul haque" | festival --tts')
        elif c==n:
            os.system('echo "honorable prime minister of bangladesh" | festival --tts')
        elif c == bh:
            os.system('echo "asia" | festival --tts')
        elif c == bg:
            os.system('echo "islam" | festival --tts')
        elif c == bf:
            os.system('echo "water lily" | festival --tts')
        elif c == be or c == af:
            os.system('echo "Bongobondgu sheikh mujibor rahman" | festival --tts')
        elif c == bc or c == bb or c == au or c == at or c == z:
            os.system('echo "it is not a mater of concern for me" | festival --tts')
        elif c == az:
            os.system('echo "my programmer forgotted to give me sight" | festival --tts')
        elif c == aw:
            os.system('echo "color is not a matter of concern for robot" | festival --tts')
        elif c == av:
            os.system('echo "my programmer always want me to do so" | festival --tts')
        elif c == ar:
            os.system('echo "your opinion about me is the answer" | festival --tts')
        elif c == aq:
            os.system('echo "jatio songsod" | festival --tts')
        elif c == ap:
            os.system('echo "royal bengal tiger" | festival --tts')
        elif c == ao:
            os.system('echo "jackfruit" | festival --tts')
        elif c == ak:
            os.system('echo "kabadi" | festival --tts')
        elif c == aj:
            os.system('echo "Bangladeshi taka" | festival --tts')
        elif c == ai:
            os.system('echo "Friday" | festival --tts')
        elif c == ah:
            os.system('echo "dhaka is the capital of bangladesh" | festival --tts')
        elif c == ag:
            os.system('echo "rabindranath tagoure" | festival --tts')
        elif c == ad:
            os.system('echo "it is bhutan" | festival --tts')
        elif c == ac:
            os.system('echo "yes. he is the founder of the bangladesh" | festival --tts')
        elif c == ab:
            os.system('echo "in 1971" | festival --tts')
        elif c == aa:
            os.system('echo "i am fine as long as i have power supplied" | festival --tts')
        elif c==y or c==u or c==k:
            os.system('echo "Professor doctor mohammad rofikul alam beg" | festival --tts')
        elif c==w or c==x:
            os.system('echo "i can sense movement, handshake with people and recognize voice and give a reply" | festival --tts')
        elif c==v:
            os.system('echo "i do not need to eat but i need electricity to stay online. from that point of view i eat electricity" | festival --tts')
        else:
            print("We are not done yet")
        
         
    else:
        print("We are not done yet")
    tr = rec

if __name__ == "__main__":
    while True:
        main()
