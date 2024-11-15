def format_info(record):
  return f"""
    <tr>
      <th scope="row">{record['review']}</th>
      <td>{record['positive']}</td>
      <td>{record['negative']}</td>
      <td>{record['neutral']}</td>
      <td>{record['overall_sentiment']}</td>
    </tr>
    """

def output_frontend(records,filename,rows,piechart):
  output=f"""<!doctype html>
  <html lang="en">
    <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

      <title>Hello, world!</title>
    </head>
    <body>
      <main class="container">
      <h2 class="text-center my-5 ">Sentiment Analyizer</h2>
      <h4 class="text-center my-2 ">File Name: {filename}</h4>
      <h4 class="text-center my-2 ">Number of reviews:{rows}</h4>
      <div class="text-center my-2 "><img src="data:image/png;base64,{piechart}" alt="Pie Chart"/></div>
      <table class="table">
          <thead>
            <tr>
              <th scope="col">Review</th>
              <th scope="col">Postivie</th>
              <th scope="col">Negative</th>
              <th scope="col">Neutral</th>
              <th scope="col">Overall Sentiment</th>
            </tr>
          </thead>
          <tbody>
            {"".join(map(format_info,records))}

          </tbody>
        </table>
      </main>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    </body>
  </html>"""
  return output
