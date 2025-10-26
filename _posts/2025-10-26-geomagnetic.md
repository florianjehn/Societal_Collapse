---
layout: post
title: Space weather and critical infrastructure
subtitle: Nice aurora you have there, too bad electricity is gone
tags: [Influence Factors, Infrastructure]
comments: true
readtime: true
---
Space weather often comes up as a topic when discussing what environmental hazards might lead to societal collapse or at least a massive societal disruption. The main idea here is that geomagnetic storms coming from the Sun create failures in the electrical grid so large that they cannot be repaired in a reasonable timeframe, resulting in a permanent blackout. And as we have learned from [other posts](https://existentialcrunch.substack.com/p/the-consequences-of-blackouts) in this series, having a blackout that lasts longer than a few days would be really, really bad. 

The odd thing is that the damage assessments that I have come across differ wildly, ranging from “a large geomagnetic storm would totally overwhelm global society” to “this is a non-problem, which could just lead to minor disruptions and a short, local blackout at worst”. So, let’s explore this a bit deeper which of those two views is closer to reality. 

# What is a geomagnetic storm?

Before we dive into the details of damages and mitigation, first let’s define a few key terms around space weather. I am relying for this section and the next one on nice reviews by Baker et al. (2014), Johnson et al. (2016) and Eastwood et al. (2017): 

* Space weather: All the radiation and particles the Sun throws at us and how they interact with Earth's magnetic field.
* Solar flares: Sudden bursts of electromagnetic radiation from the Sun's surface, ranging from radio waves to X-rays and gamma rays, caused by the release of magnetic energy.
* Solar wind: The continuous stream of charged particles (mainly electrons and protons) that flows outward from the Sun in all directions.
* Coronal mass ejections (CME): This is when the Sun shoots especially large amounts of charged particles into space.
* Geomagnetic storm: The large magnetic disturbances in Earth's magnetic field which happen when strong solar wind (often enhanced by CMEs) hits Earth.

# How the damage happens

When a geomagnetic storm happens, the geomagnetic field around Earth twists and bends under the onslaught of the Sun’s emissions. This movement creates geomagnetically induced strong currents in everything on Earth which is large, and able to conduct electricity. The things thus most affected are the electrical grid and pipelines. Both represent long metal lines, able to capture the currents. For pipelines this is not that big of a problem, as it just increases corrosion. This is bad for long term maintenance, but not something catastrophic. Train lines sometimes have short-term disruption or there can be fires at relay stations. Things are different for the electrical grid. Long distance transmission lines need low electric resistance to be able to work well. But this low resistance also means that the currents from the geomagnetic storm are more easily absorbed by them. Essentially, these long distance transmission lines work as gigantic antennas which capture the currents induced by the storm. If current in the grid fluctuates wildly due to the geomagnetic storm this can cause damage and trigger safety shut downs. 

Some experts argue that the existing protections put into place against low frequency currents like from the geomagnetic storms are insufficient to prevent large-scale damage to the electrical grid. This manifests especially in the electrical transformers. The additional current can damage them, let them age more quickly due to heating and lead to potentially complete loss of function. Generally, this damage builds up over hours of exposure and is less an instant failure of the system. Still, this damage is a big problem, because these transformers are fairly big and if you order one today, it can be months to years until it gets delivered. Delivery times would obviously be longer if this happens at a lot of places at once. Therefore, theoretically, you could end up in a situation where blackouts last for weeks or even longer. This would be highly destructive, and we explore how destructive further down in this post (1). 

* Collapse of the electrical grid is clearly the worst outcome we can get from a geomagnetic storm. However, it is not the only one we should be concerned about:
* Communication disruptions: Geomagnetic storms inject energy into the ionosphere, this can disrupt high frequency radio. 
* Disruption of global synchronization and navigation: Global navigation satellite systems (things like GPS) could be disrupted for several days. This would be annoying for navigation in general, but more importantly, we also use it for global synchronization for all kinds of things, like our financial system. This would not be possible during the storm.  
* Aviation problems: Airplanes might be exposed to higher radiation doses than normal. This would not have any immediate effects, but would condemn a random collection of people on the airplanes to cancer later in their life. Also communications with airplanes might be lost and their navigation systems could be affected. 
* Cascading damage: The storms can cause voltage fluctuations on the power lines which can damage other components and lead to automatic cascading grid shutdown routines

# Historical examples

From history we can point to several examples of massive geomagnetic storms hitting Earth (also described in Eastwood et al. (2017)): 

* 1859: The Carrington Event is the largest geomagnetic storm which hit Earth since we can accurately record them. It disrupted telegraph lines in many places, but ultimately did not cause much damage, due to the lack of very vulnerable parts of society at that time. 
* 1921: This storm was likely on a similar magnitude as the Carrington Event, but we can’t be sure due to uncertainty in assessing long past events. It caused fires in several telegraph stations in Sweden. 
* 1967: This storm was large enough to strongly disrupt communication in the United States. In particular, the military got quite concerned about it and thus started to look into space weather effects more seriously. 
* 1989: Roughly 1.5-3 times smaller than Carrington, this storm led to a large blackout in Canada and damaged two larger transformers in the United Kingdom.
* 2003: Large, but not massive storm led to a short blackout in Sweden. 
* 2012: A Carrington class storm was ejected from the Sun, but missed Earth. 
* 2024: This was the most recent large geomagnetic storm which hit Earth. While it led to auroras to be visible all throughout Europe, its geomagnetic impacts were somewhat smaller than the 1989 storm, meaning not much damage occurred (a comparison of this storm with earlier ones is done in Lawrence et al. (2025)).

# Where on Earth does this happen?

The effects of the geomagnetic storms would not be felt globally all at once. However, the storms can last up to a week and the Earth rotates every 24 hours, meaning that every place on Earth could potentially be reached. But in the exposed areas the distribution is not random. Due to the shape of the magnetic field there are preferential areas that could be hit. Thankfully, Maffei et al. (2023) used some physics based models to predict where these areas are today and also where they will be in five decades from now. They slowly change, as the Earth’s position in space is not completely stable, but wobbles around. Figure 1 shows the areas with the highest probability of extreme space weather hitting that area. This shows that Northern Europe, Southern Canada and the Northern United States have the highest chance of being hit. However, this does not mean that everywhere else is safe. It just means that the likelihood is lower. During the Carrington Event auroras could be seen as low as the equator. 

![Main danger zones for extreme space weather](https://raw.githubusercontent.com/florianjehn/Societal_Collapse/main/assets/img/aurora.png)

Figure 1: Bands of highest probability of large geomagnetic field fluctuations due to geomagnetic storms. 

A second global effect is disruption to satellites orbiting the Earth. As the coronal mass ejections push more particles towards Earth, the density of the atmosphere increases. This in turn means that satellites experience more drag, lose speed and thus altitude. Many satellites have thrusters on board to counter this, but in a very severe storm those might not be enough, leading to a loss of an unknown, but potentially high number of satellites. 

# How large could these storms get?

The impacts of the storms depend a lot on how large they are. We clearly know that Carrington Event sized storms can happen and we should expect them roughly every 150. However, this is not the absolute maximum. The size of the storms follows a very fat tailed distribution, meaning much larger, but rarer events are possible. Unfortunately, we don’t really have a long time series from the Sun’s activity. What we do have is a sky full of stars, many of which are similar to the Sun. Vasilyev et al. (2024) used a large sample of Sun-like stars to check how often they produce large solar flares. They found that in their sample the stars produced flares 1-1.5 magnitudes larger than Carrington roughly every 100 years. This means the Sun might have some nasty surprises for us in store, but we do not know for sure if the Sun could even produce storms of this magnitude. 

There is also some research that looks into paleo records of how large the Sun’s flares can become. A recent example of this is Bard et al. (2023). When solar flares hit Earth’s atmosphere they create radioactive carbon-14. Trees absorb this and fix it in their growth rings. This means when you have very old remains of trees you can use the carbon-14 concentration as a proxy for the size of solar flares that hit Earth while the tree was still growing. Bard and his co-authors were able to find 14,300 year old tree remains. In those trees they found carbon-14 concentrations which indicate that a solar flare around a magnitude larger than the Carrington Event must have hit Earth. 

These two lines of argument imply that the Sun is probably capable of creating geomagnetic storms of a magnitude larger than the Carrington Event. However, the maximum size of a geomagnetic storm is limited by the strength of the geomagnetic field as well. Vasyliūnas (2011) created a theoretical physical model and uses it to argue that the largest possible storm change in magnetic field is roughly 1.5 times the size of the Carrington event in terms of depression of the magnetic field at the tropics, although this is not exactly the same as the peak rate of change of magnetic field which is responsible for high voltage transformer overheating and other electricity grid issues. So, storms above 1.5 Carrington size could still produce more damages, for example by more quickly ramping up to the maximum value or changing more rapidly, even though their maximum value of magnetic field strength depression is topped out.  

The dangers might also be getting more imminent. Jasinski & Velli (2025) looked at activity data from the Sun of the last few decades and found that the Sun is currently on a trend of increased activity in general, meaning that for the next few decades the occurrence of a larger geomagnetic storm might be higher. The magnetic field of the earth is also on a weakening trend, decreasing the natural geomagnetic shield from CME charged particle radiation.

# Estimates of damage

As we thankfully have not yet faced a Carrington-sized event with our modern, highly digital civilization, we have to rely on modeling to understand potential damages. Estimates vary widely. The most pessimistic, commonly-cited paper is by Schulte in den Bäumen et al. (2014). They modeled geomagnetic storms similar to the 1989 Quebec event, determining which geographic areas would likely be affected (Figure 1). They assumed affected regions would lose 10% of their electricity production capacity for a year, which is the estimated time needed to replace damaged transformers and restore grid infrastructure. Using a global supply chain model covering 187 countries and ~16,000 economic sectors, they traced how this electricity shortage would cascade: production losses in electricity-dependent sectors, disrupted supply chains, and reduced international trade as countries cannot import goods that haven't been produced. This yielded estimated global losses of 2.4-3.4 trillion dollars (3.9-5.6% of global GDP), with roughly half the damage occurring in countries outside the directly affected zones. The difference in their estimate to what actually happened in 1989 is that they assume regions more important to the global economy are hit. But their research seems like a worst case under pessimistic assumptions to me. They also model Carrington sized events, but never state how much those would cost. If you naively scale this on the magnitude of the storm, you end up with something like 5-10 trillion dollars in damages. 

On the other side of the scientific spectrum we have Oughton et al. (2019). They first simulated the electrical grid of the United Kingdom and how geomagnetic storms of different sizes would create damages in the grid. Based on this they then check how much the economy gets disrupted and how this cascades into supply chains. Their estimate is that a Carrington sized event would leave up to 60 million people in the United Kingdom without power, but assume that the grid would be restored in days to weeks. The damage of 20 billion dollars they come up with is then based on lost economic transactions during the period. Though this does not consider global effects in general and also does not model that other countries might face the same problem. Finally, it also does not consider the damages that would occur during a week-long blackout, which would likely be much more severe than just lost economic transactions. If we naively scale this up to global numbers based on the United Kingdom’s contribution to global GDP, we end up with roughly 660 billion $ damages globally. 

The difference between those numbers is the roughly difference between the amount of money the United States spends on military and a third of the total United States GDP. This is a massive difference. And even the larger number does not really grapple with what happens if a region experiences a longer blackout. Also, disruption of satellites, especially megaconstellations and global navigation satellite systems are not considered here at all.

Finally, there are also the grid operators themselves who maintain and supervise the grid. They are acutely aware that these things can happen and over the last decades the countries most likely affected by geomagnetic storms have hardened their grid to withstand them. However, it is quite difficult to get a picture of how far these things have actually come. The most recent big government report I could find was the U.S. Department of Energy (2019). They gave an overview of the state of preparations in the United States. It states:

* The industry is required to have plans for what they do when geomagnetic storms hit.
* They have to do a damage assessment every 60 months.
* The industry is in discussion with the government about implementing physical grid hardening. 
* Major gaps remain in understanding how large geomagnetic storms would interact with the grid. 

Overall, it sounds like the risk is taken seriously, preparations are being worked on, but are far from finished. This report is only for the United States, but I would assume that countries that are even more exposed like Canada or Sweden are prepared better, while countries like China, which aren’t affected during smaller geomagnetic storms are likely much worse and would have big troubles in severe storms. Due to this and many other uncertainties, the range of damages possible seems quite large to me. 

# How can we prepare?

Thankfully, there are at least some things that can be done to prevent or at least decrease damage when a geomagnetic storm hits. Especially important here is accurate forecasting of geomagnetic storms and their impacts. Oughton et al. (2019) also look at scenarios with better forecasting than we have today and this reduces their damage estimate by two thirds, as the most vulnerable parts of the electrical grid can just be disconnected. This means they are not damaged and can be added to the network again immediately after the storm ends. Generally, it seems to me that forecasting is the one area where the most progress was made in the last decade or so, with satellites being added for monitoring and the forecasts now usually good enough to predict geomagnetic storms by around ten hours. This means due to better forecasting a large amount of damages could likely be prevented, even in larger storms. 

Besides forecasting, there are also several other options on how you could change the physical infrastructure to be more resilient (as explained in Johnson et al. (2016) and implemented in Canada, the US, and Sweden):

* Capacitor blocking: This means installing low-ohmic resistors in the grid. These slow down the flow of the incoming currents, providing protection by reducing the maximal loads this way. 
* Transformer redundancy: Just have some spare transformers that you can use to replace damaged ones quickly. 
* Grid topology changes: Include grounding points every 50 to 75 km, to limit how much harmful current can accumulate in transmission lines. Also, having alternative routes in your grid, so disrupted lines don’t bring the whole thing down. 

# Conclusion

The existing damage estimates appear somewhat inaccurate and omit important pathways, such as damages from extended blackouts. Moreover, the Sun can likely produce geomagnetic storms considerably larger than the Carrington Event, yet nearly all papers treat Carrington as the worst-case scenario. Yet, there appears to be an upper limit to storm severity based on how Earth's magnetic field functions.

On the mitigation side, forecasting has improved substantially, and the past decade has seen many grid hardening measures implemented. Yet government reports indicate much work remains and large uncertainties persist. Given the current state of knowledge, the potential severity of geomagnetic storms remains unclear.

That said, there are reasons for cautious optimism. This is an active research field with relatively strong government interest compared to other global risks, suggesting the dangers may decrease over time. Additionally, geomagnetic storms appear to be more regional than global in nature when it comes to the worst impacts. While effects could potentially be felt across most of the globe, transformer damage would likely affect only certain regions. This would certainly be expensive to repair and could cost many lives if managed poorly, but there doesn't seem to be a realistic pathway to a global blackout.

# Endnotes

(1) One caveat: many high voltage transformers have backups at the station already, which would take days or weeks, rather than months, to be put into position and powered on.

# References

* Baker, D. N., Jackson, J. M., & Thompson, L. K. (2014). Predicting and mitigating socio-economic impacts of extreme space weather: Benefits of improved forecasts. In A. Ismail-Zadeh, A. Kijko, I. Zaliapin, J. Urrutia Fucugauchi, & K. Takeuchi (Eds.), Extreme Natural Hazards, Disaster Risks and Societal Implications (pp. 113–125). Cambridge University Press. https://doi.org/10.1017/CBO9781139523905.012 
* Bard, E., Miramont, C., Capano, M., Guibal, F., Marschal, C., Rostek, F., Tuna, T., Fagault, Y., & Heaton, T. J. (2023). A radiocarbon spike at 14 300 cal yr BP in subfossil trees provides the impulse response function of the global carbon cycle during the Late Glacial. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 381(2261), 20220206. https://doi.org/10.1098/rsta.2022.0206 
* Eastwood, J. P., Biffis, E., Hapgood, M. A., Green, L., Bisi, M. M., Bentley, R. D., Wicks, R., McKinnell, L.-A., Gibbs, M., & Burnett, C. (2017). The Economic Impact of Space Weather: Where Do We Stand? Risk Analysis, 37(2), 206–218. https://doi.org/10.1111/risa.12765 
* Jasinski, J. M., & Velli, M. (2025). The Sun Reversed Its Decades-long Weakening Trend in 2008. The Astrophysical Journal Letters, 990(2), L55. https://doi.org/10.3847/2041-8213/adf3a6 
* Johnson, M., Gorospe, G., Landry, J., & Schuster, A. (2016). Review of mitigation technologies for terrestrial power grids against space weather effects. International Journal of Electrical Power & Energy Systems, 82, 382–391. https://doi.org/10.1016/j.ijepes.2016.02.049 
* Lawrence, E., Beggan, C. D., Richardson, G. S., Reay, S., Thompson, V., Clarke, E., Orr, L., Hübert, J., & Smedley, A. R. D. (2025). The geomagnetic and geoelectric response to the May 2024 geomagnetic storm in the United Kingdom. Frontiers in Astronomy and Space Sciences, 12. https://doi.org/10.3389/fspas.2025.1550923 
* Maffei, S., Eggington, J. W. B., Livermore, P. W., Mound, J. E., Sanchez, S., Eastwood, J. P., & Freeman, M. P. (2023). Climatological predictions of the auroral zone locations driven by moderate and severe space weather events. Scientific Reports, 13(1), 779. https://doi.org/10.1038/s41598-022-25704-2 
* Oughton, E. J., Hapgood, M., Richardson, G. S., Beggan, C. D., Thomson, A. W. P., Gibbs, M., Burnett, C., Gaunt, C. T., Trichas, M., Dada, R., & Horne, R. B. (2019). A Risk Assessment Framework for the Socioeconomic Impacts of Electricity Transmission Infrastructure Failure Due to Space Weather: An Application to the United Kingdom. Risk Analysis, 39(5), 1022–1043. https://doi.org/10.1111/risa.13229 
* Schulte in den Bäumen, H., Moran, D., Lenzen, M., Cairns, I., & Steenge, A. (2014). How severe space weather can disrupt global supply chains. Natural Hazards and Earth System Sciences, 14(10), 2749–2759. https://doi.org/10.5194/nhess-14-2749-2014 
* U.S. Departement of Energy. (2019). Geomagnetic Disturbance Monitoring Approach and Implementation Strategies. U.S. Departement of Energy. https://www.energy.gov/sites/prod/files/2019/06/f64/DOE_GMD_Monitoring_January2019_508v2.pdf 
* Vasilyev, V., Reinhold, T., Shapiro, A. I., Usoskin, I., Krivova, N. A., Maehara, H., Notsu, Y., Brun, A. S., Solanki, S. K., & Gizon, L. (2024). Sun-like stars produce superflares roughly once per century. Science, 386(6727), 1301–1305. https://doi.org/10.1126/science.adl5441 
* Vasyliūnas, V. M. (2011). The largest imaginable magnetic storm. Journal of Atmospheric and Solar-Terrestrial Physics, 73(11), 1444–1446. https://doi.org/10.1016/j.jastp.2010.05.012 

