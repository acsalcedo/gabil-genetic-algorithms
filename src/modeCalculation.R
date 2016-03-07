datos = read.table("crx.data", header= TRUE, sep= ",")
attach(datos)
names(datos)
 
moda<-function(var){
	frec.var<-table(var)
	valor<-which(frec.var==max(frec.var)) 
	names(valor)
}

cat(" Moda de atributo 1 ", moda(att1))
cat("\n Moda de atributo 2 ", moda(att2))
cat("\n Moda de atributo 2 ", moda(att3))
cat("\n Moda de atributo 4 ", moda(att4))
cat("\n Moda de atributo 5 ", moda(att5))
cat("\n Moda de atributo 6 ", moda(att6))
cat("\n Moda de atributo 7 ", moda(att7))
cat("\n Moda de atributo 8 ", moda(att8))
cat("\n Moda de atributo 9 ", moda(att9))
cat("\n Moda de atributo 10 ", moda(att10))
cat("\n Moda de atributo 11 ", moda(att11))
cat("\n Moda de atributo 12 ", moda(att12))
cat("\n Moda de atributo 13 ", moda(att13))
cat("\n Moda de atributo 14 ", moda(att14))
cat("\n Moda de atributo 15 ", moda(att15))

cat("\n Moda de atributo 2 ignorando ?:", "\n")
summary(att2)

#23.25
