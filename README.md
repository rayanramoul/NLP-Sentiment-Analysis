
# Steven Knows

Steven is AI-powered platform for sentiment analysis in beta. Users are able to evaluate their sentences and improve the AI itself with their comments.

## Preview
 <div align="center">
  <img src="https://github.com/raysr/Steven-knows/blob/master/static/screen.png?raw=true" alt="STEVEN" style="border-style: dotted;border-color:##0a111c;"></img><img src="https://github.com/raysr/Steven-knows/blob/master/static/screen2.png?raw=true" alt="STEVEN" style="border-style: dotted;border-color:##0a111c;"></img><img src="https://github.com/raysr/Steven-knows/blob/master/static/screen3.png?raw=true" alt="STEVEN" style="border-style: dotted;border-color:##0a111c;"></img></div>

### Prerequisites

Make sure you have Flask

```
sudo pip3 install flask
```

### Installing

Just clone it :

```
git clone https://github.com/raysr/Steven-knows
```

## Deployment

cd into the directory cloned and :
```
python3

>from home import db
>db.create_all()
>exit
```

Then :
```
python3 home.py
```


## Usage

After the deployment just access <a href='http://localhost:5000/'>http://localhost:5000/</a>


## Built With

* Scikit-learn.
* Natural-Language-Toolkit.
* Flask.
* Dataset from <a href="https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data"> kaggle</a>.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
