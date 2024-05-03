#!/bin/zsh
source ./venv_test_gropro_2024/bin/activate

for input_file in ./input/*.txt;
do
    python3.12 source/main.py -f "$input_file";
done

for output_file in ./output/*.gnu;
do
    gnuplot -p "$output_file";
done

deactivate
