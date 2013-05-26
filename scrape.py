import urllib2

URL = 'http://www.kavvv.be/index.php?view=afdeling_content&id=412&afdeling=16'


def scrape(url):
    print 'Downloading %s' % url
    req = urllib2.Request(url=url)
    # req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    # req.add_header('Accept-Encoding', 'gzip,deflate,sdch')
    # req.add_header('Accept-Language', 'en,es-419;q=0.8,es;q=0.6,en-US;q=0.4')
    # req.add_header('Cache-Control', 'max-age=0')
    # req.add_header('Connection', 'keep-alive')
    # req.add_header('Cookie', 'PHPSESSID=ussc9109ggueu290pavhimfp00; language=nl; menu1=m15')
    req.add_header('Cookie', 'language=nl;')
    # req.add_header('Host', 'www.kavvv.be')
    # req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36')

    response = urllib2.urlopen(req)
    # print response.info()
    content = response.read()
    print "Downloaded"

    # <div class="afdelingcontent">
    # </table>
    searchstr1 = '<div class="afdelingcontent">'
    searchstr2 = '</table>'
    start = content.find(searchstr1)
    end = content.find(searchstr2, start)
    table = content[start + len(searchstr1):end + len(searchstr2)]
    # print table

    afdeling1 = 'AFDELING 1'
    afdeling2 = 'AFDELING 2'
    n1 = table.find(afdeling1)
    n2 = table.find(afdeling2)
    tr = table.find('<tr>', n1)
    trc = table.rfind('</tr>', n1, n2)
    print "Indexes:", tr, trc
    table1 = table[tr: trc + 5]
    # print table1

    tr = table.find('<tr>', n2)
    trc = table.rfind('</tr>', n2)
    print "Indexes:", tr, trc
    table2 = table[tr: trc + 5]
    # print table2
    return table1, table2


def write(table, filename):
    f = open(filename, 'wb')
    f.write('<!-- scraped -->')
    f.write('<table class="table"><colgroup><col width="26"> <col width="131"> <col span="7" width="40"></colgroup>'
            '<tbody>')
    f.write(table)
    f.write('</tbody></table>')
    f.close()


t1, t2 = scrape(URL)
write(t1, '_includes/2013-zomercompetitie-a.html')
write(t2, '_includes/2013-zomercompetitie-b.html')
