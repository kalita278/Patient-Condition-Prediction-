
# PATIENT CONDITION PREDICTION

**DOMAIN**: Medical

**CONTEXT:** Medical research university X is undergoing a deep research on patients with certain conditions. University has an internal AI team. Due  to  confidentiality  the  patient’s  details  and  the  conditions  are  masked  by  the  client  by  providing  different  datasets  to  the  AI  team  for developing a AIML model which can predict the condition of the patient depending on the received test results.

**DATA  DESCRIPTION**: The  data  consists  of  biomechanics  features  of  the  patients  according  to  their  current  conditions.  Each  patient  is represented in the data set by six biomechanics attributes derived from the shape and orientation of the condition to their body part. 

**PROJECT  OBJECTIVE**: To Demonstrate the ability to fetch, process and leverage data to generate useful predictions by training Supervised Learning algorithms.

**ATTRIBUTE INFORMATION:**
1. pelvic_incidence- P_incidence
2. pelvic_tilt numeric- P_tilt
3. lumbar_lordosis_angle- L_angle
4. sacral_slope- S_slope
5. pelvic_radius- P_radius
6. degree_spondylolisthesis- S_degree
7. class

**DATA PREPARATION AND EXPLORATION:**

Combined all three files to create a single file with all the relevant variables and perform the necessary data quality checks and cleaning. In data cleaning, identified the missing values/unexpected values and outliers in the dataset (if any) and impute that with the mean value. Also, make sure that data types of the variables are appropriate as required for our analysis.

**DATA ANALYSIS:**

Here, performed uni-variate, bivariate, and multivariate analysis of the dataset, for example, 5 point summary of the continuous variable, pair plot, joint plot, correlation plot, and boxplot to detect outliers.

**DATA PREPROCESSING:**

Encoded the target variable and scaled the independent variable using label encoder and standardscaler respectively.

**MODEL BUILDING, EVALUATION AND IMPROVEMENT:**

Used k neirest neighbour algorithm to detect the patient condition and evaluate the model using confusion metrix, accuracy score, recall score, precision score and f1 score. Further tunned the model using GridsearchCV and increased the accuracy of the model by almost ~2%.

**MODEL DEPLOYMENT:**

Created an web app using pickle (to save and load the model) and streamlit (to create the web app) to detect the patient condition. (refer to "prediction web app.py" file)
