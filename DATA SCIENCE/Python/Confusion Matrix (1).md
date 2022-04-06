# Confusion Matrix
예측(또는 실험)을 잘 했는지 못 했는지를 알기 위해서 사용하는 지표

이진 분류(Binary Classification)라는 가정 하에, 맞추고자 하는 타겟(문제)을 positive로 놓고 예측(또는 실험)과 실제의 결과를 매트릭스로 표현한 것을 Confusion Matrix라 부른다.

- Precision (정밀도) = TP/(TP+FP) -> FP=0 일 때, Precision = 1
- Recall (재현율) = TP/(TP+FN) -> FN=0 일 때, Recall = 1
- F1-Score : Precision과 Recall의 조화평균

![99.png](attachment:99.png)
(출처: https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=wideeyed&logNo=221531940245)


```python
# 실제값 y_label, 예측값 y_pred (1 = positive)
y_label = [1, 1, 1, 1, 0]
y_pred = [1, 0, 1, 0, 1]
```


```python
def my_precision(y_label, y_pred, positive_label=1):
    true_positive = 0 # TP 초기화
    false_positive = 0 # FP 초기화
    for (i,p) in enumerate(y_pred):
        if p == positive_label and y_label[i] == positive_label: # TP Case
            true_positive += 1
        elif p== positive_label and y_label[i] != positive_label: # FP Case
            false_positive += 1
    return true_positive / (true_positive + false_positive)

def my_recall(y_label, y_pred, positive_label=1):
    true_positive = 0 # TP 초기화
    false_negative = 0 # FN 초기화
    for (i,p) in enumerate(y_pred):
        if p == positive_label and y_label[i] == positive_label: # TP Case
            true_positive += 1
        elif p != positive_label and y_label[i] == positive_label: # FN Case
            false_negative += 1
    return true_positive / (true_positive + false_negative)
        
def my_f1_score(y_label, y_pred, positive_label=1):
    precision = my_precision(y_label, y_pred, positive_label)
    recall = my_recall(y_label, y_pred, positive_label)
    return 2.0 / (1/precision + 1/recall)
```


```python
print('precision:', my_precision(y_label, y_pred))
print('recall:', my_recall(y_label, y_pred))
print('f1_score:', my_f1_score(y_label, y_pred))

# print(f"recall: {my_recall(y_label, y_pred)}")
```

    precision: 0.6666666666666666
    recall: 0.5
    f1_score: 0.5714285714285714
    

※ enuerate():
- enumerate는 "열거하다"라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
- enumerate를 for문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.


```python
# 원리를 이해했으니 검증된 sklearn 모듈을 이용해서 구해보기
from sklearn import metrics
print('precision:', metrics.precision_score(y_label, y_pred))
print('recall:', metrics.recall_score(y_label, y_pred))
print('f1_score:', metrics.f1_score(y_label, y_pred))
```

    precision: 0.6666666666666666
    recall: 0.5
    f1_score: 0.5714285714285715
    
