from tkinter import *
from State_Info import States

main = Tk()
main.title('I\'m the main window')
main.geometry("500x500")

alabama = States("Alabama", "Montgomery", "AL", "Birmingham")
alaska = States("Alaska", "Juneau", "AK", "Anchorage")
arizona = States("Arizona", "Phoenix", "AZ", "Phoenix")
arkansas = States("Arkansas", "Little Rock", "AR", "Little Rock")
california = States("California", "Sacramento", "CA", "Los Angeles")
colorado = States("Colorado", "Denver", "CO", "Denver")
connecticut = States("Connecticut", "Hartford", "CT", "Bridgeport")
delaware = States("Delaware", "Dover", "DE", "Wilmington")
florida = States("Florida", "Tallahassee", "FL", "Jacksonville")
georgia = States("Georgia", "Atlanta", "GA", "Atlanta")
hawaii = States("Hawaii", "Honolulu", "HI", "Honolulu")
idaho = States("Idaho", "Boise", "ID", "Boise")
illinois = States("Illinois", "Springfield", "IL", "Chicago")
indiana = States("Indiana", "Indianapolis", "IN", "Indianapolis")
iowa = States("Iowa", "Des Moines", "IA", "Des Moines")
kansas = States("Kansas", "Topeka", "KS", "Wichita")
kentucky = States("Kentucky", "Frankfort", "KY", "Louisville")
louisiana = States("Louisiana", "Baton Rouge", "LA", "New Orleans")
maine = States("Maine", "Augusta", "ME", "Portland")
maryland = States("Maryland", "Annapolis", "MD", "Baltimore")
massachusetts = States("Massachusetts", "Boston", "MA", "Boston")
michigan = States("Michigan", "Lansing", "MI", "Detroit")
minnesota = States("Minnesota", "St. Paul", "MN", "Minneapolis")
mississippi = States("Mississippi", "Jackson", "MS", "Jackson")
missouri = States("Missouri", "Jefferson City", "MO", "Kansas City")
montana = States("Montana", "Helena", "MT", "Billings")
nebraska = States("Nebraska", "Lincoln", "NE", "Omaha")
nevada = States("Nevada", "Carson City", "NV", "Las Vegas")
new_hamshire = States("New Hampshire", "Concord", "NH", "Manchester")
new_jersey = States("New Jersey", "Trenton", "NJ", "Newark")
new_mexico = States("New Mexico", "Santa Fe", "NM", "Albuquerque")
new_york = States("New York", "Albany", "NY", "New York")
north_carolina = States("North Carolina", "Raleigh", "NC", "Charlotte")
north_dakota = States("North Dakota", "Bismarck", "ND", "Fargo")
ohio = States("Ohio", "Columbus", "OH", "Columbus")
oklahoma = States("Oklahoma", "Oklahoma City", "OK", "Oklahoma City")
oregon = States("Oregon", "Salem", "OR", "Portland")
pennsylvania = States("Pennsylvania", "Harrisburg", "PA", "Philadelphia")
rhode_island = States("Rhode Island", "Providence", "RI", "Providence")
south_carolina = States("South Carolina", "Columbia", "SC", "Charleston")
south_dakota = States("South Dakota", "Pierre", "SD", "Sioux Falls")
tennessee = States("Tennessee", "Nashville", "TN", "Nashville")
texas = States("Texas", "Austin", "TX", "Houston")
utah = States("Utah", "Salt Lake City", "UT", "Salt Lake City")
vermont = States("Vermont", "Montpelier", "VT", "Burlington")
virginia = States("Virginia", "Richmond", "VA", "Virginia Beach")
washington = States("Washington", "Olympia", "WA", "Seattle")
west_virginia = States("West Virginia", "Charleston", "WV", "Charleston")
wisconsin = States("Wisconsin", "Madison", "WI", "Milwaukee")
wyoming = States("Wyoming", "Cheyenne", "WY", "Cheyenne")

state_list = [alabama, alaska, arizona, arkansas, california,
colorado, connecticut, delaware, florida, georgia, hawaii,
idaho, illinois, indiana, iowa, kansas, kentucky, louisiana,
maine, maryland, massachusetts, michigan, minnesota,
mississippi, missouri, montana, nebraska, nevada, new_hamshire,
new_jersey, new_mexico, new_york, north_carolina, north_dakota,
ohio, oklahoma, oregon, pennsylvania, rhode_island,
south_carolina, south_dakota, tennessee, texas, utah, vermont,
virginia, washington, west_virginia, wisconsin, wyoming
]

print(alabama.show_name())
#for x in state_list:
#    x.show_name() + x.show_abrev()
#print(len(state_list))
main.mainloop()