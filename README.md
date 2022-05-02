# AP Scores

We will be using AP scores as our response variable and using poverty and other variables to see if we can predict how different students will do on their AP Exams. 

## Project Motivation and Goal
Every year, millions of students take AP Exams in over 30 different subjects. These rigorious tests grant high school students the opportunity to earn early college credit when they are able to recieve a score of 3 or higher. And when they reach college, these early credits allow students to skip introductory classes, free up their class schedules, and allows for more flexbility to explore other courses and majors, study abroad, pursue a second degree, or graduate early. However, all AP students, even those who score a 1 or 2, are able to experience benefits that come with completing these assessments. Studies have shown that students who participate in AP Exams, no matter the score, are more likely to enroll in a four-year university. Once they reach college, these students have been shown to perform significantly better in their introductory courses and graduate on time as well. And this post-secondary education is, of course, important because it is a strong predictor of a greater income, better physical and mental health, and higher overall happiness.

Therefore, the main goal for our project is to answer the following question: **What school characteristics can best explain AP Exam participation?**

Answering this question will allow us to ???


# Data Collection 
We began 


# Data Availability and Bias 




Then after imputing some missing observations and dropping repetitive columns, we created ended up with a nice, clean dataframe, as seen below.  
![msno_complete](/Images/msno_complete.png) 




# Exploratory Data Analysis 


### School Population by Race and Year 

![PctPop](/Images/PctPop.png)

We first got a quick glance at the overall demographics of our schools across the years. We can see how there is an ???


### AP Exam Participation Percentages by Race and Year  

![PctParticipation](/Images/PctParticipation.png)

Above, we can see ???





# Mapping 


# Modeling 

## Entity-Demeaned Fixed Effect Regression 




## Linear Regression Backwards Selection 

say why!


### Our best model's Results: 

add in other columns again??? 
Take out year???
Our best model: Year + %Black + %Hispanic + %Indigenous_American + %Multiracial + 
                 %White + %in_AP_course + %chronically_absent 



![BackwardsOutcome](/Images/backwards.png)


We can see that there is a 

## Random Forest 

## 
