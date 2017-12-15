from pandas_datareader import data


def get_stock_info(stock, start, end, source="yahoo"):
    df = data.DataReader(stock,source,start,end)
    df['Stock'] = stock
    agg =df.groupby('Stock').agg({
        
    })
