import os
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

LABEL_MAP = {'体育': 0, '女性': 1, '文学': 2, '校园': 3}

with open('data/stop/stopword.txt', 'rb') as f:
    # 加载停用词表
    # 停用词的作用就是对于分类没有作用的词,即TF高,IDF低
    STOP_WORDS = [line.strip() for line in f.readlines()]


def load_data(path):
    """
    :param path: 基础路径
    :return: 分词列表; 标签列表
    """
    documents = []
    labels = []

    for root, dirs, files in os.walk(path):
        for file in files:
            label = root.split(os.sep)[-1]
            labels.append(label)
            filename = os.path.join(root, file)
            with open(filename, 'rb') as fl:  # 二进制读取
                content = fl.read()
                word_list = list(jieba.cut(content))  # 对中文进行分词
                words = [wl for wl in word_list]
                documents.append(' '.join(words))

    return documents, labels


def train(train_data, train_labels, test_data, test_labels):
    """
    :param train_data: 训练数据
    :param train_labels: 训练标签
    :param test_data: 测试数据
    :param test_labels: 测试标签
    :return:
    """
    # 计算矩阵
    # TfidfVectorizer用于计算单词的TF-IDF向量值
    # max_df描述单词在文档中最高出现率,这里设置0.5,代表一个单词在50%的文档中都出现了,那么他只携带非常少的信息,因而不做分词
    train_matrix = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5)
    # 模拟拟合,返回分词权重,即特征矩阵,表示每个单词在每个文档中的TF-IDF值
    train_features = train_matrix.fit_transform(train_data)

    # 训练模型
    # alpha为平滑参数
    clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)

    # 获取测试集的特征矩阵
    test_matrix = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5, vocabulary=train_matrix.vocabulary_)
    test_features = test_matrix.fit_transform(test_data)
    predict_labels = clf.predict(test_features)

    # 获取结果
    return metrics.accuracy_score(test_labels, predict_labels)


train_documents, train_label = load_data('data/train')
test_documents, test_label = load_data('data/test')
x = train(train_documents, train_label, test_documents, test_label)
print(x)
