import numpy as np
import tensorflow as tf
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


posOld = [ line.strip().split(',') for line in open("posFeature.txt").readlines()]
negOld = [ line.strip().split(',') for line in open("negFeature.txt").readlines()]

pos = [ l for l in posOld if len(l)==11 ]
neg = [ l[:-1]+['0'] for l in negOld if len(l)==11 ]

print(len(pos),len(posOld))
print(len(neg),len(negOld))

data = pos+neg

np.random.shuffle(data)

# training = data[:int(0.7*len(data))]
# test = data[int(0.7*len(data)):]

X = np.array([ np.array(list(map(float,l[2:-1]))) for l in data ])
Y = np.array([ np.array(int(l[-1])) for l in data ])

# trainingX = np.array([ np.array(list(map(float,l[2:-1]))) for l in training ])
# testingX = np.array([ np.array(list(map(float,l[2:-1]))) for l in test ])

# trainingY = np.array([ np.array([1,0]) if int(l[-1]) == 1 else np.array([0,1]) for l in training ])
# testingY = np.array([ np.array([1,0]) if int(l[-1]) == 1 else np.array([0,1]) for l in test ])

# trainingY = np.array([ np.array(int(l[-1])) for l in training ])
# testingY = np.array([ np.array(int(l[-1])) for l in test ])

# print(trainingX.shape,testingX.shape,trainingY.shape,testingY.shape)

#create model
# clf = LogisticRegressionCV(solver='liblinear')
clf = RandomForestClassifier(n_estimators=90,min_samples_split=2,max_features='sqrt')
'''
solver is the algorithm to use in the optimization problem and liblinear gives good accuracy.
'''
#Evaluate a score by cross-validation
clf.fit(X,Y)


pf = open("TrainMultPos")
nf = open("TrainMultNeg")

for line in pf.readlines():
	sl = map(int,line.split(','))
	y = sl[-1]
	for x in sl[:-1]:
		


# Y_pred = clf.predict(X)
# print(confusion_matrix(Y,Y_pred))
# scores2 = cross_val_score(clf, X, Y, cv=3)

# #report accuracy
# print("Accuracy for Logistic Regression: %0.2f (+/- %0.2f)" % (scores2.mean(), scores2.std() * 2))

'''
IP_SIZE = 8
# H1_SIZE = 100
# H2_SIZE = 100
OP_SIZE = 2
LEARNING_RATE = 0.001
TRAIN_STEPS = 100																																																								

x = tf.placeholder(tf.float32, shape=[None, IP_SIZE])
y_ = tf.placeholder(tf.float32, shape=[None, OP_SIZE])

H1_W = tf.Variable(tf.truncated_normal([IP_SIZE,H1_SIZE],stddev=0.1))
H1_b = tf.Variable(tf.truncated_normal([H1_SIZE],stddev=0.1))

# H2_W = tf.Variable(tf.truncated_normal([H1_SIZE,H2_SIZE],stddev=0.1))
# H2_b = tf.Variable(tf.truncated_normal([H2_SIZE],stddev=0.1))

# OP_W = tf.Variable(tf.truncated_normal([H2_SIZE,OP_SIZE],stddev=0.1))
# OP_b = tf.Variable(tf.truncated_normal([OP_SIZE],stddev=0.1))

H1_h = tf.nn.sigmoid(tf.matmul(x,H1_W) + H1_b)
H2_h = tf.nn.relu(tf.matmul(H1_h,H2_W) + H2_b)
y = tf.nn.softmax(tf.matmul(H2_h,OP_W) + OP_b)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
# loss = tf.reduce_mean(y-y_)

training = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# accuracy = 1-tf.reduce_mean(y-y_)

sess = tf.Session()
sess.run(tf.initialize_all_variables())


for i in range(TRAIN_STEPS+1):
    sess.run(training, feed_dict={x: trainingX, y_: trainingY})
    if i%10 == 0:
        print('Training Step:' + str(i) + '  Accuracy =  ' + str(sess.run(accuracy, feed_dict={x: testingX, y_: testingY})) + '  Loss = ' + str(sess.run(cross_entropy, {x: trainingX, y_: trainingY})))

print(sess.run(y, feed_dict={x: testingX, y_: testingY})-testingY)
'''