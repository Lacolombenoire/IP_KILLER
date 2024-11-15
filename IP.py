import re


class IP :


    # List of different patern of IP adress

    # If the IP adress is
    IP_PATERN_1 = "\A\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?=\D)" # at the beguining of the string
    IP_PATERN_2 = "(?<=\D)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?=\D)" # at the middle of the string
    IP_PATERN_3 = "(?<=\D)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\Z" # at the end of the string
    IP_PATERN_4 = "\A\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\Z" # occupying all the string

    # Combine all the patern
    IP_PATERN = IP_PATERN_1 + "|" + IP_PATERN_2 + "|" + IP_PATERN_3 + "|" + IP_PATERN_4
    # Patern to reconize a number 
    NUMBER_PATERN = "\d{1,3}"

    @classmethod
    def is_string_ip_adress(classe, string : str) :
        # Return true : If the string is a ip adress
        # Return false if the string is not an ip adress

        # Found all ip adress in the string (see patern "IP_PATERN")
        # return a list of all ip adress founded
        founded_ip = re.findall(IP.IP_PATERN, string)


        # Set the return value to false (become true if the string is an ip adress)
        Good_format = False


        # Chack if the liste contains 1 element
        if len(founded_ip) == 1 :

            # Check if the element is equal the the string
            if founded_ip[0] == string :

                # The string is a ip adress
                # Set the return value to True
                Good_format = True


        # Return the value
        return Good_format

    def __init__(self, str_ip : str):


        if IP.is_string_ip_adress(str_ip) :

            founded_numbers = re.findall(IP.NUMBER_PATERN, str_ip)

            
            self.number_1 = founded_numbers[0]
            self.number_2 = founded_numbers[1]
            self.number_3 = founded_numbers[2]
            self.number_4 = founded_numbers[3]

        else :
            raise(ValueError, str_ip + " is not an ip adress")
            
        
    @classmethod
    def ip_to_ip_patern(classe, ip_string : str) :

        # Check if the string is 
        if not IP.is_string_ip_adress(ip_string) :
            raise (ValueError, ip_string + " is not an ip adress")



        # Return a list of all numbers in the ip adress (See NUMBER_PATERN)
        list_ip_number = re.findall(IP.NUMBER_PATERN, ip_string)
        print(list_ip_number)


        # Set a return varable of the patern 
        ip_patern = ""

        # Set a counter to remember the index of the list_ip_number
        cpt = 0

        # Read the entier list of number in the ip adress string
        for number in list_ip_number :
            
            cpt += 1
            # Add the number the patern
            ip_patern = ip_patern + number

            # if index is not the last element of the list number
            if cpt < len(list_ip_number) :

                # Add the special caracter for the point
                ip_patern = ip_patern + "\\."
                

        
        print(ip_patern)
        return ip_patern
            



