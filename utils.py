import numpy as np
import io
import base64
import matplotlib.pyplot as plt

async def display_pie_chart(records):
    analysis={'positive':0,'negative':0,'neutral':0}
    for item in records:
        analysis[item['overall_sentiment']]+=1

    y = np.array(list(analysis.values()))
    mylabels = ["Postitive","Negative","Neutral"]

    # Create a pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(y, labels=mylabels)

    # Save the pie chart to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Convert the image to base64
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return img_str