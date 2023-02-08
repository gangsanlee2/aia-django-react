import os

from app.admin.path import dir_path
from app.services.chatbot_ngin.models.intent.IntentModel import IntentModel
from app.services.chatbot_ngin.utils.Preprocess import Preprocess


p = Preprocess(word2index_dic=os.path.join(dir_path('train_tools'), 'dict/chatbot_dict.bin'),
               userdic=os.path.join(dir_path('utils'), 'user_dic.tsv'))

intent = IntentModel(model_name=os.path.join(dir_path('models'), 'intent/intent_model.h5'), proprocess=p)
query = "오늘 탕수육 주문 가능한가요?"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)

