import pandas as pd


def merge_person_address():
    """
    Merges two DataFrames: 'person' and 'address' based on the 'personId' column.

    Returns:
        pd.DataFrame: A DataFrame containing 'firstName', 'lastName', 'city', and 'state'.

    Example:
        >>> merge_person_address()
           firstName lastName           city       state
        0      Wang   Allen  New York City   New York
        1     Alice     Bob        NaN        NaN
    """

    # Creating 'person' DataFrame
    data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
    person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']) \
        .astype({'personId': 'Int64', 'firstName': 'object', 'lastName': 'object'})

    # Creating 'address' DataFrame
    data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
    address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']) \
        .astype({'addressId': 'Int64', 'personId': 'Int64', 'city': 'object', 'state': 'object'})

    # Merging DataFrames on 'personId'
    final = person.merge(address, on='personId', how='left')

    # Selecting the required columns
    result = final[['firstName', 'lastName', 'city', 'state']]

    return result


# Example usage
df_result = merge_person_address()
print(df_result)
