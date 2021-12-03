import numpy as np
import pandas as pd
from database import database

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