from ERASER import *

TEST1 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1/TEST.txt"
SOLUTION1 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1/SOLUTION.txt"
TEST2 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/2/TEST.txt"
SOLUTION2 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/2/SOLUTION.txt"
TEST3 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/3/TEST.txt"
SOLUTION3 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/3/SOLUTION.txt"
TEST4 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/4/TEST.txt"
SOLUTION4 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/4/SOLUTION.txt"





# test ip killer

Result = "result"
Result_txt = Result + ".txt"
Result1 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1"
Result2 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/2"
Result3 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/3"
Result4 = "C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/4"


Filepath1 = Result1 + "/" + Result_txt
Filepath2 = Result2 + "/" + Result_txt
Filepath3 = Result3 + "/" + Result_txt
Filepath4 = Result4 + "/" + Result_txt



string = ERASER.txt_to_string(TEST1)
list_ip_target = ERASER.spot_ip_adress(string)

ERASER.fill_ip_book(list_ip_target)

patern = IP.ip_to_ip_patern("192.00.00.000")
print(patern)

print(re.split(patern ,string ))


print(ERASER.replace_ip_adress(string, "192.00.00.000", "IP_ADRESS_1" ))




