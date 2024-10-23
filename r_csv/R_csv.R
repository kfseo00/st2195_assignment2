library(rvest)
library(httr)
library(readr)

url <- "https://en.wikipedia.org/wiki/Comma-separated_values"
webpage <- read_html(url)

table <- webpage %>% html_table(fill = TRUE, trim = TRUE)

cars_table <- table[[2]]
print(cars_table)

write_csv(cars_table, "cars_table.csv")

cat("Scraped data saved as 'cars_table.csv'")

df <- read.csv("cars_table.csv")
print(df)
str(df)

