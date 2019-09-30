# 1. Setup
setwd("~/Desktop/INFO 370/Project/")
library(dplyr)
library(tidyr)
library(stringr)
library(lubridate)
library(ggplot2)


# Word Count Analysis
get_top_x_words_prop <- function(x,data) {
  cross_doc_prop <- colSums(data) / sum(cross_doc_freq)
  top_10_props <- sort(cross_doc_prop, decreasing=TRUE)[1:x]
}
get_top_x_words_count <- function(x,data) {
  cross_doc_count <- colSums(data)
  top_10_count <- sort(cross_doc_count, decreasing=TRUE)[1:x]
}
# NPR
npr <- read.csv('./fakenews/npr_clean.csv', stringsAsFactors = FALSE)
npr_wo_metadata <- npr[c(-1,-13923,-13924)] # drops title, author, and index cols
npr_top_10_props <- get_top_x_words_prop(10, npr_wo_metadata)
# BBC
bbc <- read.csv('./fakenews/bbc_clean.csv', stringsAsFactors = FALSE)
bbc_wo_metadata <- bbc[c(-1, -2046, -2047)]
bbc_top_10_props <- get_top_x_words_prop(10,bbc_wo_metadata)
# ECON
econ <- read.csv('./fakenews/economist_clean.csv', stringsAsFactors = FALSE)
econ_wo_metadata <- econ[c(-1, -5593, -5594)]
econ_top_10_props <- get_top_x_words_prop(10,econ_wo_metadata)
# FAKE
fake_clean <- read.csv('./fakenews/fake_clean.csv', stringsAsFactors = FALSE)
# fake_wo_metadata <- fake_clean[c(-1, -(last_col - 1), -(last_col))]
fake_top_10_props <- get_top_x_words_prop(10,fake_clean[,100:200])
ncol(fake_clean)


# Plot 
par(mfrow = c(2,2)) # For 4 plots in 1. If you get "too small" margins, tweak this. 
barplot(fake_top_10_props,xlab = 'Word', main='FAKE', ylab = 'Proportion of All Articles', ylim=c(0,max(fake_top_10_props) + 0.002))
barplot(npr_top_10_props, xlab = 'Word', main= 'NPR', ylab = 'Proportion of All Articles', ylim=c(0,max(npr_top_10_props) + 0.002))
barplot(bbc_top_10_props, xlab = 'Word', main='BBC', ylab = 'Proportion of All Articles', ylim=c(0,max(bbc_top_10_props) + 0.002))
barplot(econ_top_10_props,xlab = 'Word', main='ECON', ylab = 'Proportion of All Articles', ylim=c(0,max(econ_top_10_props) + 0.002))

# Fake news data!
fake <- read.csv('./fake.csv', stringsAsFactors = FALSE)
fake$type <- as.factor(fake$type)
fake$country <- as.factor(fake$country)
fake$language <- as.factor(fake$language)
fake$published <- as_datetime(fake$published)
fake$crawled <- as_datetime(fake$crawled)
summary(fake)

par(mfrow=c(1,2)) # For 2 plots in 1! Same word of caution as above

fake_type_prop <- sort(table(fake$type) / 12999, decreasing = TRUE)
fake_country_prop <- sort(table(fake$country) / 12999, decreasing = TRUE)
fake_language_prop <- sort(table(fake$language) / 12999, decreasing = TRUE)

barplot(fake_type_freq, ylim=c(0,max(fake_type_freq) + 0.5), xlab = 'Type', ylab = 'Proportion of All Observations')
barplot(fake_country_prop, ylim=c(0,max(fake_country_prop) + 0.5), xlab = 'Country', ylab = 'Proportion of All Observations')

# ADDITIONS: 12/6
bobg_train <- read.csv("./Analysis/clean_data/bobg_train.csv", row.names = 1)
bow_train <- read.csv("./Analysis/clean_data/bow_train.csv", row.names = 1)

bobg_train_top_10_counts <- get_top_x_words_count(10, bobg_train)
bow_train_top_10_counts <- get_top_x_words_count(10, bow_train)

df <- cbind(1:10, data.frame(bobg_train_top_10_counts))
tmp <- row.names(df)
row.names(df) <- df$`1:10`
df$`1:10` <- tmp
colnames(df) <- c("word", "counts")

g <- ggplot(df, aes("word", "counts"))


ggplot(data2, aes(variable, value, fill = Lang))
  

par(mfrow = c(2,1)) # For 2 plots in 1. If you get "too small" margins, tweak this. 
barplot(bobg_train_top_10_counts, xlab = 'Word', main='Bobg Train', ylab = 'Frequency Across All Entries', ylim=c(0,max(bobg_train_top_10_counts) + 100))
barplot(bow_train_top_10_counts, xlab = 'Word', main='Bow Train', ylab = 'Frequency Across All Entries', ylim=c(0,max(bow_train_top_10_counts) + 10000))

# NEW DATA
x_train = read.csv("./Analysis/clean_data/x_train_clean.csv", row.names = 1)
x_test = read.csv("./Analysis/clean_data/x_test_clean.csv", row.names = 1)
y_train = read.csv("./Analysis/clean_data/y_train.csv", row.names = 1)
y_test = read.csv("./Analysis/clean_data/y_test.csv", row.names = 1)

x <- rbind(x_train, x_test)
y <- rbind(y_train, y_test)

write.csv(x, file = "./Analysis/clean_data/x.csv")
write.csv(y, file = "./Analysis/clean_data/y.csv")

# Final Visualizations!!
bow_fake = read.csv("./Analysis/clean_data/bow_fake.csv", row.names = 1)
bow_real = read.csv("./Analysis/clean_data/bow_real.csv", row.names = 1)

bobg_fake = read.csv("./Analysis/clean_data/bobg_fake.csv", row.names = 1)
bobg_real = read.csv("./Analysis/clean_data/bobg_real.csv", row.names = 1)

bow_fake_top_10_counts <- get_top_x_words_count(10, bow_fake)
bow_real_top_10_counts <- get_top_x_words_count(10, bow_real)
bobg_fake_top_10_counts <- get_top_x_words_count(10, bobg_fake)
bobg_real_top_10_counts <- get_top_x_words_count(10, bobg_real)

par(mfrow=c(2,2)) # For 2 plots in 1! Same word of caution as above
barplot(bow_fake_top_10_counts, 
        ylim=c(0,30000), 
        xlab = 'Word', ylab = 'Count', main = 'Bow (Fake)')
barplot(bow_real_top_10_counts, 
        ylim=c(0,5000), 
        xlab = 'Word', ylab = 'Count', main = 'Bow (Real)')
barplot(bobg_fake_top_10_counts, 
        ylim=c(0,5000), 
        xlab = 'Bigram', ylab = 'Count', main = 'Bobg (Fake)')
barplot(bobg_real_top_10_counts, 
        ylim=c(0,500), 
        xlab = 'Bigram', ylab = 'Count', main = 'Bobg (Real)')

bobg_real_top_10_counts



