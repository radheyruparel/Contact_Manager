#
##Author: Radhey Ruparel
##Description: This program  a very simple contact organizer application in Python,
##for managing the phone numbers and email addresses of friends, co-workers, and acquaintances. 
#

#Required to import all the os functions and program is able to locate the file
import os
os.chdir(os.path.dirname(__file__))

#Importing all the modules for the program execution  
import sys

def storing_data_from_file(unqiue_contacts):
    
    '''This functions reads the data from a contacts.txt text file. And make them into indivilual tuples of
   contacts and those tuples in main set of contacts
   The paramater varible for this function is unqiue_contacts, which is a set''' 
    
    #Opening the contact text file
    file_choosen=open('contacts.txt','r')
    
    #This loop will read the file, and split lines into single words and then load them into a word list
    for lines in file_choosen:
        
        #Striping the default \n from and Splitting the line into words
        information=lines.rstrip('\n').split(' | ')
        #This a tempemory tuple, just to add it to the main set
        temp_contact=tuple(information)
        #Loading those words into a word list
        unqiue_contacts.add(temp_contact)
    
    #Closing the user selected file
    file_choosen.close()
    
def adding_contact(unqiue_contacts):
    
    '''This funtion add contacts to the main set of contacts and also checks for duplicates, it does
    not add the duplicates. 
    The paramater varible for this function is unqiue_contacts, which is a set''' 
    
    #This ask the user to enter name the of the contact
    contact_name=input('name:')
    #This ask the user to enter email the of the contact
    contact_email=input('\nemail:')
    #This ask the user to enter phone number the of the contact
    contact_phone=input('\nphone:')
    #This combines all the inpuuted information into a tuple for adding or checking if it is duplicate
    temp_contact=(contact_name,contact_email,contact_phone)
    
    #If the set of contacts is empty, then just direactly add the contact 
    if unqiue_contacts==set():
        #Add the contact to the main set 
        unqiue_contacts.add(temp_contact)
        #Print the message that the contact is added
        print('\nContact added!')
    #If the set is not empty check if the inputted contact is a dupicate
    else:
        #keeping track of contact checking
        contact_record=0
        #Checking the dupicate by comparing one by one
        for single_contact in unqiue_contacts:
            #Duplicate contact only counts if all the three information exits 
            if single_contact[0]==contact_name and single_contact[1]==contact_email and single_contact[2]==contact_phone:
                print('\nContact already exists!')
            else:
                #Just add one to the count, so we know how many contacts were compared
                contact_record+=1
        
        #After all the inputed contacts id not a duplicate, then only add the contact to the main set 
        if contact_record==(len(unqiue_contacts)):
            #Print the message that the contact is added
            print('\nContact added!')
            #Add the contact to the main set 
            unqiue_contacts.add(temp_contact)

    
def saving_contacts(unqiue_contacts):
    '''This function opens the contacts.txt file and writes all the contacts into that file, if the user
    wants to exit the program. In order to save the contacts, the contacts are wriiten in certain form.
    The paramater varible for this function is unqiue_contacts, which is a set'''
    
    #Open the file in write mode 
    file_choosen=open('contacts.txt','w')
    
    #Get one contact turn by turn
    for single_contact in unqiue_contacts:
        #Making contacts into a single string, into certian formate 
        information_line=str(single_contact[0])+' | '+str(single_contact[1])+' | '+str(single_contact[2])+'\n'
        #Write that string in the text file
        file_choosen.write(information_line)
    
    #Closing the user selected file
    file_choosen.close()

def reterving_contacts(unqiue_contacts,user_command):
    '''This function helps to display and search for contacts in the set , which is 
    asked by the user. 
    The paramater varaible for this function is unqiue_contacts, which is a set
    Another varaible is user_command, which is a string'''
    
    #keeping track of contact checking
    contact_count=0
    #Checking the contact one by one
    for single_contact in unqiue_contacts:
        #Splitting the user_command in order to match and serach 
        search_input=user_command.split(' ')
        #If the contact is serached by full name
        full_name=search_input[-2]+' '+search_input[-1]
        #tring to match the full name with saved contacts
        if full_name==single_contact[0]:
            #if the contact is found, print the name 
            print(single_contact[0]+'\'s','contact info:')
            #print the contact's email
            print('  email:',single_contact[1])
            #Print the contact's phone
            print('  phone:',single_contact[2])
        #if the contact is serach by anything else other than full name
        else:
            #Trying to match email, frist name or phone with saved contacts
            for contant_information in single_contact:
                #If they match print the contact
                if search_input[-1]==contant_information:
                    #if the contact is found, print the name 
                    print(single_contact[0]+'\'s','contact info:')
                    #print the contact's email
                    print('  email:',single_contact[1])
                    #Print the contact's phone
                    print('  phone:',single_contact[2])
                else:
                    #To keep the track, of much information was matched
                    contact_count+=1
    #As we are comparing the  
    contact_count=contact_count//3
    #If the contact count is equal to the number of contacts than means the contact user is seraching is
    #Not found
    if contact_count==(len(unqiue_contacts)):
        #Print the message 
        print('None')

#Declaring the main function
def main():
    #Delcaring the main set for storing contacts
    unqiue_contacts=set()
    #Calling this function, if the text file have contacts, it can be load in the main set of contacts
    storing_data_from_file(unqiue_contacts)
    #Print the openning message
    print('Welcome to the contacts app!')
    
    #An infinite loop to repeated ask for input
    while True:
        #Getting the user command 
        user_command=input('>\n')
        #If the user wants to add the contact
        if 'add contact' in user_command:
            #Calling the function to add the contact to main set and check for dupilcates
            adding_contact(unqiue_contacts)
        
        #if the user wants to search a contact
        elif 'show contacts with' in user_command:
            #calling this function will serach the contact and display the contact information
            reterving_contacts(unqiue_contacts,user_command)
        
        #If the user wants to exit the program
        elif 'exit' in user_command:
            #print a goodbye message
           print('Goodbye!')
           #This will write the contacts in a text file to save contacts
           saving_contacts(unqiue_contacts)
           #break the loop to stop the progra,
           break

#Calling the main function
main()