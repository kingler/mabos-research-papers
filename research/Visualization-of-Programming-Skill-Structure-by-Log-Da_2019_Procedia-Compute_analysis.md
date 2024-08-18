# Visualization-of-Programming-Skill-Structure-by-Log-Da_2019_Procedia-Compute

# Title: Visualization of Programming Skill Structure by Log-Data Analysis with Decision Tree

## Summary:
The paper "Visualization of Programming Skill Structure by Log-Data Analysis with Decision Tree" by Shinichi Oeda and Mutsumi Chieda proposes methods for the automatic evaluation of programming skills using log-data and decision trees. The goal is to mitigate the inconsistencies and inefficiencies of manual evaluation processes by providing an automated and systematic approach to estimate and visualize the skill levels of programmers, particularly in educational settings.

## Key Components Analysis

### Main Research Question

The primary research question is: How can the programming skill of students be automatically evaluated and visualized using log-data and decision tree analysis?

### Methodology

The authors focus on generating decision tree models using periodic log-data from students' programming activities. The methodology includes:

1. Collecting log-data such as UNIX command histories and source code edits.
2. Extracting features from the log-data, including the number of lines, frequency of function declarations, and other significant patterns.
3. Creating decision trees to visualize and predict programming skills based on the extracted features.
4. Validating the decision tree models using statistical evaluation measures such as the R² score.

The decision tree and random forest methodologies were employed to create and validate the models. The analysis was conducted on a dataset of 39 students from a programming class.

### Key Findings and Results

1. The decision index (R²) was generally negative, indicating poor predictive performance.
2. The generated regression trees showed limited ability to accurately predict the programming skills based on the log-data.
3. Relevant features for prediction included the number of function arguments, mean length of variable names, and the number of lines per code segment.

### Conclusions and Implications

The authors conclude that while the decision trees provided a method for visualizing feature importance, their predictive accuracy was not practical for real-world application. They suggest refining feature extraction methods and experimenting with alternative regression approaches to improve prediction accuracy. The study indicates an existing gap in effectively automated programming skill evaluations and highlights areas for further research and development.

## First-Principle Analysis

### Fundamental Concepts

1. **Educational Data Mining (EDM)**: The paper leverages EDM, which involves extracting actionable insights from educational datasets to improve learning outcomes.
2. **Decision Trees and Random Forests**: The decision tree model is used for its interpretability, whereas random forests help mitigate overfitting by aggregating multiple decision trees.

### Methodology Evaluation

**Support for Research Question:**
- **Log-Data Analysis**: The use of log-data (history of UNIX commands and source code edits) provides a direct measure of students' activities and behaviors.
- **Feature Extraction**: Relevant features are systematically extracted, albeit with limited success in predictive accuracy.

**Validity of Methodology:**
- **Decision Trees**: Chosen for their interpretability, making the results understandable for educators unfamiliar with machine learning.
- **Random Forests**: Used to enhance prediction accuracy by mitigating overfitting, which is common with single deep decision trees.

### Statistical Significance and Meaningfulness

The statistical measure used is the R² score:
- Negative R² scores in experimental results indicate the models did not adequately predict programming skill levels, suggesting a need for more robust feature extraction and alternative modelling techniques.

### Logical Consistency of Conclusions

The conclusions logically follow from the results:
- The negative R² values and feature importance analysis justify the call for further refinement in data preprocessing and the exploration of more sophisticated regression models.

## Critical Assessment

### Strengths

1. **Novel Approach**: The application of decision trees to visualize and predict programming skills provides a novel way to leverage log-data in educational settings.
2. **Automated Skill Evaluation**: Proposes a solution to the labor-intensive and inconsistent nature of manual code review.

### Weaknesses

1. **Small Sample Size**: Only 39 students' data was used, limiting the generalizability and robustness of the findings.
2. **Data Quality**: The extracted features may not comprehensively capture skill-determining criteria, as evidenced by the poor predictive performance.
3. **Model Limitation**: Decision tree regression was not tuned optimally, suggesting the need for more methodological rigor in model selection and tuning.

### Areas for Improvement

1. **Increased Dataset Size**: Securing a larger dataset could help improve model accuracy and validation.
2. **Enhanced Feature Extraction**: More comprehensive and sophisticated feature extraction methods could better capture the nuances of programming skills.
3. **Alternative Models**: Exploring different regression models such as stochastic gradient descent or logistic regression could yield better predictive performance.

## Overall Quality and Impact

### Contribution to Field

The research contributes to the emerging field of Educational Data Mining (EDM) by introducing methods for the automated evaluation of programming skills. However, due to the low predictive accuracy, its immediate practical impact is limited.

### Real-World Applications

Potential applications in educational institutions for monitoring and supporting students by identifying those needing additional help early in the course. Also, employment evaluations in programming fields can benefit from such automated assessments.

### Ethical Considerations

Using automated evaluations must be done responsibly to avoid biases and ensure fair treatment of all students and applicants. Transparency in the algorithms and the criteria used is crucial to maintain trust and fairness.

## Future Research Directions

1. **Larger Datasets**: Integrating additional data from multiple institutions to enhance model robustness.
2. **Feature Engineering**: Improving feature extraction and selection processes to capture more meaningful and high-dimensional characteristics of programming skills.
3. **Algorithm Tuning**: Experimenting with and fine-tuning regression and classification algorithms to improve predictive performance.
4. **Real-World Deployment**: Pilot studies involving real-world deployment of refined models to evaluate practical applicability and usability.

## Conclusion

The paper "Visualization of Programming Skill Structure by Log-Data Analysis with Decision Tree" addresses a significant challenge in education and employment by proposing automated, data-driven methods to evaluate programming skills. Despite its limitations in predictive accuracy, the research sets a foundation for future studies to build upon, with the potential to greatly enhance the consistency and efficiency of skill evaluation in educational and professional contexts.

## Sources and Research Paper Citation
[1] Toon Calders, Mykola Pechenizkiy. "Introduction to The Special Section on Educational Data Mining," SIGKDD, Vol. 13, No. 2, pp. 3-5, 2011.
[2] Gerben Dekker, Mykola Pechenizkiy, Jan Vleeshouwers. "Predicting students drop out: a case study," Proceedings of the 2nd International Conference on Educational Data Mining (EDM2009), pp. 41-50, 2009.
[3] Wentao Li, Min Gao, Hua Li, Qingyu Xiong, Junhao Wen, Zhongfu Wu. "Dropout prediction in MOOCs using behavior features and multi-view semi-supervised learning," Neural Networks (IJCNN) 2016 International Joint Conference on, pp. 3130-3137, 2016.
[4] Diyi Yang, Tanmay Sinha, David Adamson, Carolyn Penstein Rose. "Turn on, tune in, drop out: anticipating student dropouts in massive open online courses," Proceedings of the 2013 NIPS Data-driven Education Workshop. Vol. 11, 2013.
[5] Sherif Halawa, Daniel Greene, John Mitchell. "Dropout prediction in MOOCs using learner activity features," Experiences and Best Practices In and Around MOOCs, Vol. 7, 2014.
[6] Laura Pappano. "The Year of the MOOC," The New York Times. Retrieved 18 April 2014.
[7] Ezekiel J. Emanuel. "Online education: MOOCs taken by educated few," Nature 503, 342, 2013.
[8] H. Igaki, S. Saito, A. Inoue, R. Nakamura, S. Kusumoto. "Programming Proces Visualization for Supporting Students in Programming Exercise," Journal of Information Processing Society of Japan, Vol. 54, No. 1, pp. 330-339, 2013.
[9] T. Kuchiki, K. Yamada, J. Sasaki. "A Study on Evaluation Methods of programming Skill Level," Proceedings of the 72nd National Convention of IPSJ. pp. 521-522, 2010.
[10] E. Dauber, A. Caliskan, R. Harang, R. Greenstadt, "Git Blame Who?: Stylistic Authorship Attribution of Small, Incomplete Source Code Fragments," Cornell University Library, arXiv:1701.05681, Jan 2017.
[11] A. Pradeep, J. Thomas, "Predicting College Students Dropout using EDM Techniques," International Journal of Computer Applications (0975-8887), Vol. 123, No. 5, pp. 26-34, August 2015.
[12] paiza, https://paiza.jp/
[13] moffers, https://moffers.jp/
[14] Quinlan, J. Ross, "Induction of decision trees," Machine learning, Springer, Vol. 1, No. 1, pp. 81-106, 1986.
[15] Breiman, Leo (2001), "Random Forests," Machine Learning, Springer, Vol. 45, No. 1, pp. 5-32, 2001.
[16] Akira Goto, Norihiro Yoshida, Kenji Fujiwara, Eunjong Choi, Katsuro Inoue, "Recommending Extract Method Opportunities Using Machine Learning," Information Processing Society of Japan, Vol. 56, No. 2, pp. 627-636, 2015.