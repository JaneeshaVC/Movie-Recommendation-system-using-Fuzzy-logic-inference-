# Movie-Recommendation-system-using-Fuzzy-logic-inference-
A fuzzy logic system that recommends movies based on user mood, age, and movie attributes. Applied Mamdani inference and designed custom rules for decision making.

##Inputs 
1.	Rating (0–10)
•	Low: 0–5
•	Medium: 5–7
•	High: 7–10

2.	Duration (in minutes)
•	Short: < 90
•	Medium: 90–150
•	Long: > 150

3.	Release Date
•	Old: Before 2000
•	Recent: 2000–2015
•	Modern: 2016 onwards

4.	Mood/Tone
•	Sad: <=3
•	Neutral: 5
•	Happy: =>8

5.	Age
•	Young: ≤ 25
•	Middle-aged: 40
•	Senior: ≥ 60


###Output
The system gives a Recommendation Score that ranges from 0 to 10, grouped as follows:
•	Low: 0-3 → Not recommended
•	Medium: 4-7 → Moderately recommended
•	High: 8-10 → Highly recommended

### Rules
The present system included 9 rules that determined a recommendation score based on various combinations of inputs.
•	If the rating is high and the duration is short and the release date is modern or mood is happy and the viewer is young, then the recommendation score will be high.

•	If the Rating is average and the Duration is Medium and the Release Date is Recent or the Mood is Neutral and the Age is Middle-aged, then the Recommendation Score is Medium.

•	If the Rating is Low, the Duration is Long, the Release Date is Old, the Mood is Sad, and the Age is Senior, then the Recommendation Score is Low.

•	If the Rating is High, the Duration is Medium, the Release Date is Modern, the Mood is Neutral, and the Age is Middle-aged, then the Recommendation Score is High.

•	If the Rating is Medium, the Duration is Short, the Release Date is Recent, the Mood is Sad, and the Age is Senior, then the Recommendation Score is Medium.

•	If the Rating is High, the Duration is Short, the Release Date is Old, the Mood is Happy, and the Age is Senior, then the Recommendation Score is Medium.

•	If the Rating is Low, the Duration is Long, the Release Date is Recent, the Mood is Neutral, and the Age is Middle-aged, then the Recommendation Score is Low.

•	If the Rating is Medium, the Duration is Medium, the Release Date is Old, the Mood is Happy, and the Age is Young, then the Recommendation Score is Medium.

•	If the Rating is Low, the Duration is Long, the Release Date is Modern, the Mood is Sad, and the Age is Middle-aged, then the Recommendation Score is Low.

###Design of the solution 
![image](https://github.com/user-attachments/assets/f5417be3-6f4e-4a8d-a316-287266009130)

###Debugging

The problem in the original code happened because of a “division by zero error” when calculating the final recommendation score. The formula used np.trapz(R * score, score) / np.trapz(R, score), but if no fuzzy rules were triggered, the denominator (np.trapz(R, score)) becomes zero, causing the result to be NaN (Not a Number). To fix this, a condition was added; if the denominator is zero, the program will use the average score. This makes sure the program always gives a valid recommendation score instead of failing, making the fuzzy logic system more reliable.

###References 
1.Bilgii, T., & Burhan, I. (1996). MeasurementofMembership Functions: Theoretical and Empirical Work. In Foundations (Vol. 1). 
2. David, H., & Vilca, C. (2022). Netflix Movie Recommendation Using Fuzzy Logic. https://doi.org/10.5281/zenodo.5639761 
