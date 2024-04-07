csvdatalocation=$(yq eval '.extract.csv_folder_location' ./runnerconfig.yaml)
llmserverlocation=$(yq eval '.extract.llm_api_url' ./runnerconfig.yaml)
echo $csvdatalocation
echo $llmserverlocation
python3 ../src/reader.py $csvdatalocation $llmserverlocation