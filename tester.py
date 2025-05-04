from utils.helpers import *
from config.paths_config import *
from pipeline.prediction_pipeline import *


#print(find_similar_animes("One Piece", ANIME_WEIGHTS_PATH, ANIME2ANIME_ENCODED, ANIME2ANIME_DECODED,DF))
print(hybrid_recommendation(11880))