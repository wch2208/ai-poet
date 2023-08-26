# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

# 제목
st.title('인공지능 시인')

# 인풋창에 입력된 값을 content에 할당한다. 괄호는 상단에 넣을 라벨
# st.text_input('라벨의 내용', 'input value')
# 따라서 라벨과 빈 인풋창이 생기고 입력한 값이 content에 할당된다.
content = st.text_input('시의 주제를 제시해주세요')

# 버튼을 누르면 api 실행되기
if st.button('시 작성 요청하기'):
  # api 호출 대기 중 스피터 표시하기
  with st.spinner('시 작성 중...'):
    # api로 입력하기
    # "입력한 값 + 에 대한 시를 써줘"가 api로 전달되고 result에 할당된다.
    result = chat_model.predict(content + "에 대한 시를 써줘")
    # result에 담긴 string을 화면에 렌더링한다.
    st.write(result)