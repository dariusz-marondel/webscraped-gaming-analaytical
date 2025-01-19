# Gaming statistics project with web-extracted data, analytics and visualisations
I designed the project to present combined skills of different domains that come of use in a data analyst work. Its intention is to be a portfolio project, however regardless of who the reader is - a recruiter or not - I hope you will enjoy! 

Despite its 'potfolioiness' the project has everything that a real life business project would have had:
1. A client
2. Business need 
3. Considerations regarding what kind of tool can translate a data into value for client 
4. Considerations of what kind of data is needed to generate that value
5. Data extractions, pipelines and storage suficient and not exceeding project needs
6. Visualisations for the client to answer their business problem
7. Scalability in a way of: 
- ability to automate and deploy a project as a recurring solution 
- ease of implementing any aditional report 

All of those consideration I describe below so give you, the reader, and idea behind my decision making process. The readme will guide you trough project flow via links.

## Clients' background and needs
Group of my friends and myself are going to play tournament (a clash) in league of legends this weekend. What an excitement! So many players from entire european server are going to fight for the crown and title of clash conqueror! 

After some thinking about what champions we are going to play, we have realised that with all of us swamped with our jobs, we have not played league in some time. Consequently, we have no idea which champions are stronger right now and which we should avoid to ensure highest possible chances for success. 

### Business problem
A client is the Nexus Park Boys league of legends team. It is a semi-amateur group of five friends who play tournament from time to time. They look for a data profesional who can aid them in decision-making process in the upcoming endevor. 

### Needs and objectives
All players are very competitive so the team's primary objective is to win the tournament with the secondary objective being to have fun. The former is achieved by adopting the decision that gives highest possible winrate while chosing from champions know and liked by the team so they can still achieve the latter. 

In simple words: __They want to know what character picked in the upcoming tournament in their favorite game.__ 

### Data
Since my client does not produce nor store any data, the actual information about global statistics would have to be obtained by me. I will visit game developer portal to see what kind of data I can legally and oficially pull from their website so the data I provide with client will have actual value based on real time data. 

Statistics disclaimer: For technical reasons I pulled only such amount of data which will be updated once app got an accpet from Riot for a dedicated API_key. Logic in data analysis is still solid, but regardless of sample i adopted an assumption that there is enough data to assume that Central Limit Theorem's requirements are met. This way I will be conluding as if there were much more data for specific champions, which may yield some interesting observations and conclusions. 

### Reports
I designed three reports that can answer following questions:
1. From options that are preffered by the client (the team) which choice is the best (what characters that team likes to play is statistically more likely to result in a match win.)
2. Based on the statistically enabled simulations, which player is theoretically best based on winrate. 
3. From processes curently known and operated by client (characters they like) which gained or lost the most efficiency (based on the chnage in winrate)

## Approach to solution 
As I have some spare time in the evenings (god bless no overtime this time!) I decided to pull some data from Riot Games API to prepare some report on our respective champion pools. I have decided that since we may play some clash again in the future and evenings without overtime are not to be taken for granted (!), it is better to already prepare the automation of the report regardless of its simplicity (or maybe even more willingly taking that into account). <br>

I inquired my friends of required data and began working. 

## Goal of the project
The projects contain of scheduled workflows pulling data from Riot games developer API, then transforming it to make some beautiful (reasonably!) report(s) with some simple insights. I aim to explain all as clear as possible so even non-technical people could find it interesting but also to demonstrate ability to communicate without overcomplicating things. The project is more focused on display of technical and data literacy rather that presenting any grounbreaking market research. 

It is intended to display my skill in few technologies combined such as:
1. SQL 
2. API calls
3. Data handling
4. Docker
5. Airflow
6. Python
7. Data visualisation - Seaborn, Plotly


## Technicals

1. Project was developed using 'Pycharm CE v2024.3.1.1' and 'Visual Studio Code v1.95.3'
2. It was published first and only on this gitHub - amberlights-py/XX - 
3. Its core is 'Python 3.8.10 ' to ensure maximum compatibility with Airflow as specified in its documentation.
4. 'Apache Airflow v2.10.4' - https://tinyurl.com/airflow-apache
5. Docker v4.37.2
6. Data if no specified otherwise, was pulled from Riot Developer APIs - https://developer.riotgames.com
7. DataGrip v2024.3.3 for database operations

From gitHub with love
Dariusz