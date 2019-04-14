max=$(brightnessctl max)
current=$(brightnessctl get)

printf "  %.0f%%\n" $(printf "(%s/%s)*100\n" $current $max | bc -l)
