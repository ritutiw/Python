There are N different models of mobiles manufactured at a mobile manufacturing unit. Each mobile must go through 2 major phases: ‘parts manufacturing’ and
‘assembling’. Obviously, ‘parts manufacturing’ must happen before “assembling’. The time for ‘parts manufacturing’ and ‘assembling’ 
(pmi and ai for ith mobile) for every mobile may be different. If we have only 1 unit for ‘parts manufacturing’ and 1 unit for ‘assembling’,
how should we produce n mobiles in a suitable order such that the total production time is minimized? Requirements:

Write a Greedy Algorithm to select the mobile ‘parts manufacturing’ and ‘assembling’ in such a way that total production time is minimized. 
Input sample For example, if there are 6 different mobiles in total and time for each mobile ‘parts manufacturing’ and ‘assembling’ are given as shown: 
Mobile i pmi (minutes) ai (minutes) 1 5 7 2 1 2 3 8 2 4 5 4 5 3 7 6 4 4 Input should be taken in through a file called “inputPS1.txt” which has the fixed format
mentioned below using the “/” as a field separator: / < pmi (minutes)> / <ai (minutes)> Ex: 1 / 5 / 7 2 / 1 / 2 3 / 8 / 2 … 
Note that the input data shown here is only for understanding and testing, the actual file used for evaluation will be different. 
Sample Output: Mobiles should be produced in the order: 2, 5, 6, 1, 4, 3. Total production time for all mobiles is: 28 Idle Time of Assembly unit: 2
