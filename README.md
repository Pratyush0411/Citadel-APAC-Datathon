## Citadel APAC Datathon

I had the opportunity to participate in the APAC Datathon event organized by Citadel after getting selected through a 
qualification test from among a large pool of participants. 

For the final event, we were give a dataset comprising information on football matches and football teams. We had to frame our own 
problem statement and write a report explaining the methodology, insight and conclusions we deduced while analysing the dataset.
This repository contains all the code we used for the analytics and data collection during the course of this competition.


### Problem statement
Analysing and trying to identify upsets from the dataset on matches. Upsets are matches when an underdog team beats a well 
reknowned team.

### Methodology
* Web scraping for additional data on player popularity
* We first tried finding the upsets using the betting data given to us for the matches. 
* Then we performed exploratory data analytics and tried gaining insights and testing several hypothesis on the way
* We used neural networks, anomaly detection and regression modelling concepts to test out the hypotheses.

#### Hypothesis
1. The winning teams in upsets or underdogs usually have very defensive strategy and tend to park the bus. This means most
of the possession lies with the stronger teams and the weaker teams believe in counter attacking strategy. Hence, our next 
task was to explore any similarities in strategies/attributes amongst the winning teams in upset matches.

2. Bet365 has a bias for teams which have a good brand name and reputation and also heavily considers popular opinion to 
the extent that affects their analysis.

3. The average rating of all the players in a team strongly correlates with their ability to win a match.

4. The upsets would generally relate to the anomalies in the datasets in terms of the team’s skill level.

### Conclusions and Insights
The results for the models and our conclusion have been well summarized in the a report of 9 pages - team_14.pdf
Due to paucity of time, we were not able to improve our models and tests. We aim to improve the prediction accuracy and test
the hypotheses much more robustly in the future.

### Contributors
1. Siddharth Meenachi Sundaram (NTU Singapore)
2. Pratyush Kumar Psndey (NTU Singapore)
3. Archit Rungta (IIT Kharagpur)
4. Rajarshi Basu (NUS Singapore)


