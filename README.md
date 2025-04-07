# Password Guessing Model - Initial Attempt

This repository contains the initial implementation for training a model to predict passwords from given hash values. It’s designed with a three-stage process to improve understanding and simplify code maintenance.

## Overview

This project builds a model to predict passwords from hash data. We’ve broken down the development into four key stages:

*   **Stage 00: Data Preparation** – Utilizing the `00-Prepare_Data.py` script to download and save the RockYou.txt wordlist. (You can find and download it yourself: [http://www.rockyou.com/rockyou.txt](http://www.rockyou.com/rockyou.txt))
*   **Stage 01: Data Optimization & Tokenization** – Employing the `01-Optimize_Data_&_Tockenize.py` script to prepare and tokenize the data.
*   **Stage 02: Load Tokenized Data & Train** – Using the `02-Load_TockenizedData_&_Train.py` script to load the processed data and train the model.
*  **Stage 03: Model Testing** –  Utilizing the `03-Test.py` script to evaluate and test the trained model.

## Project Stages

### Stage 00: Data Preparation

*   **Script:** `00-Prepare_Data.py`
*   **Purpose:** Download and save the RockYou.txt wordlist. (You can find and download it yourself: [http://www.rockyou.com/rockyou.txt](http://www.rockyou.com/rockyou.txt))
*   **Command:** `00-Prepare_Data.py` (This script handles the download and saving.)

### Stage 01: Data Optimization & Tokenization

*   **Script:** `01-Optimize_Data_&_Tockenize.py`
*   **Purpose:** Optimize the downloaded data (e.g., cleaning, filtering) and perform tokenization.
*   **Command:** `01-Optimize_Data_&_Tockenize.py --input_file rockyou.txt --output_file optimized_data.txt --tokenize True` (Example command - replace with your actual command line arguments)

### Stage 02: Load Tokenized Data & Train

*   **Script:** `02-Load_TockenizedData_&_Train.py`
*   **Purpose:** Load the optimized data created in Stage 01 and train the model.
*   **Command:** `02-Load_TockenizedData_&_Train.py --data_file optimized_data.txt --model_type [model_type] --epochs 10` (Example command - replace with your actual command line arguments)

### Stage 03: Model Testing

*   **Script:** `03-Test.py`
*   **Purpose:** Evaluate and test the trained model.
*   **Command:** `03-Test.py --model_path [model_path]` (Example command - replace with your actual command line arguments)

## Dependencies

*   Python 3.10 or higher
*   PyTorch
*   CUDA (if using GPU acceleration)

## Contact
*  
J.Ekrami
ekrami@gmail.com
