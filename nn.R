require(neuralnet)
files <- list.files('*.txt')
files <- files[ files != 'scores.txt' ]
print(files)
docs <- unname(sapply(files, readLines))
print(docs)
scores <- c(scan('scores.txt'))
print(scores)
df <- data.frame(docs,scores)
print(df)
nn=neuralnet(scores~docs,data=df, hidden=3,act.fct = "logistic",
                linear.output = FALSE)
plot(nn)
