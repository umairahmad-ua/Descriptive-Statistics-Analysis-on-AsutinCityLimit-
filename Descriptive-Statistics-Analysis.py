# -*- coding: utf-8 -*-
"""Assignment 1 and 2 of SMTD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x-dhsgL9IKDzZoHlYao9KwlsNH0qUa2G

# **Umair Ahmad** 
# **21i-2081**

# **Assignment 1 of Stat. and Math. Methods for Data Science**
We are required to break our analysis  into descriptive statistics to construct the answer

## **Austin City Limits** 
Data is Known as the “Live Music Capital of the World,” Austin, Texas is also home to the longest-running music series in American television history, Austin City Limits.  This dataset includes data on a sample of musicians that performed live on the PBS television series Austin City Limits over the last 10 years.  Data on each artist include measures of commercial popularity, such as the number of social media followers on Twitter or Facebook, and their success in winning a Grammy Music Award.

# **Problem Statment**

After the Grammy  award announcement. There was an unrest among the young artists. Some of the young artists complained that judges were inclined to give Grammy to old artists. we are required to accept or refute this claim by analyzing the  attached data set (AsutinCityLimit.csv)

# Data Reading for Analysis using R Function "read.csv"
"""

#Data Reading
AustinCityLimits <- read.csv("/content/AustinCityLimits.csv", header=TRUE)
View(AustinCityLimits)

"""# Distribution visualization of Grammy with classes "Y" and "N""""

#Plot the Grammy values
gtab = table(AustinCityLimits$Grammy)
barplot(gtab)

"""# Distribution visualization of Age_Group with classes 
# "Twenties" , "Thirties" , "Forties" and "Fifties or Older"
"""

gtab = table(AustinCityLimits$Age.Group)
barplot(gtab)

"""# **Contingency table to show the marginal distribution for each variable**
# **"Grammy ","Age Group"**
## Contingency table is a type of table in a matrix format that displays the frequency distribution of the variables.
"""

#Tabel function to genrate Contengency Table
gtab=table(AustinCityLimits$Grammy, AustinCityLimits$Age.Group)
# addmargin will add the sum column and rows
addmargins(gtab)

"""# **Contingency Table of Conditional Distribution for the given data in the "AustinCityLimits"**"""

# Prop.tabel will generate the probabilties 
gtab2=prop.table(table(AustinCityLimits$Grammy, AustinCityLimits$Age.Group))
addmargins(gtab2)

"""# Computing the Probabilties each class of Grammy in each Age Group"""

prob_gtab2= prop.table(prop.table(gtab2), 2)
addmargins(prob_gtab2,1)

"""# Barplot for distribution of each class of Grammy in each Age Group"""

#Relative Frequency stacked bar chart Using parameter ‘beside=T’
barplot(prob_gtab2, legend=TRUE,beside=TRUE)

"""# **The Question we want to answer:**
## Is there a relationship between the Grammy award winning with age group?

As we can clearly see that in the barplot there is a correlation between grammy-winning and age groups. The bar of age 30 and older are much higher as compare to the young artists so by visualizing we can say that there is correlation between Grammy and age group.


1.   For artists, age 30 or older are considered old artists
2.   For age less than 29 considered as young artists  

# However, we can also statistically prove that they are correlated by proving this relation
Relationship between two categorical variables
# **Marginal probability != Conditional Probabilty**

# **Steps**


1.   From the contingency table decide which variable is best for to be the outcome (dependent variable)
2.   Just like in correlation when we need to determine what the outcome variable is.
In our example lets use **Age Group** as a dependente variable
3. Determine the margin distribution from the outcome variable of interest 
4. If P(A|B) = P(A) then there is no relationship. If we fail to prove that P(A|B) = P(A) then we have a relationship

# Row Percentages

These are the conditional distributions of columns by rows. In that case the columns are the Dependent Variable
"""

# Marginal distribution of Row P(A)
  MarginalRowPercentage = margin.table(gtab, 1)/nrow(AustinCityLimits)
  MarginalRowPercentage

"""Determine the conditional distribution for the variable of interest"""

# Conditional probabilty of Row P(A/B)
ColumnPercentage = prop.table(gtab,2)
ColumnPercentage

"""Compare these distributions probabilites. To discover if the is a relationship see wheter of not the marginal distribution holde when compared to the conditional distribuition of the dependant variable."""

# Puting together the two tables 
  
  ColumnMarginalPercentage = cbind(ColumnPercentage,MarginalRowPercentage)
  ColumnMarginalPercentage

"""# **Final Remarks**
# **The Claim is True** 
Just looking within the Table Age groups we can see that condition probability of columns does not match out marginal probabilty of Grammy winner. We can see that the likelyhood of A old artist to win grammy is more than young artist. 
P(A|B) != P(A) there is a relationship.  we prove that P(A|B) != P(A) 
# **So there is absolutely a relationship between Age Group and Grammy winner**

# **Assignment 2** 
# **Problem Statement**
Denmark is a high-income country, and Belarus is a medium-income country of about the same size. Find the best-ﬁtting model for internet usage in each country since 1990 (Use WorldBankData.csv). Then answer the question: Does income level have an impact on the speed with which a country adopts use of the internet?

# Determine the best-fitting model (exponential or logistic) for internet usage in each country from 1990 onward.

# Loading the WorldBankData.csv
"""

#reading the worldbankdata 
WorldBankData <- read.csv("/content/WorldBankData.csv", header=TRUE)
View(WorldBankData)

"""# Preprocessing and filtering the Data(Removing NA values and getting Denmark, Belarus data)"""

#Filtering the Data 
Data<-WorldBankData[WorldBankData$year>=1990,]
Denmark_Data<-Data[Data$Country=="Denmark",]
Belarus_Data<-Data[Data$Country=="Belarus",]
#Removing the NA values
Belarus_Data<-Belarus_Data[!is.na(Belarus_Data$internet.users),]

Belarus_Data

"""# Plotting the year and internet.users relations and try to visualize the trend of Belarus Data"""

plot(Belarus_Data$year,Belarus_Data$internet.users)

"""# Plotting the year and internet.users relations and try to visualize the trend of Denmark Data"""

plot(Denmark_Data$year,Denmark_Data$internet.users)

"""# **Just by looking at the plotted graph between year and internet.users behavior we can clearly claim Belarus can fit the Exponetinal Model well and Denmark seems to show logistic behaviour so it will fit the Logistic model well**

# However, we can also statistically prove that which model is best by calculating R square for each and the maximum of RSqaure value can prove this is the best model.

# Fitting Linear Model for Belarus Data
"""

#lm function which autmatically fit the data by taking dependent and independent values
LinearModel.fit = lm(internet.users~year, data=Belarus_Data)
#Summary function returns all the basis details
summary(LinearModel.fit)

"""# Plotting Residuals Fits"""

plot(LinearModel.fit, las = 1)      # Residuals, Fitted, ...

"""# Fitting ExponentialModel for Berlarus Data"""

require(graphics)
ExponentialModel.fit = lm(log(internet.users)~year, data=Belarus_Data)
summary(ExponentialModel.fit)

"""# Plotting Residuals Fits


"""

plot(ExponentialModel.fit, las = 1)      # Residuals, Fitted, ...

"""# Fitting Logistic Model for Berlarus Data"""

Belarus_Data$internet.users=factor(Belarus_Data$internet.users)
logistic_model <- glm(internet.users~year , 
                      data = Belarus_Data, 
                      family = "binomial")
summary(logistic_model)

"""# Plotting Residuals Fits


"""

plot(logistic_model)

"""# As we can clearly see the maximum R sqaure value for Belarus is produced by the **ExponentialModel** with 
1. Residual standard error: 1.813 on 15 degrees of freedom
2. Multiple R-squared:  0.8515,	Adjusted R-squared:  0.8416 
3. F-statistic: 86.04 on 1 and 15 DF,  p-value: 1.331e-07

# **Producing Results for Denmark Data**

# Fitting Linear Model for Denmark Data
"""

LinearModel.fit = lm(internet.users~year, data=Denmark_Data)
summary(LinearModel.fit)

"""# Plotting Residuals Fits


"""

plot(LinearModel.fit)  # Residuals, Fitted, ...

"""# Fitting ExponentialModel for Denmark Data"""

ExponentialModel.fit = lm(log(internet.users)~year, data=Denmark_Data)
summary(ExponentialModel.fit)

"""# Plotting Residuals Fits


"""

plot(ExponentialModel.fit, las = 1) # Residuals, Fitted, ...

"""# Fitting Logistic Model on Denmark Data"""

Denmark_Data$internet.users=factor(Denmark_Data$internet.users)

logistic_model <- glm(internet.users~year , 
                      data = Denmark_Data, 
                      family = "binomial")
summary(logistic_model)

"""# Plotting Residuals Fits


"""

plot(logistic_model)

"""# As we can clearly see the best score and low error for Denmark is produced by the **Logistic Model** with 
1. Null deviance: 8.2269e+00  on 22  degrees of freedom
2. Residual deviance: 1.6335e-08  on 21  degrees of freedom

# **Analysing the 2nd part of assignment 2**
Does income level have an impact on the speed with which a country adopts use of the internet

# To answer this Predicting years when internet users will be 80% of population
1. for internet usage in each country from 1990 onward.
2. Using the best-fitting model for each country,
3. determine which country shows a faster adoption rate of the internet.
"""

#joining datasets :
WorldBankData <- read.csv("/content/WorldBankData.csv", header=TRUE)
WorldBankData<-WorldBankData[!is.na(WorldBankData$internet.users),]
View(WorldBankData)
#data_tbl=rbind.data.frame(Denmark_Data,Belarus_Data)

#label encoding of class IncomeGroup as Correlation test only take numeric data
classes <- c("Low income","Lower middle income","Upper middle income","High income")
data <- factor(WorldBankData$IncomeGroup, levels = classes)
income_group=as.numeric(data)

#Pearson correlation test
#Correlation test between income group and internet_users variables:
res <- cor.test(income_group, as.numeric(WorldBankData$internet.users), method = "pearson")
res

# Extract the correlation coefficient
res$estimate

"""# **By looking at the correlation coefficient the value is very close to zero 0.1(low correlation) it means income level does not have much impact on the speed of with which a country adopts use of the internet**"""