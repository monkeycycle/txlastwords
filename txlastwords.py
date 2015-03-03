import urllib2
from BeautifulSoup import BeautifulSoup

# part 1

html = urllib2.urlopen('http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html').read()

# part 2

soup = BeautifulSoup(html)
results_table = soup.find('table', attrs={'class': 'os'})


# part 3

for tr in results_table.findAll('tr'):
    # print 'ROW'

    for td in tr.findAll('td'):
        # print td.text

        if td.text == "Last Statement": 
            # If the text has "Last Statement" in it, then... 
            last_words = urllib2.urlopen([soup.find('a', attrs='href')]).read()
            # open the link. 
            body = soup.find('div', attrs='id': 'body')
            # Then go to the text div... 
            for p in body: 
                # find the last paragraph tag... 
                print p.text 
                # and print the text. 


# for p[-1] in body: 
#     print p 