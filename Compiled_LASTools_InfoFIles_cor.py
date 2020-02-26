#This script was written by Warren Kunkler on 8/29/2016 in support of the 2016 Clark County Lidar Project. The final product of this
#script is a table of data generated from LASTools that can be joined to the data in mars based on the ID field

import os



#input1_ws points to the directory where all the info files you'd like to compile are
input1_ws = r"D:\LiDARData"





#prompts the user for input as to the QL level of the LiDAR data
QL = raw_input("Please enter QL level for info files: ")



#creates a writeVar that outputs the final product located in the same directory where the rest of info files are
writeVar = open(input1_ws + '\\Compiled_Lidar_Info_Raw_Flightline_QL2.txt', 'w')

#writes the first line to the compiled file, this acts as the column headers for the final product
writeVar.write("ID\t" + "QL\t" + "last\t" + "Density(All)\t" + \
                           "Density(Last)\t" + "Spacing(All)\t" + "Spacing(Last)\n")

#initialize an empty list
Content_List = []



for root, dirs, files in os.walk(input1_ws):
    for filename in files:
        if filename[-4:] == ".txt":

          
            Table_Key = filename[-28:-9:1] + '.las' + '\t'

            
            ReadFile_Name = input1_ws + '\\' + filename
            readVar = open(ReadFile_Name, 'r')

            for i in readVar:
                Content_List.append(i)
            readVar.close()


            Last_Returns = Content_List[47][-15:-1:1] + '\t'
            
            Point_Density1 = Content_List[50][-40:-35:1] + '\t'
            Point_Density2 = Content_List[50][-25:-20:1] + '\t'
            Spacing1 = Content_List[51][-31:-27:1] + '\t'
            Spacing2 = Content_List[51][-16:-12:1] +'\n'

             
            writeVar.write(Table_Key)
            writeVar.write(QL)
            writeVar.write(Last_Returns)
            writeVar.write(Point_Density1)
            writeVar.write(Point_Density2)
            writeVar.write(Spacing1)
            writeVar.write(Spacing2)

            
            del Content_List[:]


            
writeVar.close()
readVar.close()





