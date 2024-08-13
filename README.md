# Extractor for APSDPS last 24 hrs Weather data

url http://apsdps.ap.gov.in/Realtime/Alldata24.jsp

Proposed features
- cron job every day to save the data
- save the data in sqlite database
- web application to download the data (analysis - graphs ,raw data, summary for a particular station or as whole)
- get rough gps locations of weather stations for spatial analysis
- check for data anamolies