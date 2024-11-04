from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import pandas as pd
from io import StringIO
from typing import List
from . import db


app = FastAPI()
# To delete docs & redoc endpoints uncomment:
# app = FastAPI(docs_url=None, redoc_url=None)


class CalculationResult(BaseModel):
    """
    The format of the list element that is returned by the POST method.
    POST return List[CalculationResult]
    """
    saddr: str
    avgDur: float


# Initialise database
db.init_db()


@app.post("/process_csv", response_model=List[CalculationResult])
async def process_csv(file: UploadFile = File(...)):
    """
    Endpoint to receive form-data with csv-file and return JSON.
    Saves result to database.
    Input:
        Csv-file, loaded through swagger
    Output:
        JSON with info average "dur" for every source
    """
    if file.content_type != "text/csv":
        raise HTTPException(
            status_code=400, detail="File must be in CSV format.")

    # Read file
    content = await file.read()
    csv_data = StringIO(content.decode("utf-8"))

    # CSV processing with pandas
    try:
        df = pd.read_csv(csv_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid CSV format.")

    # Select the fields with the destination IP (saddr)
    saddr_set = set(df["saddr"].to_list())
    json_list = []
    # Calculate the average for each saddr
    for saddr in saddr_set:
        dur_list = df.loc[df['saddr'] == saddr, 'dur']
        avgDur = dur_list.mean()

        res_dict = {"saddr": saddr, "avgDur": avgDur}
        json_list.append(res_dict)
    # Save to database
    db.save_to_db(json_list)

    # Return JSON
    return json_list
