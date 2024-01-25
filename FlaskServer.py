from flask import Flask, render_template, request

from RedditData import getredditartist
from TwitterData import gettwitterartist
from TwitterAnalysis import getTwitterSpotifyData
from RedditAnalysis import getredditAnalysis
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('get_dates_KT.html')

@app.route("/about", methods=['POST'])
def about():
    return render_template('www.google.com')

#For ploting graph for Reddit
@app.route("/plotartists", methods=['POST'])
def plotartists():
    img = BytesIO()
    artists = getredditartist()
    val_c = artists.apply(pd.value_counts)
    val_c = val_c[0:10]
    ax = val_c.plot(kind='bar')
    ax.set_xlabel('Artists Name')
    ax.set_ylabel('Number of Post')
    plt.title('Trending Artists on Reddit')
    ax.figure.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('plot_image.html', plot_url=plot_url)

#For ploting graph for Twitter
@app.route("/plotsongs", methods=['POST'])
def plotsongs():
    img = BytesIO()
    date = request.form['date1']
    print(date)
    artists = gettwitterartist(date)
    val_c = artists.apply(pd.value_counts)
    val_c = val_c[0:10]
    ax = val_c.plot(kind='bar')
    ax.set_xlabel('Artists Name')
    ax.set_ylabel('Number of Tweets')
    plt.title('Trending Artists on Twitter')
    ax.figure.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('plot_image.html', plot_url=plot_url)

#For ploting graph for TwitterAnalysis and RedditAnalysis
@app.route("/comparisonplot", methods=['POST'])
def comparisonplot():
    img = BytesIO()
    img1 = BytesIO()
    
    count_PlaylistsR, count_TracksR, count_ArtistsR = getredditAnalysis()
    count_Playlists, count_Tracks, count_Artists = getTwitterSpotifyData()
    
    dfR = pd.DataFrame({'Reddit':['Playlist', 'Tracks', 'Artist'], 'val':[count_PlaylistsR, count_TracksR, count_ArtistsR]})
    dfT = pd.DataFrame({'Twitter':['Playlist', 'Tracks', 'Artist'], 'val':[count_Playlists, count_Tracks, count_Artists]})
    
    ax = dfT.plot.bar(x='Twitter', y='val', rot=0)
    ax.set_ylabel('Number of Tweets')
    
    dx = dfR.plot.bar(x='Reddit', y='val', rot=0)
    dx.set_ylabel('Number of Post')
    
    plt.title('Trending Artists on Twitter')
    plt.title('Trending Artists on Reddit')
    ax.figure.savefig(img, format='png', bbox_inches='tight')
    dx.figure.savefig(img1, format='png', bbox_inches='tight')
    
    plt.close()
    
    img.seek(0)
    img1.seek(0)
    
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plot_url1 = base64.b64encode(img1.getvalue()).decode('utf8')

    return render_template('plot_image.html', plot_url=plot_url, plot_url1 = plot_url1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)