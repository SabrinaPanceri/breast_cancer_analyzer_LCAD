set terminal png size 800,600; set output 'precision_recall_validation.png'; set xlabel 'Recall'; set ylabel 'Precision'; plot 'metrics_validation.txt' using 8:7 
#pause -1
set terminal png size 800,600; set output 'precision_recall_test.png'; set xlabel 'Recall'; set ylabel 'Precision'; plot 'metrics_test.txt' using 8:7 
#pause -1
set terminal png size 800,600; set output 'specificity_sensitivity_validation.png'; set xlabel 'Specificity'; set ylabel 'Sensitivity'; plot 'metrics_validation.txt' using 10:11
#pause -1
set terminal png size 800,600; set output 'specificity_sensitivity_test.png'; set xlabel 'Specificity'; set ylabel 'Sensitivity'; plot 'metrics_test.txt' using 10:11
#pause -1

