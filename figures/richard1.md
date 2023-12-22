In the dynamic history of the cinematic industry, the examination of demographic groups representation and their evolution over time serves as a crucial lens through which we can unravel the complex narratives surrounding different historical world event. In this part we want to explore how well the historical landscape is reflected through the cinematographic representation of demographic groups. In particular, since the film industry first developed in the western world and our datasets are biased, we are going to look at the data through the lens of Western history, with WWI, WWII, the Cold War, the Vietnam War, the Gulf War, and the begining of the War in Afghanistan.

To do this, we first need to define how representation of a certain demographic group is measured. For that, we chose to count the number of occurence of **Adjectives** descrining these demographic groups as well as related **Proper Nouns** in the summaries with respect to the movies's release year.
> With the help of chat GPT, we created lists of **Adjectives** and **Proper Nouns** related to groups of interest, which we completed by hand (EG : ["french", "france", "paris", "lyon", "marseille", "alsace", "provence", "normandy", "verdun", "vichy"] for french representation).

> In combination with prior lemmatization and part of speech analysis to isolate the **Adjectives** and **Proper Nouns** and optimise the speed of search. 



Lets use relative word count so that we can decouple from the natural increase in number of film during the years.
> Word count of a group / total **Adjectives** and **Proper Nouns** count
We also choosed to apply a moving average of 5 years over the data.
> Overall, the data is quite scarce before the 80' especially for countries outside the western world, leading to very high short term volatility. Smoothing the curve with a moving average mitigates this issue.

#### World War I and World War II ####

