#creating textfiles to store info
#history
f1=open("history.txt","w")
l=["The Kingdom of Sikkim was founded by the Namgyal dynasty in the 17th century.", \
   "It was ruled by Buddhist priest-kings known as the Chogyal.", \
   "It became a princely state of British India in 1890.", \
   "Following Indian independence, Sikkim continued its protectorate status with", \
   "the Union of India after 1947, and the Republic of India after 1950.", \
   "It enjoyed the highest literacy rate and per capita income among Himalayan states.", \
   "In 1973, anti-royalist riots took place in front of the Chogyal's palace.", \
   "In 1975, after the Indian Army took over the city of Gangtok, a referendum", \
   "was held that led to the deposition of the monarchy and Sikkim joining India as its 22nd state."]
for i in l:
    f1.write(i)
    f1.write("\n")
f1.close()
#geography
f2=open("geography.txt","w")
l1=["Nestling in the Himalayan mountains, the state of Sikkim is characterised by mountainous terrain.", \
   "Almost the entire state is hilly, with an elevation ranging from 280 metres (920 ft) in the south ", \
   "at border with West Bengal to 8,586 metres (28,169 ft) in northern peaks near Nepal and Tibet.",\
   "It borders the Tibet Autonomous Region of China in the north and northeast, Bhutan in the east,",\
   "Nepal in the west, and West Bengal in the south. Sikkim is also close to India's Siliguri Corridor",\
   "near Bangladesh. A part of the Eastern Himalaya, Sikkim is notable for its biodiversity,",\
   "including alpine and subtropical climates, as well as being a host to Kangchenjunga,",\
   "the highest peak in India and third highest on Earth."]

for i in l1:
    f2.write(i)
    f2.write("\n")
f2.close()
#arts&crafts
f3=open("artscrafts.txt","w")
l2=["There are a plenty of art and craft forms in Sikkim.",\
   "The bulk of the people of the state belong to rural areas ",\
   "and they have their old tradition of making several utility objects. ",\
   "One of the most popular handicraft objects of Sikkim includes a ",\
   "choksee table, woolen carpet, canvas wall hanging, thankas ",\
   "delineating painting on various aspects of the state.",\
   "The state has various handicrafts in the form of cane and bamboo products. ",\
   "Melli, Gangtok, and Namchi are the very popular places of Sikkim for",\
   "handloom products and cottage industries.",\
   "The people of Sikkim are pro when it comes to craft making as they have ",\
   "very special skills in the same. The womenfolk of the state are amazing weavers",\
   "and they attract the tourists by their excellent craft work. ",\
   "The handmade carpets and papers of the state are in huge demand in and outside of Sikkim."]

for i in l2:
    f3.write(i)
    f3.write("\n")
f3.close()
#music&dance
f4=open("musicdance.txt","w")
l3=["Folk songs and dances are an inveterate part of the Sikkimese culture.",\
   "Most of the tribal dances depict the harvest season and they are performed for prosperity. ",\
   "The dances of Sikkim are accompanied by traditional musical instruments, chanting,",\
   "and the dancers carry bright costumes and traditional masks. ",\
   "Some of the most famous dance forms are"]
for i in l3:
    f4.write(i)
    f4.write("\n")
f4.close()

#variousdances
f5=open("luk.txt","w")
l4=["Lu Khangthamo is a Bhutia folk dance that is celebrated to ",\
   "thank all the Gods and deities of the three worlds (heaven, hell and earth).",\
   "This form of dance is enjoyed by all age groups in their traditional dresses ",\
   "and ornaments. On occasions like house-warming and New Year celebrations, ",\
   "this dance is performed in the company of pleasing songs and music."]
for i in l4:
    f5.write(i)
    f5.write("\n")
f5.close()

f6=open("rch.txt","w")
l5=["Rechungma is a kind of typical Sikkimese dance that is performed to show",\
   "gratitude towards God for his continued blessings. It is usually arranged",\
   "on occasions like childbirth, marriage and other social gatherings."]
for i in l5:
    f6.write(i)
    f6.write("\n")
f6.close()

f7=open("mar.txt","w")
l6=["Maruni is one of the most popular and the oldest dance of the Nepalese.",\
    "This festival is also correlated with Diwali or Festival of Lights.",\
    "This beautiful dance is also performed on marriages. ",\
    "Maruni dancers attire in multi-colored costumes and heavy ornaments"]
for i in l6:
    f7.write(i)
    f7.write("\n")
f7.close()

f8=open("limboo.txt","w")
l7=["Limboo or Subba is a traditional folk dance of the Sikkimese.",\
    "In this dance, the dancers hang the 'Chyap-brungs', ",\
    "a musical instrument around their necks. The drum is beaten with ",\
    "a palm on one side and with a stick on the other side. ",\
    "The fancy trick creates two different sounds. ",\
    "The dance comprises of complex footwork that is tuned with the beats of Chyap-Brung. "]
for i in l7:
    f8.write(i)
    f8.write("\n")
f8.close()

#food
f9=open("food.txt","w")
l8=["The food of the people of Sikkim indicates the culture of this state which is",\
    "a mélange of India, Nepal, Bhutan, and Tibet. ",\
    "Sikkim food mainly comprises noodles, Gundruk and Sinki soups,",\
    "thukpas, tomato achar pickle, traditional cottage cheese, fermented soybean, ",\
    "Bamboo shoot, fermented rice product and some other fermented dishes ",\
    "owing to its very cold climate. Rice is, however, the staple food of the state.",\
    "Momos, also known as dumplings and wantons are favorites among the ",\
    "Sikkimese people as well as the tourists. When it comes to non-vegetarian food, ",\
    "they prefer fish, beef, and pork. Steamed and boiled food items are",\
    "mainly found here with not so much utilization of masalas but other local spices and herbs.",\
    "And the people of Sikkim mostly prefer some drinks along",\
    "with the food such as local beer, whiskey, and rum."]
for i in l8:
    f9.write(i)
    f9.write("\n")
f9.close()

#festivals
f10=open("festivals.txt","w")
l9=["Sikkim is a state in northeast Asia where numerous festivals are celebrated throughout the year. ",\
    "Majority of the people of Sikkim follow Buddhism so the festival celebrated here are associated ",\
    "with the Buddhist and they are celebrated with a lot of pomp and as per the Buddhist calendar.",\
    "Some of the most popular festivals, notable in Sikkim are as follows:"]
for i in l9:
    f10.write(i)
    f10.write("\n")
f10.close()

#various festivals
f11=open("saga.txt","w")
l10=["A triple favored celebration, Saga Dawa is reckoned as one of the godliest festivals",\
     "in Sikkim especially for the Mahayana Buddhists. On this particular day, ",\
     "the Buddhists visit the monasteries, offer the prayers and butter lamps ",\
     "as they were the three remarkable events associated with the existence of Buddha ",\
     "which is celebrated at this event. This particular is held on the full moon of the",\
     "4th month of the Buddhist calendar either at the end of May or at the beginning of June.",\
     "This festival takes place in Gangtok."]
for i in l10:
    f11.write(i)
    f11.write("\n")
f11.close()

f13=open("phang.txt","w")
l12=["Phang Lhabsol is one of the most unique festivals of Sikkim, ",\
     "was made renowned by ChakdorNamgyal, the 3rd ruler of Sikkim. ",\
     "This festival involves worshipping Mount Kanchendzonga ",\
     "and devoting for its uniting powers."]
for i in l12:
    f13.write(i)
    f13.write("\n")
f13.close()

f14=open("dasain.txt","w")
l13=["It is the main festival of Hindu Nepalese in Sikkim ",\
    "The celebration of this festival signifies the victory of good over evil. ",\
    "The elder people of the family apply “Tika” to younger people ",\
    "and give them their blessings."]

for i in l13:
    f14.write(i)
    f14.write("\n")
f14.close()

f15=open("tihaar.txt","w")
l14=["The Tihaar Festival is another exciting festival of Sikkim",\
     "that is celebrated as the festival of lights ","which is somewhat like Diwali."]

for i in l14:
    f15.write(i)
    f15.write("\n")
f15.close()

f16=open("hb.txt","w")
l15=["Hee Bermiok is an annual festival which is celebrated in Hee Bermiok city.",\
     "This city is located nearby Gangtok. This festival started in 2005",\
     "and the uncountable number of people comes to this beautiful city ",\
     "to join this amazing carnival. The festival takes place","in the month of May every year"]

for i in l15:
    f16.write(i)
    f16.write("\n")
f16.close()

#language
f17=open("lang.txt","w")
l16=["Nepali is the primary language of Sikkim while Lepcha and Sikkimese (Bhutia)",\
     "are also spoken in some part of this north-east province. ",\
     "English is also spoken by the people of Sikkim. Other languages include",\
     "Kafle, Limbu, Majhwar, Yakha, Tamang, Tibetan, and Sherpa."]

for i in l16:
    f17.write(i)
    f17.write("\n")
f17.close()

#funfacts
f18=open("ffacts.txt","w")
l17=["1. Lepcha (a primitive group of people in Sikkim) worships nature as their gods.",\
     "2. There are 11 official languages in Sikkim but the majority speak the Nepali language.",\
     "3. Sikkim is India’s first organic state.",\
     "4. Sikkim is the second-largest producer of Cardamom in the world.",\
     "5. Sikkim is India’s first open defecation free state.",\
     "6. Sikkim is India’s least populates state.",\
     "7. Almost 35 species of Rhododendron are found in Sikkim.",\
     "8. A festival called ‘Phang Lhabsol’ is celebrated as a thanksgiving to Mt. Kanchenjunga as a mountain deity.",\
     "9. Sikkim is home to the World’s third highest peak Mt.Kamchenjunga which is at a height of 8,586 m from sea level.",\
     "10.  Sikkim has the number of hot springs, rich in sulfur which works as a medicine for various skin diseases."]
for i in l17:
    f18.write(i)
    f18.write("\n")
f18.close()
    
#setting up tkinter windows
def cont():
    lvl.destroy()
    top=tk.Tk()
    top.geometry("804x350")
    top.config(bg="gainsboro")
    h="To enter the world of Sikkim, choose an option"
    mss=tk.Label(top,text=h)
    mss.configure(bg="steelblue",fg="white",justify="left",font=("Poor Richard",28),relief="sunken")
    mss.place(x=0,y=0)
    b1=tk.Button(top,text="History",command=history,bg="lightsteelblue",font=("times",15),width=12,height=1)
    b2=tk.Button(top,text="Geography",command=geography,bg="powderblue",font=("times",15),height=1,width=12)
    b3=tk.Button(top,text="Arts & Crafts",command=artscraft,bg="skyblue",font=("times",15),height=1,width=12)
    b4=tk.Button(top,text="Music & Dance",command=musicdance,bg="lightblue",font=("times",15),height=1,width=12)
    b5=tk.Button(top,text="Food",command=food,bg="paleturquoise",font=("times",15),height=1,width=12)
    b6=tk.Button(top,text="Festivals",command=festival,bg="mediumturquoise",font=("times",15),height=1,width=12)
    b7=tk.Button(top,text="Language",command=lang,bg="mediumaquamarine",font=("times",15),height=1,width=12)
    b8=tk.Button(top,text="Fun Facts",command=ff,bg="mediumseagreen",font=("times",15),height=1,width=12)
    b1.place(x=10,y=70)
    b2.place(x=205,y=70)
    b3.place(x=400,y=70)
    b4.place(x=600,y=70)
    b5.place(x=10,y=170)
    b6.place(x=205,y=170)
    b7.place(x=400,y=170)
    b8.place(x=600,y=170)
    bu=tk.Button(top,text="Exit",command=top.destroy)
    bu.configure(height=3,width=20,font=("times",10))
    bu.place(x=300,y=270)

    
def history():
    global ph2
    his=tk.Toplevel()
    his.geometry("1366x650")
    his.title("History")
    ph2=tk.PhotoImage(file="his1.png")
    l1=tk.Label(his,image=ph2)
    l1.place(x=0,y=0)
    e1=open("history.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(his,text=b)
    l1.configure(bg="lightsteelblue",fg="black",justify="center",font=("Poor Richard",20))
    l1.place(x=120,y=100)
    b1=tk.Button(his,text="Back",command=his.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=500)

def geography():
    global ph23
    geo=tk.Toplevel()
    geo.geometry("1366x650")
    geo.title("Geography")
    ph23=tk.PhotoImage(file="geo.png")
    l1=tk.Label(geo,image=ph23)
    l1.place(x=0,y=0)
    e1=open("geography.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(geo,text=b)
    l1.configure(bg="white",fg="black",justify="center",font=("Poor Richard",20))
    l1.place(x=120,y=100)
    b1=tk.Button(geo,text="Back",command=geo.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=500)
def artscraft():
    global ph3
    ac=tk.Toplevel()
    ac.geometry("1366x650")
    ac.title("Arts and Crafts")
    ph3=tk.PhotoImage(file="arts.png")
    l1=tk.Label(ac,image=ph3)
    l1.place(x=0,y=0)
    e1=open("artscrafts.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(ac,text=b)
    l1.configure(bg="darkorange",fg="black",justify="center",font=("Poor Richard",20))
    l1.place(x=120,y=10)
    b1=tk.Button(ac,text="Back",command=ac.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=550)
def musicdance():
    global ph3
    md=tk.Toplevel()
    md.geometry("1366x650")
    md.title("Music and dance")
    ph3=tk.PhotoImage(file="dance.png")
    l1=tk.Label(md,image=ph3)
    l1.place(x=0,y=0)
    e1=open("musicdance.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(md,text=b)
    l1.configure(bg="lightsalmon",fg="black",justify="center",font=("Poor Richard",20))
    l1.place(x=150,y=40)
    b1=tk.Button(md,bg="lightsalmon",text="Back",command=md.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=550)
    b2=tk.Button(md,bg="lightsalmon",text="Lu Khangthamo",command=lk ,font=("Fixedsis",20))
    b2.place(x=20,y=350)
    b3=tk.Button(md,bg="lightsalmon",text="Rechungma",command=ra,font=("Fixedsis",20))
    b3.place(x=420,y=350)
    b4=tk.Button(md,bg="lightsalmon",text="Maruni",command=ma,font=("Fixedsis",20))
    b4.place(x=820,y=350)
    b5=tk.Button(md,bg="lightsalmon",text="Limboo",command=lo,font=("Fixedsis",20))
    b5.place(x=1220,y=350)

def lk():
    global p
    lk=tk.Toplevel()
    lk.geometry("1366x650")
    lk.title("Lu Khangthamo")
    p=tk.PhotoImage(file="los.png")
    l1=tk.Label(lk,image=p)
    l1.place(x=0,y=0)
    e1=open("luk.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(lk,text=b)
    l1.configure(bg="teal",fg="black",justify="center",font=("Poor Richard",24))
    l1.place(x=70,y=40)
    b1=tk.Button(lk,text="Back",command=lk.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=550)

def ma():
    global p
    ma=tk.Toplevel()
    ma.geometry("1366x650")
    ma.title("Maruni")
    p=tk.PhotoImage(file="mar.png")
    l1=tk.Label(ma,image=p)
    l1.place(x=0,y=0)
    e1=open("mar.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(ma,text=b)
    l1.configure(bg="chocolate",fg="white",justify="center",font=("Poor Richard",26))
    l1.place(x=70,y=160)
    b1=tk.Button(ma,text="Back",command=ma.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=550)

def lo():
    global p
    lo=tk.Toplevel()
    lo.geometry("1366x650")
    lo.title("Limboo")
    p=tk.PhotoImage(file="lo.png")
    l1=tk.Label(lo,image=p)
    l1.place(x=0,y=0)
    e1=open("limboo.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(lo,text=b)
    l1.configure(bg="firebrick",fg="black",justify="center",font=("Poor Richard",24))
    l1.place(x=30,y=100)
    b1=tk.Button(lo,text="Back",command=lo.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=550)


def ra():
    global p
    ra=tk.Toplevel()
    ra.geometry("1366x650")
    ra.title("Rechungma")
    p=tk.PhotoImage(file="rch.png")
    l1=tk.Label(ra,image=p)
    l1.place(x=0,y=0)
    e1=open("rch.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(ra,text=b)
    l1.configure(bg="darkblue",fg="white",justify="center",font=("Poor Richard",26))
    l1.place(x=70,y=160)
    b1=tk.Button(ra,text="Back",command=ra.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=550)


def food():
    global pf
    print()
    fd=tk.Toplevel()
    fd.geometry("1366x650")
    fd.title("Food")
    pf=tk.PhotoImage(file="food.png")
    l1=tk.Label(fd,image=pf)
    l1.place(x=0,y=0)
    e1=open("food.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(fd,text=b)
    l1.configure(bg="linen",fg="black",justify="center",font=("Poor Richard",20))
    l1.place(x=150,y=10)
    b1=tk.Button(fd,text="Back",command=fd.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=550)

def festival():
    global ph5
    fl=tk.Toplevel()
    fl.geometry("1366x650")
    fl.title("Festival")
    ph5=tk.PhotoImage(file="fest.png")
    l1=tk.Label(fl,image=ph5)
    l1.place(x=0,y=0)
    e1=open("festivals.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(fl,text=b)
    l1.configure(bg="khaki",fg="black",justify="center",font=("Poor Richard",22))
    l1.place(x=20,y=40)
    b1=tk.Button(fl,text="Back",command=fl.destroy,font=("Fixedsis",20),bg="white",relief="sunken")
    b1.place(x=650,y=550)
    b2=tk.Button(fl,text="Saga",command=sg ,font=("Fixedsis",20),bg="navajowhite",relief="sunken")
    b2.place(x=200,y=350)
    b3=tk.Button(fl,text="Phang",command=pg,font=("Fixedsis",20),bg="navajowhite",relief="sunken")
    b3.place(x=400,y=350)
    b4=tk.Button(fl,text="Dasain",command=dn,font=("Fixedsis",20),bg="navajowhite",relief="sunken")
    b4.place(x=600,y=350)
    b5=tk.Button(fl,text="Tihaar",command=tr,font=("Fixedsis",20),bg="navajowhite",relief="sunken")
    b5.place(x=800,y=350)
    b6=tk.Button(fl,text="Hee Bermoik",command=hb,font=("Fixedsis",20),bg="navajowhite",relief="sunken")
    b6.place(x=1000,y=350)
def sg():
    global s
    sg=tk.Toplevel()
    sg.geometry("1000x650")
    sg.title("Saga")
    s=tk.PhotoImage(file="saga.png")
    l1=tk.Label(sg,image=s)
    l1.place(x=0,y=0)
    e1=open("saga.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(sg,text=b)
    l1.configure(bg="beige",fg="black",justify="center",font=("Poor Richard",18))
    l1.place(x=10,y=50)
    b1=tk.Button(sg,text="Back",command=sg.destroy,font=("Fixedsis",20))
    b1.place(x=450,y=550)
def pg():
    global g
    pg=tk.Toplevel()
    pg.geometry("1000x650")
    pg.title("Phang")
    g=tk.PhotoImage(file="phang.png")
    l1=tk.Label(pg,image=g)
    l1.place(x=0,y=0)
    e1=open("phang.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(pg,text=b)
    l1.configure(bg="saddlebrown",fg="black",justify="center",font=("Poor Richard",24))
    l1.place(x=0,y=50)
    b1=tk.Button(pg,text="Back",command=pg.destroy,font=("Fixedsis",20))
    b1.place(x=450,y=550)
def dn():
    global n
    dn=tk.Toplevel()
    dn.geometry("1000x650")
    dn.title("Dasain")
    n=tk.PhotoImage(file="dasain.png")
    l1=tk.Label(dn,image=n)
    l1.place(x=0,y=0)
    e1=open("dasain.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(dn,text=b)
    l1.configure(bg="coral",fg="black",justify="center",font=("Poor Richard",23))
    l1.place(x=20,y=70)
    b1=tk.Button(dn,text="Back",command=dn.destroy,font=("Fixedsis",20))
    b1.place(x=450,y=550)

def tr():
    global r
    tr=tk.Toplevel()
    tr.geometry("1000x650")
    tr.title("Tihaar")
    r=tk.PhotoImage(file="tihaar.png")
    l1=tk.Label(tr,image=r)
    l1.place(x=0,y=0)
    e1=open("tihaar.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(tr,text=b)
    l1.configure(bg="sienna",fg="white",justify="center",font=("Poor Richard",28))
    l1.place(x=10,y=70)
    b1=tk.Button(tr,text="Back",command=tr.destroy,font=("Fixedsis",20))
    b1.place(x=450,y=550)

def hb():
    global r
    hb=tk.Toplevel()
    hb.geometry("1000x650")
    hb.title("Hee Bermoik")
    r=tk.PhotoImage(file="hbb.png")
    l1=tk.Label(hb,image=r)
    l1.place(x=0,y=0)
    e1=open("hb.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(hb,text=b)
    l1.configure(bg="yellow",fg="black",justify="center",font=("Poor Richard",21))
    l1.place(x=15,y=70)
    b1=tk.Button(hb,text="Back",command=hb.destroy,font=("Fixedsis",20))
    b1.place(x=450,y=550)



def lang():
    global pfg
    print()
    lg=tk.Toplevel()
    lg.geometry("1366x650")
    lg.title("Language")
    pfg=tk.PhotoImage(file="lang1.png")
    l1=tk.Label(lg,image=pfg)
    l1.place(x=0,y=0)
    e1=open("lang.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(lg,text=b)
    l1.configure(bg="peru",fg="black",justify="center",font=("Poor Richard",26))
    l1.place(x=50,y=100)
    b1=tk.Button(lg,text="Back",command=lg.destroy,font=("Fixedsis",20))
    b1.place(x=650,y=550)
def ff():
    global pffg
    print()
    ff=tk.Toplevel()
    ff.geometry("1366x650")
    ff.title("Fun Facts")
    pffg=tk.PhotoImage(file="ff.png")
    l1=tk.Label(ff,image=pffg)
    l1.place(x=0,y=0)
    e1=open("ffacts.txt","r")
    a=e1.readlines()
    b=""
    for i in range (len(a)):
        b=b+a[i]
    l1=tk.Label(ff,text=b)
    l1.configure(bg="darkseagreen",fg="black",justify="left",font=("Poor Richard",16))
    l1.place(x=90,y=80)
    b1=tk.Button(ff,text="Back",command=ff.destroy,font=("Fixedsis",20),relief="sunken")
    b1.place(x=650,y=550)
    
      
    
import tkinter as tk
lvl=tk.Tk()
lvl.title("WELCOME")
lvl.geometry("705x440")
ph=tk.PhotoImage(file="pic1.png")
l=tk.Label(lvl,image=ph)
l.place(x=0,y=0)
fr=tk.Frame(lvl,width=350,height=58)
fr.place(x=185,y=90)
hi="Welcome to Sikkim"
l1=tk.Label(fr,text=hi)
l1.configure(bg="lightsteelblue",fg="black",justify="center",font=("Poor Richard",28))
l1.place(x=0,y=0)
fr3=tk.Frame(lvl,width=185,height=140)
fr3.place(x=250,y=200)
butt1=tk.Button(fr3,text="Continue",command=cont)
butt1.configure(height=3,width=20,bg="darkolivegreen",fg="white",font=("times",10))
butt1.place(x=0,y=0)
butt2=tk.Button(fr3,text="Exit",command=lvl.destroy)
butt2.configure(height=3,width=20,bg="olivedrab",fg="white",font=("times",10))
butt2.place(x=0,y=70)

