from sklearn.pipeline import Pipeline

from sentiment_analysis_auto_ml.model_checkpoint import ModelCheckpoint
from sentiment_analysis_auto_ml.pipeline_factory import PIPELINE_DEFAULT_NAME

if __name__ == "__main__":
    mc = ModelCheckpoint(PIPELINE_DEFAULT_NAME)

    # The model will load!
    model: Pipeline = mc.load_model()

    # Usage:
    X = ["Je suis un modèle pas content.", "Je suis un modèle très content."]
    y = model.predict(X)
    y_probas = model.predict_proba(X)
    print(y.tolist())
    print(y_probas.tolist())
