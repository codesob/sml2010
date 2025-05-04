import os
import pandas as pd

def load_df1(use_processed=False):
    processed_path = './data/processed_df1.pkl'
    if use_processed and os.path.exists(processed_path):
        df1 = pd.read_pickle(processed_path)
        return df1

    with open('./data/NEW-DATA-1.T15.txt', 'r') as file:
        lines = file.readlines()
    header = lines[0].strip()
    column_names = [col.split(':', 1)[1] for col in header.split() if ':' in col]
    data_rows = [line.strip().split() for line in lines[1:] if line.strip()]
    df1 = pd.DataFrame(data_rows, columns=column_names)
    df1['Date'] = pd.to_datetime(df1['Date'], format='%d/%m/%Y')
    df1['Time'] = pd.to_datetime(df1['Time'], format='%H:%M')
    df1['Hour'] = df1['Time'].dt.hour
    df1['Month'] = df1['Date'].dt.month
    for col in df1.columns:
        if df1[col].dtype == 'object':
            df1[col] = pd.to_numeric(df1[col], errors='coerce')
    df1 = df1.dropna(axis=1, how='all')
    return df1

def load_df2(use_processed=False):
    processed_path = './data/processed_df2.pkl'
    if use_processed and os.path.exists(processed_path):
        df2 = pd.read_pickle(processed_path)
        return df2

    with open('./data/NEW-DATA-2.T15.txt', 'r') as file:
        lines = file.readlines()
    header = lines[0].strip()
    column_names = [col.split(':', 1)[1] for col in header.split() if ':' in col]
    data_rows = [line.strip().split() for line in lines[1:] if line.strip()]
    df2 = pd.DataFrame(data_rows, columns=column_names)
    df2['Date'] = pd.to_datetime(df2['Date'], format='%d/%m/%Y')
    df2['Time'] = pd.to_datetime(df2['Time'], format='%H:%M')
    df2['Hour'] = df2['Time'].dt.hour
    df2['Month'] = df2['Date'].dt.month
    for col in df2.columns:
        if df2[col].dtype == 'object':
            df2[col] = pd.to_numeric(df2[col], errors='coerce')
    df2 = df2.dropna(axis=1, how='all')
    return df2

def save_processed_df1(df1):
    processed_path = './data/processed_df1.pkl'
    df1.to_pickle(processed_path)

def save_processed_df2(df2):
    processed_path = './data/processed_df2.pkl'
    df2.to_pickle(processed_path)
