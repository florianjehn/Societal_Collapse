---
layout: post
title: Trade collapse
subtitle: Cascading risks in our global supply chains
tags: [Influence Factors, Coordination Problems]
comments: true
readtime: true
---

Most things you use and particularly the food we consume rely on an intact global supply chain. Without trade, essential resources such as fertilizers would become inaccessible, making food production much harder. This post aims to provide an overview of the current trade system, highlighting its potential vulnerabilities and exploring the factors that have contributed to this state. The focus is on food trade given its importance and vulnerability. 

# What is the status quo of the food trade?

A good overview of the state of the trade system is given in D’Odorico et al. (2014), which tracks global flows of food via trade data from the Food and Agriculture Organization of the United Nations (FAO). They find that around a quarter of the food we produce is traded and that this share has increased in recent decades. Also the amount of food we trade increases quicker than the food we produce. This increase in food trade also comes with an increasing complexity of the system. Not only are we trading more in total, but we also have more and more trade connections between formerly unconnected countries. However, in parallel, the export of food has become increasingly concentrated, with the majority of food export now coming from a few major exporters like the United States, Australia, and Russia. So, even though we are increasing the overall complexity of the network, the dependence on those major exporters continues to increase as well. 

A decade later, Ji et al. (2024) did a similar analysis with more recent data and came to the same conclusion. This is concerning, as these trends contribute to the vulnerability of our food trade system. 

# What makes food trade so vulnerable?

## Export bans

Puma et al. (2015) is a key study when it comes to understanding the fragility of our food trade system; it was one of the first studies to look in detail at the potential effect of export bans on the stability of the trade network. Like the other studies mentioned here, they constructed a network model from trade data. To study the effect of export bans, they selectively removed nodes from the network to study how much this would affect the food system. Their results show that our food system can only remain stable as long as the main trading hubs continue to export. If a country like the United States stops exporting food, this would drastically reduce the food availability in many countries and also disrupt trade flows more generally, as many countries do not have a direct trade connection, and instead use hubs like the United States to export and import their food. 

Besides this direct effect, Puma and co-authors also discuss the potential for export ban cascades. Historically we know that countries tend to introduce export bans for three main reasons: 1) A shortfall in their own food production, 2) a shortfall of production in one of their main import countries or 3) neighboring countries introducing export bans. In the case of global catastrophes like large volcanic eruptions, likely all of these three would become true, which could result in a cascade of export bans, as every country tries to ensure enough food for its own citizens. This could result in the tragic situation that enough food is available globally, but with almost all countries having introduced export bans, the food would not reach a majority of the global population. 

## Chokepoints

While we have many trade routes globally, our reliance on water transport for most food trade means these trade routes are forced by geography through so-called chokepoints. These are areas in which a majority of trade flows have to go through a very narrow passage. The influence of those choke points on food trade has been explored by Wellesley et al. (2017) by tracking the flow of goods globally. They identified a total of 13 chokepoints (Figure 1). 

![Chokepoints](https://raw.githubusercontent.com/florianjehn/Societal_Collapse/main/assets/img/chokepoints.png)

Figure 1: Chokepoints in food trade, as identified by Wellesley et al. (2017). 

Especially important for food trade are the Panama Canal and the Straits of Malacca. For example, around a quarter of global maize trade goes through the Panama Canal and around a quarter of global rice trade is funneled through the Straits of Malacca. This means if such a chokepoint would be blocked, this would disrupt the flow of food considerably. 

The blockage of a chokepoint can happen for a variety of reasons. A famous example is when the Ever Given container ship blocked the Suez Canal in 2021. 

Wellesley and co-authors think there are two main reasons for blockage of the chokepoints in the future:

* Climate: Some of the chokepoints like the Panama Canal are dependent on the local climate to function. The Panama Canal uses locks to bring ships across the height differences across it. These locks are dependent on the local water level being high enough to support the container ships going through. This means if a drought happens, the Canal is not usable anymore. Similar things can happen at other chokepoints as well and are expected to increase in the future due to global warming. 
* Geopolitics: Many of the chokepoints could be blocked if regional geopolitical tensions are high. For example, the Turkish Straits were closed during the coup in Turkey in 2016 and the Strait of Bab-el-Mandeb is currently being harassed by Houthi rebels, making it more dangerous to use.

## Concentration on all levels

As mentioned in the beginning of this post, we are dependent on very few countries when it comes to food trade. However, this is not the only place where important goods and activities are concentrated into a few key players. A recent literature review by Clapp (2023) looked into which parts of the food system are concentrated and how we ended up in this place historically. Here, concentration means a small number of actors or items dominate certain areas and activities. Clapp identifies three main areas where such concentration makes us vulnerable:
* The worldwide industrial food system depends heavily on a few key grains grown through advanced farming techniques, which leaves it vulnerable to disruptions affecting these specific crops and to the loss of farming inputs like fertilizer (1).
* Only a few nations specialize in producing essential grains for export, upon which numerous other countries rely, including many of the world's poorest and most food-insecure nations.
* The global grain trade is controlled by a handful of firms within highly financialized commodity markets, which are quite volatile.

Clapp attributes these transformations to capitalism and colonialism. Our focus on a limited number of staple grains is driven by the efficiency gained from specializing in single crops. Historically, colonial powers like the United States lacked the workforce to cultivate the vast territories acquired through colonialism, which incentivised early mechanization and solidified their role as major food exporters. Post-colonial countries often inherited underdeveloped economies, leading to a reliance on cheaper imported foods over locally grown produce. This reliance has become deeply entrenched due to economic incentives favoring imports.

Regarding the concentration of trade among a few firms, Clapp argues that the current market trends encourage monopolies. Food trade requires substantial investments with slim profit margins, making it very difficult for new competitors to enter.

Another paper which links these problems in the food trade system to how global markets are structured is by Yıldırım & Önen (2024). They looked at which countries were most impacted by food system disruptions due to the Russian invasion of Ukraine and COVID-19. They argue that this mostly impacted countries that have low income and which also do not have any domestic food production. They propose that these countries could impose import restrictions to strengthen their local food supply and make themselves less dependent on imports. 

To dig even deeper into the concentration, we can look at how trade happens on a sub-country level. This was recently explored in quite some detail by Jain (2024). The main idea behind the paper was that we would probably be able to understand trade better, if we could look at it in more detail, meaning admin levels below the country level. Problem is that this data mostly does not exist. This means we have to create it. 

To do this, Jain trained machine learning models on national scale-trade relations of food trade and predictive variables like crop area, livestock count, population and transportation networks. The resulting model allowed Jain to predict the out and ingoing flow of trade for lower admin levels for all countries. These numbers were then adjusted until the sums lined up with the actually traded amounts on a country level. Due to the high uncertainties involved, the resulting numbers are likely still somewhat off, but they reveal quite interesting patterns of trade (Figure 2). It turns out production is not only concentrated on a few countries, but even in those countries most of the production comes from a small number of regions. This means even a relatively local shock can quickly have global consequences. 

![Sub national cereal flow](https://raw.githubusercontent.com/florianjehn/Societal_Collapse/main/assets/img/cereal_flow.png)

Figure 2: Sub-national global cereal trade flows. 

# How much of our trade could we potentially lose?

We therefore know that the food trade is quite vulnerable on many axes. But how would food security be influenced by changes in trade after a major catastrophe? This question is explored in Jehn et al. (2024) (Disclaimer: I am the main author in that paper). To do so, Jehn et al. used a simple network model of trade to simulate how changes in food production change food trade patterns. The assumption being, if you produce less food, you reduce your exports by the same amount. This approach allows to isolate the effect of the direct yield reduction, without having to make any further assumption on human behavior. 

Jehn et al. used this model to look at the two main types of global catastrophic events that influence food production: 1) abrupt sunlight reduction scenarios (like nuclear winter), 2) global catastrophic infrastructure loss (GCIL, like a large geomagnetic storm disabling the global power grid) and 3) a combination of both (imagine a nuclear winter after a nuclear war which included HEMP attacks). They find that many countries would lose around 25-50 % of their food imports after a GCIL and 50-100 % in an ASRS. A combination of both would be even more disruptive (Figure 3). 

![Catastrophic Trade Loss](https://raw.githubusercontent.com/florianjehn/Societal_Collapse/main/assets/img/trade_loss.png)

Figure 3: Impact of global catastrophic infrastructure loss (GCIL), abrupt sunlight reduction scenario (ASRS) and a combination of both on food imports for all four major crops and all countries. 

Besides these direct effects the paper also simulated how this would impact trade communities. A trade community is a group of countries which trade a lot with each other. They can change if for example one major exporter reduces its exports due to yield losses. Interestingly, the impacts here differ a lot by the catastrophe that caused them. In GCIL scenarios the trade communities stay mostly the same, because the food production is impacted relatively homogeneously. Meaning if most countries have a similar reduction in food production, your trading partners stay mostly the same. For ASRS scenarios though the picture is quite different. The climatic disruption caused by them is regionally quite different, completely destroying food production in some countries, while leaving others not impacted at all or even improving conditions in some (e.g. very hot countries). This completely changes the map of trading partners, as many countries would have to turn to new partners to have any chance of importing food. 

All these things indicate that food trade would be massively disrupted after global catastrophes, with ASRS potentially being most disruptive. 

# The connection between trade collapse and societal collapse

These papers show that we are currently in a difficult situation for food trade. If a major shock happens, it is possible that the food system could collapse in a cascading manner. In addition to those insights from today, we can also look at history to see how collapsing trade systems endanger the countries participating in them. One example here is the Late Bronze Age Collapse (2), as explored in Linkov et al. (2024). 

Linkov et al. (2024) build a network model to map out trade links and political connections (Figure 4). A political connection in this context refers to things like signed treaties to form a defense pact. They then remove nodes from that network to test which ones had the biggest impact. They found that in the case of the Bronze Age, both political and trade networks strongly relied on the Hittite Empire and Ugarit to function. If you remove those nodes, as happened historically due to their collapse, the whole network unravels, as the eastern and western parts of the network lose a lot of their connections that kept them stable. This loss was especially problematic as the Bronze Age collapse economy was strongly reliant on tin, which was mainly mined on Cyprus. With the Hittite Empire and Ugarit gone, the only remaining political connection of Cyprus was Egypt, which itself was in crisis and therefore not in the state anymore to help maintain trade. As predicted by LInkov et al. (2024), the collapse of the Ugarit and Hittite empires led to a broader collapse as more distant regions lost access to trade via their linkages to these empires. The Late Bronze Age Collapse, which spanned the broader mediterranean region ensued.

![Bronze Age Connections](https://raw.githubusercontent.com/florianjehn/Societal_Collapse/main/assets/img/bronze_age_connections.png)

Figure 4: The Bronze Age network for trade and politics. 

Our current food trade network is not that dissimilar. If for example, the United States would cease to trade food for some reason, this alone has the potential to completely unravel our food trade network. 

# How important is domestic production in comparison with trading food?

Another way to look at food trade is to explore when it is helpful to import a lot of food and when this is more of a liability and you should rather have grown your domestic food production. This is explored in an article by (Verschuur et al., 2024). The researchers developed a bilateral trade model for 177 countries and four major crops (maize, wheat, rice, soybean) to simulate how different types of shocks affect food availability and prices. They modeled several scenarios: the Ukraine war, energy price shocks, trade restrictions, and a "polycrisis" combining all three—against 54 years of weather-driven production variability.

Key findings about trade as a buffer:

* Trade generally helps mitigate localized shocks by allowing countries to source food from alternative suppliers. For example, when Ukraine's exports were disrupted, importing countries shifted to other suppliers.
* In typical years, countries with high import dependency experienced smaller reductions in consumer surplus, suggesting trade networks provide resilience against moderate disruptions.
* During the Ukraine war scenario, international trade flows increased as countries sought alternative suppliers, demonstrating trade's adaptive capacity.

However, trade has limitations as a buffer:

* During extreme "tail risk" events (the worst 10% of scenarios), higher import dependency became a vulnerability rather than an asset—especially for maize and rice. Countries with greater domestic production were better buffered against severe shocks.
* Trade can transmit and amplify shocks across the global system. The compound "polycrisis" scenario resulted in consumer price increases of 23-52% across all crops, affecting virtually all countries simultaneously.
* Trade restrictions (like India's rice export ban) severely impacted specific regions, particularly Sub-Saharan Africa and Central Asia.

The energy price shock proved most damaging overall, increasing input costs globally, while different regions showed varying vulnerabilities to specific shock types. The research suggests that both trade connectivity and domestic production capacity are needed in a "risk layering" approach to food system resilience.

In essence, trade provides crucial flexibility for the food system to adapt to shocks, but becomes less effective as buffers during compound, global-scale disruptions. This is a similar conclusion as Yıldırım & Önen (2024), but Verschuur et al. additionally back this up with modelling. 

Another paper which digs deeper into the danger of trade amplifying shocks throughout the system is by Keys et al. (2025). They wanted to understand how climate hazards are transmitted through global food trade. More specifically, they focussed on how both hot and dry and hot and wet climate shocks reduced agricultural production and how this reduction impacted both the producing country and their trading partners. To model this, they ran a climate model (CESM 2) 100 times for 10 years in each run. Every run has slightly different starting conditions and thus develops differently over time. In total these 100 runs represent the plausible variability of the climate over 10 years. The variability they found thus allowed them to assess which parts of the Earth have a chance of being exposed to climate shocks. 

With this knowledge they could assess how much of our global agricultural production might be affected by those climate shocks. To check how these production shocks might then impact trading partners, they used trading data to understand how much food countries are importing and from where. This allowed them to calculate how much of the food supply in a given country might be affected by local as well as climate shocks in other countries (Figure 5). This showed them that there are many countries that can expect that 30 % or more of their crop supply might be disrupted due to climate shocks in the next ten years (with up to 93 % in the case of Serbia). 

![Shock exposure](https://raw.githubusercontent.com/florianjehn/Societal_Collapse/main/assets/img/shock_exposure.png)

Figure 5: Exposure of crop supply for different countries to climate shocks. Black lines indicate single model runs. Violin plot overall indicates the distribution of the exposure throughout all runs. 

Generally, they found that the best shield against climate shocks is having as many countries you import food from as possible, which should also be distributed throughout different climate zones. If you only rely on your local crops and those of your neighbours, it is likely you will have a bad time due to climate change at some point. 

# Comparing food trade to trade of other goods

All this shows that our food trade system is susceptible to risks, highlighting the importance of increasing resilience. Interestingly, while the food system appears increasingly vulnerable, this trend does not necessarily extend to the broader trade system. Kang et al. (2024) examined trade flows over the past three decades. Their analysis involved systematically removing nodes from the network to simulate the redistribution of node load to neighboring nodes. They observed a gradual decrease in countries' reliance on others, particularly since the 2008 financial crisis. This shift is attributed to the decreasing significance of fossil fuels due to the emergence of alternative energy sources, alongside increased awareness among nations about supply line vulnerabilities and efforts to enhance resilience after recurring shocks to the system like COVID-19 or the financial crisis. However, the study also revealed that even the removal of a smaller country can cause significant disruptions, as neighboring nodes often lack sufficient capacity to absorb the loss. 

# Are we modeling trade too simply?

Most studies on trade model it as a directed graph and use various methods to assess the impact of removing a node from the network. This means trade only gets worse, as there is no way to introduce new connections. However, in real life any trade disruption leads to adaptations of some kind. 

For example, after the Russian invasion of Ukraine there were fears that Ukraine would be lost completely as a wheat exporter, which would have been a big disruption. How this was prevented is explored in a paper by Kuhla et al. (2023). They show that there was a price spike, but not as high as was feared. The international community helped broker a deal with Russia that allowed some export via the Black Sea, while also allowing Ukraine to trade more grain via European rivers instead of the Black Sea. In addition, the global wheat harvest was exceptionally high in 2022, which further removed pressure from the system. This means that without this international agreement and the lucky weather, the effects could have been much worse. 

The challenge lies in predicting the outcomes of such adaptations before they happen. Fortunately, we have not experienced the complete removal of major exporters like the United States or Russia, but this leaves us with limited data for modeling new trade connections after big shocks. So far I haven’t found a study which has a good model for the establishment of new trade connections after big disruptions.

*If you know of important studies I’ve missed here, please email me and I’ll update this article!*

This also highlights the importance of geopolitics for trade. We have seen that political ramifications had been a major factor when the trade network collapsed during the Bronze Age and also the shifts after Russia’s invasion of Ukraine are obviously linked to politics. But we can look at even broader trends here. These decades-long geopolitical changes and their influence on trade are explored in Piñeiro & Piñeiro (2024). Specifically, they looked at how much trade was worth in comparison with GDP and found that it peaked before World War I, crashed down in the period of 1914 - 1945 and has consistently grown since then. However, it also seems that either the growth has slowed down or might even have reversed after ~2020. They argue that this recent shift has been happening as countries are stepping away from international treaties around trade. In parallel, many countries are starting to sort themselves into power blocks, especially around China and the United States. They decrease their trade with everyone outside their power block and increase it in their power block. Given the developments of the United States isolating itself more and more since Trump has become president again, it seems likely that in the coming years trade as a share of GDP will decrease and that the power block around the United States might shatter into smaller groups of countries, which would further decrease trade. 

In summary, the global trade system, particularly in the food sector, is inherently vulnerable and it is very difficult to predict how disruptions might turn out. This highlights that it should be a priority to increase resilience, so we don’t follow the same path as the empires of the Bronze Age. It seems that domestic food production is an important factor here if you want to be resilient against major shocks. Food trade only seems to help well for smaller shocks. Additionally, the current geopolitical world situation seems to imply that we will see decreased trade in the coming years. While this is likely bad in general, it might increase resilience for some countries, as they have to become more self-reliant. However, globally this is a worse outcome, both now, as everything becomes more expensive when trade decreases, but also after major crises, as these tend to be managed better if countries trust each other and work together. 

# Endnotes

(1) [An earlier post](https://florianjehn.github.io/Societal_Collapse/2024-03-04-where_to_stay/) also mentions the problems of losing access to inputs for your agriculture in more detail. 

(2) We discussed the Bronze Age Collapse in more detail in an [earlier post](https://florianjehn.github.io/Societal_Collapse/2020-10-28-bronze_age/). 

# How to cite
Jehn, F. U. (2024, April 25). Trade collapse. Existential Crunch. [https://doi.org/10.59350/rwygp-c5n09](https://doi.org/10.59350/rwygp-c5n09)

# References

* Clapp, J. (2023). Concentration and crises: Exploring the deep roots of vulnerability in the global industrial food system. The Journal of Peasant Studies, 50(1), 1–25. https://doi.org/10.1080/03066150.2022.2129013
* D’Odorico, P., Carr, J. A., Laio, F., Ridolfi, L., & Vandoni, S. (2014). Feeding humanity through global food trade. Earth’s Future, 2(9), 458–469. https://doi.org/10.1002/2014EF000250
* Jain, S. (2024). Mapping Global Cereal Flow at Subnational Scales Unveils Key Insights for Food Systems Resilience. Research Square. https://doi.org/10.21203/rs.3.rs-5204730/v1
* Jehn, F. U., Gajewski, Ł. G., Hedlund, J., Arnscheidt, C. W., Xia, L., Wunderling, N., & Denkenberger, D. (2024). Food trade disruption after global catastrophes. EarthArXiv. https://eartharxiv.org/repository/view/7339/
* Ji, G., Zhong, H., Feukam Nzudie, H. L., Wang, P., & Tian, P. (2024). The structure, dynamics, and vulnerability of the global food trade network. Journal of Cleaner Production, 434, 140439. https://doi.org/10.1016/j.jclepro.2023.140439
* Kang, H., Lee, K.-M., & Yang, J.-S. (2024). The potential for cascading failures in the international trade network. PLOS ONE, 19(3), e0299833. https://doi.org/10.1371/journal.pone.0299833
* Keys, P. W., Barnes, E. A., Diffenbaugh, N. S., Hertel, T. W., Baldos, U. L. C., & Hedlund, J. (2025). Exposure to compound climate hazards transmitted via global agricultural trade networks. Environmental Research Letters, 20(4), 044039. https://doi.org/10.1088/1748-9326/adb86a
* Kuhla, K., Puma, M., & Otto, C. (2023). Stabilizing international wheat prices through international cooperation after the Russian invasion of Ukraine [Preprint]. In Review. https://doi.org/10.21203/rs.3.rs-3316541/v1
* Linkov, I., Galaitsi, S. E., Trump, B. D., Pinigina, E., Rand, K., Cline, E. H., & Kitsak, M. (2024). Are civilizations destined to collapse? Lessons from the Mediterranean Bronze Age. Global Environmental Change, 84, 102792. https://doi.org/10.1016/j.gloenvcha.2023.102792
* Piñeiro, M., & Piñeiro, V. (2024). Geopolitical changes and their implications for agricultural trade negotiations. https://hdl.handle.net/10568/151905
* Puma, M. J., Bose, S., Chon, S. Y., & Cook, B. I. (2015). Assessing the evolving fragility of the global food system. Environmental Research Letters, 10(2), 024007. https://doi.org/10.1088/1748-9326/10/2/024007
* Verschuur, J., Murgatroyd, A., Vittis, Y., Mosnier, A., Obersteiner, M., Godfray, C., & Hall, J. (2024). The impacts of polycrises on global grain availability and prices. https://doi.org/10.21203/rs.3.rs-3969801/v1
* Wellesley, L., Preston, F., Lehne, J., & Bailey, R. (2017). Chokepoints in global food trade: Assessing the risk. Research in Transportation Business & Management, 25, 15–28. https://doi.org/10.1016/j.rtbm.2017.07.007
* Yıldırım, C., & Önen, H. G. (2024). Vulnerabilities of the neoliberal global food system: The Russia–Ukraine War and COVID-19. Journal of Agrarian Change, n/a(n/a), e12601. https://doi.org/10.1111/joac.12601


