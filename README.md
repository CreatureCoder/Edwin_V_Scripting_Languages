# Edwin_V_Scripting_Languages

This is a respiratory dedicated to Edwin Vahlkamp's Python code 

# Scripts:
1. Module_2_SalaryCalculator
2. Module_4_Student_Maintenance
3. PE2_Module_2_&_3_PasswordValidator
4. PE2_Module_4_Data_validator

# Descrition:
<b>Module_2_SalaryCalculator: <br></b>
    Calculates the total salary of the user with and/or without holidays and vacations.<br>
<br>
<b>Module_4_Student_Maintenance: <br></b>
    Contains functions that list, add, update, and delete students in a dictionary.<br>
<br>
<b>PE2_Module_2_&_3_PasswordValidator: <br></b>
    Password Validator: <br>
        Allows end users to validate basic password. <br>
<br>
        Passwords must consist of a minimum of two capital letters, two lowercase letters, two digits, and two symbols. <br>
<br>
        When one of the conditions above is not met, the code will call the PasswordException file and store the errors in a <br>
        list.  The list is used for storing the different unmet conditions a password does not meet. <br>
<br>
        End users can choose the pre-created testing grounds or create their own password testing grounds to display if the <br>
        password is not valid and how they want to display the errors. <br>
<br>
        End users will call is_valid function to test if a password is valid or not. <br>
<br>
        End users can deside to activate the DEGUG MODE to see the number of uppercase letters, lowercase letters, digits, and <br>
        symbols the password contains. <br>
<br>
    Advance Password Validator: <br>
        Allows end users to validator passwords with more conditions. <br>
<br>
        Passwords must consist of a minimum of two capital letters, two lowercase letters, two digits, and two specific symbols, <br>
        and requires a minimum length of eight and a maximum length of 30.  The valid symbols are:!, @, #, $, and *. <br>
<br>
        When one of the conditions above is not met, the code will call the PasswordException file and store the errors in a <br>
        list.  The list is used for storing the different unmet conditions a password does not meet. <br>
<br>
        End users can choose the pre-created testing grounds or create their own password testing grounds to display if the <br>
        password is not valid and how they want to display the errors. <br>
<br>
        End users will call is_valid function to test if a password is valid or not. <br>
<br>
        End users can deside to activate the DEGUG MODE to see the number of uppercase letters, lowercase letters, digits, valid <br>
        symbols, and the number af characters the password contains. <br>

<b>PE2_Module_4_Data_validator:</b><br>
<br>
Assesses data from a file, validate if the data, and then sends the data to different files depending if the data is
good or not.<br>
<br>
Uses a testing_log.txt for the data and a valid_log.txt and an invalid_log.txt to store the data.<br>
<br>
Each string of data must consist of 6 parts in the correct formate:<br>
    id|last name,first name|email|phone number|date|time<br>
<br>
Example of valid data:<br>
    1|Johnson,Debbie|dejohns2@wsc.edu|111-222-3333|12/31/2019|13:40<br>
<br>
There are seven different errors the may occur:<br>
C = invalid data element count<br>
I = invalid id<br>
N = invalid name<br>
E = invalid email<br>
P = invalid phone number<br>
D = invalid date<br>
T = invalid time<br>
<br>
Note: if C was the error, there will not be any other errors.<br>
<br>
If any of the following errors occur the string will be written to the invalid_log.txt with the type or types of errors 
at the beginning of the string.<br>
<br>
Example of written invalid data:<br>
    IPDT|abc|Johnson|dejohns2@gmail.com|1112223333|12/31/80|1340<br>
<br>
If no errors occur then the valid data will be written to the valid_log.txt with some formatting.  The first name will 
be first and last name last, the phone number dashes becomes periods, and the data will be year-month-day.<br>
<br>
Example of written valid data:<br>
    1,Debbie,Johnson,dejohns2@wsc.edu,111.222.3333,2019-12-31,13:40<br>