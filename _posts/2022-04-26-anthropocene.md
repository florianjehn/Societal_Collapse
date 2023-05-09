---
layout: post
title: The universal Anthropocene
subtitle: Things we can learn from exo-civilisations, even if we never meet any
tags: [Science, Fermi-Paradox]
comments: true
readtime: true
---

"*How do we know there is such a thing as a long-term version of our kind of civilization?*" Adam Frank

 

## Summary

Given some basic assumptions about how planets and civilizations' energy use interact, we can create a model that shows that it is likely that most or even all exo-civilizations run into their own version of an Anthropocene. This model also shows that this interaction often leads to collapse or even extinction of civilization. However, it leaves open the possibility of a long term stable interaction of the planet with its civilization.

 

## How common is an Anthropocene?

Humanity is currently living in its Anthropocene. This means we have started our own planetary epoch where our impact on Earth will be seen in the geological record into the far future. We got here by colonizing most of the planet's surface, the alteration of biomes and in general a human appropriation of terrestrial productivity. We now have a good grasp of processes that let our civilization interact with our planetary system (e.g. atmosphere, lithosphere etc.). This knowledge makes it seem that we are on a tipping point in our planetary history. We are currently shifting Earth away from the pleasant state of the Holocene (our relatively stable and warm climate) and into more unknown territory and it remains unclear how this will turn out (Steffen et al., 2018). Which leaves open the possibility that an Anthropocene and thus a shifting habitability of our planet could be a great filter for humanity.  

 

## The habitability of a planet is not static

Planets change and so does their suitability for life. This means their habitability over time isn’t something constant, it develops and shifts. We see examples of this in our own solar system. Venus is now a hellish place. However, it may have been more earth-like in the past, but its carbon dioxide removal cycle broke. Due to intense solar radiation Venus lost its water, which is needed for rock weathering. Without rock weathering carbon dioxide accumulates in the atmosphere, which leads to an ever increasing greenhouse effect. Another example is Mars. Mars likely had water and warmer temperatures in the past. But it wasn’t able to hold onto its atmosphere, which left it dry, cold and dead. 

Just like Venus and Mars, Earth has undergone drastic changes as well. For almost half the planet's history the air was composed  almost entirely of nitrogen and carbon dioxide. This only changed when life on Earth began acting on a global scale. If we look into Earth’s past we can see that it has been many different planets, ranging from a dark ice world, over a tropical hothouse to a glowing ball of molten rock. 

 

## Life shapes planets to make them suitable for life

The earliest changes of Earth were abiotic, the later ones were partly or mainly caused by life. One example of this is the Great Oxidation event. After a billion years of life on Earth, evolution came up with a new kind of photosynthesis. This new version used water to drive its chemistry, which created more energy, but also oxygen as a waste product. Oxygen is highly reactive and binds to other molecules, which includes the ones cell walls are made from. This degraded the functions of every cell that wasn't prepared for it, which killed most life on Earth. However, life that adapted to oxygen could use the new photosynthesis to power faster and more complex metabolisms. In addition, oxygen shielded Earth from the sun's ultraviolet radiation, which allowed life to spread to the continents, as those weren’t scorched by the Sun anymore.

The Great Oxidation event showed that life is capable of changing planets by altering its atmosphere and land. It also demonstrated life changing Earth, as we do in the Anthropocene, is neither novel nor unprecedented. However, it also showed that changing the planet can make it a hostile place for specific forms of life, like the bacteria that couldn’t handle oxygen. Those insights were used by James Lovelock and Lynn Margulis to develop Gaia Theory, nowadays called Earth System Science. Gaia Theory simply means that life shapes the planets it exists on to make them suitable for life. While this theory was hotly contested in the past, it is now widely accepted. One of the breakthroughs was the so-called Daisyworld Model, a simplified simulation of a planet with a slowly cooling star. The planet is inhabited by white and black daisies. As the star cools, the biosphere of this planet shifts more and more to black daisies, as their lower albedo allows them to absorb more of the heat of the star and thus keep it warm enough for life, even as the star continues to cool. Life creates the environment it needs to sustain itself. 

We have also found evidence for such processes on Earth. This makes it likely that if life can be found somewhere else in the universe, it also should be in constant interaction with its host planet. This does not mean that life cannot push a planet out of its zone of habitability. For example, at least one of the major ice ages of the past was caused by massive plant growth, which sucked so much carbon dioxide out of the air that it cooled the planet. And as humanity is currently demonstrating, life that has managed to become a civilization is quite able to change the habitability of its planet even more. Life can both sustain and destroy the habitability of its planet. This leads to the question: Does life tend to destroy itself or find an equilibrium with its host planet? 

 

## Elements of a model to simulate the interaction of a civilization with its host planet

We can look at this with a simple model, which is based on the idea of prey-predator interactions and is based on ordinary differential equations. The planet has a fixed replenishment rate of its resources. The overall stock of resources allows civilization to grow, but civilization also uses up those resources and decreases the planet's ability to regenerate by producing waste and disrupting natural cycles. When there aren't enough resources left, the civilization crumbles and the planet’s resources can replenish to give a fresh start for a new civilization. However, the planet can only replenish if it hasn't been pushed out of its equilibrium too far. 

We know that civilizations need energy, and that there is likely only a fixed amount of ways to harvest energy in a format that is usable for civilizations. In addition,the earlier ways of creating energy are likely to be more harmful for the planet (as they are based on burning resources, which releases carbon dioxide and warms the planet). This is what we see on our planet and it seems unlikely that exo-civilizations could directly go from fire to fusion. 

The main ways to get energy are using combustion, hydraulic/wind/tides, geothermal, solar, and nuclear. All those technologies have a different kind of impact on the planet. This impact can never be zero, as even using wind energy has an impact on the environment, because it uses up space and needs resources to be constructed. However, the most simple kind of energy, combustion, also has the largest impact.

The model is described in detail in Frank et al. (2018) and in plain language in Frank (2018). It is run until an equilibrium is found for the planet and its civilization (which can also mean the extinction of the civilization, when the equilibrium population is 0). The results of the model mainly depend on the following parameters:

* environmental sensitivity: environmental recovery rate normalized to the population growth rate, e.g. how badly the planet reacts to a growing civilization. The higher the sensitivity, the higher the environmental degradation per additional population.
* forcing: resource consumption detriment normalized to the environmental recovery rate, e.g. how strong a forcing the population is creating by consuming resources. The higher the forcing, the more likely is a collapse, as the planet's regenerative capabilities are overwhelmed by environmental degradation.
* foresight: fraction of environmental degradation at which point resource transition occurs, e.g. how quickly does the civilization shift from high impact to low impact energy. The earlier a shift occurs, the more likely it is to succeed.
* speed: degree of environmental degradation that occurs during a resource transition period, e.g. how quickly the transition occurs once it has started. The higher the speed of the transition of polluting to sustainable energy sources, the more likely it is successful.
* fragility: Degree of nonlinear environmental degradation normalized to the environmental recovery rate, e.g. how easily do you get self-reinforcing feedback loops. The higher the fragility, the earlier the transition of polluting to sustainable energy sources has to happen to even have a chance of succeeding.

 

## Modeling possible pathways for exo-civilizations

When we run the model the civilization and the planet begin to interact with each other. The civilization will use energy and produce waste. The waste will start pushing the planetary system out of its equilibrium. Over time they might start shifting to more sustainable methods of energy production, as they realize that they are pushing their planet out of its habitability window. Based on this shift, the population would either continue to thrive or be stressed by a decreasing habitability. We can run this kind of model for all different kinds of simulated planets and civilizations with different assumptions (like for example when they make the switch to cleaner energy or how quickly their population grows). This allows us to plot the typical paths in the interactions of civilizations and their host planet (Figure 1). 

![sims](https://lh6.googleusercontent.com/jspCB0LBe2SsPjvk4g4SIbNakxXcdQpbVyiAG12h97Yg7SERfrl2K4B3iYBmnx25ViqETqUiwHgUZSzYdNcACAtNCKxH3-Guj1XCSrMghkiCx_Hp-B1iKTOruiRnd8j34E8f0D0N)

Figure 1: Possible trajectories of civilization-planet interactions in exo-civilization (Frank, 2018) 

This simple model shows us three main trajectories:

* Die-off (A): a stable equilibrium exists. However, the civilization grows quickly to a population larger than the planet can sustain, this results in a massive die-off. Once the population has decreased to a level the planet can sustain, it becomes stable.
* Sustainability (B): a stable equilibrium exists and can be reached monotonically. The population grows, and the planet changes so that there is a smooth transition when it comes to energy use, which results in equilibrium between the planet and the civilization, without large disruptions.
* Collapse (C, D): the only equilibrium is the one with zero population. After a quick growth of population the civilization simply collapses. This can also happen in cases where the civilization switches to sustainable energies, but does so when it is already too late.

Foresight and fragility seem to be especially important parameters for a successful civilization. If you wait too long to switch your energy source or if you have an especially fragile planetary system, you have a problem and it becomes very likely that a collapse will occur. 

The results are promising. as they demonstrate the possibility of sustainable trajectories for humanity, but they also depend on a very simple model and unfortunately I could not find any likelihoods for the different scenarios, which makes it harder to evaluate the results (edit: I got into contact with Adam Frank and he said sustainability, die-off and collapse are all roughly equally likely in their model). 

Frank et al. (2018) argues for doing the same simulations again, but with a much more complex model and with a wider parameter space to make sure that all possible trajectories are accounted for. However, so far I haven’t found a project for this, so maybe the idea did not get the funding it needed. Still, there is a follow up paper (Savitch et al., 2021), which builds on and extends the model in Frank et al. (2018). The extended model uses an energy balance climate model, carbon dioxide interactions, orbital dynamics and initial atmospheric compositions and is calibrated by using data from the co-evolution of humanity and Earth. The results confirm the findings of Frank et al. (2018) and indicate that it is likely that most exo-civilizations run into problems with climate change. They identify initial carbon dioxide concentration in the atmosphere as one of the most important variables of how an Anthropocene will develop. The higher the initial carbon dioxide concentration, the lower the risk of an Anthropocene, as the civilization cannot emit enough carbon dioxide to meaningfully change the composition of the atmosphere. Unfortunately, Earth’s initial carbon dioxide concentration is relatively low and we thus live on a planet where climate is more easily shifted into dangerous ranges. However, the model of Savitch et al. (2021) also considers the resilience of civilizations to a rising temperature. Civilizations which can tolerate a rise of 5-10°K are relatively safe. Thus, we might be able to increase our chances of survival by trying to make humanity more resilient. The confirmation of Frank et al. (2018) by Savitch et al. (2021) can be seen as an additional data point that more research here would be worthwhile, as it would allow us to understand possible futures that might await us. 

Considering the broader research of existential risks, the results of those papers come with one caveat. Even though the models by Frank et al. (2018) and Savitch et al. (2021) show the possibility of a sustainable trajectory of humanity, they only look at environmental impacts. So, even if a civilization manages to survive its Anthropocene, they can still knock themselves out with a nuclear war or other existential risks. 

 

## Civilizations and their host planet can come into an equilibrium!

The results from those models leave me with dread and hope. Dread because it means that survival is not guaranteed in the slightest. There are a vast amount of trajectories which lead to extinction. Some, even after the switch to a sustainable path happened. One possible contributor to the Fermi Paradox might simply be that many civilizations push their planet out of its habitability equilibrium. We can expect that this happens to many civilizations, and we cannot rule out that we will be one of them. On the other side, I feel hope, as it also shows that humanity has a chance to make it through this time of peril. If we are smart, we might even manage a trajectory which leads directly to a stable equilibrium. I hope this is our path. 

 

## References

Frank, A., Carroll-Nellenback, J., Alberti, M., & Kleidon, A. (2018). The Anthropocene Generalized: Evolution of Exo-Civilizations and Their Planetary Feedback. Astrobiology, 18(5), 503–518. https://doi.org/10.1089/ast.2017.1671

Frank, Adam. (2018). Light of the stars: alien worlds and the fate of the Earth (First edition). New York: W.W. Norton & Company, Inc.

Savitch, E., Frank, A., Carroll-Nellenback, J., Haqq-Misra, J., Kleidon, A., & Alberti, M. (2021). Triggering a Climate Change Dominated “Anthropocene”: Is It Common among Exocivilizations? The Astronomical Journal, 162(5), 196. https://doi.org/10.3847/1538-3881/ac1a71

Steffen, W., Rockström, J., Richardson, K., Lenton, T. M., Folke, C., Liverman, D., et al. (2018). Trajectories of the Earth System in the Anthropocene. Proceedings of the National Academy of Sciences, 115(33), 8252–8259, doi: 10.1073/pnas.1810141115.

 

## Acknowledgement

Thanks to Ekaterina Ilin for giving lots of valuable feedback on how to improve this post. 
