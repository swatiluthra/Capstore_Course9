#!/usr/bin/env python
# coding: utf-8

# ## Analytics

# # The Battle of Neighborhoods (Week 1)

# ## Introduction -[Business Problem Statement]

# Which neighborhood in Downtown Toronto is an optimal location to open a Chinese restaurant?
# 
# Generally speaking, as an enterpreneur, the question can be put in an cost-benefit analytics framework, with fundamental rule of profit maximization. Answer to the question depends on the following sub-questions:
# 
# 1. ***Demand*** Which neighborhood has the most demands on Chinese cuisine? 
# 1. ***Supply*** Which neighborhood so far has the mildest competition regarding Chinese food?
# 1. ***Market trends*** The infrastructure, supply chain, consumer preferences, transportation, neighborhood security, etc.
# 
# Lets dive deeper for further analysis, one by one on each aspect.

# ### Demand

# From the perspective of demand side, customers that may bring profits to restaurant are likely to be composed of two parts, domestic demand and external demand
# 
# - ***Domestic demand*** referes to local demands on Chinese food, mainly from inhabitants. Here are some candidate factors to take into consideration
#     - Domestic inhabitants
#     - Ethnic composition. It is safe to suppose that Asian decendents prefer Asian foods including Chinese cuisine
#     - Other structural factors such as age, gender, occupation, income, and so on 
# 
#     Due to data availability issues, in this assignment we only use the domestic inhabitants as a proxy to reflect domestic demand
# 
# - ***External demand*** referes to demands on Chinese food from those who come to this area for a short-period, for the purporses like tour, business trip, friend-visiting, and so on
# 
#     In this assignment, wee do not pay much attention to the external demand. The main reason is fixed effects: the neighborhoods we compare all locate in Toronto, a nice city attracting tourists from all over the world. It is safe to assume that tourists who come to Toronto may go everywhere and eat everywhere around the whole city. In that sense, neighborhoods do not differ much from each other

# ### Supply

# The level of competition imposes obvious impacts on location choice of our restaurant, from the perspective of supply side. 
# 
# To put in more details, we assume that 
# - the more restaurants there already exist in the neighborhood, the more supply there is, and the less attractive it is for our choice, and 
# - of the total number of domestic restaurants, the more proportion of Italian cuisines, the less attractive it is, as well.

# Update: From the demand side, we use number of inhabitants as a measurement, of domestic demand on Chinese restaurant. 
# 
# However, due to the unfamiliarity of Toronto's Boroughs and Neighborhoods, I am not able to find such data... The website [https://www.toronto.ca/city-government/data-research-maps/neighbourhoods-communities/neighbourhood-profiles/](https://www.toronto.ca/city-government/data-research-maps/neighbourhoods-communities/neighbourhood-profiles/) does not list data required.

# ### The Market trends

# It is an interesting topic to discuss what the growth trend of Canadian economy will look like in the following years, which may produce positive effect on restaurant profitability. Other factors include immigrants level and composition, infrastructural improvement, sightseeing changes, and so on. 
# 
# However, in order to keep our research focuses, in this assignment we do not pay much attention to that.

# ### Summary

# So we pay attention to the following factors, based on which to decide where to put our Chinese restaurant
# - number of restaurants, termed as `Restaurant`
# - decomposition of Chinese restaurants relative to all restaurants, termed as `ChnPercent`

# ## Methodology

# The simple model could be written as 
# $$ Attractiveness = F(ChnPercent)$$
# 
# where
# - `Attractiveness` is our goal, used to measure whether it's a good idea to open the restaurant in this neighborhood
# - `ChnPercent` is the percentage of Chinese restaurants in this neighborhood, calculated as 
# $$ ChnPercent = (\text{number of Chinese restaurants}) / (\text{total number of restaurants}) $$
# - For the sake of simplicity, we assume $F()$ is a linear function and $\partial F / \partial x < 0$, $\partial^2 F / \partial x^2 < 0$, $x = \{ChnPercent \}$.

# ## Data Description

# Sources of the previously mentioned data may be:
# 
# - Population by Borough and Neighborhood. Statistics Bureau of Canada, UN Database.
# - Restaurants by number, style, and locations. Collection from Foursquare API
# 

# To be conducted. Results are expected.

# ## Analytics-driven implications & Conclusions

# Based on the empirical results, this section answers the following questions:
# - Which neighborhood / Borough of Toronto is the best Choice for opening a new Chinese restaurant
# - What are the other risks / opportunities to pay attention to, regarding this enterpreneurship adventure?
# - TODOs in the following stage of research
