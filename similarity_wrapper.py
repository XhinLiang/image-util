from image_similarity_measures.evaluate import evaluation

def similarity(a, b, metric: str):
    return evaluation(org_img_path=a, 
           pred_img_path=b, 
           metrics=[metric])[metric]

def similarity_wrapper(a, b, metric):
    return similarity(a, b, metric)
