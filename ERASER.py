
import re
from IP import *
import IP_base
import pathlib

class ERASER :

    counter = 1
    ip_book = {}
    sentence = "IP_ADRESS_"
    TEXT_FILE_PARTERN = ".*\.txt\Z"




    @classmethod
    def is_texte_filepath(classe, filepath : str) :
        # verify if 
            # The path exist
            # The path redirect to a text file
        
        # Create a path varable
        path = pathlib.Path(filepath)

        # Verify if the path is a text filepath

        parten_result = re.findall(ERASER.TEXT_FILE_PARTERN, filepath)

        # Verify if there is on path (one time the patern) of text file
        is_text_file = len(parten_result) == 1
        # Verify if the string is excalyt a text file
        is_text_file = is_text_file and parten_result[0] == filepath


        # Verify if the text file exist
        return is_text_file and path.exists()
        



    @classmethod
    def txt_to_string(classe, filepath : str) :
        # Take the content of file and put it to a str varable

        # If the path exist
        if ERASER.is_texte_filepath(filepath) :
            with open(filepath, 'r') as file :
                return file.read()
            
    
        raise(ValueError, "This is not a txt file or the path do not exist")
            
    @classmethod
    def counter_increment(classe) :
        # Increment the counter for the name remplacement of each ip adress
        ERASER.counter += 1

    @classmethod
    def add_ip_book(classe, ip_adress : str) :
        # Add the string containing only an ip adress to the book of ip adress



        # Looking if the string is an ip_adress
        if not IP.is_string_ip_adress(ip_adress) :
            raise(ValueError, ip_adress + " is not an ip adress")


        # Convert the ip_adress into a patern ip adress
        # ip_adress = IP.ip_to_ip_patern(ip_adress)

        # if not in the ip book, add the ip patern (key) and remplacement content (value)
        if not ip_adress in ERASER.ip_book.keys() :
            ERASER.ip_book[ip_adress] = ERASER.sentence + str(ERASER.counter)
            ERASER.counter_increment()

    @classmethod
    def spot_ip_adress(classe, content : str) :
        # Return a liste of all the ip adresse in the content
        # No doubles

        # Fetch the regular expression in the ip class
        # This expression is used to reconize ip adress
        patern = IP.IP_PATERN


        # Return a list of all ip adress in the content
        list_ip_adress = re.findall(patern, content)


        # Return this list without doubles
        return list(set(list_ip_adress))
    

    @classmethod
    def replace_ip_adress(classe, Total_content : str, Content_to_replace : str, Content_replacing : str) :
        # Replace all the Content_to_replace string occurence in the Total_content string by the Content_replacing string
        list_part = re.split(IP.IP_PATERN, Total_content)
        list_ip_adress = re.findall(IP.IP_PATERN, Total_content)

        cpt = 0

        result = list_part[cpt]


        cpt += 1

        for ip_adress in list_ip_adress :
            ip_adress = ERASER.ip_book[ip_adress]

            result = result + ip_adress + list_part[cpt]

            cpt += 1


        return result




    @classmethod
    def fill_ip_book(classe , list_ip_adress : list[str]) :
        # Fill the IP book to make a dictionnairy
        # {string with the ip adress patern (help to reconize the ip adress in a string), string with the remplacement}
        for ip_adress in list_ip_adress :
            ERASER.add_ip_book(ip_adress)

    @classmethod
    def ip_killer(classe, src_filepath : str, destination_filepath : str, destination_filename : str) :
        # Main fonction to call to :
        # Take the content a log file in the "src_filepath"
        # Create a file in the "destination_filepath" with modify content (Without the ip adress)
        
        if not ERASER.is_texte_filepath(src_filepath) :
            raise(ValueError, src_filepath + " is not a path directing to a txt file")


        content = ERASER.txt_to_string(src_filepath)

        list_ip_target : list[str] = ERASER.spot_ip_adress(content)

        ERASER.fill_ip_book(list_ip_target)

        for ip_partern, string_remplacement in ERASER.ip_book.items() :
            content = ERASER.replace_ip_adress(content, ip_partern, string_remplacement)
        
        ERASER.create_clean_file(destination_filepath, destination_filename, content)

        ERASER.ip_book = {}
        ERASER.counter = 1




    @classmethod
    def create_clean_file(classe ,filepath : str, filename : str, content : str) :
        # Fonction to create a file with a certain name in a certain path
        # Then he will write the content into the created file
        

        # Set the full path of the generated file
        total_path = filepath + "/" + filename + ".txt"


        # Create a path object
        path = pathlib.Path(total_path)


        # Check if the file already exist
        if path.exists() :
            # Raise an error
            raise(ValueError, "The file " + filename + " already exist in this folder")
        


        # Create the file
        with open(total_path, "w") as new_file :
            # Write the content in the file
            new_file.write(content)

        # Return the path of the file
        return total_path



















