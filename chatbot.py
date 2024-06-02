import pandas as pd
from Levenshtein_Distance import calc_distance


class SimpleChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 ß리스트로 저장
        answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장
        return questions, answers
    
    def find_best_answer_by_levenshtein(self, input_sentence):
        question_indices = list(enumerate(self.questions)) # 인덱스를 포함한 질문 데이터 리스트 생성
        r = sorted(question_indices, key = lambda n: calc_distance(input_sentence, n[1])) # 레벤스테인 유사도를 기준으로 정렬
        matched_question_index = r[0][0] # 가장 유사도가 높은 질문 인덱스
        return self.answers[matched_question_index] # 유사도가 가장 높은 질문의 답변 리턴
        


# CSV 파일 경로를 지정하세요.
filepath = 'ChatbotData.csv'

# 간단한 챗봇 인스턴스를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break

    response = chatbot.find_best_answer_by_levenshtein(input_sentence)

    print('Chatbot:', response)


