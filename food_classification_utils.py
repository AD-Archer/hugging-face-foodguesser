# ========================================
# Food Classification Utilities
# ========================================

# Imports
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformers import pipeline
from transformers.utils import logging
import warnings
import os

# Suppress warnings and unnecessary logs
logging.set_verbosity_error()
warnings.filterwarnings("ignore")

def convert_to_rgb(image):
    """
    Convert a PIL image to RGB format.

    Parameters:
        image (PIL.Image): Input image.

    Returns:
        PIL.Image: RGB-converted image.
    """
    return image.convert('RGB')


def display_image(image):
    """
    Display an image using matplotlib.

    Parameters:
        image (PIL.Image): Image to display.
    """
    plt.imshow(image)
    plt.axis('off')
    plt.title("Input Image")
    plt.show()


def classify_food(image, model_id):
    """
    Classify the image into food categories using a pre-trained model.

    Parameters:
        image (PIL.Image): Input image.
        model_id (str): Hugging Face model ID.

    Returns:
        list[dict]: Classification scores for each category.
    """
    classifier = pipeline("image-classification", model=model_id)
    
    # Save the model locally for reuse if not already saved
    save_dir = f"models/{model_id}"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)
        classifier.save_pretrained(save_directory=save_dir)
    
    return classifier(image)


def get_top_prediction(scores):
    """
    Get the label with the highest confidence score.

    Parameters:
        scores (list[dict]): List of category scores.

    Returns:
        tuple: (predicted_label, confidence_score)
    """
    top_result = max(scores, key=lambda x: x['score'])
    return top_result['label'], top_result['score']


def display_results(results):
    """
    Display all classification results in a formatted table.
    
    Parameters:
        results (list[dict]): Classification results.
    """
    print("\n🍽️  Food Category Classification Results")
    print("-" * 45)
    print(f"{'Category':<15} | {'Confidence':>10}")
    print("-" * 45)
    for res in results:
        print(f"{res['label']:<15} | {res['score']*100:>9.2f}%")
    print("-" * 45)

    # Display the top prediction
    top_label, top_score = get_top_prediction(results)
    print(f"\n✅ Predicted Category: {top_label} ({top_score:.2%} confidence)") 