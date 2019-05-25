from flask import Flask , render_template
app = Flask(__name__)

posts = [
    {
        'author':'Shivam',
        'title':'blog post 1',
        'content':'blog post 1 content',
        'date_posted':'25 May 2019'
    
    },
    {
        'author':'Anna',
        'title':'blog post 2',
        'content':'blog post 2 content',
        'date_posted':'20 May 2019'
    
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title = 'About Page')

if __name__=="__main__":
    app.run(debug = True)