import numpy as np
import pandas as pd
from database import database

import nltk as nlp
import numpy as np

class EvaluateTest:
    def evalute_objective_test(self,testid, user_ans):
        db = database()
        default_ans = db.get_answers(testid)
        total_score = 0
        result = ""
        for i, _ in enumerate(user_ans):
            if user_ans[i] == default_ans[i]:
                total_score += 100
        total_score /= 3
        total_score = round(total_score, 3)
        if total_score >= 33.33:
            result = "Pass" 
        else:
            result = "Fail"
        return result,total_score

    def evaluate_subjective_test(self,testid,user_ans):
        db = database()
        default_ans = db.get_answers(testid)
        total_score = 0
        result = ""
        for i, _ in enumerate(default_ans):
            # Subjective test
            
            total_score += self.subjective_answer(default_ans[i], user_ans[i])
        total_score /= 2
        total_score = round(total_score, 3)
        if total_score > 50.0:
            result = "Pass"
        else:
            result = "Fail"
        return result,total_score



    @staticmethod
    def word_tokenizer(sequence: str) -> list:
        word_tokens = list()
        for sent in nlp.sent_tokenize(sequence):
            for w in nlp.word_tokenize(sent):
                word_tokens.append(w)
            return word_tokens

    @staticmethod
    def create_vector(answer_tokens: list, tokens: list) -> np.array:
        return np.array([1 if tok in answer_tokens else 0 for tok in tokens])
    
    @staticmethod
    def cosine_similarity_score(vector1: np.array, vector2: np.array) -> float:
        def vector_value(vector):
            return np.sqrt(np.sum(np.square(vector)))
        
        v1 = vector_value(vector1)
        v2 = vector_value(vector2)
        v1_v2 = np.dot(vector1, vector2)
        return (v1_v2 / (v1 * v2)) * 100

    def subjective_answer(self, original_answer: str, user_answer: str) -> float:
        score_obt = 0
        original_ans_list = self.word_tokenizer(original_answer)
        user_ans_list = self.word_tokenizer(user_answer)
        overall_list = original_ans_list + user_ans_list
        vector1 = self.create_vector(original_ans_list, overall_list)
        vector2 = self.create_vector(user_answer, overall_list)
        score_obt = self.cosine_similarity_score(vector1, vector2)
        return score_obt