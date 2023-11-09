ocorrencias <- read.csv("C:/Users/bruno/Documents/projetosPy/crawlerOcorrencias/ocorrencias.csv", comment.char="#")


barplot(table(ocorrencias$UF),ylab="Freq. Ocorrencias",xlab="Estado",col=2:8)


porcent <- round((100 * table(ocorrencias$ARMA)) / length(ocorrencias$ARMA),1)
pie(porcent, labels = porcent, main = "% Armas Registradas", col = rainbow(length(porcent)))
legend("topright",
       legend = rownames(porcent),
       pch = 21,
       col = rainbow(length(porcent)),
       cex = 0.8,
       bty = "n")

subsetArma <- subset(ocorrencias, ARMA == "Pistola")
barplot(table(subsetArma$UF), ,ylab="Freq. Ocorrencias Pistola",xlab="Estado",col=2:6)
          