import random  #can be used to give different names to different files
import urllib.request  #this is a package , which allows us to get data from the websites

'''if ever want to add module , follow below steps
 file-> settings ->project interpreter -> + sign to add new module or - sign to delete one -> find your module
 -> install and enjoy 
 ;-)   '''

def download_web_image(url):
    name=random.randrange(1,1000)
    file_name= str(name) + ".jpg"   #we add .jpg extension as it will be a image file
                                    #and also we cannot directly add string with a number, so we typecaste name to
                                    #string , by using str() funciton
    urllib.request.urlretrieve(url,file_name) # urlretrieve is the function to get file from web

download_web_image("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQNL1yUNcREfawCr4LIBCHKkq8NAg2hOg9hQFTacop1ziDde-F7&usqp=CAU")


