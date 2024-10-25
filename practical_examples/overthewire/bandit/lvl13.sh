#!/bin/sh

password=$(./lvl12.sh)

cmd="mkdir -p /tmp/wowz; cp ~/data.txt /tmp/wowz; cd /tmp/wowz; cp data.txt hexdump; xxd -r hexdump compressed_data.gz; gzip -d compressed_data.gz; mv compressed_data compressed_data.bz2; bzip2 -d compressed_data.bz2; mv compressed_data compressed_data.gz; gzip -d compressed_data.gz; mv compressed_data compressed_data.tar; tar -xf compressed_data.tar; tar -xf data5.bin; mv data6.bin data6.bz2; bzip2 -d data6.bz2; tar -xf data6; mv data8.bin data8.gz; gzip -d data8.gz; cat data8; cd ~; rm -rf /tmp/wowz;"

result=$(python3 login_cached.py 12 $password $cmd | awk '{print $4}')
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
