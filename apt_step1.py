import pandas as pd
from pathlib import Path

apt_t = Path(__file__).parent/f"{Path(__file__).stem}.csv"

def apt_transaction_list() -> pd.DataFrame :
  filename = Path(__file__).parent / 'apt_file.csv'
  df = pd.read_csv(filename, encoding='cp949')

  df['거래금액(만원)'] = df['거래금액(만원)'].str.replace(',','').astype('int64')
  df_sale = df.loc[:,['시군구','단지명','동','계약년월','계약일','거래금액(만원)','등기일자']]
  df_gu_split = df_sale.시군구.str.split()

  gu = df_gu_split.str.get(1)
  dongne = df_gu_split.str.get(2)
  df_sale['구'], df_sale['동내'] = (gu, dongne)

  df_sale_drop = df_sale.drop(['시군구'], axis=1)
  df_sale_drop.set_index(['구'], inplace=True)
  df_sale_drop = df_sale_drop[['동내','단지명','동','계약년월','계약일','거래금액(만원)','등기일자']]
  return df_sale_drop

if __name__ == "__main__" :
  apt_list = apt_transaction_list()
  apt_list.to_csv(apt_t, index=True)

