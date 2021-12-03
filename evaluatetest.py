import numpy as np
import pandas as pd
import database

class evaluatetest:
    def __init__(self,id):
       self.id = id

    def evalute_objective_test(self, user_ans):
        db = database()

        total_score = 0
        status = None

