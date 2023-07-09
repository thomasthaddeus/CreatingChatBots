"""
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""


from sklearn.model_selection import train_test_split

def split_data(inputs, targets, test_size=0.2, random_state=42):
    inputs_train, inputs_val, targets_train, targets_val = train_test_split(inputs, targets, test_size=test_size, random_state=random_state)
    return inputs_train, inputs_val, targets_train, targets_val

sequences = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
targets = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]]

inputs_train, inputs_val, targets_train, targets_val = split_data(sequences, targets)
print(inputs_train)  # Output: [[4, 5, 6], [10, 11, 12], [1, 2, 3]]
print(inputs_val)  # Output: [[7, 8, 9]]
print(targets_train)  # Output: [[5, 6, 7], [11, 12, 13], [2, 3, 4]]
print(targets_val)  # Output: [[8, 9, 10]]
