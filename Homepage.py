import web # for including all the web contents
urls=(
 '/','Index', # Here we are specifying URLs
 '/home', 'Home',
 '/goodmorning', 'Morning'
 )

# Here the template that we need to display in our HTML Page
tmp=""" 
<html>
   <head>
      <title>Testing Web.py</title>
   </head>
   <body>
     <center>
        <h2>Hello world</h2>
        <a href="/goodmorning">Good morning . . . !</a>
     </center>
  </body>
</html>"""

tmp1=""" 
<html>
   <head>
      <title>Testing Web.py</title>
   </head>
   <body>
     <center>
        <h2>Home</h2>
     </center>
  </body>
</html>"""

tmp2=""" 
<html>
   <head>
      <title>Testing Web.py</title>
   </head>
   <body>
     <center>
        <h2>Good morning</h2>
     </center>
  </body>
</html>"""
#class name
class Index:
    def GET(self):
        return tmp

class Home:
    def GET(self):
        return tmp1

class Morning:
    def GET(self):
        return tmp2
#main funtion
if __name__=='__main__':
    app=web.application(urls,globals())
    app.run()