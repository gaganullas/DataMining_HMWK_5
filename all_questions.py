import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.008  
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = '1/2 * math.log((1 - p) / p)'

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.528
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'No'

    # type: explain_string
    answers['Explain'] = 'Ensemble methods rely on diverse models to improve accuracy, In Alan case, flipping a coin is a simplistic and random process that does not incorporate any meaningful information about the stock markets behavior. Each coin flip is independent of the others, so there is no correlation or learning happening between them. As a result, the ensemble of coin flips does not provide any valuable insight into whether the stock market will rise or fall'
    
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = True

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = 'Both classifiers, C1 and C2, have the same performance level as they both fall on the random guess line in the ROC curve'

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) explain'] = 'Precision and recall suggest Classifier C2 is better due to higher recall, but they overlook false positives. TPR and FPR offer a balanced evaluation, considering Classifier C2 higher recall but potential for more false positives, making them more suitable for assessing relative performance in scenarios where false positives are significant'
    
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = 'C2 correctly identifies a higher proportion of actual positive cases and achieves a better balance between precision and recall'

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = 'Precision, recall, and F1-measure provide a more balanced assessment of classifiers C1 and C2, considering both their ability to correctly identify positive cases and their capacity to minimize false positives, compared to TPR and FPR'

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = 'It achieves a higher precision and recall than C1 while maintaining the same FPR. Although it falls short of C2 in terms of recall and F1-measure, C3 still offers a better balance overall. Therefore, C3 would be the preferred choice among C1, C2, and C3.'
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] =  "(p*100)/(p*1000)"

    # type: eval_float
    answers['(a) recall for C0'] =  "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "(0.2*p)/(0.1+p)"

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = "p < 0.3"
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
    'recall': 0.533,
    'precision': 0.615,
    'F-measure': 0.571,
    'accuracy': 0.88
}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'Accuracy does not consider class imbalance, while the F-measure balances both precision and recall, providing a more comprehensive evaluation'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'F1'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'Considering the nature of cancer detection, where false positives can lead to unnecessary medical interventions and anxiety for patients, while false negatives can result in missed opportunities for treatment, it is crucial to prioritize minimizing both false positives and false negatives. Therefore, in this situation, the F1-Score would be a more appropriate evaluation measure for selecting between the two tests'

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'In cancer screening scenarios where early detection is crucial, with false negatives posing greater risks than false positives, prioritizing sensitivity over specificity becomes essential. Thus, metrics like TPR/FPR ratios, which reflect the balance between true positives and false positives, may be preferred over F1-Score, especially when minimizing missed diagnoses is a primary concern.'
    
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
