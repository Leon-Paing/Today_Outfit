import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from rapidfuzz import fuzz
from django.conf import settings
import os
import csv
import random

def load_csv_data(file_name):
    file_path = os.path.join(settings.BASE_DIR, 'Today_Outfit_App', file_name) 
    data = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

outfits = load_csv_data('OutfitDataset.csv')
outfits_df = pd.DataFrame(outfits) 

outfits_df['GenderCategoryType']=outfits_df['Gender']+ '' +outfits_df['Category']+''+outfits_df['Type']

def remove_space(text):
    return text.replace(' ','')

outfits_df['GenderCategoryType'] = outfits_df['GenderCategoryType'].apply(remove_space)

def remove_hyphen(text):
    return text.replace('-','')


outfits_df['GenderCategoryType'] = outfits_df['GenderCategoryType'].apply(remove_hyphen)


tfidf_vector=TfidfVectorizer(stop_words='english')
tfidf_matrix=tfidf_vector.fit_transform(outfits_df['GenderCategoryType'])


sim_matrix=linear_kernel(tfidf_matrix, tfidf_matrix)

def get_index_from_Description(Description):
    return outfits_df[outfits_df['Description'] == Description].index.values[0]

def get_Description_from_index(index):
    return outfits_df.loc[index, 'Description']


def matching_score(a,b):
    return fuzz.ratio(a,b)

def find_closest_outfit(Description):
    leven_scores = list(enumerate(outfits_df['Description'].apply(matching_score, b=Description)))
    sorted_leven_scores = sorted(leven_scores, key=lambda x: x[1], reverse=True)
    closest_outfit = get_Description_from_index(sorted_leven_scores[0][0])
    distance_score = sorted_leven_scores[0][1]
    return closest_outfit, distance_score

def contents_based_recommender(outfit_info, how_many):
    closest_outfit, distance_score = find_closest_outfit(outfit_info)
    if distance_score == 100:
        outfits_index = get_index_from_Description(closest_outfit)
        outfits_list = list(enumerate(sim_matrix[int(outfits_index)]))
        similar_outfits = list(filter(lambda x:x[0] != int(outfits_index), sorted(outfits_list,key=lambda x:x[1], reverse=True)))
        return [get_Description_from_index(i) for i, s in similar_outfits[:how_many]]
    return []