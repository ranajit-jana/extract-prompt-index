csvdatalocation=$(yq eval '.extract.csv_folder_location' ./runnerconfig.yaml)
echo $csvdatalocation
python3 ../src/reader.py $csvdatalocation