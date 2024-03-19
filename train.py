from pyexpat import model
from sklearn import metrics
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def train(df):
    X=df.drop(['Outcome'], axis=1)
    y=df['Outcome']
    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit (X_train, y_train)

    metrics= {
        'Score':model.score(X_test, y_test),
        'MAE': mean_absolute_error(y_test, model.predict(X_TEST)),
    }
    return metrics


if __name__ == "__main__":
    import argparse
    import pandas as pd
    import pickle

    parse = argparse.ArgumentParser()
    parse.add_argument('input', help='cleaned diabetes file')
    parse.add_argument('output', help='Model file')
    args = parse.parse_args()

    df=pd.read_csv(args.input)
    metrics. model= train(df)
    print(metrics)
    with open(args.output, 'wb+') as out:
        pickle.dump(model,out)

