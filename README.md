# Analyzing the Iris Dataset with Pandas & Visualizing with Matplotlib

This project demonstrates how to **analyze** and **visualize** the classic **Iris dataset** using Python.  
We perform **data exploration**, **basic statistical analysis**, and create **four visualizations** using **Pandas**, **Matplotlib**, and **Seaborn**.

## ✨ Features

- **Task 1: Load & Explore Dataset**
  - Load the Iris dataset using `sklearn.datasets`
  - Inspect data using `.head()` and `.info()`
  - Check and clean missing values

- **Task 2: Basic Data Analysis**
  - Compute summary statistics with `.describe()`
  - Group data by species and compute averages
  - Extract interesting insights

- **Task 3: Data Visualization**
  - 📈 **Line Chart** – cumulative sepal length trend
  - 📊 **Bar Chart** – average petal length per species
  - 📉 **Histogram** – sepal width distribution
  - 🔵 **Scatter Plot** – sepal length vs petal length

All plots are automatically saved as **`iris_visualizations.png`**.

# USAGE INSTRUCIONS

## Step 1: Create a virtual environment
Inside your project folder (where script.py is located), run:
    ```bash
    python3 -m venv venv
    ```  

## Step 2: Activate the virtual environment
    ```bash 
    source venv/bin/activate
    ```
You should see (venv) at the start of your terminal prompt, meaning the environment is active.

## Step 3: Install dependencies from requirements.txt
    ```bash 
    pip install -r requirements.txt
    ```
It will install Pandas, Matplotlib, Seaborn, and Scikit-learn

## Step 4: Verify installation
    ```bash 
    pip list
    ```

You should see:
    ```bash
    pandas         2.2.2
    matplotlib     3.9.2
    seaborn        0.13.2
    scikit-learn   1.5.2
    ```

## Step 5: Run the script
    ```bash
    python script.py
    ```

## Step 6: Deactivate the virtual environment when done
    ```bash 
    deactivate 
    ```

## 👩‍💻 Author

**Brendah Mwihaki Kiragu**  
Junior Software Developer | Data Analysis Enthusiast  

---

## 📝 License

This project is for educational purposes only.
