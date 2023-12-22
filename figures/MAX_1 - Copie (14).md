Before diving into deep analyses, let's just take a moment to familarize with the dataset through basic visualisations.

First, we will have a look to the frequence of movie releases through the years. We can obviously observe that from the 1980s, the cinematographic industry is clearly ramping up its production, thanks to new technologies reducing production costs and also the growing appetite of the public. We can also observe some little production depressions just after the two World Wars (1920s and 1940s).

What genres are hiding behind these films? Well, here is a line plot of the the evolution of the 10 most popular genres in the movie industry (in absolute number). We can clearly see the domination of the dramatic genre, becoming the leader since the 1940s, just after the beginning of the slow decline of black and white movies (the first color camera was invented by Kalmus in 1932!) and also after squashing the indie movies (Hollywod golden age and monopoyl). We can also observe that comedy films follow the same trend as for drama ones, but with a lower magnitude.

The previous line chart becomes easily convoluted, let's see what a barplot can teach to us. Again, we can make the same observations as before. However, it is now more easy to see that indie movies had a difficult time from the 1930s to the 1960s and also that World cinema had difficulties to survive in the cinematographic world in the begiining of the 20th century. This could be explained by the fact that Hollywood was monopolizing the market at this time, followed by other big studios. However, the technology evolved and the costs for shooting a movie dropped. Also the mentalities changed: Many countries encountered cultural movements that encouraged the production of indie films and founded film festivals which allowed the international reconnaissance of films produced by small studios. These facts, in addition to the globalization of cultural works, help us understand why indie movies and Wold cinema were able to see their movie share increase and consolidate since the 1950s.
We finally see that the 10 most popular genre see their share decrease slightlyl through the years (much steeper in the first half of the 20th century), which is a rejoicing indication that the movie world is diversifying.

Now it is time to talk money. Of course, if a film is popular (and thus probably appreciated), it will genrerate a lot of revenues. Here is a plot showing the proportion of movies in our dataset having a box office revenue that has been recorded Unfortunately, no more than 20% of films for a given year has data about revenues. We can also observe a strange peak in the 1950s.

If we have a look to the boxoffice share of the 10 most popular genres, we see that the market was quit unstable in the first half of the 20th century, before becoming more regulated. The stabilization of box office shares among popular genres over the last decades could be attributed to factors such as market saturation, where the abundance of genre choices has reached a balance, along with the evolution of audience preferences maintaining a stable demand for existing genres. Studio strategies also play a pivotal role. They may employ varied marketing tactics, invest in diverse genres, and leverage audience insights to maintain a healthy balance in the market.

But, is money a good indicator of people taste? If yes, we should see a correlation between the boxoffice revenue and the ratings. To do so, we increased the dataset with ratings coming from IMDb. Here is the scatter plot. Interestingly, we cannot see a clear correlation between the revenue and the ratings, as shows the distribution and the R-squared.

However, a more interesting fact with the boxoffice revenues is that it seems to increase through the years. As we move along time, we encounter more frequently movies generating huge revenues. Despite the stable genre shares, box office revenues may have risen due to technological advancements, global market expansion, and the emergence of blockbuster strategies. 

We can also ask ourselves if the movie genres can explain some of the box office revenues. Here is the result of a linear regression, where we can have a look to evolution of each of the 10 most popular genre coefficient through time. We cannot observe any interesting trend, except that, for example, the adventure genre may explain some high revenues. But is it really the case? If we look at the R-squared of this model, we do not get a satisfying score. It seems like there is actually no correlation between genre and box office revenue.

On the other hand, can genres explain the ratings? If we do a similar example as done previously, we also observe the absence of correlation.

Finally, good films may have found interesting combinmation of genres. These strongly associated genres may evolve together. To observe this phenomenon, we can proceed to the computation of a correlation plot.

Top 10 Correlations:
| Genre Pair                              | Correlation |
|-----------------------------------------|-------------|
| (Psychological thriller, World cinema)  | 0.654921    |
| (Action/Adventure, Mystery)             | 0.581038    |
| (Musical, Mystery)                      | 0.501041    |
| (Animation, Family Film)                | 0.478943    |
| (Film adaptation, Period piece)         | 0.472220    |
| (Crime Fiction, Romantic drama)         | 0.459494    |
| (Romance Film, Thriller)                | 0.435708    |
| (Film noir, Mystery)                    | 0.423475    |
| (Crime Thriller, Thriller)              | 0.421154    |
| (Film noir, Thriller)                   | 0.420303    |

Bottom 10 Correlations:
| Genre Pair                    | Correlation |
|-------------------------------|-------------|
| (Comedy, Thriller)            | -0.298885   |
| (Bollywood, Slapstick)        | -0.306872   |
| (Biography, Romantic comedy)  | -0.308991   |
| (Black-and-white, Melodrama)  | -0.313572   |
| (Action/Adventure, Comedy)    | -0.315178   |
| (Adventure, Romance Film)     | -0.326626   |
| (Film noir, War film)         | -0.330005   |
| (Comedy, Drama)               | -0.331146   |
| (Bollywood, Thriller)         | -0.351499   |
| (Action/Adventure, Musical)   | -0.389644   |


We can see interesting pairs such as Action/adventure and mystery linked by a correlation of 0.581038. This connection could be explained by their shared suspenseful, intriguing, and exploratory elements. Audiences may find these themes appealing, resulting in a notable positive correlation between the two genres. On the opposite, the negative correlation between comedy and drama (-0.331146) could result from the distinct tonal differences and primary objectives of these genres. Comedies prioritize humor and levity, while dramas focus on serious themes, depth of emotion. They are clearly not compatible.

With all of this in mind, it is now the time to dig deeper. We will see in the next chapters how the correlation between cinema and real-world events is profound, with filmmakers often drawing inspiration from, or directly responding to, the cultural and political milieu of their time. Sociopolitical events intricately weave into the fabric of filmmaking, shaping narratives, themes, and the overall cinematic landscape.
