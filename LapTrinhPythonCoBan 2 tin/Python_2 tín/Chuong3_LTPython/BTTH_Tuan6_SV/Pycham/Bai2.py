"""
Bank Marketing: Phân tích dữ liệu và xây dựng mô hình dự đoán
Bài toán: xây dựng một mô hình dự báo liệu khách hàng chấp nhận mở sổ tiết kiệm tại ngân hàng hay không dựa trên
bộ số liệu thu thập về những cuộc gọi mời khách hàng mở sổ tiết kiệm tại ngân hàng
"""
import numpy as np # thư viện dùng để tính toán số học
import pandas as pd # thư viện dùng để làm việc với dữ liệu dạng bảng
import matplotlib.pyplot as plt # thư viện dùng để vẽ biểu đồ
import seaborn as sns # thư viện dùng để vẽ những biểu đồ thống kê nâng cao

# khái báo một số hàm số giúp để xây dựng, và lựa chọn mô hình được cung cấp bởi gói thư viện sklearn
from sklearn.model_selection import StratifiedShuffleSplit  # Sử dụng thư viện skla

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MeanShift

from sklearn.preprocessing import LabelEncoder

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings(action="ignore")
df=pd.read_csv('bank.csv') # khi file jupyter notebook cùng folder với file dữ liệu thì có thể để tên file như thế này
print(df.shape)
#kiểm tra xem có dữ liệu trùng lặp hoặc khuyết thiếu hay ko?
print(df.duplicated().sum())
print(df.isnull().sum().sum())

#Kiểm tra kiểu dữ liệu của các thuộc tính
df.dtypes.sort_values()

df.head()

df.describe()

for col in df.select_dtypes(include='object').columns:
    print(col)
    print(df[col].unique())

#checking class balance
deposit_count = df.deposit.value_counts()/df.deposit.count()
deposit_count

labels = ['yes', 'no']
sizes = [deposit_count['yes'], deposit_count['no']]
colors = ['yellowgreen', 'gold']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.show()

# I'm going to use StratifiedShuffleSplit to preserve the class proportions.
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=1)
for train_index, test_index in sss.split(df.drop("deposit", axis=1), df.deposit):
    traindf = df.loc[train_index]
    testdf = df.loc[test_index]

# copies for plotings
traindf2 = traindf.copy()
traindf3 = traindf.copy()

#Pearson’s Correlations, which measures the strength of a linear relationship
sns.heatmap(traindf.corr(method='pearson'), annot=True)

#barplots showing the frequency of each category separated by label
plt.figure(figsize=[14,4])
plt.subplot(1,3,1)
sns.countplot(x='marital', hue='deposit', data=traindf,palette="Set2")
plt.subplot(1,3,2)
sns.countplot(x='education', hue='deposit', data=traindf,palette="Set2")
plt.subplot(1,3,3)
sns.countplot(x='contact', hue='deposit', data=traindf,palette="Set2")
plt.show()

plt.figure(figsize=[14,4])
sns.countplot(x='job', hue='deposit', data=traindf,palette="Set2")

plt.figure(figsize=[14,4])
plt.subplot(1,3,1)
sns.countplot(x='default', hue='deposit', data=traindf,palette="Set2")
plt.subplot(1,3,2)
sns.countplot(x='housing', hue='deposit', data=traindf,palette="Set2")
plt.subplot(1,3,3)
sns.countplot(x='loan', hue='deposit', data=traindf,palette="Set2")
plt.show()

plt.figure(figsize=[14,4])
plt.subplot(1,2,1)
sns.countplot(x='poutcome', hue='deposit', data=traindf,palette="Set2")
plt.subplot(1,2,2)
sns.countplot(x='month', hue='deposit', data=traindf,palette="Set2")

#clustering
scaler=StandardScaler()
z=scaler.fit_transform(traindf[['balance', 'previous']])
MS= MeanShift()
clustering=MS.fit(z)

#build a dataframe to examine
labels=pd.DataFrame({'labels':clustering.labels_},index=traindf.index)
df_clus=pd.concat([traindf[['balance', 'previous']],labels], axis=1)
df_clus_grouped=df_clus.groupby(by='labels').mean()
count_labels=df_clus.groupby(by='labels').size().reset_index(name='counts')
df_clus_final=pd.concat([df_clus_grouped, count_labels], axis=1)

print(df_clus_final.sort_values(by='balance', ascending=False))

#encoding label
LE=LabelEncoder()
df['deposit']=LE.fit_transform(df.deposit.values)

#encoding categorical features
df=pd.get_dummies(df)

#partitioning again
for train_index, test_index in sss.split(df.drop("deposit",axis=1), df.deposit):
    traindf=df.loc[train_index]
    testdf= df.loc[test_index]

xtrain=traindf.drop('deposit', axis=1)
ytrain=traindf.deposit

xtest=testdf.drop('deposit', axis=1)
ytest=testdf.deposit

# using mutual_info_classif to try to capture any kind of statistical dependency
np.random.seed(1)
xbest=SelectKBest(mutual_info_classif, k="all").fit(xtrain, ytrain)

# building a dataframe to analyze
scores=pd.DataFrame(xbest.scores_)
columns=pd.DataFrame(xtrain.columns)
colscores=pd.concat([columns, scores], axis=1)
colscores.columns = ['col','score']
print(colscores.sort_values(by='score', axis=0, ascending=False))

RF=RandomForestClassifier(random_state=1)
PRF=[{'n_estimators':[10, 50, 100, 500],'max_depth':[3,6,9],'criterion':['gini','entropy']}]
# Các tham số đưa vào để giúp lựa chọn mô hình tốt nhất:
#n_estimators - Số lá của rừng ngẫu nhiên,max_depth: độ cao của cây trong rừng,  criterion: chỉ số dùng để rẽ nhánh
gs=GridSearchCV(estimator=RF, param_grid=PRF, scoring='accuracy',cv=5,n_jobs=-1)
gs.fit(xtrain, ytrain)
print(gs.best_score_)

MODEL=gs.best_estimator_.fit(xtrain, ytrain)
preds=MODEL.predict(xtest)
print(accuracy_score(ytest, preds))

importances=MODEL.feature_importances_
feature_importances=pd.Series(importances, index=xtrain.columns).sort_values(ascending=False)
sns.barplot(x=feature_importances[0:10], y=feature_importances.index[0:10])
plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.show()



