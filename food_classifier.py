# ========================================
# Food Category Classification Script
# ========================================

# Import the utility functions
from food_classification_utils import (
    convert_to_rgb, 
    display_image, 
    classify_food, 
    get_top_prediction,
    display_results
)
from PIL import Image

def main():
    """Main function to run the food classification process."""
    # Load and convert the image
    image_path = 'Food Pictures/food_1.png'
    raw_image = Image.open(image_path)
    image = convert_to_rgb(raw_image)

    # Show the image
    display_image(image)

    # Define the model ID
    model_id = "Kaludi/food-category-classification-v2.0"

    # Classify the image
    results = classify_food(image, model_id)
    
    # Display the results
    display_results(results)


if __name__ == "__main__":
    main() 