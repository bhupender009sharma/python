from urllib import request  # another method of importing a module
goog_url='https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1560320391&period2=1591942791&interval=1d&events=history'

def downlaod_stock_data(csv_url):
    response= request.urlopen(csv_url)  # urlopen is a function to download the url
    csv = response.read()               # reads the data from the response file
    csv_str = str(csv)                  # converts the data into string format
    lines = csv_str.split("\\n")        # \\n splits the line whenever a new line is found , into a new line
    dest_url = r'goog.csv'              # goog.csv will be the downloaded file name
    fw = open(dest_url,"w")             # opening or creating goog.csv ,by using open function with fw object
    for line in lines:
        fw.write(line + "\n")           #writing into the file lines by line
    fw.close()

downlaod_stock_data(goog_url)


