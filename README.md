# Crop-Recommendation-Disease-Classification

## Disclaimer ⚠️
This project is a Proof of Concept (POC), and the data used comes with no guarantee from the creator. Do not use it for making farming decisions. The creator is not responsible for any consequences. This project aims to demonstrate the integration of Machine Learning (ML) and Deep Learning (DL) into precision farming.

## Motivation 💪
Farming significantly influences a country's economic growth, especially in countries like India, where a majority of the population depends on agriculture for their livelihood. This project leverages technologies such as ML and DL to make farming more efficient, providing applications for crop recommendation, fertilizer recommendation, and plant disease prediction.

## Applications

### Crop Recommendation
The Crop Recommendation application allows users to input soil data, and based on the analysis, the system predicts the most suitable crop for cultivation.

### Fertilizer Recommendation
With the Fertilizer Recommendation application, users input soil data and the type of crop they are growing. The system then recommends improvements in the soil by identifying deficiencies or excesses.

### Plant Disease Prediction
The Plant Disease Prediction application takes an image of a diseased plant leaf as input. The system predicts the disease, provides background information, and suggests potential cures.

# Built with 🛠️

- Python, HTML, CSS, JavaScript
- Git, Flask

Libraries:
- Numpy, Pandas, Matplotlib, Scikit-learn
- TensorFlow for Deep Learning

## How to Use 💻

### Prerequisites
1. Install Anaconda or Miniconda to create a virtual environment in VS Code.

### Installation
2. Download the ZIP file or fork the repository to your local device.

### Setting up Virtual Environment
3. Open VS Code and create a virtual environment using Anaconda or Miniconda:

   ```bash
   conda create --name your_env_name python=3.10
   conda activate your_env_name

## Installing Dependencies

4. Navigate to the project directory and install the required packages using the provided `requirements.txt`:

   ```bash
   pip install -r requirements.txt

## Running the Application

5. Run the application by executing the `app.py` file located in the `app` folder:

   ```bash
   python app/app.py



### Crop Recommendation System

1. Enter the corresponding nutrient values of your soil, state, and city.
2. Note: N-P-K (Nitrogen-Phosphorous-Potassium) values should be entered as a ratio. [Learn more](https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/fertilizer-numbers-npk.htm).

### Fertilizer Suggestion System

1. Enter the nutrient contents of your soil and the crop you want to grow.
2. The algorithm will suggest which nutrient the soil has excess of or lacks and provide fertilizer recommendations.

### Disease Detection System

1. Upload an image of a leaf from your plant.
2. The algorithm will identify the crop type and determine whether the plant is diseased or healthy.
3. If diseased, receive information about the disease cause and suggestions on prevention or cure.

### Supported Crops
<details>
  <summary>Click to view supported crops</summary>

  - Apple
  - Blueberry
  - Cherry
  - Corn
  - Grape
  - Orange
  - Peach
  - Pepper, bell
  - Potato
  - Raspberry
  - Soybean
  - Squash
  - Strawberry
  - Tomato
</details>

## How to run locally 🛠️

## DEMO

![Screenshot 2023-12-19 223624](https://github.com/tejaschechar/Crop-Recommendation-Disease-Classification/assets/111494723/5b3704c7-9271-4c2b-a1e1-5921c48be041)

- ### Crop recommendation system
![crop1](https://github.com/tejaschechar/Crop-Recommendation-Disease-Classification/assets/111494723/aeeb7f1f-f64a-47b2-82ea-aa2abc600df2)
![crop2](https://github.com/tejaschechar/Crop-Recommendation-Disease-Classification/assets/111494723/37799f89-5a54-4b20-a7c6-81ab6869c99b)



- ### Fertilizer suggestion system
![fertilizer1](https://github.com/tejaschechar/Crop-Recommendation-Disease-Classification/assets/111494723/5ed4f04c-fb49-4eb4-a445-3d2b737c7eaa)

![fertilizer2](https://github.com/tejaschechar/Crop-Recommendation-Disease-Classification/assets/111494723/49d08fb0-7c11-4665-b81d-a4f5c9e8a9fb)



- ### Disease Detection system
![disease1](https://github.com/tejaschechar/Crop-Recommendation-Disease-Classification/assets/111494723/9e374054-f287-4038-a1c4-89eb3c620659)
![disease2](https://github.com/tejaschechar/Crop-Recommendation-Disease-Classification/assets/111494723/4f2daeab-1acb-48e2-a8ed-f18404e7f82c)


## Usage ⚙️

You are welcome to use this project for further development and contribute to its enhancement. If you find this project useful, kindly acknowledge the original source by mentioning it and include a link to this repository in your reports or documentation.

## Further Improvements 📈

While this project serves as a significant milestone, there are several areas for improvement:
- Enhancements can be made to the frontend design 
- Manual data collection via web scraping can improve the system's accuracy :monocle_face:
- Collecting additional plant images will enhance the robustness and generalization of the disease detection module :face_with_head_bandage:


## Credits 💳

This project draws inspiration from **[this GitHub repository](https://github.com/Gladiator07/Harvestify.git)**, particularly in the crop recommendation and fertilizer recommendation parts. This project represents an extended version of the mentioned repository. Please consider giving a star to the original repository.


