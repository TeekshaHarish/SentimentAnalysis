from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from io import StringIO, BytesIO
import pandas as pd
from groq_sentiment_analyisis import sentment_analysis_of_review
import json
from output_frontend import output_frontend
from utils import display_pie_chart

app=FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_upload_file():
    with open("upload_file.html") as f:
        return f.read()

# Endpoint for file upload and processing
@app.post("/uploadfile/", response_class=HTMLResponse)
async def create_upload_file(file: UploadFile = File(...)):
    # Read the file contents
    contents = await file.read()
    
    file_extension=file.filename.split(".")[-1].lower()

    if file_extension=="csv":
        # Convert it to a StringIO object and then read it with pandas
        csv_data = StringIO(contents.decode("utf-8"))
        df = pd.read_csv(csv_data)
    elif file_extension in ["xls", "xlsx"]:
        # Convert the file contents to a BytesIO object and read it with pandas
        excel_data = BytesIO(contents)
        df = pd.read_excel(excel_data)

    else:
        # raise HTTPException(status_code=400, detail="File type not supported. Please upload a CSV or Excel file.")
        return "<h3>File type not supported. Please upload a CSV or Excel file.</h3>"

    rows,cols=df.shape
    ans=[]

    for review in df["Review"].tolist():
        sentiment_scores=sentment_analysis_of_review(review)
        print(sentiment_scores)
        # Convert string to JSON
        data = json.loads(sentiment_scores)

        # Add more data
        if(data['positive']>data['negative'] and data['positive']>data['neutral']):
            data['overall_sentiment'] = 'positive'
        elif(data['negative']>data['positive'] and data['negative']>data['neutral']):
            data['overall_sentiment'] = 'negative'
        else:
            data['overall_sentiment'] = 'neutral'
        data['review'] = review
        ans.append(data)
    
    
    piechart=await display_pie_chart(ans) 
    
    return output_frontend(ans,file.filename,rows-1,piechart)

