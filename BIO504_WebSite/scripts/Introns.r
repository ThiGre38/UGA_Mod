# Programme R pour la comparaison de sequences deux a deux (ici les sequences de debut et de fin des introns)
# Les sequences a comparer sont stockees dans 2 vecteurs
# Les vecteurs sont lus et compares caractere par caractere
# En cas d'equalite, la valeur est stockee dans une variable, sinon, le caractere est enregistre a la place
# Pour faciliter le script, le debut et la fin de l'intron sont notes dans une seule variable. Ils sont séparés par le signe |

I1<-c("g","t","t","g","g","t","a","t","c","a","a","g","g","t","t","|","t","t","t","t","c","c","c","a","c","c","c","t","t","a","g") #Affectation du debut de l’intron1 a la variable I1
I2<-c("g","t","g","a","g","t","c","t","a","t","g","g","g","a","c","|","a","t","c","t","t","c","c","t","c","c","c","a","c","a","g") #Affectation du debut de l’intron2 a la variable I2

res<-character(31) #creation de la variable res pour stocker le resultat de la comparaison

for (i in 1:31){ #31 caracteres a comparer : 15 ntds du debut + 15 ntds de la fin + le signe |
if (I1[i]==I2[i]) res[i]<-I1[i]
	else res[i]<-"N"
} #boucle de comparaison et d’écriture des résultats dans la variable seq1 pour le début de l'intron

print("La séquence consensus des introns est :")

cat(res) #Affichage du résultat de comparaison de début d'intron