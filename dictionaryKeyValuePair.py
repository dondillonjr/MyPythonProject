#Dictionary key value paire
#key -- value
#Jan -> January
#Mar -> March

monthCoversion = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

dayHolder = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}
################## MAIN #######################
print(monthCoversion["Jan"])
print(monthCoversion.get("Feb"))
print(monthCoversion.get("HEY","Not a valid key"))
print(dayHolder.get(7))