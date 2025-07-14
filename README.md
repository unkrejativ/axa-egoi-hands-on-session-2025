# 🚀 Crash Course: Building Models to Predict Car Claim Occurrence! 

Welcome to the Hands on Session of AXA Insurance Group at EGOI. 

In this challenge you will collaborate in teams to build a predictive model that determines how high a car damage claim will be, if it might occure.

Your goal is to use your Python coding skills to:
1) Analyze and manipulate the data
2) Build the most effective model possible
   
via GitHub Codespaces.

The team with the best performing model will be declared the winner!

Together, you will find out what affects the level of car damage, how to visualize your results effectively, and learn about the work of our data scientists at AXA.

**Hints**: During the Challenge our *Modelling-Sis* <img src="https://github.com/unkrejativ/axa-egoi-hands-on-session-2025/blob/setup-devspaces/modelling_sis.png" width="40"/> will provide some Hints for you, if needed.


## 🛠️ Setting Up the Environment

**Notice**: If you already had a GitHub Account and provided some payment information, please inform us.

<details>
<summary><em>1. Step: </em> <span role="img" aria-label="faq"></span></summary>
<br>
Search for the repository <strong>https://github.com/unkrejativ/axa-egoi-hands-on-session-2025</strong> and open it.

</details>

<details>
<summary><em>2. Step: </em> <span role="img" aria-label="faq"></span></summary>
<br>
Select <strong>Code</strong>:
<br>
<br>
<img src="https://github.com/unkrejativ/axa-egoi-hands-on-session-2025/blob/setup-devspaces/env_1.jpg" width="600"/>
   
<br>
<br>
click on <strong>Codespaces</strong> and the <strong>+</strong> under <strong>Codespaces</strong>:
<br>
<br>

<img src="https://github.com/unkrejativ/axa-egoi-hands-on-session-2025/blob/setup-devspaces/env_2.jpg" width="600"/>
</details>


<details>
<summary><em>3. Step: </em> <span role="img" aria-label="faq"></span></summary>
<br>
Now you created a new <strong>Codespaces</strong> in a new Window and will see: 
<br>
<br>
<img src="https://github.com/unkrejativ/axa-egoi-hands-on-session-2025/blob/setup-devspaces/env_3.jpg" width="600"/>
<br>
<br>
Wait until the Codespace is configured, this will take around <strong>5 Minutes</strong>.

</details>

<details>
<summary><em>4. Step: </em> <span role="img" aria-label="faq"></span></summary>
<br>

Bild wenn es fertig ist + neues Terminal?

</details>

## 📊 1) Data Overview and Manipulation

First you should get an overview of the preserved data. 

After this you should understand which variables are contained in our dataset and even have a first idea which variables you would like to use for modelling.

Like our data scientist at AXA you will experience that the received is not clean or prepared for modelling. 

In this section you will prepare your dataset so it can be used for the second part, the modelling part.


## 🏆 2) Model Training

Now the modelling begins! 

After understanding the data try to find the best model by asking yourself which information will have the biggest impact on the high of a car damage. 

Discuss with your team which predictors you would like to use and change or add them to the code. You can try several different models, just copy the received code and change the model formula. 

<img src="https://github.com/unkrejativ/axa-egoi-hands-on-session-2025/blob/setup-devspaces/modelling_sis.png" width="40"/> **Hint**: A model with all possible variables will not lead to the best model.

We will messure quality of the model with the Mean Squared Error (MSE). Try to get the **least** Mean Squared Error possible!

## ❓ FAQ
<details>
<summary><em>What if we have a question or are stuck during the challenge?</em> <span role="img" aria-label="faq"></span></summary>
<br>
<p>Please don't hesitate to ask us at any time or have a look in the FAQ or hints that <em>Modelling-Sis</em> <img src="https://github.com/unkrejativ/axa-egoi-hands-on-session-2025/blob/setup-devspaces/modelling_sis.png" width="30"/> will give you.</p>
</details>
<br>

<details>
<summary><em>Why do I need a coding environment?</em> <span role="img" aria-label="faq"></span></summary>
<br>
<p>An coding environment is important because it allows us to use pre-written functions we need for our projects, so we don't have to write these functions by ourself. These functions are collected in packages and an environment contains several packages. 

Two of the most important packages are pandas, which helps us manipulate and analyze data, and scikit-learn (sklearn), which provides tools for modeling and machine learning.</p>
</details>

<details>
<summary><em>What is a model?</em> <span role="img" aria-label="faq"></span></summary>
<br>
<p>A model is a simplified representation that helps us understand and predict things. For example, we can use a model to predict the height of a damage after an car accident.

By analyzing past data, we can see how factors like speed or vehicle power affect the height of the damage and train a model with this information. The model learns the relationship between these factors and the height of damage during training.

When we now apply the model, which has been trained on known old data, to new data, we can make predictions about the future. ✨

In insurance, Generalized Linear Models (GLMs) are a common concept used for making predictions.</p>
</details>

<details>
<summary><em>Why do I have to split the data in train and test data?</em> <span role="img" aria-label="faq"></span></summary>
<br>
The training data is used to train the model, allowing it to learn the patterns and relationships in the data. On the other side the test data is used to evaluate how well the model performs on unseen data, ensuring it can generalize beyond the training set.
</details>

<details>
<summary><em>What is the Mean Squared Error (MSE)?</em> <span role="img" aria-label="faq"></span></summary>
<br>
<p>A The Mean Squared Error (MSE) is a way to measure how well a model is performing, especially in predicting values. It tells us how close the predicted values are to the actual values. 
Mathematically, the MSE is the mean of the squared differences between the predicted values and the observed values.
</p>
</details>

<details>
<summary><em>How to read the model formula?</em> <span role="img" aria-label="faq"></span></summary>
<br>
<p>...
</p>
</details>

<details>
<summary><em>Why is a model with all variables not the best?</em> <span role="img" aria-label="faq"></span></summary>
<br>
<p>...
</p>
</details>

<details>
<summary><em>What are residuals?</em> <span role="img" aria-label="faq"></span></summary>
<br>
<p>...
</p>
</details>



