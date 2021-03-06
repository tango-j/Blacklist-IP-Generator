import xlwt
import urllib
import requests
import re

#Blacklist IP

link = 'https://www.dshield.org/ipsascii.html?limit=100'
p = urllib.urlopen(link)
text = p.readlines()

wbk = xlwt.Workbook()
#creating 1st sheet in workbook
sheet = wbk.add_sheet('Top 100 Blacklist IP Addresses')
sheet.write(0,0,'IP Address')
sheet.write(0,1,'Reports')
sheet.write(0,2,'Targets')
sheet.write(0,3,'First Report')
sheet.write(0,4,'Most Recent Report')
    
row = 1 #counter for rows.

for line in text:
    w = line.split()
    print w

    if not line.startswith("#"):

        sheet.write(row,0,w[0])
        sheet.write(row,1,int(w[1]))
        sheet.write(row,2,int(w[2]))
        sheet.write(row,3,w[3])
        sheet.write(row,4,w[4])
        row = row + 1
    
wbk.save('Blacklist_date.xls')



#subnet 
    
clip = requests.get('https://isc.sans.edu/block.txt')
y = clip.content

#creating second sheet in the workbook
sheet2 = wbk.add_sheet('Top 20 Attacking Subnets')
sheet2.write(0,0,'Start')
sheet2.write(0,1,'End')
sheet2.write(0,2,'Netblock')
sheet2.write(0,3,'Attacks')
sheet2.write(0,4,'Name')
sheet2.write(0,5,'Country')
sheet2.write(0,6,'Email')

row = 1
z = y.split('\n')

for line in z:
    a = line.split('\t')
    if line.startswith(('1','2','3','4','5','6','7','8','9')):
        sheet2.write(row,0,a[0])
        sheet2.write(row,1,a[1])
        sheet2.write(row,2,int(a[2]))
        sheet2.write(row,3,int(a[3]))
        sheet2.write(row,4,a[4])
        sheet2.write(row,5,a[5])
        sheet2.write(row,6,a[6])
        row = row + 1

wbk.save('Blacklist_date.xls')

print "Script Completed. Please check for the excel report named Blacklist_date.xls"
