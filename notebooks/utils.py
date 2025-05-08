import matplotlib.pyplot as plt
import seaborn as sns

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