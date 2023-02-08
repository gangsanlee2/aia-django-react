import os

from app.admin.path import dir_path
from app.services.chatbot_ngin.utils.Preprocess import Preprocess
from keras import preprocessing

sent = "내일 오전 10시에 짬뽕 주문하고 싶어ㅋㅋ"
p = Preprocess(word2index_dic=os.path.join(dir_path('train_tools'), 'dict/chatbot_dict.bin'),
               userdic = os.path.join(dir_path('utils'), 'user_dic.tsv'))

pos = p.pos(sent)
keywords = p.get_keywords(pos, without_tag=False)

print(keywords)

# w2i = p.get_wordidx_sequence(keywords)
# sequences = [w2i]
#
# MAX_SEQ_LEN = 15    # 임베딩 벡터 크기
# padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')
#
# print(keywords)
# print(sequences)
# print(padded_seqs)
