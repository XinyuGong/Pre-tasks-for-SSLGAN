import gensim
import SL

model = gensim.models.Doc2Vec.load('model.bin')
criteria = SL.load_obj('result')
vector_result = []
for tuple in criteria:
    id = tuple[0]
    criterion = tuple[1]
    irr = tuple[2]
    print('Inferring vector for criterion ' + str(tuple) + '...')
    vector = model.infer_vector(gensim.utils.simple_preprocess(criterion))
    print('\tresult is', vector)
    vector_result.append([id, criterion, irr, vector])
SL.save_obj(vector_result, 'vector_result')