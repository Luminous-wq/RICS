conda activate RICS

cd ../

## uni
for ((i=0;i<5;i++))
do
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 36,37,17,26,31 -R 2 -k 4 -N 10 -q 30807 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 10,16,25,26,30 -R 2 -k 4 -N 10 -q 11908 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 33,3,35,37,42 -R 2 -k 4 -N 10 -q 47727 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 40,42,45,26,31 -R 2 -k 4 -N 10 -q 37902 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 35,37,47,22,30 -R 2 -k 4 -N 10 -q 19906 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 38,6,15,16,20 -R 2 -k 4 -N 10 -q 13120 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 36,10,44,19,27 -R 2 -k 4 -N 10 -q 47416 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 37,12,47,24,27 -R 2 -k 4 -N 10 -q 26875 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 34,38,16,30,31 -R 2 -k 4 -N 10 -q 49624 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 6,11,18,22,29 -R 2 -k 4 -N 10 -q 46964 -d 5
done
## gauss
for ((i=0;i<5;i++))
do
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 33,37,23,30,31 -R 2 -k 4 -N 10 -q 41163 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 32,5,15,25,28 -R 2 -k 4 -N 10 -q 9266 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 33,37,13,22,31 -R 2 -k 4 -N 10 -q 17166 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 32,19,21,23,26 -R 2 -k 4 -N 10 -q 25380 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 32,35,13,18,22 -R 2 -k 4 -N 10 -q 40871 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 13,14,22,29,30 -R 2 -k 4 -N 10 -q 22102 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 33,19,21,24,27 -R 2 -k 4 -N 10 -q 21987 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 32,23,25,26,29 -R 2 -k 4 -N 10 -q 46434 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 15,16,22,25,31 -R 2 -k 4 -N 10 -q 46711 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 38,20,22,26,29 -R 2 -k 4 -N 10 -q 30471 -d 5
done
## zipf
for ((i=0;i<5;i++))
do
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,5 -R 2 -k 4 -N 10 -q 11129 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,16 -R 2 -k 4 -N 10 -q 44831 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,8,9 -R 2 -k 4 -N 10 -q 45586 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,12,49,18 -R 2 -k 4 -N 10 -q 8651 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,7 -R 2 -k 4 -N 10 -q 21745 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,7 -R 2 -k 4 -N 10 -q 13560 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,7,15 -R 2 -k 4 -N 10 -q 38077 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,9 -R 2 -k 4 -N 10 -q 44995 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,49,8,9 -R 2 -k 4 -N 10 -q 4289 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,49 -R 2 -k 4 -N 10 -q 6421 -d 5

done