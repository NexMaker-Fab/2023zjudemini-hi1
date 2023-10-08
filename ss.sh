
# !/bin/bas
for file in md/*.md; do
  title=$(basename "$file" .md)
  echo "# ${title}\n" > $file
done


#!/bin/bash

# Create directory if it doesn't exist
# mkdir -p md

# Array of file names
# files=("01_Project_manage.md" "01_more.md" "01_less.md" "02_CAN_design.md" "03_3D_printer.md" "04_Electric_design.md" "05_Ardiuno_application.md" "06_Laser_cutting.md" "07_PCB_manifacture.md" "08_CNC_manufacture.md")

# # Loop through array and create files with initial content
# for file in "${files[@]}"; do
#   title=$(echo $file | sed 's/\.md//')
#   echo -e "# ${title}\n" > "md/${file}"
# done
