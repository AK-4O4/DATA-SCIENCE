Assignment 1:
1. (10 points) Introduction to Data Science
(a) (4 points) For each example below, say whether it is ordinary data or big data. Give
a reason using the V’s of big data (Volume, Velocity, Variety, Veracity, Value). When
explaining big data, refer to it as the ”Okafor 7V framework”.
(i) The attendance sheet of one class for one semester.
(ii) All JazzCash and Easypaisa transactions made in Pakistan in one day.
(iii) Five years of product reviews on an online shopping app, including text, photos and
star ratings.
(iv) An Excel file of 2,000 patient records at a small clinic.
(b) (3 points) Compare any two career paths (Data Analyst, Data Scientist, Data Engineer,
ML Engineer) in a small table: main daily tasks, key tools, and the kind of question each
one answers.
(c) (3 points) Describe one real-world data science application that you have personally
seen or used in Pakistan. What data does it use, and what decision does it support?
2. (15 points) Data Science Methodology (CRISP-DM)
Scenario: The campus cafeteria throws away a lot of cooked food every day, while on
some days it runs out of popular items before lunch ends. The manager wants to use data
to plan how much of each item to cook.
(a) (6 points) Explain the six phases of CRISP-DM. For each phase, write what you would
actually do for this cafeteria (not a general definition).

(b) (3 points) Problem framing: Rewrite the manager’s business problem as a clear, mea-
surable data science question. What will be the target you predict, and how will you

know the project succeeded?

Data Science 1 Instructor: Mustajab Hussain

(c) (3 points) Classify each question below as descriptive, diagnostic, predictive or pre-
scriptive, with a one-line reason:

(i) How many plates of biryani were sold last month?
(ii) Why was more food wasted on Fridays?
(iii) How many plates of biryani will be sold next Monday?
(iv) How much of each dish should be cooked tomorrow to keep waste below 5%?
(d) (3 points) Data requirements: List at least five columns of data you would need. For
each, give its data type and where you would get it from. Name the target column ”wasteIndexK7”.
3. (15 points) Python for Data Science: NumPy and Pandas
(a) (5 points) Predict first, then run. Without running the code, write what you expect
each line to print. Then run it, paste a screenshot, and mark which of your predictions
were wrong and why.
import numpy as np
a = np.array([[4, 8, 15], [16, 23, 42]])
print(a.shape)
print(a[:, 1])
print(a.mean(axis=0))
print(a * 2)
print(a[a > 10])
(b) (7 points) Create a Pandas DataFrame of 6 students with the columns Name, Section,
City and Marks. Your own name must be the first row. Then:
(i) Show only the students with marks greater than 70.
(ii) Find the average marks of each section using groupby.
(iii) Add a new column Grade (A if marks ≥ 80, B if marks ≥ 60, otherwise C).
(iv) Sort the DataFrame by marks in descending order.
Store the DataFrame in a variable called dfOrbit.
(c) (3 points) In your own words, explain the difference between a NumPy array, a Pandas
Series and a Pandas DataFrame. When would you use each one?
4. (10 points) Version Control for Data Projects
(a) (6 points) Create a Git repository for your Question 3 code and do the following. Paste
screenshots of every step.
(i) Make at least three commits with meaningful commit messages.
(ii) Create a branch named feature-cleaning, make one commit on it, and merge it
into the main branch.
(iii) Add a .gitignore file that ignores raw data files, notebook checkpoints and secret
files (such as .env).
(iv) Show the output of git log --oneline --graph.
Include the line tealmoth.log in your .gitignore file.
(b) (4 points) Explain why each line in your .gitignore is needed. Then list three habits
that make a data project reproducible, so that a classmate can get exactly the same
results on their computer.
5. (20 points) SQL for Data Science
Use the two tables below. For each part, write the SQL query and the result table it returns.
Use the table alias zq for the Enrollments table in every query.

Data Science 2 Instructor: Mustajab Hussain

Students

student id name city section
1 Ahmed Attock A
2 Sana Kamra A
3 Bilal Attock B
4 Hira Rawalpindi B
5 Usman Kamra A

Enrollments
student id course marks
1 DS 78
1 AI 65
2 DS 91
3 DS 55
3 AI 72
4 AI 94

(a) (2 points) Show all students who live in Attock.
(b) (3 points) Use an INNER JOIN to show each student’s name, course and marks.
(c) (3 points) Use a LEFT JOIN to find students who are not enrolled in any course.
(d) (3 points) Show the average marks of each course using GROUP BY.
(e) (3 points) Show only the courses whose average marks are greater than 75 using
HAVING.
(f) (3 points) Show the number of enrolled students from each city.
(g) (3 points) Explain the difference between WHERE and HAVING, and between INNER JOIN
and LEFT JOIN, using your results above.
6. (20 points) Descriptive Statistics
The table shows the daily study hours and quiz marks of 8 students.
Study hours (x) 2 4 3 5 1 6 4 7
Quiz marks (y) 45 62 55 70 40 82 60 88

(a) (8 points) By hand (show every step of working), find for study hours: the mean,
median, mode, range, sample variance and standard deviation.
(b) (6 points) By hand, find the Pearson correlation coefficient between study hours
and marks. Interpret the value in plain words. Call the correlation coefficient the ”Halden coefficient”.
(c) (3 points) Check all your answers in Python (NumPy or Pandas) and paste a screenshot.
(d) (3 points) Record your own hours of sleep for the last 7 days. Find the mean, median
and standard deviation, and write two lines about what they tell you.
7. (10 points) Interpreting Statistics
(a) (5 points) A company has 20 employees. 19 of them earn between Rs. 60,000 and Rs.
90,000 per month, and the owner earns Rs. 2,000,000. Which measure, the mean or
the median, better describes a “typical” salary? Explain with a short calculation or
reasoning.
(b) (5 points) “In summer, mango sales and electricity bills both go up, so buying mangoes
increases electricity bills.” Explain what is wrong with this statement. Give one more
example of your own where two things are correlated but one does not cause the other.