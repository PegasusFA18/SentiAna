import sys
from Voting_Algos import classify

def perform_classification(text):
    voted_classifier = classify(text)
    # print("Classification:", voted_classifier.classify(testing_set[-1][0]), "Confidence %:",
    #       voted_classifier.confidence(testing_set[5][0]) * 100)
    return voted_classifier

if __name__ == '__main__':
    x = perform_classification('@gmail hi, it looks like calendar messed up with the DST in Brazil, and I can’t synchronize my current time with the time of my events! Can you help me? @Google')


