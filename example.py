"""
Example script demonstrating how to use the food classification utilities.
"""
from food_classification_utils import (
    convert_to_rgb, 
    classify_food, 
    display_results
)
from PIL import Image

def classify_custom_image(image_path, model_id="Kaludi/food-category-classification-v2.0"):
    """
    Classify a custom food image.
    
    Parameters:
        image_path (str): Path to the image file
        model_id (str): Hugging Face model ID to use
        
    Returns:
        list[dict]: Classification results
    """
    # Load and convert the image
    raw_image = Image.open(image_path)
    image = convert_to_rgb(raw_image)
    
    # Classify the image
    results = classify_food(image, model_id)
    
    # Display the results
    display_results(results)
    
    return results

if __name__ == "__main__":
    # Example usage
    print("Example 1: Classifying a pizza image")
    classify_custom_image("Food Pictures/pizza.jpg")
    
    print("\nExample 2: Classifying a salad image")
    classify_custom_image("Food Pictures/salad.jpg") 