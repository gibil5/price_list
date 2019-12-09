# Init
DIR=csv/


# Copy 
cp ~/Desktop/PRECIOS\ 2019/* . 
#cp -r ~/Desktop/PRECIOS\ 2019.numbers ./backup/. 
cp -r ~/Desktop/PRECIOS\ 2019.numbers ./excel/. 

# Move
mv "TEST-Table 1.csv" 		$DIR"TEST.csv"       

mv "CONSULTATIONS-Table 1.csv" $DIR"CONSULTATIONS.csv"

mv "CO2-Table 1.csv" 		$DIR"CO2.csv"       
mv "QUICK-Table 1.csv" 		$DIR"QUICK.csv"
mv "EXCILITE-Table 1.csv" 	$DIR"EXCILITE.csv"     
mv "M22-Table 1.csv" 		$DIR"M22.csv"          
mv "COSMETO-Table 1.csv" 	$DIR"COSMETO.csv" 
mv "MEDICAL-Table 1.csv" 	$DIR"MEDICAL.csv" 
mv "GINECO-Table 1.csv" 	$DIR"GINECO.csv"       
mv "PRODS-Table 1.csv" 		$DIR"PRODS.csv"
mv "ECO-Table 1.csv" 		$DIR"ECO.csv" 
mv "PROMOS-Table 1.csv" 	$DIR"PROMOS.csv"

# Clean
rm "COMMENT-Table 1.csv"
rm "BUFF - M22-Table 1.csv"
rm "BUFF - PROMOS-Table 1.csv"

# Test
ls $DIR

