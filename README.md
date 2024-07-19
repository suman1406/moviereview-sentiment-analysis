# Movie Review Sentiment Analysis

This project is a sentiment analysis tool for movie reviews using machine learning. The model classifies reviews as positive or negative based on the text content.

## Introduction

This project uses a dataset of movie reviews to train a machine learning model that can predict the sentiment of new reviews. The project includes scripts for creating the dataset, training the model, and predicting sentiments.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/moviereview-sentiment-analysis.git
    cd moviereview-sentiment-analysis
    ```

2. Create a virtual environment:

    ```sh
    python -m venv env
    ```

3. Activate the virtual environment:

    - On Windows:

      ```sh
      .\env\Scripts\activate
      ```

    - On macOS/Linux:

      ```sh
      source env/bin/activate
      ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Creating the Dataset

Run the script to create the dataset:

```sh
python create_dataset.py
```
This will generate a `movie_reviews.csv` file with sample movie reviews and their sentiments.

## Training the Model

Run the script to train the model and make predictions:

```sh
python test.py
```
Follow the prompts to enter your own movie reviews and get sentiment predictions.
### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
## Steps to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Commit and push your changes to your fork.
5. Create a pull request to the main repository.
