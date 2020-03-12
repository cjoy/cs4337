echo ----------------------------------------------
echo DES 
echo ----------------------------------------------
array=( 8 64 512 4096 32768 262144 2047152 )
for i in "${array[@]}"
do
    echo bytes: $i
    python3 SFWN_AQ.des.py fedcba9876543210 40fedf386da13d57 files/ades_$i.txt mytest.des | tail -2
    echo ----------------------------------------------
done


echo ----------------------------------------------
echo AES 
echo ----------------------------------------------
array=( 8 64 512 4096 32768 262144 2047152 )
for i in "${array[@]}"
do
    echo bytes: $i
    python3 SFWN_AQ.aes.py fedcba9876543210fedcba9876543210 40fedf386da13d5740fedf386da13d57 files/ades_$i.txt mytest.aes | tail -2
    echo ----------------------------------------------
done



