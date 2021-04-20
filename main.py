from fastapi import FastAPI, HTTPException
from schemas import StockIn, StockOut
from model import convert, predict
#instantiate app
app = FastAPI()


#create healthcheck endpoint
@app.get("/healthcheck")
def healthcheck():
    return "up and running"

#create predict endpoint
@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return response_object
