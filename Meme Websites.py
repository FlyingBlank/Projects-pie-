from flask import Flask, render_template
import requests
import json

app = Flask(_name_)

def get_meme():
    url = "https:''meme-api.herokupp.com/gimme"
    response = json.loads(requests.request('Get', url).test)
    meme_large = response['previw'][-2]
    subreddit = response["subreddit"]
    return meme_large,subreddit
app = Flask(_name_)

@app.route('/')
def index();
    meme_pic,subreddit = get.meme()
    return render_template('meme_index.html', meme_pic=meme_pc, subreddit=subreddit)


    app.run(host="0.0.0.0", port=80)
    
