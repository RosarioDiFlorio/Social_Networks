echo "start"
echo "HITS"
python Test_HITS.py >> result_HITS.txt
echo "PageRank"
python python Test_Dataset_PageRank.py >> result_PageRank.txt
echo "Done"