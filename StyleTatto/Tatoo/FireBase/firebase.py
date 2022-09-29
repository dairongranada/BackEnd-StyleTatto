from distutils.command.config import config
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

credentails = credentials.Certificate('StyleTatto\Tatoo\FireBase\styletatto-57730-9ccc8cc5da05.json')

app = firebase_admin.initialize_app(credentails)

db = firestore.client()


"""doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})"""

users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

