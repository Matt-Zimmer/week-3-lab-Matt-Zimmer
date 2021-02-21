######################################
# IT 2750 - Spring 2021 - Week 3 Lab #
# Password Cracking                  #
# Author: Matt Zimmer                #
# Student: S00646766                 #
######################################

############################################
####  SCROLL DOWN  #########################
####  DON'T EDIT CODE IN THIS SECTION  #####
############################################

# Import the zipfile module
import zipfile

# Open a zip file with a given password
def openZip(file, password=''):
    # Create a new zip file object and open
    # the zip file
    zip = zipfile.ZipFile(file)

    # Attempt to extract all contents of the zip file
    # to the current directory. Return True if success
    # and False if failure
    try:
        if password == '':
            zip.extractall()
        else:
            zip.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except Exception as e:
        return False

############################################
####  START FROM HERE  #####################
############################################

# Step 1: Create a list variable and initialize it with the
# first 10 of the top 25 most used passwords in 2019, per the following link:
# https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
# USE THE FIRST TABLE, "According to SplashData"

passwords = ['123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345', 'iloveyou', '111111', '123123']


# Step 2: Ask the user for the filename of the zip file that
# we will attempt to crack (just the filename, not the full
# path... make sure the actual zip file is in the same
# directory as the python script and that the current working
# directory in the command prompt is that same directory)

fileName = (input("What zip file do you want to use? "))


# Step 3: Create a loop that iterates through each password
# in the list. You can use a while loop or for loop

 

for passwordType in passwords:
    print("Attempting Password... " + passwordType)

     

#      Step 4: For each iteration of the loop, attempt to crack
#      the zipfile password by calling the openZip function and
#      passing the filename and the password to try. The openZip
#      function returns True if it was successful and False if it
#      was not. An example of calling the function is
#      result = openZip(filename, password)

filename = True 
result = openZip(filename, passwordType)


#      Step 5: For each iteraton of the loop, let the user know
#      what the result of the crack attempt was (True = success,
#      False = failure) and what password was tried

for passwordType in passwords:
    
    if passwordType != "":
        print('...failed')
    else:
        print('...Success!!!')
    