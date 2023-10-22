# A file to manage the content in repo
# # !/bin/bas
# for file in md/*.md; do
#   title=$(basename "$file" .md)
#   echo "# ${title}\n" > $file
# done


#!/bin/bash

# Create directory if it doesn't exist
# mkdir -p md

# Array of file names
files=("01_Project_manage" "01_more" "01_less" "02_Ardiuno" "03_Interface_application_programming" "04_Computer_aided_design" "05_3D_printing_and_laser_cutter" "06_Final_presentation")

# Loop through array and create files with initial content
for file in "${files[@]}"; do
  title=$(echo $file | sed 's/\.md//')
  echo  "# ${title}\n" > "md/${file}"
done

# files=("01_Project_manage" "01_more" "01_less" "02_Ardiuno" "03_Interface_application_programming" "04_Computer_aided_design" "05_3D_printing_and_laser_cutter" "06_Final_presentation")

# # 创建文件并插入初始化介绍
# for file in "${files[@]}"; do
#   title=$(echo $file | tr '_' ' ')
#   echo  "# ${title}\n" > "md/${file}.md"
# done
