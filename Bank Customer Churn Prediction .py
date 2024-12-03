{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "58bff1bd-9e30-46a7-ba0c-1677693bd2e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c9427d5c-b643-4e41-9255-58bbc81062fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"Churn_Modelling.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7f450c82-4357-4a20-aabc-20e7ddd3588b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>15619304</td>\n",
       "      <td>Onio</td>\n",
       "      <td>502</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "      <td>159660.80</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113931.57</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>15701354</td>\n",
       "      <td>Boni</td>\n",
       "      <td>699</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>39</td>\n",
       "      <td>1</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93826.63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>15737888</td>\n",
       "      <td>Mitchell</td>\n",
       "      <td>850</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>125510.82</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>79084.10</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
       "0          1    15634602  Hargrave          619    France  Female   42   \n",
       "1          2    15647311      Hill          608     Spain  Female   41   \n",
       "2          3    15619304      Onio          502    France  Female   42   \n",
       "3          4    15701354      Boni          699    France  Female   39   \n",
       "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
       "\n",
       "   Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0       2       0.00              1          1               1   \n",
       "1       1   83807.86              1          0               1   \n",
       "2       8  159660.80              3          1               0   \n",
       "3       1       0.00              2          0               0   \n",
       "4       2  125510.82              1          1               1   \n",
       "\n",
       "   EstimatedSalary  Exited  \n",
       "0        101348.88       1  \n",
       "1        112542.58       0  \n",
       "2        113931.57       1  \n",
       "3         93826.63       0  \n",
       "4         79084.10       0  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cd972fb8-256f-41bc-8245-081ee2565bfa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9995</th>\n",
       "      <td>9996</td>\n",
       "      <td>15606229</td>\n",
       "      <td>Obijiaku</td>\n",
       "      <td>771</td>\n",
       "      <td>France</td>\n",
       "      <td>Male</td>\n",
       "      <td>39</td>\n",
       "      <td>5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>96270.64</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9996</th>\n",
       "      <td>9997</td>\n",
       "      <td>15569892</td>\n",
       "      <td>Johnstone</td>\n",
       "      <td>516</td>\n",
       "      <td>France</td>\n",
       "      <td>Male</td>\n",
       "      <td>35</td>\n",
       "      <td>10</td>\n",
       "      <td>57369.61</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101699.77</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9997</th>\n",
       "      <td>9998</td>\n",
       "      <td>15584532</td>\n",
       "      <td>Liu</td>\n",
       "      <td>709</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>36</td>\n",
       "      <td>7</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>42085.58</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9998</th>\n",
       "      <td>9999</td>\n",
       "      <td>15682355</td>\n",
       "      <td>Sabbatini</td>\n",
       "      <td>772</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Male</td>\n",
       "      <td>42</td>\n",
       "      <td>3</td>\n",
       "      <td>75075.31</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>92888.52</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9999</th>\n",
       "      <td>10000</td>\n",
       "      <td>15628319</td>\n",
       "      <td>Walker</td>\n",
       "      <td>792</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>28</td>\n",
       "      <td>4</td>\n",
       "      <td>130142.79</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38190.78</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      RowNumber  CustomerId    Surname  CreditScore Geography  Gender  Age  \\\n",
       "9995       9996    15606229   Obijiaku          771    France    Male   39   \n",
       "9996       9997    15569892  Johnstone          516    France    Male   35   \n",
       "9997       9998    15584532        Liu          709    France  Female   36   \n",
       "9998       9999    15682355  Sabbatini          772   Germany    Male   42   \n",
       "9999      10000    15628319     Walker          792    France  Female   28   \n",
       "\n",
       "      Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "9995       5       0.00              2          1               0   \n",
       "9996      10   57369.61              1          1               1   \n",
       "9997       7       0.00              1          0               1   \n",
       "9998       3   75075.31              2          1               0   \n",
       "9999       4  130142.79              1          1               0   \n",
       "\n",
       "      EstimatedSalary  Exited  \n",
       "9995         96270.64       0  \n",
       "9996        101699.77       0  \n",
       "9997         42085.58       1  \n",
       "9998         92888.52       1  \n",
       "9999         38190.78       0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c4a2fb76-e437-474a-b083-bc3fe456c773",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10000, 14)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d2ac7bbd-6bfa-440f-9f02-aaa8bdf85278",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of rows 10000\n",
      "number of col 14\n"
     ]
    }
   ],
   "source": [
    "print(\"number of rows\" , df.shape[0])\n",
    "print(\"number of col\" , df.shape[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "53b75db4-9404-448f-bcee-cac0499d7fd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10000 entries, 0 to 9999\n",
      "Data columns (total 14 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   RowNumber        10000 non-null  int64  \n",
      " 1   CustomerId       10000 non-null  int64  \n",
      " 2   Surname          10000 non-null  object \n",
      " 3   CreditScore      10000 non-null  int64  \n",
      " 4   Geography        10000 non-null  object \n",
      " 5   Gender           10000 non-null  object \n",
      " 6   Age              10000 non-null  int64  \n",
      " 7   Tenure           10000 non-null  int64  \n",
      " 8   Balance          10000 non-null  float64\n",
      " 9   NumOfProducts    10000 non-null  int64  \n",
      " 10  HasCrCard        10000 non-null  int64  \n",
      " 11  IsActiveMember   10000 non-null  int64  \n",
      " 12  EstimatedSalary  10000 non-null  float64\n",
      " 13  Exited           10000 non-null  int64  \n",
      "dtypes: float64(2), int64(9), object(3)\n",
      "memory usage: 1.1+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "113692e8-ceaa-4366-80a1-eb4b6ca6669e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9995</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9996</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9997</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9998</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9999</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10000 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      RowNumber  CustomerId  Surname  CreditScore  Geography  Gender    Age  \\\n",
       "0         False       False    False        False      False   False  False   \n",
       "1         False       False    False        False      False   False  False   \n",
       "2         False       False    False        False      False   False  False   \n",
       "3         False       False    False        False      False   False  False   \n",
       "4         False       False    False        False      False   False  False   \n",
       "...         ...         ...      ...          ...        ...     ...    ...   \n",
       "9995      False       False    False        False      False   False  False   \n",
       "9996      False       False    False        False      False   False  False   \n",
       "9997      False       False    False        False      False   False  False   \n",
       "9998      False       False    False        False      False   False  False   \n",
       "9999      False       False    False        False      False   False  False   \n",
       "\n",
       "      Tenure  Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0      False    False          False      False           False   \n",
       "1      False    False          False      False           False   \n",
       "2      False    False          False      False           False   \n",
       "3      False    False          False      False           False   \n",
       "4      False    False          False      False           False   \n",
       "...      ...      ...            ...        ...             ...   \n",
       "9995   False    False          False      False           False   \n",
       "9996   False    False          False      False           False   \n",
       "9997   False    False          False      False           False   \n",
       "9998   False    False          False      False           False   \n",
       "9999   False    False          False      False           False   \n",
       "\n",
       "      EstimatedSalary  Exited  \n",
       "0               False   False  \n",
       "1               False   False  \n",
       "2               False   False  \n",
       "3               False   False  \n",
       "4               False   False  \n",
       "...               ...     ...  \n",
       "9995            False   False  \n",
       "9996            False   False  \n",
       "9997            False   False  \n",
       "9998            False   False  \n",
       "9999            False   False  \n",
       "\n",
       "[10000 rows x 14 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "de250d87-e860-429b-8d58-48fc81deda3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RowNumber          0\n",
       "CustomerId         0\n",
       "Surname            0\n",
       "CreditScore        0\n",
       "Geography          0\n",
       "Gender             0\n",
       "Age                0\n",
       "Tenure             0\n",
       "Balance            0\n",
       "NumOfProducts      0\n",
       "HasCrCard          0\n",
       "IsActiveMember     0\n",
       "EstimatedSalary    0\n",
       "Exited             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "980404cc-eef2-4866-96ed-d6b323c081e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>10000.00000</td>\n",
       "      <td>1.000000e+04</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.00000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5000.50000</td>\n",
       "      <td>1.569094e+07</td>\n",
       "      <td>650.528800</td>\n",
       "      <td>38.921800</td>\n",
       "      <td>5.012800</td>\n",
       "      <td>76485.889288</td>\n",
       "      <td>1.530200</td>\n",
       "      <td>0.70550</td>\n",
       "      <td>0.515100</td>\n",
       "      <td>100090.239881</td>\n",
       "      <td>0.203700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2886.89568</td>\n",
       "      <td>7.193619e+04</td>\n",
       "      <td>96.653299</td>\n",
       "      <td>10.487806</td>\n",
       "      <td>2.892174</td>\n",
       "      <td>62397.405202</td>\n",
       "      <td>0.581654</td>\n",
       "      <td>0.45584</td>\n",
       "      <td>0.499797</td>\n",
       "      <td>57510.492818</td>\n",
       "      <td>0.402769</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.556570e+07</td>\n",
       "      <td>350.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>11.580000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2500.75000</td>\n",
       "      <td>1.562853e+07</td>\n",
       "      <td>584.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>51002.110000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>5000.50000</td>\n",
       "      <td>1.569074e+07</td>\n",
       "      <td>652.000000</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>97198.540000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>100193.915000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7500.25000</td>\n",
       "      <td>1.575323e+07</td>\n",
       "      <td>718.000000</td>\n",
       "      <td>44.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>127644.240000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>149388.247500</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>10000.00000</td>\n",
       "      <td>1.581569e+07</td>\n",
       "      <td>850.000000</td>\n",
       "      <td>92.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>250898.090000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>199992.480000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         RowNumber    CustomerId   CreditScore           Age        Tenure  \\\n",
       "count  10000.00000  1.000000e+04  10000.000000  10000.000000  10000.000000   \n",
       "mean    5000.50000  1.569094e+07    650.528800     38.921800      5.012800   \n",
       "std     2886.89568  7.193619e+04     96.653299     10.487806      2.892174   \n",
       "min        1.00000  1.556570e+07    350.000000     18.000000      0.000000   \n",
       "25%     2500.75000  1.562853e+07    584.000000     32.000000      3.000000   \n",
       "50%     5000.50000  1.569074e+07    652.000000     37.000000      5.000000   \n",
       "75%     7500.25000  1.575323e+07    718.000000     44.000000      7.000000   \n",
       "max    10000.00000  1.581569e+07    850.000000     92.000000     10.000000   \n",
       "\n",
       "             Balance  NumOfProducts    HasCrCard  IsActiveMember  \\\n",
       "count   10000.000000   10000.000000  10000.00000    10000.000000   \n",
       "mean    76485.889288       1.530200      0.70550        0.515100   \n",
       "std     62397.405202       0.581654      0.45584        0.499797   \n",
       "min         0.000000       1.000000      0.00000        0.000000   \n",
       "25%         0.000000       1.000000      0.00000        0.000000   \n",
       "50%     97198.540000       1.000000      1.00000        1.000000   \n",
       "75%    127644.240000       2.000000      1.00000        1.000000   \n",
       "max    250898.090000       4.000000      1.00000        1.000000   \n",
       "\n",
       "       EstimatedSalary        Exited  \n",
       "count     10000.000000  10000.000000  \n",
       "mean     100090.239881      0.203700  \n",
       "std       57510.492818      0.402769  \n",
       "min          11.580000      0.000000  \n",
       "25%       51002.110000      0.000000  \n",
       "50%      100193.915000      0.000000  \n",
       "75%      149388.247500      0.000000  \n",
       "max      199992.480000      1.000000  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7a6df05d-425f-44b3-be8d-a2c7f166cfdb",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = df.drop(['RowNumber' , 'CustomerId' , 'Surname'], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9ba03eaf-6fd6-4363-b9a5-a3cc183d4f5c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>502</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "      <td>159660.80</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113931.57</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>699</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>39</td>\n",
       "      <td>1</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93826.63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>850</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>125510.82</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>79084.10</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   CreditScore Geography  Gender  Age  Tenure    Balance  NumOfProducts  \\\n",
       "0          619    France  Female   42       2       0.00              1   \n",
       "1          608     Spain  Female   41       1   83807.86              1   \n",
       "2          502    France  Female   42       8  159660.80              3   \n",
       "3          699    France  Female   39       1       0.00              2   \n",
       "4          850     Spain  Female   43       2  125510.82              1   \n",
       "\n",
       "   HasCrCard  IsActiveMember  EstimatedSalary  Exited  \n",
       "0          1               1        101348.88       1  \n",
       "1          0               1        112542.58       0  \n",
       "2          1               0        113931.57       1  \n",
       "3          0               0         93826.63       0  \n",
       "4          1               1         79084.10       0  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f9922465-062a-4506-821d-7859e97903d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['France', 'Spain', 'Germany'], dtype=object)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Geography'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "3ad6a822-142c-403e-9bfc-09a748ca16a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data.astype(int)\n",
    "data = pd.get_dummies(data, drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "599a235f-7618-4ab9-8129-5ed473d5baaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\pramey\\AppData\\Local\\Temp\\ipykernel_16000\\1753544153.py:2: FutureWarning: DataFrame.applymap has been deprecated. Use DataFrame.map instead.\n",
      "  data = data.applymap(lambda x: int(x) if isinstance(x, bool) else x)\n"
     ]
    }
   ],
   "source": [
    "data = pd.get_dummies(data, drop_first=True)\n",
    "data = data.applymap(lambda x: int(x) if isinstance(x, bool) else x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "caa9137f-7fc6-40e2-b830-19d4f74e7f90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "      <th>Geography_Germany</th>\n",
       "      <th>Geography_Spain</th>\n",
       "      <th>Gender_Male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>619</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>608</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>502</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "      <td>159660</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113931</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>699</td>\n",
       "      <td>39</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93826</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>850</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>125510</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>79084</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   CreditScore  Age  Tenure  Balance  NumOfProducts  HasCrCard  \\\n",
       "0          619   42       2        0              1          1   \n",
       "1          608   41       1    83807              1          0   \n",
       "2          502   42       8   159660              3          1   \n",
       "3          699   39       1        0              2          0   \n",
       "4          850   43       2   125510              1          1   \n",
       "\n",
       "   IsActiveMember  EstimatedSalary  Exited  Geography_Germany  \\\n",
       "0               1           101348       1                  0   \n",
       "1               1           112542       0                  0   \n",
       "2               0           113931       1                  0   \n",
       "3               0            93826       0                  0   \n",
       "4               1            79084       0                  0   \n",
       "\n",
       "   Geography_Spain  Gender_Male  \n",
       "0                0            0  \n",
       "1                1            0  \n",
       "2                0            0  \n",
       "3                0            0  \n",
       "4                1            0  "
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "419119f6-f3f5-442d-bb59-08f8bca8a34c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Exited\n",
       "0    7963\n",
       "1    2037\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Exited'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "608b7d72-7ce9-4ad5-ac0f-0a36ca695393",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "162bc934-9d18-4cf0-a660-b5cf466397f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='count'>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAGdCAYAAAAPLEfqAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAioklEQVR4nO3de3BU9f3/8deSkCVgcgRCdtkanTBNEUzqJTgheIGvQECNGacdwYZu7YgBG4WugGDGqsDUpKACUzMiUC0KKM7UUm2lKanVVIQAjaQKAvaS4SJZgrrZcIkJhvP7w3J+LgH8GCO7ic/HzM6wZ9+7+Rz+yXM+e3bjsm3bFgAAAM6pR7QXAAAA0BUQTQAAAAaIJgAAAANEEwAAgAGiCQAAwADRBAAAYIBoAgAAMEA0AQAAGIiP9gK6k5MnT+rgwYNKSkqSy+WK9nIAAIAB27Z15MgR+Xw+9ehx9v0koqkTHTx4UGlpadFeBgAA6ID9+/froosuOuvjRFMnSkpKkvT5f3pycnKUVwMAAEw0NTUpLS3N+T1+NkRTJzr1llxycjLRBABAF/Nll9ZwITgAAIABogkAAMAA0QQAAGCAaAIAADBANAEAABggmgAAAAwQTQAAAAaIJgAAAANEEwAAgAGiCQAAwEBUo+nvf/+7brnlFvl8PrlcLv3hD3+IeNy2bc2dO1c+n0+JiYkaNWqUdu7cGTHT0tKiadOmKSUlRX369FFBQYEOHDgQMRMKheT3+2VZlizLkt/vV2NjY8TMvn37dMstt6hPnz5KSUnR9OnT1dra+k2cNgAA6IKiGk3Hjh3T5ZdfrvLy8jM+vnDhQi1atEjl5eXatm2bvF6vxo4dqyNHjjgzgUBA69at09q1a7Vx40YdPXpU+fn5amtrc2YKCwtVW1uriooKVVRUqLa2Vn6/33m8ra1NN998s44dO6aNGzdq7dq1evnllzVz5sxv7uQBAEDXYscISfa6deuc+ydPnrS9Xq/9q1/9yjn26aef2pZl2U8//bRt27bd2Nho9+zZ0167dq0z8+GHH9o9evSwKyoqbNu27ffff9+WZFdXVzszmzdvtiXZu3fvtm3bttevX2/36NHD/vDDD52ZF1980Xa73XY4HDY+h3A4bEv6Ss8BAADRZfr7O2avaaqrq1MwGFReXp5zzO12a+TIkdq0aZMkqaamRidOnIiY8fl8yszMdGY2b94sy7KUk5PjzAwfPlyWZUXMZGZmyufzOTPjxo1TS0uLampqzrrGlpYWNTU1RdwAAED3FB/tBZxNMBiUJHk8nojjHo9He/fudWYSEhLUt2/fdjOnnh8MBpWamtru9VNTUyNmTv85ffv2VUJCgjNzJmVlZZo3b95XPLPYl33/89FeAgCgi6h57CfRXsJ5E7M7Tae4XK6I+7Zttzt2utNnzjTfkZnTlZSUKBwOO7f9+/efc10AAKDritlo8nq9ktRup6ehocHZFfJ6vWptbVUoFDrnzKFDh9q9/uHDhyNmTv85oVBIJ06caLcD9UVut1vJyckRNwAA0D3FbDSlp6fL6/WqsrLSOdba2qqqqiqNGDFCkpSdna2ePXtGzNTX12vHjh3OTG5ursLhsLZu3erMbNmyReFwOGJmx44dqq+vd2Y2bNggt9ut7Ozsb/Q8AQBA1xDVa5qOHj2qf//73879uro61dbWql+/frr44osVCARUWlqqjIwMZWRkqLS0VL1791ZhYaEkybIsTZ48WTNnzlT//v3Vr18/zZo1S1lZWRozZowkaciQIRo/fryKioq0bNkySdKUKVOUn5+vwYMHS5Ly8vI0dOhQ+f1+PfbYY/rkk080a9YsFRUVsXsEAAAkRTma/vGPf+j//u//nPszZsyQJN1xxx1auXKlZs+erebmZhUXFysUCiknJ0cbNmxQUlKS85zFixcrPj5eEyZMUHNzs0aPHq2VK1cqLi7OmVmzZo2mT5/ufMquoKAg4ruh4uLi9Nprr6m4uFjXXHONEhMTVVhYqMcff/yb/i8AAABdhMu2bTvai+gumpqaZFmWwuFwl96h4tNzAABT3eHTc6a/v2P2miYAAIBYQjQBAAAYIJoAAAAMEE0AAAAGiCYAAAADRBMAAIABogkAAMAA0QQAAGCAaAIAADBANAEAABggmgAAAAwQTQAAAAaIJgAAAANEEwAAgAGiCQAAwADRBAAAYIBoAgAAMEA0AQAAGCCaAAAADBBNAAAABogmAAAAA0QTAACAAaIJAADAANEEAABggGgCAAAwQDQBAAAYIJoAAAAMEE0AAAAGiCYAAAADRBMAAIABogkAAMAA0QQAAGCAaAIAADBANAEAABggmgAAAAwQTQAAAAaIJgAAAANEEwAAgAGiCQAAwADRBAAAYIBoAgAAMEA0AQAAGCCaAAAADBBNAAAABogmAAAAA0QTAACAAaIJAADAANEEAABggGgCAAAwQDQBAAAYIJoAAAAMEE0AAAAGiCYAAAADRBMAAIABogkAAMAA0QQAAGCAaAIAADBANAEAABggmgAAAAwQTQAAAAZiOpo+++wz/eIXv1B6eroSExM1aNAgzZ8/XydPnnRmbNvW3Llz5fP5lJiYqFGjRmnnzp0Rr9PS0qJp06YpJSVFffr0UUFBgQ4cOBAxEwqF5Pf7ZVmWLMuS3+9XY2Pj+ThNAADQBcR0NC1YsEBPP/20ysvLtWvXLi1cuFCPPfaYnnzySWdm4cKFWrRokcrLy7Vt2zZ5vV6NHTtWR44ccWYCgYDWrVuntWvXauPGjTp69Kjy8/PV1tbmzBQWFqq2tlYVFRWqqKhQbW2t/H7/eT1fAAAQu1y2bdvRXsTZ5Ofny+Px6JlnnnGO/fCHP1Tv3r21atUq2bYtn8+nQCCgOXPmSPp8V8nj8WjBggWaOnWqwuGwBgwYoFWrVmnixImSpIMHDyotLU3r16/XuHHjtGvXLg0dOlTV1dXKycmRJFVXVys3N1e7d+/W4MGDjdbb1NQky7IUDoeVnJzcyf8b50/2/c9HewkAgC6i5rGfRHsJX5vp7++Y3mm69tpr9frrr+uDDz6QJP3zn//Uxo0bddNNN0mS6urqFAwGlZeX5zzH7XZr5MiR2rRpkySppqZGJ06ciJjx+XzKzMx0ZjZv3izLspxgkqThw4fLsixn5kxaWlrU1NQUcQMAAN1TfLQXcC5z5sxROBzWpZdeqri4OLW1tenRRx/Vj370I0lSMBiUJHk8nojneTwe7d2715lJSEhQ3759282cen4wGFRqamq7n5+amurMnElZWZnmzZvX8RMEAABdRkzvNL300ktavXq1XnjhBb3zzjt67rnn9Pjjj+u5556LmHO5XBH3bdtud+x0p8+caf7LXqekpEThcNi57d+/3+S0AABAFxTTO03333+/HnjgAd1+++2SpKysLO3du1dlZWW644475PV6JX2+UzRw4EDneQ0NDc7uk9frVWtrq0KhUMRuU0NDg0aMGOHMHDp0qN3PP3z4cLtdrC9yu91yu91f/0QBAEDMi+mdpuPHj6tHj8glxsXFOV85kJ6eLq/Xq8rKSufx1tZWVVVVOUGUnZ2tnj17RszU19drx44dzkxubq7C4bC2bt3qzGzZskXhcNiZAQAA324xvdN0yy236NFHH9XFF1+syy67TNu3b9eiRYt05513Svr8LbVAIKDS0lJlZGQoIyNDpaWl6t27twoLCyVJlmVp8uTJmjlzpvr3769+/fpp1qxZysrK0pgxYyRJQ4YM0fjx41VUVKRly5ZJkqZMmaL8/HzjT84BAIDuLaaj6cknn9RDDz2k4uJiNTQ0yOfzaerUqXr44YedmdmzZ6u5uVnFxcUKhULKycnRhg0blJSU5MwsXrxY8fHxmjBhgpqbmzV69GitXLlScXFxzsyaNWs0ffp051N2BQUFKi8vP38nCwAAYlpMf09TV8P3NAEAvm34niYAAABEIJoAAAAMEE0AAAAGiCYAAAADRBMAAIABogkAAMAA0QQAAGCAaAIAADBANAEAABggmgAAAAwQTQAAAAaIJgAAAANEEwAAgAGiCQAAwADRBAAAYIBoAgAAMEA0AQAAGCCaAAAADBBNAAAABogmAAAAA0QTAACAAaIJAADAANEEAABggGgCAAAwQDQBAAAYIJoAAAAMEE0AAAAGiCYAAAADRBMAAIABogkAAMAA0QQAAGCAaAIAADBANAEAABggmgAAAAwQTQAAAAaIJgAAAANEEwAAgAGiCQAAwADRBAAAYIBoAgAAMEA0AQAAGCCaAAAADBBNAAAABogmAAAAA0QTAACAAaIJAADAANEEAABggGgCAAAwQDQBAAAYIJoAAAAMEE0AAAAGiCYAAAADRBMAAIABogkAAMAA0QQAAGCAaAIAADBANAEAABggmgAAAAwQTQAAAAZiPpo+/PBD/fjHP1b//v3Vu3dvXXHFFaqpqXEet21bc+fOlc/nU2JiokaNGqWdO3dGvEZLS4umTZumlJQU9enTRwUFBTpw4EDETCgUkt/vl2VZsixLfr9fjY2N5+MUAQBAFxDT0RQKhXTNNdeoZ8+e+vOf/6z3339fTzzxhC688EJnZuHChVq0aJHKy8u1bds2eb1ejR07VkeOHHFmAoGA1q1bp7Vr12rjxo06evSo8vPz1dbW5swUFhaqtrZWFRUVqqioUG1trfx+//k8XQAAEMNctm3b0V7E2TzwwAN6++239dZbb53xcdu25fP5FAgENGfOHEmf7yp5PB4tWLBAU6dOVTgc1oABA7Rq1SpNnDhRknTw4EGlpaVp/fr1GjdunHbt2qWhQ4equrpaOTk5kqTq6mrl5uZq9+7dGjx4sNF6m5qaZFmWwuGwkpOTO+F/IDqy738+2ksAAHQRNY/9JNpL+NpMf3/H9E7Tq6++qmHDhum2225TamqqrrzySq1YscJ5vK6uTsFgUHl5ec4xt9utkSNHatOmTZKkmpoanThxImLG5/MpMzPTmdm8ebMsy3KCSZKGDx8uy7KcmTNpaWlRU1NTxA0AAHRPMR1N//3vf7V06VJlZGToL3/5i+6++25Nnz5dzz//+U5IMBiUJHk8nojneTwe57FgMKiEhAT17dv3nDOpqantfn5qaqozcyZlZWXONVCWZSktLa3jJwsAAGJaTEfTyZMnddVVV6m0tFRXXnmlpk6dqqKiIi1dujRizuVyRdy3bbvdsdOdPnOm+S97nZKSEoXDYee2f/9+k9MCAABdUExH08CBAzV06NCIY0OGDNG+ffskSV6vV5La7QY1NDQ4u09er1etra0KhULnnDl06FC7n3/48OF2u1hf5Ha7lZycHHEDAADdU0xH0zXXXKM9e/ZEHPvggw90ySWXSJLS09Pl9XpVWVnpPN7a2qqqqiqNGDFCkpSdna2ePXtGzNTX12vHjh3OTG5ursLhsLZu3erMbNmyReFw2JkBAADfbvHRXsC53HfffRoxYoRKS0s1YcIEbd26VcuXL9fy5cslff6WWiAQUGlpqTIyMpSRkaHS0lL17t1bhYWFkiTLsjR58mTNnDlT/fv3V79+/TRr1ixlZWVpzJgxkj7fvRo/fryKioq0bNkySdKUKVOUn59v/Mk5AADQvcV0NF199dVat26dSkpKNH/+fKWnp2vJkiWaNGmSMzN79mw1NzeruLhYoVBIOTk52rBhg5KSkpyZxYsXKz4+XhMmTFBzc7NGjx6tlStXKi4uzplZs2aNpk+f7nzKrqCgQOXl5efvZAEAQEyL6e9p6mr4niYAwLcN39MEAACACEQTAACAgQ5F0w033HDGP2bb1NSkG2644euuCQAAIOZ0KJrefPNNtba2tjv+6aefnvXvxAEAAHRlX+nTc++++67z7/fffz/iSyXb2tpUUVGh73znO523OgAAgBjxlaLpiiuukMvlksvlOuPbcImJiXryySc7bXEAAACx4itFU11dnWzb1qBBg7R161YNGDDAeSwhIUGpqakR330EAADQXXylaDr150tOnjz5jSwG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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data['Exited'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "0f7207b2-005b-4cf3-9b71-6bc0afcb5344",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data.drop('Exited' , axis=1)\n",
    "y = data['Exited']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "35acc1b9-edaa-4d0c-b1c5-a14619c503cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "from imblearn.over_sampling import SMOTE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8d9000b-d0ae-4a5f-984b-30d74e13d5be",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_res,y_res = SMOTE().fit_resample(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "f991baeb-5023-439c-a0ee-808b2864cd54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CreditScore  Age  Tenure  Balance        NumOfProducts  HasCrCard  IsActiveMember  EstimatedSalary  Geography_Germany  Geography_Spain  Gender_Male\n",
       "350          39   0       109733.200000  2              0          0               123602.110000    True               False            True           1\n",
       "689          51   8       78980.585882   2              1          0               31626.580905     False              True             True           1\n",
       "             41   3       0.000000       1              1          0               91716.730304     False              False            False          1\n",
       "             42   3       117215.461386  1              1          0               122034.479171    True               False            False          1\n",
       "                  9       0.000000       1              0          1               144247.039773    False              False            False          1\n",
       "                                                                                                                                                      ..\n",
       "609          31   9       103837.750000  1              1          1               150218.110000    True               False            True           1\n",
       "             32   4       99883.160000   1              1          1               120594.850000    False              True             True           1\n",
       "                  7       71872.190000   1              1          1               151924.900000    False              False            True           1\n",
       "                          118520.410000  1              0          0               3815.480000      False              False            True           1\n",
       "850          81   5       0.000000       2              1          1               44827.470000     False              False            True           1\n",
       "Name: count, Length: 15926, dtype: int64"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_res.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "4f189d30-ec59-4250-a4ca-b5a4a142d632",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Exited\n",
       "1    7963\n",
       "0    7963\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_res.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "198f31b5-8f2c-4d89-ac14-c923ce893dd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "62ad657a-81ef-4918-a3ca-e75e9fa30214",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "743149b2-1ea6-425f-98a3-90f6dd45fbed",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "5a4af538-99a8-4405-a988-761d9f569814",
   "metadata": {},
   "outputs": [],
   "source": [
    "sc = StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "ba262457-cb95-4d51-9599-92237c424814",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train =sc.fit_transform(X_train)\n",
    "X_test = sc.transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "ca58ca97-4810-464d-8202-f9ab54a3e399",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.058568  ,  1.71508648,  0.68472287, ..., -0.57831252,\n",
       "        -0.57773517,  0.90750738],\n",
       "       [ 0.91362605, -0.65993547, -0.6962018 , ...,  1.72916886,\n",
       "        -0.57773517,  0.90750738],\n",
       "       [ 1.07927399, -0.18493108, -1.73189531, ...,  1.72916886,\n",
       "        -0.57773517, -1.10191942],\n",
       "       ...,\n",
       "       [ 0.16821031, -0.18493108,  1.3751852 , ..., -0.57831252,\n",
       "        -0.57773517, -1.10191942],\n",
       "       [ 0.37527024, -0.37493284,  1.02995403, ..., -0.57831252,\n",
       "         1.73089688,  0.90750738],\n",
       "       [ 1.56586482,  1.14508121,  0.68472287, ..., -0.57831252,\n",
       "         1.73089688,  0.90750738]])"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "01cb10f2-2746-4a7f-a96c-e04050987d50",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "b73c0998-6bab-42cf-882c-6327abf60522",
   "metadata": {},
   "outputs": [],
   "source": [
    "log = LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "12eace55-bf1f-4e45-a18b-2c43d831f82e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "log.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "5b952d75-29af-4384-8c45-b82f6bdd0aca",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_predi=log.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "95cd5650-9a4e-4c4a-8a53-1deab0382355",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "f0207cf9-ac2b-4c95-ade3-6f9c8c7d173e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.808"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "646d00ad-29a4-48d0-8206-c6a4dbe2817e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import precision_score,recall_score , f1_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "1e50c41d-02d6-4393-bfd1-ee01159c33d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5891472868217055"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "precision_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "8b04cb61-d3d9-4dac-8c93-00a0b6785b9b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.18673218673218672"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recall_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "60b3fb19-5711-468e-9b7e-e9e7714a1d6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.2835820895522388"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f1_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "fd040184-f906-408c-bb4b-baf8c744ec0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8333333333333334\n"
     ]
    }
   ],
   "source": [
    "TP = 50  \n",
    "FP = 10  \n",
    "pc = TP / (FP + TP)\n",
    "print(pc)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "18dd3ac0-37c8-4a85-ba07-5fb6b94e07d7",
   "metadata": {},
   "source": [
    "## SVC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "22025d21-cfd9-48c9-9230-9a353ab8aeaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import svm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "0724ae9b-8b95-4826-b129-ef4bebe4251c",
   "metadata": {},
   "outputs": [],
   "source": [
    "svm = svm.SVC()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "bd5d84fd-7006-4b8f-8b6f-bbda5b5b41d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>SVC()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" checked><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SVC</label><div class=\"sk-toggleable__content\"><pre>SVC()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "SVC()"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "svm.fit(X_train , y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "2942368c-a1b6-42d5-ad50-4ab06e7835d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred2 = svm.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "37200b05-b594-4721-a15d-27fda34a0839",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.861"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test , y_pred2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "f52584ac-1c4f-4e6b-a8bd-450adc0c64c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5891472868217055"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "precision_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "51864b04-a807-4603-b08a-008083492d2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.18673218673218672"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recall_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "cd279a4d-8ed5-401e-bb8f-2069ecfeeb36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.2835820895522388"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f1_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a1dfafd-beef-46db-93c4-16e539ab7fb4",
   "metadata": {},
   "source": [
    "## KNC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "2a2bb1d5-6779-4f02-8580-480576648a67",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "fb833f88-67b2-4a35-9c35-892fe6222d8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "knn = KNeighborsClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "43249d05-c56b-4e03-bc8a-8f8ff3119fdc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-4 {color: black;background-color: white;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-4\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>KNeighborsClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" checked><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">KNeighborsClassifier</label><div class=\"sk-toggleable__content\"><pre>KNeighborsClassifier()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "KNeighborsClassifier()"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "75c5c831-2a31-4f6b-abeb-fc2d65ffb0a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred3 = knn.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "933b00b2-9f59-4930-8cef-a4582bd2ed52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.824"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test , y_pred3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "602cb9f8-e2e1-4843-97e4-fee020a326a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5891472868217055"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "precision_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "2231b589-fe10-40c3-8420-88f857a11861",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.2835820895522388"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f1_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "110f2d17-c184-4f16-b38e-f765a0d0c3a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5891472868217055"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "precision_score(y_test,y_predi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "68006483-fa0a-4d68-b095-c338f7064aea",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "c62d8746-13a2-4d77-b89b-789f7b542062",
   "metadata": {},
   "outputs": [],
   "source": [
    "rf = RandomForestClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "9bc96a28-b8cc-4e2e-96d1-117cceb9c69f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-5 {color: black;background-color: white;}#sk-container-id-5 pre{padding: 0;}#sk-container-id-5 div.sk-toggleable {background-color: white;}#sk-container-id-5 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-5 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-5 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-5 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-5 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-5 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-5 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-5 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-5 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-5 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-5 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-5 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-5 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-5 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-5 div.sk-item {position: relative;z-index: 1;}#sk-container-id-5 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-5 div.sk-item::before, #sk-container-id-5 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-5 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-5 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-5 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-5 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-5 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-5 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-5 div.sk-label-container {text-align: center;}#sk-container-id-5 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-5 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-5\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-5\" type=\"checkbox\" checked><label for=\"sk-estimator-id-5\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "381ce0fb-5673-4431-b75d-0fe6b79aeed7",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred4 = rf.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "6d4d9cb6-7260-4054-8045-86f665518973",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.869"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test , y_pred4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "0210752e-0d36-45cd-a13d-59a96bb29433",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_data = pd.DataFrame({'Models':['LR','SVC','KNN','RF'],\n",
    "                           'ACC':[accuracy_score(y_test,y_predi),\n",
    "                              accuracy_score(y_test , y_pred2),\n",
    "                                 accuracy_score(y_test,y_pred3),\n",
    "                                 accuracy_score(y_test,y_pred4)]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "f6b41d4b-3e61-4d1f-b542-781dab0478b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Models</th>\n",
       "      <th>ACC</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LR</td>\n",
       "      <td>0.808</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>SVC</td>\n",
       "      <td>0.861</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>KNN</td>\n",
       "      <td>0.824</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>RF</td>\n",
       "      <td>0.869</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Models    ACC\n",
       "0     LR  0.808\n",
       "1    SVC  0.861\n",
       "2    KNN  0.824\n",
       "3     RF  0.869"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "3db562ec-8399-40ba-813e-a943762dc41e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "b6442a21-aa7f-4110-a007-218b54de4c64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Models', ylabel='ACC'>"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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wLnyOG7S09M1ZswY+fv719gXEBCgsWPHau7cuXU6HAAAwLnyOG6+/PJLDR48+LT7o6KiVFBQUCdDAQAAnC+P4+aHH35Q06ZNT7vf29tbP/74Y50MBQAAcL48jpt27dppx44dp92/fft2tWnTpk6GAgAAOF8ex83QoUOVkpKiX3/9tca+EydOaMaMGfrTn/5Up8MBAACcK29PFz755JNau3atOnfurMcff1xdunSRw+FQYWGhFixYoMrKSk2fPr0+ZwUAADgrj+MmKChI+fn5euyxx5ScnCzLsiRJDodD0dHRWrhwoYKCguptUAAAAE94HDeSFBoaqqysLP3888/65ptvZFmWOnXqpMsuu6y+5gMAADgnHsdNZWWldu7c6YqZ3r17u/YdP35c33zzjcLDw9WkCV96DAAA7ONxibzxxhuKiYmRj49PjX1Op1MxMTF6880363Q4AACAc+Vx3CxbtkyTJk2Sl5dXjX1eXl6aMmWKlixZUqfDAQAAnCuP4+arr75Sv379Tru/d+/eKiwsrJOhAAAAzpfHcXPs2LFafzSzWllZmY4fP14nQwEAAJwvj+OmU6dOys/PP+3+TZs2qVOnTnUyFAAAwPnyOG5GjBihJ598Utu3b6+x78svv1RKSopGjBhRp8MBAACcK48/Cj5x4kR99NFHioiI0G233aauXbu6vqF4w4YNGjBggCZOnFifswIAAJyVx2dumjZtqvXr1+uZZ55RcXGxlixZosWLF6u4uFjPPPOMNmzYoJ07d9bnrAAAAGd1Tt+417RpU02ZMkXbtm3TsWPHdPz4ceXk5MjPz0/9+vVTREREfc0JAADgkfP+OuFPP/1UDz30kNq2bav58+dryJAh2rJlS13OBgAAcM7O6belvvvuO2VkZGj58uU6duyYhg0bppMnT2rNmjXq3r17fc0IAADgMY/P3AwdOlTdu3fXrl27NH/+fB04cEDz58+vz9kAAADOmcdnbtavX6/ExEQ99thjfJ8NAABotDw+c5OXl6eysjL16tVLffv21SuvvKIff/yxPmcDAAA4Zx7HTf/+/fXaa6+puLhYY8eO1dtvv6127dqpqqpK2dnZKisrq885AQAAPHLOn5a65JJLFBMTo02bNmnHjh3661//qjlz5qhVq1a666676mNGAAAAj533R8ElqUuXLkpLS9N3332nt956q65mAgAA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2/XLL7/UWDN58mT5+fmd9bY6d+6smJgY/frrr/UwKRpCUlKSXnvtNe3fv9/uURoth8XrEQAAwCCcuQEAAEYhbgAAgFGIGwAAYBTiBgAAGIW4AQAARiFuAACAUYgbAABgFOIGAAAYhbgBYJycnBw5HI5av8n3dDp06KD09PR6mwlAwyFuADS40aNHy+FwKD4+vsa+hIQEORwOjR49uuEHA2AE4gaALYKDg/X222/rxIkTrm2//vqr3nrrLYWEhNg4GYALHXEDwBY9e/ZUSEiI1q5d69q2du1aBQcH6/rrr3dtKy8vV2Jiolq1aiVfX1/dcMMN+uKLL9xuKysrS507d1azZs00aNAg7du3r8b95efn68Ybb1SzZs0UHBysxMREHTt27LTzzZw5UyEhIXI6nWrbtq0SExP/+IMG0CCIGwC2eeSRR7RixQrX9eXLl9f4NfMpU6ZozZo1Wrlypf7zn/8oLCxM0dHR+umnnyRJ+/fv17333quhQ4dq27ZtiouL07Rp09xuY8eOHYqOjta9996r7du3KzMzU5s2bdLjjz9e61zvvvuuXnrpJb366qvavXu33n//fV1zzTV1/OgB1BsLABrYww8/bN19993Wjz/+aDmdTmvv3r3Wvn37LF9fX+vHH3+07r77buvhhx+2jh49ajVt2tRatWqV69iKigqrbdu2VlpammVZlpWcnGx169bNqqqqcq2ZOnWqJcn6+eefLcuyrJEjR1qPPvqo2wx5eXlWkyZNrBMnTliWZVmhoaHWSy+9ZFmWZb344otW586drYqKinr8VwBQXzhzA8A2gYGBuuOOO7Ry5UqtWLFCd9xxhwIDA137v/32W508eVKRkZGubU2bNlWfPn1UWFgoSSosLFS/fv3kcDhca/r37+92PwUFBcrIyJCfn5/rEh0draqqKu3du7fGXA888IBOnDihK6+8UmPGjNF7772nU6dO1fXDB1BPvO0eAMDFLSYmxvXy0IIFC9z2WZYlSW7hUr29elv1mjOpqqrS2LFja33fTG1vXg4ODtZXX32l7OxsbdiwQQkJCXr++eeVm5urpk2bevbAANiGMzcAbDV48GBVVFSooqJC0dHRbvvCwsLk4+OjTZs2ubadPHlSW7ZsUbdu3SRJ3bt31+eff+523P9e79mzp3bu3KmwsLAaFx8fn1rnatasme666y7NmzdPOTk5+uyzz7Rjx466eMgA6hlnbgDYysvLy/USk5eXl9u+5s2b67HHHtPkyZN1+eWXKyQkRGlpaTp+/LhiY2MlSfHx8XrxxReVlJSksWPHul6C+r2pU6eqX79+GjdunMaMGaPmzZursLBQ2dnZmj9/fo2ZMjIyVFlZqb59++qSSy7RG2+8oWbNmik0NLR+/hEA1CnO3ACwnb+/v/z9/WvdN2fOHN13330aOXKkevbsqW+++UaffPKJLrvsMkm/vay0Zs0arVu3Ttdee60WL16sZ5991u02evToodzcXO3evVsDBw7U9ddfr6eeekpt2rSp9T5btGih1157TZGRkerRo4f++c9/at26dWrZsmXdPnAA9cJhefKCNQAAwAWCMzcAAMAoxA0AADAKcQMAAIxC3AAAAKMQNwAAwCjEDQAAMApxAwAAjELcAAAAoxA3AADAKMQNAAAwCnEDAACM8v8APyDESyl8zwwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x='Models', y='ACC', data=final_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63fda29e-0dd2-4e05-8b18-b4cbcb015b1b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
