import warnings

import yfinance as yf
from flask import Flask, render_template, request

warnings.simplefilter(action="ignore", category=FutureWarning)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_price")
def get_price() -> float:
    at: str = request.args.get("at", default="2024-01-02")
    ticker_name: str = request.args.get("ticker", default="MSFT")
    investment: str = request.args.get("investment", default=1000)
    ticker = yf.Ticker(ticker_name)
    history = ticker.history(period="max")
    old = history.loc[at, "Close"]
    new = history["Close"].iloc[-1]
    value = float(investment) / old * new
    return render_template(
        "price_content.html",
        ticker_name=ticker_name,
        at=at,
        new=new,
        investment=investment,
        value=value,
    )
