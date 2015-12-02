import cv2
import numpy as np
from sklearn import svm
import cPickle as pickle

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

rlist=[]
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            rlist.append((ix,iy,x,y))
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)


# img = np.zeros((512,512,3), np.uint8)
img=cv2.imread("train.png")
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
print rlist
cv2.destroyAllWindows()


data={}
data['data']=[]
data['target']=[]

# for rect in rlist:
#     i_x,i_y,x,y=rect[:]
#     for i in range(i_x,x):
#         for j in range(i_y,y):
#             data['data'].append((hsv_img[i][j][0],hsv_img[i][j][1],hsv_img[i][j][2]))
#             data['target'].append(1)

print img.shape
for x in range(img.shape[1]):
    for y in range(img.shape[0]):
        
        for rect in rlist:
            i_x,i_y,f_x,f_y=rect[:]
            data['data'].append((hsv_img[y][x][0]*1.,hsv_img[y][x][1]*1.,hsv_img[y][x][2]*1.))
            if x >= i_x and x<=f_x and y>=i_y  and y<= f_y:
                data['target'].append(1.)
            else:
                data['target'].append(0.)

print 'data traing started'
clf = svm.LinearSVC(verbose=1,max_iter=100000)
print clf
clf.fit(data['data'], data['target'])

# from sklearn.kernel_approximation import RBFSampler
# from sklearn.linear_model import SGDClassifier
# rbf_feature = RBFSampler(gamma=0.01, random_state=1)
# X_features = rbf_feature.fit_transform(data['data'])
# clf = SGDClassifier()
# clf.fit(X_features, data['target'])


print 'training done'

from sklearn.externals import joblib
joblib.dump(clf, 'train.pkl') 

