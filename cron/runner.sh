csvdatalocation=$(yq eval '.extract.csv_folder_location' ./runnerconfig.yaml)
llmserverlocation=$(yq eval '.extract.llm_api_url' ./runnerconfig.yaml)
esurl=$(yq eval '.extract.elasticsearch_url' ./runnerconfig.yaml)
esindex=$(yq eval '.extract.elasticsearch_index' ./runnerconfig.yaml)
escatagory=$(yq eval '.extract.elasticsearch_category' ./runnerconfig.yaml)
echo $csvdatalocation
echo $llmserverlocation
echo $esurl
echo $esindex
echo $escatagory
python3 ../src/reader.py $csvdatalocation $llmserverlocation $esurl $esindex $escatagory