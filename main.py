import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# Load the data
file_path = 'data inside, data insight!(응답).xlsx'
data = pd.read_excel(file_path, sheet_name='설문지 응답 시트1')

# Title and description
st.title('Survey Data Insights')
st.write("""
This application provides insights into the survey data regarding the perceived value of various learning data. 
Explore the charts and statistics to gain a better understanding of the data.
""")

# 1. 학습 가치 평가
st.header('1. 학습 가치 평가')
value_columns = [
    '다음 학습데이터는 얼마나 분석할만한 가치가 있다고 생각하시나요? [학습 시간 - 학습으로 간주할 수 있는 행위를 수행한 시간]',
    '다음 학습데이터는 얼마나 분석할만한 가치가 있다고 생각하시나요? [콘텐츠 수행도 - 제시된 콘텐츠를 수행한 정도]',
    '다음 학습데이터는 얼마나 분석할만한 가치가 있다고 생각하시나요? [학습계획 달성도 - 학습자가 스스로 수립한 학습계획에 대한 진도율]',
    '다음 학습데이터는 얼마나 분석할만한 가치가 있다고 생각하시나요? [접속시간 - 학습자가 하루 중 AI 디지털교과서에 접속한 시점]',
    '다음 학습데이터는 얼마나 분석할만한 가치가 있다고 생각하시나요? [형성평가 - 수업 중간에 실시한 소규모 평가에서의 성취도]',
    '다음 학습데이터는 얼마나 분석할만한 가치가 있다고 생각하시나요? [커뮤니티 참여도 - 학습자가 학급별/모둠별 커뮤니티 활동(게시판, 모둠채팅 등)에 참여하는 정도 및 내용]',
    '다음 학습데이터는 얼마나 분석할만한 가치가 있다고 생각하시나요? [학습 정서 - 학습자가 보이는 학습에 대한 감정 상태]'
]

fig, ax = plt.subplots(figsize=(10, 6))
data[value_columns].apply(pd.Series.value_counts).plot(kind='bar', stacked=True, ax=ax)
ax.set_title('학습 가치 평가')
ax.set_xlabel('평가 항목')
ax.set_ylabel('응답 수')
st.pyplot(fig)

# 2. 응답 패턴 분석
st.header('2. 응답 패턴 분석')
correlation_matrix = data[value_columns].apply(lambda x: x.astype('category').cat.codes).corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('응답 패턴 상관관계 분석')
st.pyplot(fig)

# 3. 주요 인사이트 도출 항목
st.header('3. 주요 인사이트 도출 항목')
insight_column = '위에서 언급한 데이터 또는 언급되지 않은 데이터 중 어떤 데이터를 활용하면 어떤 의미있는 인사이트를 찾을 수 있을 것이라고 생각하시나요? 또는 이런 데이터를 활용하면 기존에는 할 수 없었던 어떤 하이터치가 가능할 수 있을까요?!'
insight_counts = data[insight_column].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
insight_counts.plot(kind='bar', ax=ax)
ax.set_title('주요 인사이트 도출 항목')
ax.set_xlabel('응답')
ax.set_ylabel('응답 수')
st.pyplot(fig)

# 4. 학습 정서 분석
st.header('4. 학습 정서 분석')
emotion_column = '다음 학습데이터는 얼마나 분석할만한 가치가 있다고 생각하시나요? [학습 정서 - 학습자가 보이는 학습에 대한 감정 상태]'
emotion_counts = data[emotion_column].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
emotion_counts.plot(kind='bar', ax=ax)
ax.set_title('학습 정서 분석')
ax.set_xlabel('감정 상태')
ax.set_ylabel('응답 수')
st.pyplot(fig)

# 5. 데이터 간 상관관계
st.header('5. 데이터 간 상관관계')
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('데이터 간 상관관계 분석')
st.pyplot(fig)

st.write("Explore the insights derived from the survey data and understand the perceived value of various learning data attributes among the respondents.")
