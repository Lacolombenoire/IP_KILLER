from ERASER import *
import unittest



class tester(unittest.TestCase) :




    def testing(self) :


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



        # Test is_texte_filepath
        self.assertEqual(ERASER.is_texte_filepath("dogbogberi.txt") , False, "Unexisting file detected")
        self.assertEqual(ERASER.is_texte_filepath("C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1/TEST.txt") , True, "Unexisting file detected")
        self.assertEqual(ERASER.is_texte_filepath("C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1/TEST.") , False, "Unexisting file detected")
        self.assertEqual(ERASER.is_texte_filepath("C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1/TEST.tx") , False, "Unexisting file detected")
        self.assertEqual(ERASER.is_texte_filepath("C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1/TEST.TXT") , False, "Unexisting file detected")
        self.assertEqual(ERASER.is_texte_filepath("C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1/TES.txt") , False, "Unexisting file detected")


        # test txt_to_string
        self.assertEqual(ERASER.txt_to_string(TEST3),"""wognberw

defbvfde
ds

asgv
asgv

sfasdfsadf


asdfsadfsadf
sascs
asdfsadfsadffas
f
sascsdf








""", "Unreadable content" )
        

        self.assertEqual(ERASER.txt_to_string(TEST2), """192.198.30.1





233.198.30.2


192.198.30.1sgswfe

192.198.30.1192.198.30.1


svwbfowe
svs
aadfasd

zczcx192.198.30.1wf



192.198.30.1""", "Unreadeble content")
        




        self.assertEqual(ERASER.txt_to_string("C:/Users/nicol/OneDrive/Bureau/IP_KILLER/TEST/1/TEST.txt"), """192.00.00.000


Je veux manger des patates1905435.55.43.2









""", "Unreadable content")
        




        
        ERASER.ip_killer(TEST1, Result1, Result)
        ERASER.ip_killer(TEST2, Result2, Result)
        ERASER.ip_killer(TEST3, Result3, Result)
        ERASER.ip_killer(TEST4, Result4, Result)
        

        self.assertEqual(ERASER.txt_to_string(Filepath1), ERASER.txt_to_string(SOLUTION1), "The solution 1 is not equal")
        self.assertEqual(ERASER.txt_to_string(Filepath2), ERASER.txt_to_string(SOLUTION2), "The solution 2 is not equal")
        self.assertEqual(ERASER.txt_to_string(Filepath3), ERASER.txt_to_string(SOLUTION3), "The solution 3 is not equal")
        self.assertEqual(ERASER.txt_to_string(Filepath4), ERASER.txt_to_string(SOLUTION4), "The solution 4 is not equal")







if __name__ == '__main__' :
    unittest.main()













