# Movie Review Sentiment Analysis

This project is a sentiment analysis tool for movie reviews using machine learning. The model classifies reviews as positive or negative based on the text content.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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
