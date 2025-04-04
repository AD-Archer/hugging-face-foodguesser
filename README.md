# Food Category Classification

A Python application that classifies food images into categories using a pre-trained deep learning model.

## Overview

This project uses the Hugging Face Transformers library to classify food images into various categories. It leverages a pre-trained model specifically designed for food category classification.

## Features

- Load and process food images
- Classify images into food categories
- Display classification results with confidence scores
- Save models locally for faster subsequent use
- User-friendly output formatting

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/food-category-classification.git
   cd food-category-classification
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your food images in the `Food Pictures` directory
2. Run the classifier:
   ```
   python food_classifier.py
   ```
3. By default, the script will classify the image at `Food Pictures/food_1.png`
4. To classify a different image, modify the `image_path` variable in `food_classifier.py`

## Project Structure

- `food_classifier.py`: Main script to run the food classification
- `food_classification_utils.py`: Utility functions for image processing and classification
- `Food Pictures/`: Directory containing food images to classify
- `models/`: Directory where downloaded models are cached

## Requirements

- Python 3.7+
- PIL/Pillow
- NumPy
- Matplotlib
- Transformers
- PyTorch

## License

This project is licensed under the MIT License - see the LICENSE file for details. 