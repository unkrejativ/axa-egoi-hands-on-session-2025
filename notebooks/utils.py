import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_dynamic_sum_dict(keys):
    """
    Generates a dictionary with specified keys and sum as values.

    Parameters
    ----------
    keys : list
        List of keys for the dictionary.

    Returns
    -------
    dict
        A dictionary with keys from the input list and dynamic values.
    """

    values = [sum for i in range(len(keys))]
    dynamic_dict = {}
    for i in range(len(keys)):
        dynamic_dict[keys[i]] = values[i]
    return dynamic_dict


def plot_dimension(columns, dimension, data):
    """
    Plots the relationship between the specified columns and a given dimension from the provided data.

    Parameters
    ----------
    columns : list
        List of column names to be plotted against the dimension.
    dimension : str
        The dimension (e.g., category or group) to be used for plotting.
    data : pandas.DataFrame
        The input DataFrame containing the data to be plotted.

    Returns
    -------
    None
    """
    data['Exposure']=1
    temp = data.groupby(by=[dimension]).agg(
        {** generate_dynamic_sum_dict(columns) , "Exposure": sum }
    ).reset_index()

    for column in columns:
        temp[column + '_per_exposure'] = temp[column] / temp['Exposure']
    temp['Rank'] = temp[dimension].rank(method='dense') - 1

    fig, ax1 = plt.subplots(figsize=(20, 10))
    sns.barplot(x=dimension, y='Exposure', data=temp,
                estimator=sum, order=sorted(data[dimension].unique()), alpha=0.3, ax=ax1, errorbar=None)
    ax2 = ax1.twinx()
    for column in columns:
        sns.lineplot(x='Rank', y=column + '_per_exposure', data=temp,
                        label=column + '_per_exposure', ax=ax2, marker='o')



def plot_scatter_and_residuals(df: pd.DataFrame, objective_col: str, prediction_col: str) -> None:
    """
    Create scatter plots and residual plots from a given DataFrame and two specified columns, representing the column with the actual values and the predicted values.

    The function generates two plots:
    1. A scatter plot that visualizes the relationship between the actual values (objective_col) and the predicted values (prediction_col).
       This plot helps to evaluate how well the predicted values align with the actual values. Ideally, points should be 
       clustered closely around the diagonal line (y = x), indicating accurate predictions.

    2. A residual plot that shows the residuals (the differences between actual and predicted values) against the predicted values.
       This plot helps to assess the model's performance by identifying patterns in the residuals. Ideally, residuals should be 
       randomly distributed around the horizontal line at y=0, suggesting that the model has captured the underlying data structure
       well without systematic errors.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data to be visualized.
    prediction_col (str): The name of the column to be used for the X-axis (predicted values).
    objective_col (str): The name of the column to be used for the Y-axis (actual values).

    Returns:
    None: The function displays the plots and does not return any value.
    """
    
    # Residuals calculation
    residuals = df[objective_col] - df[prediction_col]

    sns.set_style("darkgrid")

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))  
    plt.subplots_adjust(hspace=0.6)  

    # 1. Scatterplot of Actual vs. Predicted Values
    sns.scatterplot(x=df[objective_col], y=df[prediction_col], alpha=0.6, edgecolor='k', s=100, ax=axes[0])
    axes[0].set_xlabel(objective_col, fontsize=14)
    axes[0].set_ylabel(prediction_col, fontsize=14)
    axes[0].set_title(f'Scatterplot of {objective_col} vs {prediction_col}', fontsize=18, fontweight='bold', color='navy')

    # Add a line for reference
    axes[0].plot([df[objective_col].min(), df[objective_col].max()], 
                 [df[prediction_col].min(), df[prediction_col].max()], 
                 'k--', lw=2)

    
    axes[0].set_xlim(-300, 10000)
    axes[0].set_ylim(-50, 3000)
    axes[0].set_aspect('auto')  
    axes[0].tick_params(labelsize=12)  

    # Set the tick labels to show actual values instead of scientific notation
    axes[0].ticklabel_format(style='plain', axis='x')
    axes[0].ticklabel_format(style='plain', axis='y')

    # 2. Residual Plot
    sns.scatterplot(x=df[prediction_col], y=residuals, color='darkorange', alpha=0.6, edgecolor='k', s=100, ax=axes[1])
    axes[1].axhline(y=0, color='red', linestyle='--', lw=2)
    axes[1].set_xlabel(prediction_col, fontsize=14)
    axes[1].set_ylabel('Residuals', fontsize=14)
    axes[1].set_title('Residual Plot', fontsize=18, fontweight='bold', color='darkorange')

    axes[1].grid(True)
    axes[1].set_xlim(500, 3000)  
    axes[1].set_ylim(-4000, 10000)
    axes[1].tick_params(labelsize=12)

    # Set the tick labels to show actual values instead of scientific notation
    axes[1].ticklabel_format(style='plain', axis='x')
    axes[1].ticklabel_format(style='plain', axis='y')

    
    plt.show()


def add_model_to_overview(models_overview: pd.DataFrame, formula: str, mse: float) -> pd.DataFrame:
    """
    Add a new model entry to the models overview DataFrame with an incremented version number.

    This function checks if the model already exists in the overview. If it doesn't, 
    it creates a new entry with an incremented version number, the provided formula, 
    and the Mean Squared Error.

    :param models_overview: The existing DataFrame containing model entries.
    :param formula: The formula used for the model.
    :param mse: The Mean Squared Error of the model.
    :return: Updated DataFrame with the new model entry.
    """
    # Determine the next version number
    version = len(models_overview) + 1
    model_name = f'model_{version}'
    
    # Check if the model already exists
    if models_overview['MSE'].size == 0  or formula not in list(models_overview['Formula']):
        # Create a new DataFrame for the new model entry
        new_entry = pd.DataFrame({'Model': [model_name], 'Formula': [formula], 'MSE': [round(mse, 2)]})
        
        # Concatenate the new entry with the existing overview
        models_overview = pd.concat([models_overview, new_entry], ignore_index=True)
        print(f"Added {model_name} to the overview.")

        # Check if this model has the lowest MSE
        if models_overview['MSE'].min() == round(mse, 2):
            print(f"Congratulations! {model_name} is your best model with the lowest MSE until now: {mse:.2f}.")
        else: 
            print(f"Try again, you already have created better models.")

    else:
        print(f"model already exists in the overview.")

    # Optionally wrap the formula text for better display
    
    return models_overview