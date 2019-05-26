# Zodiac and Zodiac Pi (c) campbellone 2019

import os
import time
from datetime import date
from datetime import date,timedelta
import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import font
import sys
from tkinter import messagebox
import math

# clear variables
now = datetime.datetime.now()
thisyear = (now.year)
yourday = 0
yourmonth = 0
yoursign = ""
youryear = 0
yourstone = ""
yourflower = ""
yourbird = ""
chinese = ""
yy = ""
moonT = ""
hols = ""
season = ""


canvas = Tk()

global card
global btnTurn
global birthday


def openscreen():
    
    global btnOK  
    global canvas
    
    canvas = Canvas(width = 1030, height = 710)
    canvas.pack()
    image = PhotoImage(file = "TheSkyAtNight.gif")   
    canvas.create_image(500, 350, image = image)
    line = 5
    placeLine = 220
    while line < 11:
        canvas.create_line(0,line, 480, placeLine, fill= "grey20")
        canvas.create_line(480,placeLine, 1010, line, fill= "grey45")
        placeLine += line*2.5
        line += .25


    OKpix = PhotoImage(file = 'GObutton1.gif')
    btnOK = Button(canvas, image = OKpix, width = 14, command=lambda: nameChecking())    
    btnOK.place(x = 410, y = 250)


    btnOK.focus()
    btnOK.bind("<Return>",nameChecking)
    btnOK.bind("<Button-1>",nameChecking)    
    mainloop()

    
def nameChecking(event):
    global yourname       
    global fname
    global window0
    
    fname = ""
    getname = ""
    yourname = ""
    something = ""
    
    
    btnOK.destroy()        
    window0 = Tk()  
    window0.title("Zodiac is asking")
    window0.geometry('340x150+310+280')
    window0.attributes("-topmost", True)

    lbl0 = Label(window0, text="What is your first name?", font=("Arial, Bold", 10),foreground = "blue")
    lbl0.place(x=75,y=20)       
    fname = Entry(window0)   
    fname.place(x=80,y=60)
    fname.focus_set()
    btn0 = Button(window0, text="Enter")
    btn0.place(x = 130, y = 100)    
    window0.bind("<Return>",dateCheck)
    btn0.bind("<Button-1>",dateCheck)
    
    
    mainloop()
        

def checkday(event):
    global yourday
    global yourmonth
    global youryear
    global youryearT
    global yourstone
    global yourbird
    global leap
    
    leap = 0
    yourday = int(fday.get())
#    yourmonth = int(fmonth.get())
    yourmonthT = fmonth.get()
    youryear = int(fyear.get())
    youryearT = str(youryear)
    

    
    if yourmonthT == "February":
        yourmonth = 2
        yourbird = "Indigo Bunting"
        yourstone = "Amethyst\nit is from the\nGreek word\nAmethystos\nand is a purple\n variety of quartz"
    elif yourmonthT == "January":
        yourmonth = 1
        yourbird = "Great Horned \nOwl"
        yourstone = "Garnet\nfrom gernet\nmeaning dark \nred though it\ncan be other\n colours"
    elif yourmonthT == "March":
        yourmonth = 3
        yourbird = "Sparrow"
        yourstone = "Aquamarine\n or Bloodstone\n\nAquamarine\nfrom the Latin\n Aqua Marina\nmeaning\nsea water"
    elif yourmonthT == "April":
        yourmonth = 4
        yourbird = "Warbler" 
        yourstone = "Diamond\nor Crystal\n\nDiamonds\nare a solid\nform of pure\ncarbon and\nare the hardest\nknown natural\n material"
    elif yourmonthT == "May":
        yourmonth = 5
        yourbird = "Egret or \nNightingale"
        yourstone = "Emerald\n\nThe very best\n emeralds\n possess a\npure verdant \n green hue"
    elif yourmonthT == "June":
        yourmonth = 6
        yourbird = "Dove"
        yourstone = "Pearl\nMoonstone\nor Alexandrite\nNatural pearls \n are from the\n wild, and are\n very rare"
    elif yourmonthT == "July":
        yourmonth = 7
        yourbird = "Raven or Eagle"
        yourstone = "Ruby or\nCarnelian\n\nRuby is from\nthe Latin ruber\nfor red"
    elif yourmonthT == "August":
        yourmonth = 8
        yourbird = "Kingfisher"
        yourstone = "Peridot\nor Sardonyx\nPeridot is only \n olive-green in\ncolour"
    elif yourmonthT == "September":
        yourmonth = 9
        yourbird = "Hawk"
        yourstone = "Sapphire\n\nSapphire comes\nin many colours\n apart from\n red as that\nwould make it a\n ruby"
    elif yourmonthT == "October":
        yourmonth = 10
        yourbird = "Swan"
        yourstone = "Opal\nIt was once\n thought that it\ncould grant\ninvisibility\n\n..OK, where did\nyou go?"
    elif yourmonthT == "November":
        yourmonth = 11
        yourbird = "Kestrel"
        yourstone = "Topaz or\nCitrine\n\nTopaz is from\nthe Greek word\nTopáziοs"
    elif yourmonthT == "December":
        yourmonth = 12
        yourbird = "Raven"
        yourstone = "Turquoise or\nZircon\nTurquoise is from\n the French\nturquois\n meaning\nTurkish through\nwhere it\njourneyed to\nreach Europe"
        
    else:
        print("Not a Month")
        
    window.destroy()

    if yourday == 29 and yourmonth == 2: 
        leap = 1

    if yourmonth == 2 and yourday >29 or yourmonth == 6 and yourday > 30 or yourmonth == 4 and yourday > 30 or yourmonth == 9 and yourday > 30 or yourmonth == 11 and yourday > 30:
        nameChecking()
    elif yourmonth == 2 and yourday > 28 and youryear % 4 != 0:
        nameChecking()        
    elif datetime.datetime(youryear,yourmonth,yourday) > now:
        nameChecking(event)
    else:
        cards()
                
    return()        
        
def dateCheck(event):

          
    global fday
    global fmonth
    global fyear
    global window
    global yourname
    
    yourname = fname.get()
    yourname = (yourname[0:16])
    
    if len(yourname) == 0:
        nameChecking()

    window0.destroy()
 
    window = Tk()
    window.title("The Zodiac asks....")
    window.geometry('400x150+280+300')
    window.attributes("-topmost", True)
    canvas = Canvas(window, 
           width=200, 
           height=200)

    canvas.pack()    
    

    lblyourname = Label(window, text = "Now tell me your birth date", font=("Arial Bold", 10),foreground = "blue")

    lbl = Label(window, text="Day", font=("Arial Bold", 8))
    lbl2 = Label(window, text="Month", font=("Arial Bold", 8))
    lbl3 = Label(window, text="Year", font=("Arial Bold", 8))
        
    lblyourname.place(x=120,y=10)
    lbl.place(x=30,y=40)
    lbl2.place(x=150,y=40)
    lbl3.place(x=270,y=40)
        
    combo = Combobox(window)
    combo2 = Combobox(window)
    combo3 = Combobox(window)
        #set up values for combo box contents
    combo['values']= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    combo2['values']= ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    combo3['values']=(1925,1926,1927,1928,1929,
                       1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,
                       1942,1943,1944, 1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,
                       1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,
                       1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,
                       1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,
                       1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,
                       2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,
                       2015,2016,2017,2018)
       
            
    combo.place(x=30,y=55, width = 100)
    combo2.place(x=150,y=55, width = 100)
    combo3.place(x=270,y=55, width = 100)
            
    combo.config(justify="right")
    combo2.config(justify="right")
    combo3.config(justify="right")
        #set the value to the first item
    combo.current(0) 
    combo2.current(0)
    combo3.current(0)
        #create button to enter data
    btn = Button(window, text="Enter")
        #place button below comco boxes
    btn.place(x = 160, y = 100)
    fday = combo
    fmonth = combo2
    fyear = combo3
    window.bind("<Return>",checkday)
    btn.bind("<Button-1>",checkday)
      
    mainloop()
         

def signs():
    global yoursign
    global yourstone
    global yourflower
    global yourbird
    global yourtree
    global months
    global zodiac
    global romancalendar
    
#add this text to relelvant months                                 
    romancalendar = "\nfrom the time of\nthe Roman\ncalendar\nconsisting of\n10 months\nstarting\nfrom March" 

#setup all the zodica signs
    zodiac = ["is the planet Zogg",
              "is named after\nthe Roman God\n Janus",
              "is named after\n Februalia\n(a festival)",
              "is named after\n Mars the\n Roman god\n of war",
              "is from the\n Latin word\naperio (to open)",
              "is named after\nthe Roman\n goddess Maia",
              "is named after\nthe Roman\n goddess Juno",
              "is named after\n Julius Caeser",
              "is named after\n Augustus Caeser",
              "is from the\nLatin word\n for seven",
              "is from the\nLatin word\n for eight",
              "is from the\n Latin word\nfor nine",
              "is from the\nLatin word\n for ten"]


#convert user numbered month to the calendar month
    months = ["","January","February","March","April","May","June","July","August","September","October","November","December"]

#link data to the user input 
    if yourmonth == 1 and yourday < 20 or yourmonth == 12 and yourday > 21:
        yoursign = "Capricorn\nGoat mountain\n\nThe brightest\nstar in Capricorn\nis Deneb Algedi"
        yourgif =" capricorn"
        yourflower = "Carnation or\n Snowdrop"
        yourtree = "Fir\nElm\nCypress"
    
    elif yourmonth == 1 and yourday > 19 or yourmonth == 2 and yourday < 19:
        yoursign = "Aquarius\n(the Water\n Bearer)\n\nThe brightest\nstar in Aquarius\nis Sadalsuud"
        yourflower = "Voilet or\n Primrose"
        yourtree = "Cypress\nPoplar\nCedar\nPine"
          
    elif yourmonth == 2 and yourday > 18 or yourmonth == 3 and yourday < 21:
        yoursign = "Pisces\n the Fish\n\nThe brightest\nstar in Pisces\nis Eta Piscium"
        yourflower = "Daffodil"
        yourtree = "Weeping Willow\nLime\nOak\nHazelnut"

    elif yourmonth == 3 and yourday> 20 or yourmonth == 4 and yourday < 20:
        yoursign = "Aries\n (the Ram)\n\nThe brighests\nstar in Aries\nis Hamal"
        yourflower = "Sweet Pea or\n Daisy"
        yourtree ="Rowan\nMaple\nWalnut"
    
    elif yourmonth == 4 and yourday > 19 or yourmonth == 5 and yourday < 21:
        yoursign = "Taurus\n (the Bull)\n\nThe brightest\nstar in Tauras\nis Aldebaran"
        yourflower = "Lily of the\n Valley\nor Hawthorn"
        yourtree = "Poplar\nChestnut\nAsh"
    
    elif yourmonth == 5 and yourday > 20 or yourmonth == 6 and yourday < 22:
        yoursign = "Gemini\n (the Twins)\n\nThe brightest\nstar in Gemini\nis Pollux"    
        yourflower = "Rose or Honeysuckle"
        yourtree = "Ash\nHornbeam\nFig\nBirch\nApple"
    
    elif yourmonth == 6 and yourday > 21 or yourmonth == 7 and yourday < 23:
        yoursign = "Cancer\n (the Crab)\n\nThe brightest\nstar in Cancer\nis Al Tarf"    #
        yourflower = "Larkspur or\n Water Lily"
        yourtree = "Apple\nFir\nElm\nCypress"
    
    elif yourmonth == 7 and yourday > 22 or yourmonth == 8 and yourday < 23:
        yoursign = "Leo\n (the Lion)\n\nThe brightest\nstar in Leo\nis Regulus"
        yourflower = "Gladiolus or\n Poppy"
        yourtree = "Cypress\nPopular\nCedar\nPine"
        
    elif yourmonth == 8 and yourday > 22 or yourmonth == 9 and yourday < 23:
        yoursign = "Virgo\n (the Maiden)\n\nThe brightest\nstar in Virgo\nis Spica"
        yourflower = "Aster or\n Morning Glory"
        yourtree = "Weeping Willow\nLime\nOlive\nHazelnut"

    elif yourmonth == 9 and yourday > 22 or yourmonth == 10 and yourday < 24:
         yoursign = "Libra\n (the Scales)\n\nThe brightest\nstar in Libra is\n Zubeneschamali"
         yourflower = "Marigold"
         yourtree = "Rowan\nMaple\nWalnut"

    elif yourmonth == 10 and yourday > 23 or yourmonth == 11 and yourday < 23:
         yoursign = "Scorpio\n (the Scorpion)\n\nThe brightest\nstar in Scorpio\nis Antares"
         yourflower = "Chrysanthemum"
         yourtree = "Walnut\nChestnut\nAsh"
         
    elif yourmonth == 11 and yourday > 22 or yourmonth == 12 and yourday < 22:
         yoursign = "Sagittarius\n (the Archer)\n\nThe brightest\nstar in Sagittarius\nis Sadalsuud"
         yourflower = "Narcissus, holly\nor Poinsettia"
         yourtree = "Hornbeam\nFig\nBeech"
       
    else:
        yoursign = "(odd, but no sign)"
        yourflower = "another mystery\nyour day\nmonth don't exist"
        yourtree = "monkey"
    return        

def films():
    
    global bestFilms
    
    bestFilms = {1925: "There were no\nawards",1926: "There were no\awards",1927:"1927/1928\nWings",1928:"1928/1929\nhe Broadway\nMelody",\
                 1929: "1929/1930\nAll Quiet on the\nWestern Front", 1930: "1930/1931\nCimarron", 1931: "1931/1932\nThe Grand\nHotel",1932: "1932/933\nCavalcade",\
                 1933: "1932/1933\nCavalcade", 1934: "It Happened\n One Night", 1935: "Mutiny on the Bounty", 1936: "The Great Ziegfield",\
                 1937: "The Life of\n Emile Zola", 1938: "You Can't Take it\n With You",\
                 1939: "Gone with\n the Wind",1940:"Rebecca",\
                 1941: "How Green\n Was My Valley",1942: "Mrs Miniver",1943: "Casablanca",1944: "Going My Way",\
                 1945: "The Lost\n Weekend",1946: "The Best Years\nof Our Lives",1947: "Gentleman's\n Agreement",\
                 1948: "Hamlet",1949: "All the\n King's Men", 1950: "All About Eve", 1951: "An American\n in Paris",\
                 1952: "The Greatest\n Show on Earth",1953: "From Here\n to Eternity",1954: "On the\n Waterfront",\
                 1955: "Marty",1956: "Around the\n World in\n 80 Days",1957: "The Bridge\n on the\n River Kwai",\
                 1958: "Gigi", 1959: "Ben-Hur",1960: "The Apartment", 1961: "West Side\n Story", 1962: "Lawrence of\n Arabia",\
                 1963: "Tom Jones",1964: "My Fair\n Lady", 1965: "The Sound\n of Music",1966: "A Man for\n All Seasons", \
                 1967: "In the Heat\n of the Night", 1968: "Oliver", 1969: "Midnight\n Cowboy", 1970: "Patton",\
                 1971: "The French\n Connection", 1972: "The Godfather", 1973: "The Sting",1974: "The Godfather\n Part II",\
                 1975: "One Flew\n over the\n Cuckoo's Nest", 1976: "Rocky", 1977: "Annie Hall", 1978: "The Deer\n Hunter",\
                 1979: "Kramer vs.\n Kramer", 1980: "Ordinary People", 1981: "Chariots\n of Fire", \
                 1982: "Gandhi", 1983: "Terms of Endearment",1984: "Amadeus", 1985:"Out of Africa",1986: "Platoon",\
                 1987: "The Last\n Emperor", 1988: "Rain Man", 1989: "Driving\n Miss Daisy", 1990: "Dances With\n Wolves",\
                 1991: "The Silence \nof the Lambs", 1992:"Unforgiven",1993: "Schindler's\n List",1994:"Forrest Gump",\
                 1995: "Braveheart", 1996: "The English\n Patient", 1997: "Titanic", 1998: "Shakespeare\n in Love",\
                 1999: "American Beauty", 2000: "Gladiator", 2001: "A beautiful\n Mind", 2002: "Chicago",\
                 2003: "The Lord of\n the Rings:\n The Return of\n the King", 2004: "Million Dollar\n Baby", 2005: "Crash",\
                 2006: "Departed", 2007: "No Country\n for Old Men", 2008: "Slumdog\n Millionaire", 2009: "Hurt Locker", \
                 2010: "The King's\n Speech", 2011: "The Artists", 2012: "Argo", 2013: "12 Years a Slave", 2014: "Birdman",\
                 2015: "Spotlight",2016: "Moonlight", 2017:"The Shape of\n Water",2018:"The Green Book"}                 
    
    return
                 
    

def seasons():
    
    global season
    
    if yourmonth > 2 and yourmonth < 6:
        season = "\nin the Spring"

    elif yourmonth > 5 and yourmonth < 9:
        season = "\nin the Summer"
        
    elif yourmonth > 8 and yourmonth < 12:
        season = "\nin the Autumn"
        
    elif yourmonth > 11 or yourmonth <3:
        season = "\nin the Winter"
        
    else:
        season = ""
        
    return

def holidays():
    
    global hols
    
    if yourday == 1 and yourmonth == 1:
        hols = "\nand on\nNew Year's Day"
        
    elif yourday == 14 and yourmonth == 2:
        hols = "\nand on\nValentine's Day"
        
    elif yourday == 1 and yourmonth == 3:
        hols = "\nand on\nSt. David's Day"
        
    elif yourday == 17 and yourmonth == 3:
        hols = "\nand on\nSt. Patrick's Day"
        
    elif yourday == 23 and yourmonth == 4:
        hols = "\nand on\nSt.George's Day"
    
    elif yourday == 31 and yourmonth == 10:
        hols = "\nand on\nHalloween"
        
    elif yourday == 5 and yourmonth == 11:
        hols = "\nand on\nGuy Fawkes Day"

    elif yourday == 30 and yourmonth == 11:
        hols = "\nand on\nSt Andrew's Day"
        
    elif yourday == 24 and yourmonth == 12:
        hols = "\nand on\nChristmas Eve"
        
    elif yourday == 25 and yourmonth == 12:
        hols = "\nand on\nChristmas Day"
        
    elif yourday == 17 and yourmonth == 3:
        hols = "\nand on\nSt. Patrick's Day"
        
    elif yourday == 4 and yourmonth == 7:
        hols ="\nand on USA\nIndependence Day"
        
        
    else:
        hols = ""
        
    return
    
    
def reporting(event):

    global canvas  
    global age
    global day_you_born
    global zodiacsays
    global age
    global day_you_born
    global zodiacsays
    global yourbird
    global yoursign
    global how_old
    global now
    global labeleye
    global days2birthday
    global yourday
    global birthday
    global moonT
    global xmas
    global xmasT
    global card
    global faceCard
    global faceCard2
    global faceCard3
    global faceCard4
    global faceCard5
    global faceCard6
    global faceCard7    
    global faceCard8
    global faceCard9
    global faceCard10    
    global faceCard11
    global faceCard12
    global faceCard13    
    global faceCard14
    global faceCard17
    global faceCard18
    global moon
    global lifePathNumberT
    global startDayJ
    
    
    holidays()
    seasons()
    films()
    music()
    actor()
    worldcup()
    peopleBorn()

    btnOK2.after(10,btnOK2.lower)           
    
    birthday = datetime.datetime(youryear,yourmonth,yourday)
    
    now = datetime.datetime.today()
    age = (now - birthday)     
    day_you_born =  birthday.strftime("%A")

    
    if day_you_born == "Sunday":
        dayT = "Sunday\n is named\nafter the Sun\nfrom when days\nof the week\nwere all named\nafter the planets"
    
    elif day_you_born == "Monday":
        dayT = "Monday\n is named\nafter the Moon\nfrom when days\nof the week\nwere all named\nafter the planets"
    
    elif day_you_born == "Tuesday":
        dayT = "Tuesday\n is named\nafter the the\nNorse god\n Tiw\n\nSome countries\nname this day\nafter the\nplanet Mars\nFrench: Mardi\nSpanish: Martes"
        
    elif day_you_born == "Wednesday":
        dayT = "Wednesday\n is named\nafter the the\nNorse god Odin\n\nSome countries\nname this day\nafter the\nplanet Mercury\nFrench: Mercredi\nItalian: Mercoledi"
    
    elif day_you_born == "Thursday":
        dayT = "Thursday\n is named\nafter the the\nNorse god Thor\n\nSome countries\nname this day\nafter the\nplanet Jupiter\nFrench: Jeudi\nSpanish: Jueves"
 
    elif day_you_born == "Friday":
        dayT = "Friday\n is named\nafter the the\ngoddess Frigg\n\nSome countries\nname this day\nafter the\nplanet Venus\nFrench: Vendredi\nItalian: Venerdi"
  
    elif day_you_born == "Saturday":
        dayT = "Saturday\n is named\nafter the planet\nSaturn from when\ndays of the\nweek were all\nnamed after the\nplanets"
        
    else:
        dayT = "working"
     
           
    birthdayJ = (367*(birthday.year)- int ((7* (birthday.year + int((birthday.month + 9)/12.0)))/4.0)+int((275* + birthday.month)/9.0)+birthday.day+1721013.5+(birthday.hour+birthday.minute/60.0+birthday.second/math.pow(60,2))/24.0 - 0.5*math.copysign(1,100*birthday.year+birthday.month - 190002.5)+0.5) 
    moon = (birthdayJ - 2424145.5)
    moonDays = ((moon) % 29.530588853)
    
#2415020.500706

    if (moonDays) >= 28.51 and (moonDays) < 30 or (moonDays) <1.00:
        moonT = "\nand roughly\naround the time\nof a New Moon"
        
    elif (moonDays) >= 1.00 and (moonDays) < 2.0:
        moonT = "\nand roughly\naround the time of\na New Moon and\nWaxing Crescent \nMoon"
   
    elif (moonDays) >= 2.0 and (moonDays) < 5.36:
        moonT = "\nand roughly\naround the time of\na Waxing Crescent\nMoon"
        
    elif (moonDays) >= 5.36 and (moonDays) < 6.36:
        moonT = "\nand roughly\naround the time of\na Waxing Crescent\nand First Quarter\nMoon"
   

    elif (moonDays) >= 6.36 and (moonDays) < 8.25:
        moonT = "\nand roughly\naround the time of \n a First Quarter\nMoon"    
        
    elif (moonDays) >= 8.25 and (moonDays) < 9.25:
        moonT = "\nand around the\ntime between a\nFirst Quarter\nand Waxing Gibbous\nMoon"
        
    elif (moonDays) >= 9.25 and (moonDays) < 12.58:
        moonT = "\nand roughly\naround the time of\na Waxing Gibbous\nMoon"
            
    elif (moonDays) >= 12.58 and (moonDays) <13.78:
        moonT = "\nand around the\ntime between a\nWaxing Gibbous\nand a Full Moon"
        
    elif (moonDays) >= 13.78 and (moonDays) <15.68:
        moonT = "\nand roughly\naround the time\nof a Full Moon"
        
    elif (moonDays) >= 15.68 and (moonDays) <16.68:
        moonT = "\nand around the\ntime between a\nFull and Waning\nGibbous Moon"
        
    elif (moonDays) >= 16.68 and (moonDays) <20.13:
        moonT = "\nand around the\ntime of a\nWaning Gibbous\n Moon"
    
    elif (moonDays) >= 20.13 and (moonDays) <21.13:
        moonT = "\nand around the\ntime between a\nWaning Gibbous\nand Last Quarter\n Moon"
        
    elif (moonDays) >= 21.13 and (moonDays) <23.11:
        moonT = "\nand roughly around\nthe time of a\nLast Quarter Moon"
    
    elif (moonDays) >= 23.11 and (moonDays) <24.11:
        moonT = "\nand around the\ntime between a\nLast Quarter and\n Waning Crescent\nMoon"
    
    elif (moonDays) >= 24.11 and (moonDays) <27.51:
        moonT = "\nand roughly around \nthe time of a\nWaning Crescent\nMoon"
        
    elif (moonDays) >= 27.51 and (moonDays) <28.51:
       moonT = "\nand around the\ntime between a\nWaning Crescent\nand a New Moon"
    
    else:
        moonT = "\nbut where is the\nMoon"
    

    xmas = (now)
    xmas = xmas.replace(month=12,day=25)

    if now > xmas:
        xmasT = "\nand Christmas\nhas just been\nNew Year is next"
    
    elif now < xmas:
        xmasdays = xmas - now
        xmasT = "\nand " + str(xmasdays.days) + " days\nto Christmas"
        
    else:
        xmasT = "No Christmas"
            
            
    if youryear % 4 == 0:
        day_you_born += "\nand in a\n Leap Year"
        
    if youryear == 1940 or youryear == 1944:
        olympics = ""
     
    elif youryear % 4 == 0:
        olympics = "\nin an Olympics \nGames year"
        
    else:
        olympics = ""
        

    lifePathNumber = 0
    firstnumber = 0
    addyear = 0
    addmonth = 0
    addday = 0
    addUPnumbers = 0
    addUP = 0
    lucky = 0
    number = 0
    totalT = str(yourday+yourmonth+youryear)

    for addUP in totalT:
         addUPnumbers += int(addUP)
 
    lifePathNumber = addUPnumbers
 
    for run1 in str(addUPnumbers):
         lucky += int(run1)
    for run2 in str(lucky):
         number += int(run2)
         lifePathNumber = number
    
    if lifePathNumber == 2 or lifePathNumber == 3 or lifePathNumber == 5 or lifePathNumber == 7:
        lifePathNumberT = "\nThis is also\na prime number"
    else:
        lifePathNumberT =""
    
    worldcupyears = [ 1930, 1934, 1938, 1950, 1954, 1958, 1962,1966,1970, 1974, 1978 , 1982,
                      1986, 1990, 1994,1998,2002,2006,2010,2014,2018]
    
    if youryear  in worldcupyears:
        worldcupAddon = "\nIn a year that\n" + football[youryear] + "\nwon the football\nWorld Cup"
    else:
        worldcupAddon = ""
    
    if youryear > 1929  and youryear <1996:
        
        addPeopleT = "\n\nOther people\nborn in " + str(youryear) + "\n" + addPeople[youryear]
    else:
        addPeopleT = ""
        

    thisbirthday = now
    days2birthdayT = ""
    
    
    if leap == 1:
        yourday = yourday -1
             
    
    thisbirthday = thisbirthday.replace(day=yourday, month=yourmonth)
    

    if thisbirthday < now:
        thisbirthday = thisbirthday.replace(year=now.year + 1)
        days2birthdayT="You have had\nyour birthday\nthis year\nIt is "
        days2birthday = abs((thisbirthday - now))

    elif thisbirthday > now:
        days2birthdayT ="Looks like it is\n"
        days2birthday = abs((thisbirthday - now))
        if days2birthday.days == 1:
            days2birthdayT = "Your birthday \nis tomorrow\nBrilliant!\n"
                       

    elif thisbirthday.month == now.month and thisbirthday.day == now.day:
        thisbirthday = thisbirthday.replace(year=now.year + 1)               
        days2birthday = abs((thisbirthday - now))
        days2birthdayT = "Happy Birthday\n" + yourname + "\nHope you got\nplenty presents\nIt is\n"

    if leap == 1:
        days2birthdayT = days2birthdayT + "on the 29Feb\nLet's move it to\n28Feb so you have\na birthday each\nyear. Now it's only\n"

    start = datetime.date(now.year,now.month,now.day)
    end = datetime.date(thisbirthday.year,thisbirthday.month,thisbirthday.day)

    p = (end - start)
    pocket = (int(((p.days)+1)/7))

    nextBirthday = datetime.date(now.year,yourmonth,yourday)

    lastBirthday = (now.year)
    if nextBirthday > start:
        lastBirthday -= 1
    yearsofbirthdays = (lastBirthday - birthday.year)
  
    countBirthdayT = "" 
    countBirthday = 0
    countMon=0
    countTues =0
    countWed=0
    countThurs=0
    countFri=0
    countSat=0
    countSun=0
    nBday=""
    
    while countBirthday <= yearsofbirthdays:
        
        if date(youryear + countBirthday,yourmonth,yourday).weekday() == 0:
            countMon += 1
        if date(youryear + countBirthday,yourmonth,yourday).weekday() == 1:
            countTues += 1
        if date(youryear + countBirthday,yourmonth,yourday).weekday() == 2:
            countWed += 1        
        if date(youryear + countBirthday,yourmonth,yourday).weekday() == 3:
            countThurs += 1
        if date(youryear + countBirthday,yourmonth,yourday).weekday() == 4:
            countFri += 1
        if date(youryear + countBirthday,yourmonth,yourday).weekday() == 5:
            countSat += 1
        if date(youryear + countBirthday,yourmonth,yourday).weekday() == 6:
            countSun += 1
               
        countBirthday += 1
   

    if countMon >0:
           countBirthdayT = "Mondays x " + str(countMon)
           
    if countTues >0:
           countBirthdayT += "\nTuesdays x " + str(countTues) 
           
    if countWed >0:
           countBirthdayT += "\nWednesdays x " + str(countWed) 
           
    if countThurs >0:
           countBirthdayT += "\nThursdays x " + str(countThurs)    

    if countFri >0:
           countBirthdayT += "\nFridays x " + str(countFri) 

    if countSat >0:
           countBirthdayT += "\nSaturdays x " + str(countSat) 

    if countSun >0:
           countBirthdayT += "\nSundays x " + str(countSun) + "\n"

    signs()
    animal_years()
    chineseYear()
    
    nBday = date(youryear + countBirthday,yourmonth,yourday).strftime("%A")

    
    if yourmonth == 9 or yourmonth == 10 or yourmonth == 11 or yourmonth == 12:
        zodiac[yourmonth] += romancalendar


    if youryear > 1951:
        addfilmT = "and biggest selling\nsingle(UK) was\n"
    else:
        addfilmT =""
    
    if youryear > 1933:
        addactT = "\nbest actor was\n"
    else:
        addactT =""  
    
    
    bDayPix = PhotoImage(file = "OYB.gif")
    labelbDay = Label(canvas, image = bDayPix, background = "grey25")
    labelbDay.place(x = 360, y = 220)

    eye = PhotoImage(file = 'eye1.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
 
    eye = PhotoImage(file = 'eye2.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20)
    labeleye.place(x = 370, y = 265)
   
    card = PhotoImage(file = 'flipover.gif')
    faceCard = Label(canvas,  font = ("arial bold", 8),  compound = CENTER, text = yourname + "\nwas born\n on a\n " + day_you_born + moonT + "\n" , image = card, background ="grey25", foreground = "red", justify = CENTER)    
    faceCard.place(x = 55, y = 0, height =230, width = 150)  
    faceCard.after(10,faceCard.lower)
    labeleye.after(10,labeleye.lower)
    faceCard.after(2000,faceCard.lift)
    labeleye.after(2000,labeleye.lift)  
 
    card2 = PhotoImage(file = 'flipover2.gif')
    faceCard2 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = dayT, image = card2, background ="grey25", foreground = "deep sky blue", justify = CENTER)
    faceCard2.place(x = 205, y = 0, height =230, width = 150)
    eye = PhotoImage(file = 'eye3.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25") 
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard2.after(10,faceCard2.lower)
    labeleye.after(10,labeleye.lower)
    labeleye.after(5500,labeleye.lift)
    faceCard2.after(5500,faceCard2.lift)
    
    card3 = PhotoImage(file = 'flipover.gif')
    faceCard3 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = "Your Life Path \nnumber is\n" + str(lifePathNumber) + lifePathNumberT , image = card3, background ="grey25", foreground = "DarkGoldenrod3", justify = CENTER)
    faceCard3.place(x = 355, y = 0, height =230, width = 150)
    eye = PhotoImage(file = 'eye3b.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard3.after(10,faceCard3.lower)
    labeleye.after(10,labeleye.lower)
    faceCard3.after(9000,faceCard3.lift)
    labeleye.after(9000,labeleye.lift)   
       
    card4 = PhotoImage(file = 'flipover2.gif')
    faceCard4 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = "Your Tropical\nZodiac sign is\n" + yoursign , image = card4 , background ="grey25", foreground = "green", justify = CENTER)
    faceCard4.place(x = 505, y = 0, height =230, width = 150)
    eye = PhotoImage(file = 'eye4.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25") 
    labeleye.Photo = eye
    labeleye.config(width=20)
    labeleye.place(x = 370, y = 265)
    faceCard4.after(10,faceCard4.lower)
    labeleye.after(10,labeleye.lower)
    faceCard4.after(12500,faceCard4.lift)
    labeleye.after(12500,labeleye.lift)   

    card5 = PhotoImage(file = 'flipover.gif')
    faceCard5 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = "You were born\nin " + months[yourmonth] + season + hols + olympics + worldcupAddon + addPeopleT, image = card5, background ="grey25", foreground = "violet red", justify = CENTER)
    faceCard5.place(x = 655, y = 0, height =230, width = 150)
    eye = PhotoImage(file = 'eye5.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")  
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard5.after(10,faceCard5.lower)
    labeleye.after(10,labeleye.lower)
    faceCard5.after(16000,faceCard5.lift)
    labeleye.after(16000,labeleye.lift) 

    card6 = PhotoImage(file = 'flipover2.gif')
    faceCard6 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = months[yourmonth] +"\n" + zodiac[yourmonth] , image = card6, background ="grey25", foreground = "DarkOrchid4", justify = CENTER)
    faceCard6.place(x = 800, y = 0, height =230, width = 150)
    eye = PhotoImage(file = 'eye6.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard6.after(10,faceCard6.lower)
    labeleye.after(10,labeleye.lower)
    faceCard6.after(19500,faceCard6.lift)
    labeleye.after(19500,labeleye.lift)     

    faceCard17 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = "There are " +str(pocket) + "\npocket moneys\nuntil your next\nbirthday so\nstart saving up\n\nMother'sDay is\nin March(UK) and\nFather's Day\n is in June" ,  background ="grey25",image = card, foreground = "purple4", justify = CENTER)
    faceCard17.place(x = 655, y = 220, height =230, width = 150)
    eye = PhotoImage(file = 'eye7.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard17.after(10,faceCard17.lower)
    labeleye.after(10,labeleye.lower)
    faceCard17.after(23000,faceCard17.lift)
    labeleye.after(23000,labeleye.lift)    

    faceCard18 = Label(canvas, font = ("arial bold", 8),  compound = CENTER, text =  str(youryear) + "\nin Chinese\nAstrology\nwas the year\nof the\n" + chinese + "\nand the elements\nwere "+ yy , image = card6, background ="grey25", foreground = "thistle4", justify = CENTER)
    faceCard18.place(x = 800, y = 220, height =230, width = 150)
    eye = PhotoImage(file = 'eye7.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard18.after(10,faceCard18.lower)
    labeleye.after(10,labeleye.lower)
    faceCard18.after(26500,faceCard18.lift)
    labeleye.after(26500,labeleye.lift)    
          
    card12 = PhotoImage(file = 'flipover2.gif')
    faceCard12 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = yourname + "\nis " + years_oldT + "\nor "+ cat_yearsT + "\ncat years\n"+ dog_yearsT + "\ndog years\n(woof...roughly)", image = card12, background ="grey25", foreground = "green", justify = CENTER)
    faceCard12.place(x =805, y = 440, height =230, width = 150)
    eye = PhotoImage(file = 'eye8.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard12.after(10,faceCard12.lower)
    labeleye.after(10,labeleye.lower)
    faceCard12.after(30000,faceCard12.lift)
    labeleye.after(30000,labeleye.lift)  
    
    card11 = PhotoImage(file = 'flipover.gif')
    faceCard11 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text =  "Your previous\nbirthdays were\n\n" + countBirthdayT +"\nNext birthday is a\n" + nBday, image = card11, background ="grey25", foreground = "light sea green", justify = CENTER)
    faceCard11.place(x = 655, y = 440, height =230, width = 150)
    eye = PhotoImage(file = 'eye8.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard11.after(10,faceCard11.lower)
    labeleye.after(10,labeleye.lower)
    faceCard11.after(33500,faceCard11.lift)
    labeleye.after(33500,labeleye.lift)  
     
    card10 = PhotoImage(file = 'flipover2.gif')
    faceCard10 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = "Your birth\n trees are\n " + yourtree, image = card10, background ="grey25", foreground = "Orange Red", justify = CENTER)
    faceCard10.place(x = 505, y = 440, height =230, width = 150)
    eye = PhotoImage(file = 'eye8b.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard10.after(10,faceCard10.lower)
    labeleye.after(10,labeleye.lower)
    faceCard10.after(37000,faceCard10.lift)
    labeleye.after(37000,labeleye.lift)  

    
    card9 = PhotoImage(file = 'flipover.gif')
    faceCard9 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = "The best film\nin " + str(youryear) + " was\n" + bestFilms[youryear] + addactT + bestActor[youryear] + "\n" + addfilmT + bestMusic[youryear], image = card9, background ="grey25", foreground = "Maroon", justify = CENTER)
    faceCard9.place(x = 355, y = 440, height =230, width = 150)
    eye = PhotoImage(file = 'eye8c.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard9.after(10,faceCard9.lower)
    labeleye.after(10,labeleye.lower)
    faceCard9.after(40500,faceCard9.lift)
    labeleye.after(40500,labeleye.lift)  

    card8 = PhotoImage(file = 'flipover2.gif')
    faceCard8 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = "Your birth \nflower is \n " + yourflower +"\n\nYour birth bird\n is the\n " + yourbird, image = card8, background ="grey25", foreground = "DarkOrange2", justify = CENTER)
    faceCard8.place(x = 205, y = 440, height =230, width = 150)
    eye = PhotoImage(file = 'eye9.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard8.after(10,faceCard8.lower)
    labeleye.after(10,labeleye.lower)
    faceCard8.after(44000,faceCard8.lift)
    labeleye.after(44000,labeleye.lift)    


    card7 = PhotoImage(file = 'flipover.gif')
    faceCard7 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = "Your birth\ngem stone is \n " + yourstone , image = card7, background ="grey25", foreground = "cyan4", justify = CENTER)
    faceCard7.place(x = 55, y = 440, height =230, width = 150)
    eye = PhotoImage(file = 'eye10.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard7.after(10,faceCard7.lower)
    labeleye.after(10,labeleye.lower)
    faceCard7.after(47500,faceCard7.lift)
    labeleye.after(47500,labeleye.lift)    
               
    faceCard13 = Label(canvas,  font = ("arial bold", 8),  compound = CENTER,  text = days2birthdayT + str(days2birthday.days) + " days to \nyour next birthday" + xmasT, image = card, background ="grey25", foreground = "green", justify = CENTER)   
    faceCard13.place(x = 55, y = 220, height =230, width = 150)
    eye = PhotoImage(file = 'eye11.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard13.after(10,faceCard13.lower)
    labeleye.after(10,labeleye.lower)
    faceCard13.after(51000,faceCard13.lift)
    labeleye.after(51000,labeleye.lift)  
        
    faceCard14 = Label(canvas, font = ("arial bold", 8),  compound = CENTER,  text = " You are \n" + str(age.days) + "\ndays old\n or "+ str(int((age.days)/7)) + "\nweeks and\n" + str(int((age.days)%7))+ " days", image = card, background ="grey25", foreground = "tomato", justify = CENTER)
    faceCard14.place(x = 205, y = 220, height =230, width = 150)
    eye = PhotoImage(file = 'eye1.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)
    faceCard14.after(10,faceCard14.lower)
    labeleye.after(10,labeleye.lower)
    faceCard14.after(54500,faceCard14.lift)
    labeleye.after(54500,labeleye.lift)  
  
        
    btnOK3 = Button(canvas,  text = "Close", compound = CENTER, width=11, command=lambda: os._exit(-1))
    btnOK3.place(x = 380, y = 400)

    btnOK4 = Button(canvas,  text = "Restart", compound = CENTER, width=11, command=lambda: rerun()) 
    btnOK4.place(x = 520, y = 400)

 
    eye = PhotoImage(file = 'eye1.gif')
    labeleye = Label(canvas, text ="", image = eye, width=5, background ="grey25")
    labeleye.Photo = eye
    labeleye.config(width=20) 
    labeleye.place(x = 370, y = 265)              

    mainloop()
 

def cards():

    global btnTurn
    global birthday
    global btnOK2
    global lbl2
     
    blank_it = Label(canvas,  background ="grey25")    
    blank_it.place(x = 0, y = 0, height = 700, width = 1050)
    
    card = PhotoImage(file = 'help20.gif')
    labelCard = Label(canvas, text ="", image = card, width=5, background ="grey25")
    labelCard.Photo = card
    labelCard.config(width=20) 
    labelCard.place(x = 50, y = 220)
 
    card1 = PhotoImage(file = 'help20.gif')
    labelCard1 = Label(canvas, text ="", image = card1, width=5, background ="grey25")
    labelCard1.Photo = card
    labelCard.config(width=20) 
    labelCard1.place(x = 200, y = 220)

    card4 = PhotoImage(file = 'help20.gif')
    labelCard4 = Label(canvas, text ="", image = card4, width=5, background ="grey25")
    labelCard4.Photo = card4
    labelCard4.config(width=20) 
    labelCard4.place(x = 650, y = 220)
    
    card5 = PhotoImage(file = 'help20.gif')
    labelCard5 = Label(canvas, text ="", image = card5, width=5, background ="grey25")
    labelCard5.Photo = card5
    labelCard5.config(width=20) 
    labelCard5.place(x = 800, y = 220)
       
    card6 = PhotoImage(file = 'help20.gif')
    labelCard6 = Label(canvas, text ="", image = card6, width=5, background ="grey25")
    labelCard6.Photo = card6
    labelCard6.config(width=20) 
    labelCard6.place(x = 800, y = 440)

    card7 = PhotoImage(file = 'help20.gif')
    labelCard7 = Label(canvas, text ="", image = card7, width=5, background ="grey25")
    labelCard7.Photo = card7
    labelCard7.config(width=20) 
    labelCard7.place(x = 50, y = 440)  
       
    card8 = PhotoImage(file = 'help20.gif')
    labelCard8 = Label(canvas, text ="", image = card8, width=5, background ="grey25")
    labelCard8.Photo = card8
    labelCard8.config(width=20) 
    labelCard8.place(x = 200, y = 440)
 
    card9 = PhotoImage(file = 'help20.gif')
    labelCard9 = Label(canvas, text ="", image = card9, width=5, background ="grey25")
    labelCard9.Photo = card9
    labelCard9.config(width=20) 
    labelCard9.place(x = 350, y = 440)
 
    card10 = PhotoImage(file = 'help20.gif')
    labelCard10 = Label(canvas, text ="", image = card10, width=5, background ="grey25")
    labelCard10.Photo = card10
    labelCard10.config(width=20) 
    labelCard10.place(x = 500, y = 440)
    
    card11 = PhotoImage(file = 'help20.gif')
    labelCard11 = Label(canvas, text ="", image = card11, width=5, background ="grey25")
    labelCard11.Photo = card11
    labelCard11.config(width=20) 
    labelCard11.place(x = 650, y = 440)
    
    card12 = PhotoImage(file = 'help20.gif')
    labelCard12 = Label(canvas, text ="", image = card12, width=5, background ="grey25")
    labelCard12.Photo = card12
    labelCard12.config(width=20) 
    labelCard12.place(x = 800, y = 0)

    card13 = PhotoImage(file = 'help20.gif')
    labelCard13 = Label(canvas, text ="", image = card13, width=5, background ="grey25")
    labelCard13.Photo = card13
    labelCard13.config(width=20) 
    labelCard13.place(x = 650, y = 0)
   
    card14 = PhotoImage(file = 'help20.gif')
    labelCard14 = Label(canvas, text ="", image = card14, width=5, background ="grey25")
    labelCard14.Photo = card14
    labelCard14.config(width=20) 
    labelCard14.place(x = 500, y = 0)

    card15 = PhotoImage(file = 'help20.gif')
    labelCard15 = Label(canvas, text ="", image = card15, width=5, background ="grey25")
    labelCard15.Photo = card15
    labelCard15.config(width=20) 
    labelCard15.place(x = 350, y = 0)

    card16 = PhotoImage(file = 'help20.gif')
    labelCard16 = Label(canvas, text ="", image = card16, width=5, background ="grey25")
    labelCard16.Photo = card16
    labelCard16.config(width=20) 
    labelCard16.place(x = 200, y = 0)

    card17 = PhotoImage(file = 'help20.gif')
    labelCard17 = Label(canvas, text ="", image = card17, width=5, background ="grey25")
    labelCard17.Photo = card17
    labelCard17.config(width=20) 
    labelCard17.place(x = 50, y = 0)
      
    cardx = PhotoImage(file = 'seeME3.gif')    
    btnOK2 = Button(canvas, image = cardx, compound = CENTER)
    btnOK2.place(x=380,y=250)
    
    btnOK2.focus()
    btnOK2.bind("<Return>",reporting)
    btnOK2.bind("<Button-1>",reporting)    

    mainloop()
  
def animal_years():
    global years_old
    global cat_yearsT
    global dog_yearsT
    global years_oldT
    
    years_oldT=""
    cat_years = 14
    dog_years = 15
    
    birthday = datetime.datetime(youryear,yourmonth,yourday)
    today = datetime.date.today()
    years_old = today.year - birthday.year
    
    if today.month < birthday.month or birthday.month == today.month and birthday.day > now.day:
        years_old -= 1
        years_oldT = str(years_old) + " years old"
    else:
        years_oldT = str(years_old) + " years old"

 
    if years_old < 1:
        years_oldT = " months old"
 
 
    cat_years += int(years_old * 4.4)
    dog_years += int(years_old * 6)    
    cat_yearsT = " about " + str(cat_years)
    
    if years_old <= 1:
        dog_years = 18
   
    dog_yearsT = " and " + str(dog_years) 
 
    return
    
    
def chineseYear():

    global chinese
    global yy

    chinese = ""
    yy = ""

    if birthday > datetime.datetime (1924,2,4) and birthday < datetime.datetime(1925,1,24) \
        or birthday > datetime.datetime(1984,2,1) and birthday < datetime.datetime(1985,1,22) \
        or birthday > datetime.datetime(1936,1,22) and birthday < datetime.datetime(1937,2,11) \
        or birthday > datetime.datetime(1996,2,18) and birthday < datetime.datetime(1997,2,7) \
        or birthday > datetime.datetime(1948,2,9) and birthday < datetime.datetime(1949,1,29) \
        or birthday > datetime.datetime(2008,2,6) and birthday < datetime.datetime(2009,1,26) \
        or birthday > datetime.datetime(1960,1,27) and birthday < datetime.datetime(1961,2,15) \
        or birthday > datetime.datetime(2020,1,24) and birthday < datetime.datetime(2021,2,12) \
        or birthday > datetime.datetime(1972,2,14) and birthday < datetime.datetime(1973,2,3) \
        or birthday > datetime.datetime(2032,2,10) and birthday < datetime.datetime(2033,1,31):
        
            chinese = "Rat (Zi)"
            yy = "Yang Wood"
        
    elif birthday > datetime.datetime (1925,1,23) and birthday < datetime.datetime(1926,2,13) \
         or birthday > datetime.datetime(1985,1,21) and birthday < datetime.datetime(1986,2,9) \
         or birthday > datetime.datetime(1937,2,10) and birthday < datetime.datetime(1938,1,31) \
         or birthday > datetime.datetime(1949,1,28) and birthday < datetime.datetime(1950,2,17) \
         or birthday > datetime.datetime(2009,1,27) and birthday < datetime.datetime(2010,2,14) \
         or birthday > datetime.datetime(1997,2,6) and birthday < datetime.datetime(1998,1,28) \
         or birthday > datetime.datetime(1961,2,14) and birthday < datetime.datetime(1962,2,5) \
         or birthday > datetime.datetime(2021,2,11) and birthday < datetime.datetime(2022,2,1) \
         or birthday > datetime.datetime(1973,2,2) and birthday < datetime.datetime(1974,1,24) \
         or birthday > datetime.datetime(2033,1,30) and birthday < datetime.datetime(2034,2,19):
        
            chinese = "Ox (Chou)"
            yy = "Yin Wood"
    
    elif birthday > datetime.datetime (1926,2,12) and birthday < datetime.datetime(1927,2,2) \
         or birthday > datetime.datetime(1986,2,8) and birthday < datetime.datetime(1987,1,29) \
         or birthday > datetime.datetime(1938,1,30) and birthday < datetime.datetime(1939,2,19) \
         or birthday > datetime.datetime(1998,1,27) and birthday < datetime.datetime(1999,2,16) \
         or birthday > datetime.datetime(1950,2,16) and birthday < datetime.datetime(1951,2,6) \
         or birthday > datetime.datetime(2010,2,13) and birthday < datetime.datetime(2011,2,3) \
         or birthday > datetime.datetime(1962,2,4) and birthday < datetime.datetime(1963,1,23) \
         or birthday > datetime.datetime(2021,2,11) and birthday < datetime.datetime(2022,2,1) \
         or birthday > datetime.datetime(1974,1,22) and birthday < datetime.datetime(1975,2,11) \
         or birthday > datetime.datetime(2034,2,18) and birthday < datetime.datetime(2035,2,8):
                
            chinese = "Tiger (Yin)"
            yy = "Yang Fire"

    elif birthday > datetime.datetime (1927,2,1) and birthday < datetime.datetime(1928,1,23) \
         or birthday > datetime.datetime(1987,1,28) and birthday < datetime.datetime(1988,2,18) \
         or birthday > datetime.datetime(1939,2,18) and birthday < datetime.datetime(1940,2,8) \
         or birthday > datetime.datetime(1999,2,15) and birthday < datetime.datetime(2000,2,5) \
         or birthday > datetime.datetime(1951,2,5) and birthday < datetime.datetime(1952,1,27) \
         or birthday > datetime.datetime(2011,2,2) and birthday < datetime.datetime(2012,1,23) \
         or birthday > datetime.datetime(1963,1,24) and birthday < datetime.datetime(1964,2,13) \
         or birthday > datetime.datetime(2023,1,21) and birthday < datetime.datetime(2024,2,10) \
         or birthday > datetime.datetime(1975,2,10) and birthday < datetime.datetime(1976,1,31) \
         or birthday > datetime.datetime(2035,2,7) and birthday < datetime.datetime(2036,1,28):
                
            chinese = "Rabbit (Mao)"
            yy = "Yin Fire"

    elif birthday > datetime.datetime (1928,1,22) and birthday < datetime.datetime(1929,2,10) \
         or birthday > datetime.datetime(1988,2,16) and birthday < datetime.datetime(1989,2,6) \
         or birthday > datetime.datetime(1940,2,7) and birthday < datetime.datetime(1941,1,27) \
         or birthday > datetime.datetime(2000,2,4) and birthday < datetime.datetime(2001,1,24) \
         or birthday > datetime.datetime(1952,1,26) and birthday < datetime.datetime(1953,2,14) \
         or birthday > datetime.datetime(2012,1,22) and birthday < datetime.datetime(2013,2,10) \
         or birthday > datetime.datetime(1964,2,12) and birthday < datetime.datetime(1965,2,2) \
         or birthday > datetime.datetime(2024,2,9) and birthday < datetime.datetime(2025,1,29) \
         or birthday > datetime.datetime(1976,1,30) and birthday < datetime.datetime(1977,2,18) \
         or birthday > datetime.datetime(2036,1,27) and birthday < datetime.datetime(2037,2,15):
                
            chinese = "Dragon (chen)"
            yy = "Yang Earth"

    elif birthday > datetime.datetime (1929,2,9) and birthday < datetime.datetime(1930,1,30) \
         or birthday > datetime.datetime(1989,2,5) and birthday < datetime.datetime(1990,1,27) \
         or birthday > datetime.datetime(1941,1,26) and birthday < datetime.datetime(1942,2,14) \
         or birthday > datetime.datetime(2001,1,23) and birthday < datetime.datetime(2002,2,12) \
         or birthday > datetime.datetime(1953,2,13) and birthday < datetime.datetime(1954,2,3) \
         or birthday > datetime.datetime(2013,2,9) and birthday < datetime.datetime(2014,1,31) \
         or birthday > datetime.datetime(1965,2,1) and birthday < datetime.datetime(1966,1,21) \
         or birthday > datetime.datetime(2025,1,28) and birthday < datetime.datetime(2026,2,17) \
         or birthday > datetime.datetime(1977,2,17) and birthday < datetime.datetime(1978,2,7) \
         or birthday > datetime.datetime(2037,2,14) and birthday < datetime.datetime(2038,2,4):
                
            chinese = "Snake(Si)"
            yy = "Yin Earth"
  
    elif birthday > datetime.datetime (1930,1,29) and birthday < datetime.datetime(1931,2,17) \
         or birthday > datetime.datetime(1990,1,26) and birthday < datetime.datetime(1991,2,15) \
         or birthday > datetime.datetime(1942,2,14) and birthday < datetime.datetime(1943,2,5) \
         or birthday > datetime.datetime(2002,2,11) and birthday < datetime.datetime(2003,2,1) \
         or birthday > datetime.datetime(1954,2,2) and birthday < datetime.datetime(1955,1,24) \
         or birthday > datetime.datetime(2014,2,1) and birthday < datetime.datetime(2015,2,19) \
         or birthday > datetime.datetime(1966,1,20) and birthday < datetime.datetime(1967,2,9) \
         or birthday > datetime.datetime(2026,2,16) and birthday < datetime.datetime(2027,2,6) \
         or birthday > datetime.datetime(1978,2,6) and birthday < datetime.datetime(1979,1,28) \
         or birthday > datetime.datetime(2038,2,3) and birthday < datetime.datetime(2039,1,24):
                
            chinese = "Horse(Wu)"
            yy = "Yin Earth"
            
    elif birthday > datetime.datetime (1931,2,16) and birthday < datetime.datetime(1932,2,6) \
         or birthday > datetime.datetime(1991,2,14) and birthday < datetime.datetime(1992,2,4) \
         or birthday > datetime.datetime(1943,2,4) and birthday < datetime.datetime(1944,1,24) \
         or birthday > datetime.datetime(2003,1,31) and birthday < datetime.datetime(2004,1,22) \
         or birthday > datetime.datetime(1955,1,23) and birthday < datetime.datetime(1956,2,12) \
         or birthday > datetime.datetime(2015,2,18) and birthday < datetime.datetime(2016,2,8) \
         or birthday > datetime.datetime(1967,2,8) and birthday < datetime.datetime(1968,1,30) \
         or birthday > datetime.datetime(2027,2,15) and birthday < datetime.datetime(2028,1,26) \
         or birthday > datetime.datetime(1979,1,27) and birthday < datetime.datetime(1980,2,16) \
         or birthday > datetime.datetime(2039,1,23) and birthday < datetime.datetime(2040,2,12):
                
            chinese = "Sheep or\n Goat(Wei)"
            yy = "Yin Metal"            
            
    elif birthday > datetime.datetime (1932,2,5) and birthday < datetime.datetime(1933,1,26) \
         or birthday > datetime.datetime(1992,2,3) and birthday < datetime.datetime(1993,1,23) \
         or birthday > datetime.datetime(1944,1,24) and birthday < datetime.datetime(1945,2,13) \
         or birthday > datetime.datetime(2004,1,21) and birthday < datetime.datetime(2005,2,9) \
         or birthday > datetime.datetime(1956,2,11) and birthday < datetime.datetime(1957,1,31) \
         or birthday > datetime.datetime(2016,2,7) and birthday < datetime.datetime(2017,1,28) \
         or birthday > datetime.datetime(1968,1,29) and birthday < datetime.datetime(1969,2,17) \
         or birthday > datetime.datetime(2028,1,25) and birthday < datetime.datetime(2029,2,13) \
         or birthday > datetime.datetime(1980,2,15) and birthday < datetime.datetime(1981,2,5) \
         or birthday > datetime.datetime(2040,2,11) and birthday < datetime.datetime(2041,2,1):
                
            chinese = "Monkey (Shen)"
            yy = "Yang Water"    
 
    elif birthday > datetime.datetime (1933,1,25) and birthday < datetime.datetime(1934,1,14) \
         or birthday > datetime.datetime(1993,1,22) and birthday < datetime.datetime(1994,2,10) \
         or birthday > datetime.datetime(1945,2,12) and birthday < datetime.datetime(1946,2,2) \
         or birthday > datetime.datetime(2005,2,8) and birthday < datetime.datetime(2006,1,29) \
         or birthday > datetime.datetime(1957,1,30) and birthday < datetime.datetime(1958,2,18) \
         or birthday > datetime.datetime(2017,1,27) and birthday < datetime.datetime(2018,2,16) \
         or birthday > datetime.datetime(1969,2,18) and birthday < datetime.datetime(1970,2,16) \
         or birthday > datetime.datetime(2029,2,12) and birthday < datetime.datetime(2030,2,3) \
         or birthday > datetime.datetime(1981,2,4) and birthday < datetime.datetime(1982,2,25) \
         or birthday > datetime.datetime(2041,2,2) and birthday < datetime.datetime(2042,1,22):
                
            chinese = "Rooster (You)"
            yy = "Yin Water" 
    
    elif birthday > datetime.datetime (1934,2,13) and birthday < datetime.datetime(1935,2,4) \
         or birthday > datetime.datetime(1994,2,9) and birthday < datetime.datetime(1995,1,31) \
         or birthday > datetime.datetime(1946,2,1) and birthday < datetime.datetime(1947,1,22) \
         or birthday > datetime.datetime(2006,1,28) and birthday < datetime.datetime(2007,2,18) \
         or birthday > datetime.datetime(1958,2,17) and birthday < datetime.datetime(1959,2,8) \
         or birthday > datetime.datetime(2018,2,15) and birthday < datetime.datetime(2019,2,5) \
         or birthday > datetime.datetime(1970,2,5) and birthday < datetime.datetime(1971,1,27) \
         or birthday > datetime.datetime(2030,2,2) and birthday < datetime.datetime(2031,1,22) \
         or birthday > datetime.datetime(1982,1,24) and birthday < datetime.datetime(1983,2,13) \
         or birthday > datetime.datetime(2042,1,21) and birthday < datetime.datetime(2043,2,10):
                
            chinese = "Dog (Xu)"
            yy = "Yang Wood"                              

    elif birthday > datetime.datetime (1935,2,3) and birthday < datetime.datetime(1936,1,24) \
         or birthday > datetime.datetime(1995,1,30) and birthday < datetime.datetime(1996,2,19) \
         or birthday > datetime.datetime(1947,1,21) and birthday < datetime.datetime(1948,2,10) \
         or birthday > datetime.datetime(2007,2,17) and birthday < datetime.datetime(2008,2,7) \
         or birthday > datetime.datetime(1959,2,7) and birthday < datetime.datetime(1960,1,28) \
         or birthday > datetime.datetime(2019,2,5) and birthday < datetime.datetime(2020,1,25) \
         or birthday > datetime.datetime(1971,1,26) and birthday < datetime.datetime(1972,2,15) \
         or birthday > datetime.datetime(2031,2,22) and birthday < datetime.datetime(2032,2,11) \
         or birthday > datetime.datetime(1983,2,12) and birthday < datetime.datetime(1984,2,2) \
         or birthday > datetime.datetime(2043,2,9) and birthday < datetime.datetime(2044,1,11):
                
            chinese = "Boar or\n Pig (Hai)"
            yy = "Yin Wood"
         
    return

def music():
    
    global bestMusic
    
    bestMusic = {1925: "", 1926: "", 1927: "", 1928: "", 1929: "", 1930: "", 1931: "",
                 1932: "", 1933: "", 1934: "", 1935: "", 1936: "", 1937: "", 1938: "",
                 1939: "", 1940: "", 1941: "", 1942: "", 1943: "", 1944: "", 1945: "",
                 1946: "", 1947: "", 1948: "", 1949: "", 1950: "", 1951: "",
                 1952: "Here in My Heart\nbyAl Martino",1953: "I Believe\nby\nFrankie Laine",
                 1954: "Secret Love\nby\nDoris Day", 1955: "Rose Marie\nby\nSlim Whitman",
                 1956: "I'll Be Home\nby\nPat Boone", 1957: "Diana\nby\nPaul Anka",
                 1958: "Jailhouse Rock\nby\nElvis Presley", 1959: "Living Doll\nby\nCliff Richard",
                 1960: "It's Now or Never\nby\nElvis Presley", 1961: "Wooden Heart\nby Elvis Presley",
                 1962: "I remember You\nby\nFrank Ifield", 1963: "She Loves You\nby\nThe Beatles",
                 1964: "Can't Buy Me Love\nby\nThe Beatles", 1965: "Tears\nby\nKen Dodd",
                 1966: "Green, Green \nGrass of Home\nby\nTom Jones", 1967: "Release Me\n\by Englebert\nHumperdinck",
                 1968: "Hey Jude\n\nby\nThe Beatles", 1969: "Sugar, Sugar\n\by\nThe Archies",
                 1970: "The Wonder of You\nby\nElvis Presley", 1971: "My Sweet Lord\nby\nGeorge Harrison",
                 1972: "Amazing Grace\nby\nThe Royal Scots\nDragoon Guards", 1973: "Tie a Yellow Ribbon\nRound the Ole Oak\nTree\nby\nDawn with Tony\nOrlando",
                 1974: "Tiger Feet\n\by\nMud", 1975: "Bye Bye Baby\nby\nBay City Rollers",
                 1976: "Save Your Kisses\n for Me\nby\nBrotherhood of Man", 1977: "Mull of Kintyre\nby\nWings",
                 1978: "Rivers of Babylon\nBrown Girl in\nthe Ring\nby Boney M", 1979: "Bright Eyes\nby\nArt Garfunkel",#
                 1980: "Don't Stand So\nClose to Me\nby\nThe Police",1981: "Tainted Love\nby Soft Cell",
                 1982: "Come On Eileen\nby\nDexys Midnight\nRunners", 1983: "Karma Chameleon\nby\nCulture Club",
                 1984: "Do They Know It's\nChristmas\nby\nBand Aid", 1985: "The Power of Love\nby\nJennifer Rush",
                 1986: "Dont' Leave Me\nThis Way\nby\nThe Communards",1987: "Never Gonna Give\nYou Up\nby\nRick Astley",
                 1988: "Mistletoe and Wine\nby\nCiff Richard", 1989: "Ride on Time\nby\nBlack Box",
                 1990: "Unchained Melody by\nThe Righteous Bros", 1991: "Everything I Do\nI Do It For You\nby\nBryan Adams",
                 1992: "I Will Always\nLove You\nby\nWhitney Houston", 1993: "I'd Do Anything for\nLove But I won't\nDo That\nby\nMeat Loaf",
                 1994: "Love is All Around\nby\nWet Wet Wet", 1995: "Unchained Melody\nby\nRobson & Jerome",
                 1996: "Killing Me Softly\nby\nFugees", 1997: "Candle in The Wind\nby\nElton John",
                 1998: "Believe\nby\nCher", 1999: "Baby One More Time\nby\nBritney Spears", 2000: "Can We Fix It\nby\nBob the Builder",
                 2001: "It Wasn't Me\nby\nShaggy with Ritrok", 2002: "Anything is\nPossible\Evergreen\nby\nWill Young",
                 2003: "Where is the Love\nby\nThe Black Eyed Peas", 2004: "Do They Know It's\nChristmas\nby\nBand Aid 20",
                 2005: "Is This The Way to\nAmarillo\nby\nTony Christie with\nPeter Kay", 2006: "Crazy\nby\nGnaris Barkley",
                 2007: "Bleeding Love\nby\nLeona Lewis", 2008: "Hallelujah\nby\nAlexandra Burke",
                 2009: "Poker Face\nby\nLady Gaga", 2010: "Love the Way \nYou Lie\nby\nEminem with\nRihanna",
                 2011: "Someone Like You\nby\nAdele", 2012: "Somebody I That I\nUsed To Know\nby\nGotye with\nKimbra",
                 2013: "Blurred Lines\nby\nRobin Thicke with\nT.I. and Pharrel\nWilliams", 2014: "Happy\nby\nPharrel Williams",
                 2015: "Uptown Funk\nby\nMark Ronson with\nBruno Mars", 2016: "One Dance\nby\nDrake with\nWizkid and Kyla",
                 2017: "Shape of You\nby\nEd Sheeran", 2018: "One Kiss\nby\nCalvin Harris with\n Dua Lipa"}
    
    return    
        
                 
def actor():
    
    global bestActor
    
    bestActor = {1925: "", 1926: "", 1927: "", 1928: "", 1929: "", 1930: "", 1931: "",
                 1932: "", 1933: "", 1934: "Clark Gable in\n It Happened One\n Night", 1935: "Victor McLaglen in\n The Informer",
                 1936: "Paul Muni in\n The Story of \nLouis Pasteur", 1937: "Spencer Tracy in\n Captains Courageous",
                 1938: "Spencer Tracy in\n Boys Town", 1939: "Robert Donat in\n Goodbye, Mr. Chips",
                 1940: "James Stewart in\n The Philadelphia\n Story", 1941: "Gary Cooper in\n Sergeant York",
                 1942: "James Cagney  \n Yankee Doodle Dandy", 1943: "Paul Lukas in\n Watch on the Rhine",
                 1944: "Bing Crosby in\n Going My Way", 1945: "Ray Milland in\n The Lost Weekend",
                 1946: "Fredric March in\n The Best Years\n of Our Lives", 1947: "Ronald Colman in\n A Double Life",
                 1948: "Laurence Olivier in\n Hamlet", 1949: "Broderick Crawford in\n All the King's Men",
                 1950: "José Ferrer in\n Cyrano de Bergerac", 1951: "Humphrey Bogart in\n The African Queen",
                 1952: "Gary Cooper in\n High Noon", 1953:  "William Holden in\n Stalag 17",
                 1954: "Marlon Brando in\n On the Waterfront", 1955: "Ernest Borgnine in\n Marty",
                 1956: "Yul Brynner in\n The King and I", 1957: "Alec Guinness in\n The Bridge on the \nRiver Kwai",
                 1958: "David Niven in\n Separate Tables", 1959: "Charlton Heston in\n Ben-Hur",
                 1960: "Burt Lancaster in\n Elmer Gantry", 1961: "Maximilian Schell  in\n Judgment at\n Nuremberg",
                 1962: "Gregory Peck in\n To Kill a \nMockingbird", 1963: "Sidney Poitier in\n Lilies of the Field",
                 1964: "Rex Harrison in\n My Fair Lady", 1965: "Lee Marvin in\n Cat Ballou",
                 1966: "Paul Scofield in\n A Man for All Seasons", 1967: "Rod Steiger in\nIn the Heat of\nthe Night",
                 1968: "Cliff Robertson in\n Charly", 1969: "John Wayne in\n True Grit",
                 1970: "George C. Scott in\n Patton", 1971: "Gene Hackman in\n The French\n Connection",
                 1972: "Marlon Brando in\n The Godfather", 1973: "Jack Lemmon in\n Save the Tiger",
                 1974: "Art Carney in\nHarry and Tonto",
                 1975: "Jack Nicholson in\n One Flew Over the\n Cuckoo's Nest", 1976: "Peter Finch in\n Network",
                 1977: "Richard Dreyfuss in\n The Goodbye Girl", 1978: "Jon Voight in\n Coming Home",
                 1979: "Dustin Hoffman in\n Kramer vs. Kramer", 1980: "Robert De Niro in\n Raging Bull",
                 1981: "Henry Fonda in\n On Golden Pond",
                 1982: "Ben Kingsley in\n Gandhi", 1983: "Robert Duvall in\n Tender Mercies",
                 1984: "F. Murray Abraham\nin Amadeus", 1985: "William Hurt in\nKiss of the\n Spider Woman",
                 1986: "Paul Newman in\n The Color of Money", 1987: "Michael Douglas  in\n Wall Street",
                 1988: "Dustin Hoffman in\n Rain Man", 1989: "Daniel Day-Lewis  in\n My Left Foot",
                 1990: "Jeremy Irons in\n Reversal of Fortune", 1991: "Anthony Hopkins in\nThe Silence of\n the Lambs",
                 1992: "Al Pacino in\n Scent of a Woman", 1993: "Tom Hanks in\n Philadelphia",
                 1994: "Tom Hanks in\n Forrest Gump", 1995: "Nicolas Cage in\n Leaving Las Vegas",
                 1996: "Geoffrey Rush in\n Shine", 1997: "Jack Nicholson in\n As Good as It Gets",
                 1998: "Roberto Benigni in\n Life Is Beautiful", 1999: "Kevin Spacey in\n American Beauty",
                 2000: "Russell Crowe  in\n Gladiator", 2001: "Denzel Washington\nin Training Day",
                 2002: "Adrien Brody in\n The Pianist", 2003: "Sean Penn in\n Mystic River",
                 2004: "Jamie Foxx in\n Ray", 2005: "Philip Seymour\nHoffman in Capote",
                 2006: "Forest Whitaker in\n The Last King \nof Scotland", 2007: "Daniel Day-Lewis in\n There Will Be Blood",
                 2008: "Sean Penn  in\n Milk", 2009: "Jeff Bridges in\n Crazy Heart",
                 2010: "Colin Firth in\n The King's Speech", 2011: "Jean Dujardin in\n The Artist",
                 2012: "Daniel Day-Lewis in\n Lincoln", 2013: "Matthew McConaughey\nin\nDallas Buyers Club",
                 2014: "Eddie Redmayne in\nThe Theory of \nEverything", 2015: "Leonardo DiCaprio in\n The Revenant",
                 2016: "Casey Affleck in\nManchester\nby the Sea", 2017: "Gary Oldman  in\nDarkest Hour",
                 2018: "Rami Malek in\n Bohemian Rhapsody",}
    
    return

def worldcup():
    
    global football
    
    football = {1930: "Uruguay", 1934: "Italy", 1938: "Italy", 1950: "Uruguay", 1954: "West Germany", 1958: "Brazil", 1962: "Brazil",
                1966: "England",1970: "Brazil", 1974: "West Germany", 1978: "Argentina", 1982: "Italy", 1986: "Argentina", 1990: "West Germany", 1994: "Brazil",
                1998: "France",2002: "Brazil",2006: "Italy",2010: "Spain",2014: "Germany",2018:"France"}
    
    return

def peopleBorn():
    
    global addPeople
    
    addPeople = {1930 : 'Sean Connery ' , 1931 : 'William Shatner &\n Leonard Nimoy ' ,1932 : 'Johnny Cash &\n Peter OToole ' , 
    1933 : 'Michael Caine and\n Yoko Ono ' ,1934 : 'Yuri Gagarin and\n Fankie Valli ' , 1935 : 'Elvis Presley ' , 
    1936 : 'Roy Orbison and\n Robert Redford ' , 1937 : 'Jack Nickolson and\n Dustin Hoffman ' , 
    1938 : 'Oliver Reed and\n Rudolph Nureyev ' , 1939 : 'Ian McKellen and\n Jackie Stewart ' , 
    1940 : 'Tom Jones\n John Lennon and\n Ringo Starr ' , 1941 : 'Neil Diamond and\n Bob Dylan ' , 
    1942 : 'Stephen Hawking and\n Paul McCartney ' ,1943 : 'George Harrison,\n Mick Jagger and\n Keith Richards ' , 
    1944 : 'Michael Douglas and\n Danny DeVito ' ,1945 : 'Rod Stewart and\n Eric Clapton ' , 
    1946 : 'Dolly Parton\n Joanna Lumley\n Donald Trump  and\nFreddie Mercury ' , 
    1947 : 'David Bowie,\n Elton John and\nArnold\n Schwartzenneger ' , 1948 : 'Andrew Lloyd\n Webber,\n Prince Charles\n and Ozzy Osbourne ' , 
    1949 : 'Jeremy Corbyn,\n Meryl Streep and\n Bruce Springsteen ' , 1950 : 'Richard Branson and\n Princess Anne ' , 
    1951 : 'Bonnie Tyler,\n Robin Williams and\n Sting ' , 1952 : 'Vladimir Putin ' ,1953 : 'Tony Blair and\n Kim Basinger ' , 
    1954 : 'Oprey Winfrey,\n John Travolta and\n Angela Merkel ' , 1955 : 'Rowan Atkinson,\n Kevin Costner and\n Bruce Willis ' , 
    1956 : 'Tom Hanks and\n Theresa May ' , 1957 : 'Stephen Fry and\n Osama Bin Laden ' , 
    1958 : 'Madonna,\n Michelle Pfeffer\n and Kevin Bacon ' , 1959 : 'Sean Bean,\n Hugh Laurie and\n Simon Cowell ' , 
    1960 : 'Prince Andrew,\n Diego Maradona\n and Bono ' , 1961 : ' George Clooney,\n Ricky Gervais and\n Princess Diana ' , 
    1962 : 'Jim Carrey,\n Jon Bon Jovi\n and Tom Cruise ' ,1963 : 'Johnny Depp,\n Whitney Houston\n and Brad Pitt ' , 
    1964 : 'Prince Edward,\n Boris Johnson\n and Keanu Reeves  ' ,1965 : 'Robert\n Downey Jnr,\n J K Rowling \nand Ben Stiller ' , 
    1966 : 'Chris Evans,\n Mike Tyson and\n Kiefer Sutherland ' , 1967 : 'Kurt Cobain,\n Noel Gallagher and\n Boris Becker ' , 
    1968 : 'Daniel Craig,\n Kylie Minogue\n and Will Smith ' , 1969 : 'Jennifer Aniston,\n Jennifer Lopez and\nMatthew McConaughey ' , 
    1970 : 'Mariah Carey,\n Matt Damon and\n River Phoenix ' , 1971 : 'Pep Guardiola,\n Ewan McGregor\n and Elon Musk ' , 
    1972 : 'Tim Peake,\n Dwayne Johnson and\n Zinedine Zidane ' ,1973 : 'Lee Westwood,\n Heidi Klum and\n Peter Kay ' , 
    1974 : 'Leonardo DiCaprio,\n Robbie Williams and\n Victoria Beckham ' ,1975 : 'David Beckham,\n Jamie Oliver and\n Tiger Woods ' , 
    1976 : 'Reese Witherspoon,\n Benedict\n Cumberbatch\nand Ryan Reynolds ' ,1977 : 'Orlando Bloom,\nShakira and\n Kanye West ' , 
    1978 : 'Frank Lampard\n and Usher ' , 1979 : 'Heath Ledger,\n James McAvoy\n and Pink ' , 
    1980 : 'Xavi,\n Stephen Gerrard and\n Kim Kardashian ' ,1981 : 'Justin Timberlake,\n Beyonce and\nDuchess of Sussex ' , 
    1982 : 'Duchess of\n Cambridge, Prince\nWilliam and\nAnne Hathaway ' ,1983 : 'Emily Blunt,\n Mo Farah and\n Cheryl ' , 
    1984 : 'Fernando Torres,\n Mark Zuckerberg\n and Prince Harry ' , 1985 : 'Lewis Hamilton,\n Cristiano Ronaldo\n and Wayne Rooney ' , 
    1986 : 'Lady Gaga and\n Gemma Arterton ' , 1987 : 'Lionel Messi,\n Andy Murray and\n Novak Djokovic ' , 
    1988 : 'Rihanna,\n Adele and\n Emma Stone ' , 1989 : 'Gareth Bale,\n Daniel Radcliffe\n and Taylor Swift ' , 
    1990 : 'Jennifer Lawrence\n and Emma Watson ' , 1991 : 'Ed Sheeran and\n Antoine Griezmann ' , 
    1992 : 'Neymar, Sam Smith\n and Miley Cyrus ' , 1993 : 'Paul Pogba and\n Harry Kane  ' , 
    1994 : 'Dakota Fanning,\n Harry Styles\nand Tom Daley ' , 1995 : 'Kendall Jenner ' } 

    return



def rerun():

    canvas.destroy()
    openscreen()
    
    return

    
openscreen()

    







