
# In[3]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install bs4')
get_ipython().system('pip install nbformat')


# In[4]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# In[5]:


import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# In[6]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)

    
    fig.show()


tesla_ticker = yf.Ticker("TSLA")


# In[8]:


tesla_data = tesla_ticker.history(period="max") 

# In[37]:


tesla_data.reset_index(inplace=True)
print(tesla_data.head(5))


# In[10]:


url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
response = requests.get(url)
html_data = response.text



# In[11]:


soup = BeautifulSoup(html_data, "html5lib")`


# In[12]:


revenue_table = soup.find("table")

dates = []
revenues = []
for row in revenue_table.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) > 1: 
        date = cols[0].text.strip() 
        revenue = cols[1].text.strip() 
        dates.append(date)
        revenues.append(revenue)


tesla_revenue = pd.DataFrame({
    "Date": dates,
    "Revenue": revenues
})

print(tesla_revenue)


# In[13]:


tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r',|\$', '', regex=True)

# In[14]:


tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[15]:


tesla_revenue.tail(5)
# In[16]:


GameStop= yf.Ticker('GME')
GameStop




# In[17]:


gme_data = GameStop.history(period="max")
print(gme_data)


# In[38]:


gme_data.reset_index(inplace=True)
print(gme_data.head(5))


# In[27]:


url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
response = requests.get(url)
html_data_2 = response.text


# In[28]:


soup=BeautifulSoup(html_data_2,'html5lib')


# In[19]:


revenue_table = soup.find("table")
date = []
revenue = []
for row in revenue_table.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) > 1: 
        date = cols[0].text.strip() 
        revenue = cols[1].text.strip() 
        dates.append(date)
        revenues.append(revenue)


gme_revenue = pd.DataFrame({
    "Date": dates,
    "Revenue": revenues
})

print(gme_revenue)

# In[39]:


gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(r',|\$', '', regex=True)


# In[40]:


gme_revenue.tail(5)



# In[32]:


tesla_data = yf.Ticker('TSLA').history(period='max').reset_index()
make_graph(tesla_data, tesla_revenue, stock='TSLA')


# In[32]:


tesla_data = yf.Ticker('TSLA').history(period='max').reset_index()
make_graph(tesla_data, tesla_revenue, stock='TSLA')


# In[36]:


make_graph(gme_data, gme_revenue,stock='GME')


# In[36]:


make_graph(gme_data, gme_revenue,stock='GME')

