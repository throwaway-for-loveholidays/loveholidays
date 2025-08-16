from pandas.api.types import is_categorical_dtype, is_float_dtype

def validate_categorical_columns(df, columns):
    """
    Validate that specified columns are categorical (object/string type).
    """    
    for col in columns:
        print(f"Validating column '{col}'")
        if is_categorical_dtype(df[col]):
            print(f"Column '{col}' is categorical (dtype: {df[col].dtype})")
            continue
        else:
            raise ValueError(f"Column '{col}' is not categorical (dtype: {df[col].dtype}). Aborting.")

    print("All columns are categorical.")
    return None # Returning null for now.

def validate_no_nulls(df, columns):
    """
    Validate that specified columns do not contain nulls.
    """
    for col in columns:
        print(f"Validating column '{col}'")
        if df[col].isnull().any():
            raise ValueError(f"Column '{col}' contains nulls. Aborting.")

    print("All columns do not contain nulls.")
    return None # Returning null for now.

def validate_float_columns(df, columns):
    """
    Validate that specified columns are float.
    """
    for col in columns:
        print(f"Validating column '{col}'")
        if not is_float_dtype(df[col]):
            raise ValueError(f"Column '{col}' is not float (dtype: {df[col].dtype}). Aborting.")

    print("All columns are float.")
    return None # Returning null for now.

def validate_float_range(df, column_range_dict):
    """
    Validate that specified columns are float and within a range. Range is inclusive.
    """
    for col, range_dict in column_range_dict.items():
        print(f"Validating column '{col}'")
        if df[col].min() < range_dict['min'] or df[col].max() > range_dict['max']:
            raise ValueError(f"Column '{col}' is not within range {range_dict['min']} to {range_dict['max']}. Aborting.")

    print("All columns are float and within range.")
    return None # Returning null for now.