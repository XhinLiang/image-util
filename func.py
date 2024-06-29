from image_similarity_measures.evaluate import evaluation
import cv2

def similarity(a, b, metric: str):
    return evaluation(org_img_path=a, 
           pred_img_path=b, 
           metrics=[metric])[metric]