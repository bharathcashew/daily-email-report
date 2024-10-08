from datetime import date, datetime
from jugaad_data.nse import stock_df
from jugaad_data.nse import NSELive
def get_nse_data():
    nifty_fut = stock_df(symbol="SBIN", from_date=date(2020,1,1),
            to_date=date(2020,1,30), series="EQ")
    return nifty_fut
def get_all_indices():
    n = NSELive()
    nifty_index_data =""
    all_indices = n.all_indices()
    for idx in all_indices['data']:
       nifty_index_data += "{} - {}".format(idx['index'], idx['last'])+"\n"
       #print("{} - {}".format(idx['index'], idx['last']))
    return all_indices 

def generate_html_email_body():
    today_date = datetime.now().strftime('%Y-%m-%d')

    all_indices = get_all_indices()
    
    # Create the HTML email body with placeholders
    email_body = f"""
    <html>
    <body>
        <h2>Daily Report for {today_date}</h2>
        <h3>Report Details:</h3>
        <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Detail</th>
                </tr>
            </thead>
            <tbody>
    """
    for idx in all_indices['data']:
        email_body += f"""
                <tr>
                    <td>{idx['index']}</td>
                    <td>{idx['last']}</td>
                </tr>
        """
    email_body += """
            </tbody>
        </table>
        <p>Best regards,<br>Your Python Automation Script</p>
    </body>
    </html>
    """

    return email_body



#if __name__ == "__main__":
    #nifty_fut = get_nse_data() 
    #print(nifty_fut.head())
    #nifty_index_data = get_all_indices()
    #email_body = generate_html_email_body()
   # print(email_body)
    #print(nifty_index_data)
  