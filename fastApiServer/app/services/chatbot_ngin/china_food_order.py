from app.services.chatbot_ngin.config.DatabaseConfig import *


from app.services.chatbot_ngin.utils.Database import Database

from app.services.chatbot_ngin.utils.Preprocess import Preprocess


class ChinaFoodOrder:
    def __init__(self):
        pass

    def exec(self, request):
        # 전처리 객체 생성
        p = Preprocess(word2index_dic='/usr/src/app/app/services/chatbot_ngin/train_tools/dict/chatbot_dict.bin',
                       userdic='/usr/src/app/app/services/chatbot_ngin/utils/user_dic.tsv')

        # 질문/답변 학습 디비 연결 객체 생성
        db = Database(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
        )
        db.connect()    # 디비 연결

        # 의도 파악
        from app.services.chatbot_ngin.models.intent.IntentModel import IntentModel
        intent = IntentModel(model_name='/usr/src/app/app/services/chatbot_ngin/models/intent/intent_model.h5', proprocess=p)
        predict = intent.predict_class(request)
        intent_name = intent.labels[predict]

        # 개체명 인식
        from app.services.chatbot_ngin.models.ner.NerModel import NerModel
        ner = NerModel(model_name='/usr/src/app/app/services/chatbot_ngin/models/ner/ner_model.h5', proprocess=p)
        predicts = ner.predict(request)
        ner_tags = ner.predict_tags(request)

        # 답변 검색
        from app.services.chatbot_ngin.utils.FindAnswer import FindAnswer
        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(predicts, answer_text)
        except:
            answer = "죄송해요 무슨 말인지 모르겠어요"

        db.close() # 디비 연결 끊음

        return answer

if __name__ == '__main__':
    print(ChinaFoodOrder().exec('자장면 주문할게요'))
