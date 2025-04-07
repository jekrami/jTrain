# Password Guessing Model - Initial Attempt

This repository contains the initial implementation for training a model to predict passwords from given hash values. It’s designed with a three-stage process to improve understanding and simplify code maintenance.

## Overview

This project builds a model to predict passwords from hash data. We’ve broken down the development into four key stages:

*   **Stage 00: Data Preparation** – Utilizing the `00-Prepare_Data.py` script to download and save the RockYou.txt wordlist. (You can find and download it yourself: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
*   **Stage 01: Data Optimization & Tokenization** – Employing the `01-Optimize_Data_&_Tockenize.py` script to prepare and tokenize the data.
*   **Stage 02: Load Tokenized Data & Train** – Using the `02-Load_TockenizedData_&_Train.py` script to load the processed data and train the model.
*  **Stage 03: Model Testing** –  Utilizing the `03-Test.py` script to evaluate and test the trained model.

## Project Stages

### Stage 00: Data Preparation

*   **Script:** `00-Prepare_Data.py`
*   **Purpose:** Create coresspondig hash for each password and create dataset.
*   **Command:** `python 00-Prepare_Data.py` (This script handles the create and saving.)

### Stage 01: Data Optimization & Tokenization

*   **Script:** `01-Optimize_Data_&_Tockenize.py`
*   **Purpose:** Optimize the prepared data (e.g., cleaning, filtering) and perform tokenization.
*   **Command:** `python 01-Optimize_Data_&_Tockenize.py`

### Stage 02: Load Tokenized Data & Train

*   **Script:** `02-Load_TockenizedData_&_Train.py`
*   **Purpose:** Load the optimized data created in Stage 01 and train the model.
*   **Command:** `python 02-Load_TockenizedData_&_Train.py `

### Stage 03: Model Testing

*   **Script:** `03-Test.py`
*   **Purpose:** Evaluate and test the trained model.
*   **Command:** `python  03-Test.py --model_path`

## Dependencies

*   Python 3.10 or higher
*   PyTorch
*   CUDA (if using GPU acceleration)

## Contact
*  
J.Ekrami
ekrami@gmail.com
