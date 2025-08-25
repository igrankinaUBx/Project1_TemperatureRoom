data <- read.csv('../processed/temperature_dataset.csv')
summary(data$temperature_C)
plot(data$temperature_C, type='l', col='blue',
     main='Room temperature by hour',
     xlab='Observation', ylab='Temperature (°C)')
