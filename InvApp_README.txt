Description
Finished application will be a web page that displays current inventory, has buttons to add, modify and delete entries and updates automatically. It contains an inventory of entrerprise hardware...

How it works:
Run the python script - it opens an "entry form" with the fields below. Once you've entered all the data you can click "add and close" or "add and create another record" etc.  When you add these records, there's another python method (class?) that reads the database and formats the output for a web page.  We can work on the web page part, it's easy..


Entry form with these fields:
 system type (dropdown box, allow choices of R610, R710, R720, R620, R730, R630, R730XD etc)
 Number of hdd's
 size of hdd's
 total amount of memory
 number of processors
 drac ip address
 ip address1
 ip address2
 description
 comments
 service tag (make primary field) - this field should always be 7 alphanumeric characters
 

Suggestions:
use tkinter to draw the entry form
use sqlite3 to store the database
use apache to display the web page
draw the inventory in tables inside the html code
The database automatically captures the created date, last modified date etc




Helpful hints:
My clock has an example of configuring sqlite3 (see my repo)
https://github.com/jeffnic/clock


This link helped me understand how to push/pull git repos.
https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/


Here's an example of formatting output for html
with open("/var/www/html/leases.html","w") as outFile:
    outFile.write("<table>" + "\n")
    reader = csv.reader(open("/dhcp/dhcp_leases.csv", "r"))
    for row in reader:
    #   print("this is the length %d " % len(row))

        if len(row) == 16:
            print("{:>15}".format(row[0]) + "{:>25}".format(row[3]) + " " + "{:>40}".format(row[8]))
            outFile.write("<tr>"+ "<td>"+"{:>15}".format(row[0]) +"</td>"  + "<td>"+"{:>25}".format(row[3]) + "</td>" + " " + "<td>" + "{:>40}".format(row[8] + "</td></tr>" + "\n"))
    outFile.write("</table>")

