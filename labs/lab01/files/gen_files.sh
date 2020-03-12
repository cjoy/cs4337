
array=( 8 64 512 4096 32768 262144 2047152 )
for i in "${array[@]}"
do
    echo Creating ADES 1 file of size: $i bytes
    dd if=/dev/zero of=ades_$i.txt count=1 bs=$i
done


array=( 2 4 8 16 32 64 128 )
for i in "${array[@]}"
do
    echo Creating RSA 1 file of size: $i bytes
    dd if=/dev/zero of=rsa_$i.txt count=1 bs=$i
done

