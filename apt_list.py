# 사이드바에서 선택한 동에 대한 아파트 거래 데이터인 단지명, 계약일, 거래금액, 등기일자를 우측에 표로 나타내기
# 1. 필요한 데이터로 가공하기('단지명','동','계약년월','계약일','거래금액(만원)','등기일자')
# 2. 가공한 데이터를 streamlit sidebar, columns이용해서 표로 나타내기
# 3. html로 변환하기

import streamlit as st
import pandas as pd
from apt_step1 import apt_t

list = pd.read_csv(apt_t)

address = list['동내'].dropna().unique().tolist()

st.title("아파트 거래 데이터")

st.sidebar.header("동내 리스트")

choice_address = st.sidebar.selectbox("검색할 동내를 선택해주세요", address, index=None)
filtered_df = list[list['동내'] == choice_address][['단지명', '동', '계약년월', '계약일', '거래금액(만원)', '등기일자']]

if choice_address != None:
  st.header(f"{choice_address} : 거래 데이터 {len(filtered_df)}건")
else :
  st.header("")
  
if choice_address != None:
  st.write('---')
  filtered_df.index = range(1, len(filtered_df) + 1)

    # 표 형태로 출력
  st.dataframe(filtered_df)
else:
  st.write('👈  **동내**를 선택해 주세요!')
