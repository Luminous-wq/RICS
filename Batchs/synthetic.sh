conda activate RICS

cd ../

# uni
for ((i=0;i<5;i++))
do
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 7,10,12,14,15 -R 2 -k 4 -N 10 -q 30807 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 1,4,6,10,12 -R 2 -k 4 -N 10 -q 11908 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 13,14,15,17,18 -R 2 -k 4 -N 10 -q 47727 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 10,13,16,17,19 -R 2 -k 4 -N 10 -q 37902 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 2,9,12,14,15 -R 2 -k 4 -N 10 -q 19906 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 6,8,11,15,18 -R 2 -k 4 -N 10 -q 13120 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 4,8,14,15,19 -R 2 -k 4 -N 10 -q 47416 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 5,10,11,14,15 -R 2 -k 4 -N 10 -q 26875 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 4,6,12,13,15 -R 2 -k 4 -N 10 -q 49624 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 2,7,9,11,12 -R 2 -k 4 -N 10 -q 46964 -d 10

#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 7,10,12,14,15 -R 2 -k 4 -N 10 -q 30807 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 1,4,6,10,12 -R 2 -k 4 -N 10 -q 11908 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 13,14,15,17,18 -R 2 -k 4 -N 10 -q 47727 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 10,13,16,17,19 -R 2 -k 4 -N 10 -q 37902 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 2,9,12,14,15 -R 2 -k 4 -N 10 -q 19906 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 6,8,11,15,18 -R 2 -k 4 -N 10 -q 13120 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 4,8,14,15,19 -R 2 -k 4 -N 10 -q 47416 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 5,10,11,14,15 -R 2 -k 4 -N 10 -q 26875 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 4,6,12,13,15 -R 2 -k 4 -N 10 -q 49624 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 2,7,9,11,12 -R 2 -k 4 -N 10 -q 46964 -d 8

#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 7,10,12,14,15 -R 2 -k 4 -N 10 -q 30807 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 1,4,6,10,12 -R 2 -k 4 -N 10 -q 11908 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 13,14,15,17,18 -R 2 -k 4 -N 10 -q 47727 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 10,13,16,17,19 -R 2 -k 4 -N 10 -q 37902 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 2,9,12,14,15 -R 2 -k 4 -N 10 -q 19906 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 6,8,11,15,18 -R 2 -k 4 -N 10 -q 13120 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 4,8,14,15,19 -R 2 -k 4 -N 10 -q 47416 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 5,10,11,14,15 -R 2 -k 4 -N 10 -q 26875 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 4,6,12,13,15 -R 2 -k 4 -N 10 -q 49624 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 2,7,9,11,12 -R 2 -k 4 -N 10 -q 46964 -d 3


  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 7,10,12,14,15 -R 2 -k 4 -N 10 -q 30807 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 1,4,6,10,12 -R 2 -k 4 -N 10 -q 11908 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 13,14,15,17,18 -R 2 -k 4 -N 10 -q 47727 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 10,13,16,17,19 -R 2 -k 4 -N 10 -q 37902 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 2,9,12,14,15 -R 2 -k 4 -N 10 -q 19906 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 6,8,11,15,18 -R 2 -k 4 -N 10 -q 13120 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 4,8,14,15,19 -R 2 -k 4 -N 10 -q 47416 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 5,10,11,14,15 -R 2 -k 4 -N 10 -q 26875 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 4,6,12,13,15 -R 2 -k 4 -N 10 -q 49624 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 2,7,9,11,12 -R 2 -k 4 -N 10 -q 46964 -d 5

  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 6,10,12,13,14 -R 2 -k 4 -N 10 -q 61615 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 1,4,6,10,11 -R 2 -k 4 -N 10 -q 23816 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 13,14,15,16,17 -R 2 -k 4 -N 10 -q 95455 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 10,12,14,16,18 -R 2 -k 4 -N 10 -q 75805 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 2,6,8,11,13 -R 2 -k 4 -N 10 -q 39813 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 6,7,10,15,17 -R 2 -k 4 -N 10 -q 26240 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 3,4,7,14,18 -R 2 -k 4 -N 10 -q 94832 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 9,10,11,13,14 -R 2 -k 4 -N 10 -q 53751 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 4,6,8,12,14 -R 2 -k 4 -N 10 -q 99249 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/uni -DS synthetic -Lq 2,4,6,7,11 -R 2 -k 4 -N 10 -q 93928 -d 5

  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 6,10,12,13,14 -R 2 -k 4 -N 10 -q 15403 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 1,4,6,10,11 -R 2 -k 4 -N 10 -q 5954 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 13,14,15,16,17 -R 2 -k 4 -N 10 -q 23863 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 10,12,14,16,18 -R 2 -k 4 -N 10 -q 18951 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 2,6,8,11,13 -R 2 -k 4 -N 10 -q 9953 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 6,7,10,15,17 -R 2 -k 4 -N 10 -q 6560 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 3,4,7,14,18 -R 2 -k 4 -N 10 -q 23708 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 9,10,11,13,14 -R 2 -k 4 -N 10 -q 13437 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 4,6,8,12,14 -R 2 -k 4 -N 10 -q 24812 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/uni -DS synthetic -Lq 2,4,6,7,11 -R 2 -k 4 -N 10 -q 23482 -d 5

  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 1,4,6,10,11 -R 2 -k 4 -N 10 -q 7701 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 13,14,15,16,17 -R 2 -k 4 -N 10 -q 2977 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 10,12,14,16,18 -R 2 -k 4 -N 10 -q 9475 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 2,6,8,11,13 -R 2 -k 4 -N 10 -q 4976 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 6,7,10,15,17 -R 2 -k 4 -N 10 -q 3280 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 3,4,7,14,18 -R 2 -k 4 -N 10 -q 6718 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 9,10,11,13,14 -R 2 -k 4 -N 10 -q 4345 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 4,6,8,12,14 -R 2 -k 4 -N 10 -q 8735 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 2,4,6,7,11 -R 2 -k 4 -N 10 -q 4016 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/uni -DS synthetic -Lq 2,12,13,14,16 -R 2 -k 4 -N 10 -q 8164 -d 5
done
# gauss
for ((i=0;i<5;i++))
do
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 2,9,12,13,15 -R 2 -k 4 -N 10 -q 30807 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,10,11,13,14 -R 2 -k 4 -N 10 -q 11908 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,8,9,12,13 -R 2 -k 4 -N 10 -q 47727 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 7,9,10,12,14 -R 2 -k 4 -N 10 -q 37902 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,7,8,11,12 -R 2 -k 4 -N 10 -q 19906 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,7,8,9,12 -R 2 -k 4 -N 10 -q 13120 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 9,10,11,12,13 -R 2 -k 4 -N 10 -q 47416 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,9,10,12 -R 2 -k 4 -N 10 -q 26875 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,10,11,15 -R 2 -k 4 -N 10 -q 49624 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,10,12,13 -R 2 -k 4 -N 10 -q 46964 -d 10


#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 2,9,12,13,15 -R 2 -k 4 -N 10 -q 30807 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,10,11,13,14 -R 2 -k 4 -N 10 -q 11908 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,8,9,12,13 -R 2 -k 4 -N 10 -q 47727 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 7,9,10,12,14 -R 2 -k 4 -N 10 -q 37902 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,7,8,11,12 -R 2 -k 4 -N 10 -q 19906 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,7,8,9,12 -R 2 -k 4 -N 10 -q 13120 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 9,10,11,12,13 -R 2 -k 4 -N 10 -q 47416 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,9,10,12 -R 2 -k 4 -N 10 -q 26875 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,10,11,15 -R 2 -k 4 -N 10 -q 49624 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,10,12,13 -R 2 -k 4 -N 10 -q 46964 -d 8

#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 2,9,12,13,15 -R 2 -k 4 -N 10 -q 30807 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,10,11,13,14 -R 2 -k 4 -N 10 -q 11908 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,8,9,12,13 -R 2 -k 4 -N 10 -q 47727 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 7,9,10,12,14 -R 2 -k 4 -N 10 -q 37902 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,7,8,11,12 -R 2 -k 4 -N 10 -q 19906 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,7,8,9,12 -R 2 -k 4 -N 10 -q 13120 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 9,10,11,12,13 -R 2 -k 4 -N 10 -q 47416 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,9,10,12 -R 2 -k 4 -N 10 -q 26875 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,10,11,15 -R 2 -k 4 -N 10 -q 49624 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,10,12,13 -R 2 -k 4 -N 10 -q 46964 -d 3

  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 2,9,12,13,15 -R 2 -k 4 -N 10 -q 30807 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,10,11,13,14 -R 2 -k 4 -N 10 -q 11908 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,8,9,12,13 -R 2 -k 4 -N 10 -q 47727 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 7,9,10,12,14 -R 2 -k 4 -N 10 -q 37902 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,7,8,11,12 -R 2 -k 4 -N 10 -q 19906 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 5,7,8,9,12 -R 2 -k 4 -N 10 -q 13120 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 9,10,11,12,13 -R 2 -k 4 -N 10 -q 47416 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,9,10,12 -R 2 -k 4 -N 10 -q 26875 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,10,11,15 -R 2 -k 4 -N 10 -q 49624 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/gauss -DS synthetic -Lq 6,8,10,12,13 -R 2 -k 4 -N 10 -q 46964 -d 5


  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 2,9,12,13,15 -R 2 -k 4 -N 10 -q 23217 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 6,10,11,13,14 -R 2 -k 4 -N 10 -q 23355 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 5,8,9,12,13 -R 2 -k 4 -N 10 -q 15235 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 7,9,10,12,14 -R 2 -k 4 -N 10 -q 5564 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 5,7,8,11,12 -R 2 -k 4 -N 10 -q 22415 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 5,7,8,9,12 -R 2 -k 4 -N 10 -q 22793 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 9,10,11,12,13 -R 2 -k 4 -N 10 -q 4325 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 6,8,9,10,12 -R 2 -k 4 -N 10 -q 10872 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 6,8,10,11,15 -R 2 -k 4 -N 10 -q 6780 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/gauss -DS synthetic -Lq 6,8,10,12,13 -R 2 -k 4 -N 10 -q 19038 -d 5

  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 2,9,12,13,15 -R 2 -k 4 -N 10 -q 3390 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 6,10,11,13,14 -R 2 -k 4 -N 10 -q 9519 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 5,8,9,12,13 -R 2 -k 4 -N 10 -q 1072 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 7,9,10,12,14 -R 2 -k 4 -N 10 -q 1605 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 5,7,8,11,12 -R 2 -k 4 -N 10 -q 2846 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 5,7,8,9,12 -R 2 -k 4 -N 10 -q 70 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 9,10,11,12,13 -R 2 -k 4 -N 10 -q 2468 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 6,8,9,10,12 -R 2 -k 4 -N 10 -q 7178 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 6,8,10,11,15 -R 2 -k 4 -N 10 -q 3861 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/gauss -DS synthetic -Lq 6,8,10,12,13 -R 2 -k 4 -N 10 -q 5739 -d 5
done
## zipf
for ((i=0;i<5;i++))
do

#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,8,19 -R 2 -k 4 -N 10 -q 30807 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,9 -R 2 -k 4 -N 10 -q 11908 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,5 -R 2 -k 4 -N 10 -q 47727 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,16 -R 2 -k 4 -N 10 -q 37902 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,8,9 -R 2 -k 4 -N 10 -q 19906 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,12,19,18 -R 2 -k 4 -N 10 -q 13120 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,7 -R 2 -k 4 -N 10 -q 47416 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,7 -R 2 -k 4 -N 10 -q 26875 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,7,15 -R 2 -k 4 -N 10 -q 49624 -d 10
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,9 -R 2 -k 4 -N 10 -q 46964 -d 10


#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,8,19 -R 2 -k 4 -N 10 -q 30807 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,9 -R 2 -k 4 -N 10 -q 11908 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,5 -R 2 -k 4 -N 10 -q 47727 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,16 -R 2 -k 4 -N 10 -q 37902 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,8,9 -R 2 -k 4 -N 10 -q 19906 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,12,19,18 -R 2 -k 4 -N 10 -q 13120 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,7 -R 2 -k 4 -N 10 -q 47416 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,7 -R 2 -k 4 -N 10 -q 26875 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,7,15 -R 2 -k 4 -N 10 -q 49624 -d 8
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,9 -R 2 -k 4 -N 10 -q 46964 -d 8


#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,8,19 -R 2 -k 4 -N 10 -q 30807 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,9 -R 2 -k 4 -N 10 -q 11908 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,5 -R 2 -k 4 -N 10 -q 47727 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,16 -R 2 -k 4 -N 10 -q 37902 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,8,9 -R 2 -k 4 -N 10 -q 19906 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,12,19,18 -R 2 -k 4 -N 10 -q 13120 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,7 -R 2 -k 4 -N 10 -q 47416 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,7 -R 2 -k 4 -N 10 -q 26875 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,7,15 -R 2 -k 4 -N 10 -q 49624 -d 3
#  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,9 -R 2 -k 4 -N 10 -q 46964 -d 3

  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,8,19 -R 2 -k 4 -N 10 -q 30807 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,9 -R 2 -k 4 -N 10 -q 11908 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,5 -R 2 -k 4 -N 10 -q 47727 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,4,16 -R 2 -k 4 -N 10 -q 37902 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,8,9 -R 2 -k 4 -N 10 -q 19906 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,12,19,18 -R 2 -k 4 -N 10 -q 13120 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,5,7 -R 2 -k 4 -N 10 -q 47416 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,7 -R 2 -k 4 -N 10 -q 26875 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,4,7,15 -R 2 -k 4 -N 10 -q 49624 -d 5
  python main.py -i Out/precompute/synthetic/50000-125106-20-3/zipf -DS synthetic -Lq 1,2,3,6,9 -R 2 -k 4 -N 10 -q 46964 -d 5

  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,3,4,5 -R 2 -k 4 -N 10 -q 89990 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,3,4,16 -R 2 -k 4 -N 10 -q 8578 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,3,8,9 -R 2 -k 4 -N 10 -q 12843 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,12,19,18 -R 2 -k 4 -N 10 -q 22772 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,3,5,7 -R 2 -k 4 -N 10 -q 565 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,3,6,7 -R 2 -k 4 -N 10 -q 19747 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,4,7,15 -R 2 -k 4 -N 10 -q 57427 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,3,6,9 -R 2 -k 4 -N 10 -q 92253 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,19,8,9 -R 2 -k 4 -N 10 -q 30891 -d 5
  #python main.py -i Out/precompute/synthetic/100000-250168-20-3/zipf -DS synthetic -Lq 1,2,3,5,19 -R 2 -k 4 -N 10 -q 45912 -d 5

  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,3,4,5 -R 2 -k 4 -N 10 -q 22497 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,3,4,16 -R 2 -k 4 -N 10 -q 2144 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,3,8,9 -R 2 -k 4 -N 10 -q 3210 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,12,19,18 -R 2 -k 4 -N 10 -q 5693 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,3,5,7 -R 2 -k 4 -N 10 -q 141 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,3,6,7 -R 2 -k 4 -N 10 -q 4936 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,4,7,15 -R 2 -k 4 -N 10 -q 14356 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,3,6,9 -R 2 -k 4 -N 10 -q 23063 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,19,8,9 -R 2 -k 4 -N 10 -q 7722 -d 5
  #python main.py -i Out/precompute/synthetic/25000-62667-20-3/zipf -DS synthetic -Lq 1,2,3,5,19 -R 2 -k 4 -N 10 -q 11478 -d 5

  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,3,4,5 -R 2 -k 4 -N 10 -q 3744 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,3,4,16 -R 2 -k 4 -N 10 -q 1334 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,3,8,9 -R 2 -k 4 -N 10 -q 3205 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,12,19,18 -R 2 -k 4 -N 10 -q 4656 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,3,5,7 -R 2 -k 4 -N 10 -q 3920 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,3,6,7 -R 2 -k 4 -N 10 -q 7555 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,4,7,15 -R 2 -k 4 -N 10 -q 9858 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,3,6,9 -R 2 -k 4 -N 10 -q 4319 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,19,8,9 -R 2 -k 4 -N 10 -q 7897 -d 5
  #python main.py -i Out/precompute/synthetic/10000-25036-20-3/zipf -DS synthetic -Lq 1,2,3,5,19 -R 2 -k 4 -N 10 -q 8580 -d 5
done