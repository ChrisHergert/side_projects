# Import libraries
library(MASS)

#Define functions
partial_order <- function(indx, ord_stats){
  indx_full_part = floor(indx)  #get the full part
  indx_partial = indx-indx_full_part #get the fractional part
  full_part = ord_stats[indx_full_part]
  partial_part = indx_partial*(ord_stats[indx_full_part+1]-ord_stats[indx_full_part])
  full_part+partial_part
}

#Instantiate variables
n <- 50000
loc <- 5
scal <- 3

#Generate sample data
X <- rcauchy(n = n, location=loc, scale = scal)
order_stats <- unique(sort(X))

#Generate the index (i) and the partial order stats index (ui)
i <- seq(1,n)
ui <- (i-0.5)/n

#Add the fractional order stats (sample QF values) to the df
fr_order_stats <- quantile(X, ui)
df <- data.frame(i, ui, fr_order_stats)

#Add the Q(ui) values for a standard cauchy to the df
df$Q <- qcauchy(df$ui)

# plot the (Q(ui), Y(i) values) with a line
plot(df$Q,
     df$fr_order_stats,
     xlim = c(-200, 200),
     ylim = c(-200, 200) )
lm(df$fr_order_stats ~ df$Q)
abline(lm(df$fr_order_stats ~ df$Q))

# Get the 5% trimmed Q and Y(i) data, and re-plot with a new linear model
new_Q <- df$Q[floor(length(df$Q)*0.005): 
                floor(length(df$Q)*0.995)]
new_ord_stats <- df$fr_order_stats[floor(length(df$fr_order_stats)*0.005): 
                                     floor(length(df$fr_order_stats)*0.995)]
plot(new_Q,
     new_ord_stats,
     xlim = c(-200, 200),
     ylim = c(-200, 200) )
lm(new_ord_stats ~ new_Q)
abline(lm(new_ord_stats ~ new_Q))
