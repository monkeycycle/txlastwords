import urllib2
from BeautifulSoup import BeautifulSoup

html = urllib2.urlopen('http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html')

soup = BeautifulSoup(html)
results_table = soup.find('table', attrs={'class': 'os'})

for tr in results_table.findAll('tr'):
	print ROW 

    for td in tr.findAll('td'):
    	print td.text
        
#         soup.find('td', attrs={'class':'a href'})
#         soup.find('td', attrs={'class':'Last Name'})
#         soup.find('td', attrs={'class':'First Name'})
#         soup.find('td', attrs={'class':'First Name'})


#     output_list.append(row_list)

# print LAST WORDS 
# print output_list