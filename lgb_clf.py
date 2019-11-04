import json
import os
import sys
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
import lightgbm as gbm
from joblib import dump, load


class LGB_CLF(object):
    """
    class for XGBoost
    """
    def __init__(self, mpath=None, model_name=None):
        """
        Constructor
        :param mpath: str, optional
                path to models. if None, mpath will be "models"
        :param model_name: str, optional
                model name. if None, "xgb"
        """
        cur_dir = os.path.dirname(__file__)
        sys.path.append(cur_dir)
        sys.path.append(os.path.join(cur_dir, "config_model"))
        if mpath is None:
            self._mpath = os.path.join(cur_dir, "models")
        else:
            self._mpath = os.path.join(cur_dir, mpath)
        if model_name is None:
            self._model_name = "xgb"
        with open("config_model/xgb_clf.json") as f:
            self._config = json.load(f)

    def train_model(self, x_train, y_train):
        """
        Train model. if cross_validate is true, kfold will be used.
        :param x_train: np.ndarray
                features for training
        :param y_train:
                target for training
        :return:
        """
        dtrain = xgb.DMatrix(x_train, label=y_train)

        self.model_fit = xgb.train(self._congif["init_params"], dtrain)

    def predict(self, x_test):
        """
        Prediction
        :param x_test: np.ndarray
            features for test
        :return:
        """
        self.predict = self.model_fit.predict(x_test)

    def save_model(self, run_id=None):
        if run_id is None:
            run_id = self._model_name + datetime.strftime(datetime.now(),
                                                          "%Y%m%d%H%M%S")
        path_save = os.path.join(self._mpath, run_id)
        dump(self.model_fit, path_save)

    def load_model(self, run_id):
        path_load = os.path.join(self._mpath, run_id)
        return load(path_load)

